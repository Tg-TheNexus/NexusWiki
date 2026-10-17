"""
Dynamic changelog generator for NexusPrism wiki.

Reads git log (conventional commits) from the plugin repo,
translates each entry to PT-BR and ES, and prepends them to
the three changelog files in the wiki docs folder.

Translation: deep-translator (Google free backend by default).
             Set DEEPL_API_KEY env var for DeepL quality instead.

Multi-language commits (skip translation entirely):
    Write the commit body with flag-emoji section headers and the
    content for each language beneath them:

        🇺🇸
        Hello world!

        - Added: something cool
        - Fixed: a nasty bug

        🇧🇷
        Olá mundo!

        - Adicionado: algo legal
        - Corrigido: um bug feio

        🇪🇸
        ¡Hola mundo!

        - Añadido: algo genial
        - Corregido: un feo bug

    Supported flag markers (per line, alone): 🇺🇸 🇬🇧 🇧🇷 🇵🇹 🇪🇸
    Discord shortcode aliases also accepted: :flag_us: :flag_br: :flag_es:
    Two or more language sections make a multi-language commit.

Usage:
    python generate_changelog.py \\
        --repo-path /path/to/NexusPrismIA \\
        --wiki-path /path/to/NexusWiki/docs

    # Dry run (prints without writing):
    python generate_changelog.py ... --dry-run

    # Force re-process from a specific SHA:
    python generate_changelog.py ... --from-sha abc1234
"""

import argparse
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─── Commit type → (icon, English label) ──────────────────────────────────────

TYPE_MAP = {
    'feat':     ('✨', 'Added'),
    'feature':  ('✨', 'Added'),
    'fix':      ('🐛', 'Fixed'),
    'bugfix':   ('🐛', 'Fixed'),
    'perf':     ('⚡', 'Performance'),
    'refactor': ('♻️', 'Changed'),
    'docs':     ('📚', 'Documentation'),
    'chore':    ('🔧', 'Maintenance'),
    'build':    ('🔧', 'Maintenance'),
    'ci':       ('🔧', 'Maintenance'),
    'security': ('🔒', 'Security'),
    'revert':   ('⏪', 'Reverted'),
    'style':    ('🎨', 'Style'),
    'test':     ('🧪', 'Tests'),
}

# Per-language labels for section headings and breaking-changes header.
# These are rendered directly — they never go through the translator.
# lang key: 'en' | 'pt' | 'es'
SECTION_LABELS: dict[str, dict[str, tuple[str, str]]] = {
    # commit-type → (icon, label)  per language
    'en': {
        'feat':     ('✨', 'Added'),
        'feature':  ('✨', 'Added'),
        'fix':      ('🐛', 'Fixed'),
        'bugfix':   ('🐛', 'Fixed'),
        'perf':     ('⚡', 'Performance'),
        'refactor': ('♻️', 'Changed'),
        'docs':     ('📚', 'Documentation'),
        'chore':    ('🔧', 'Maintenance'),
        'build':    ('🔧', 'Maintenance'),
        'ci':       ('🔧', 'Maintenance'),
        'security': ('🔒', 'Security'),
        'revert':   ('⏪', 'Reverted'),
        'style':    ('🎨', 'Style'),
        'test':     ('🧪', 'Tests'),
        'breaking': ('💥', 'Breaking Changes'),
    },
    'pt': {
        'feat':     ('✨', 'Adicionado'),
        'feature':  ('✨', 'Adicionado'),
        'fix':      ('🐛', 'Corrigido'),
        'bugfix':   ('🐛', 'Corrigido'),
        'perf':     ('⚡', 'Desempenho'),
        'refactor': ('♻️', 'Alterado'),
        'docs':     ('📚', 'Documentação'),
        'chore':    ('🔧', 'Manutenção'),
        'build':    ('🔧', 'Manutenção'),
        'ci':       ('🔧', 'Manutenção'),
        'security': ('🔒', 'Segurança'),
        'revert':   ('⏪', 'Revertido'),
        'style':    ('🎨', 'Estilo'),
        'test':     ('🧪', 'Testes'),
        'breaking': ('💥', 'Mudanças Críticas'),
    },
    'es': {
        'feat':     ('✨', 'Añadido'),
        'feature':  ('✨', 'Añadido'),
        'fix':      ('🐛', 'Corregido'),
        'bugfix':   ('🐛', 'Corregido'),
        'perf':     ('⚡', 'Rendimiento'),
        'refactor': ('♻️', 'Modificado'),
        'docs':     ('📚', 'Documentación'),
        'chore':    ('🔧', 'Mantenimiento'),
        'build':    ('🔧', 'Mantenimiento'),
        'ci':       ('🔧', 'Mantenimiento'),
        'security': ('🔒', 'Seguridad'),
        'revert':   ('⏪', 'Revertido'),
        'style':    ('🎨', 'Estilo'),
        'test':     ('🧪', 'Tests'),
        'breaking': ('💥', 'Cambios Críticos'),
    },
}

# Display order for section types inside a date group
TYPE_ORDER = [
    'breaking', 'feat', 'feature', 'fix', 'bugfix',
    'security', 'perf', 'refactor', 'docs',
    'chore', 'build', 'ci', 'revert', 'style', 'test',
]

BREAKING_ICON, BREAKING_LABEL = '💥', 'Breaking Changes'

# SHA state file stored inside wiki docs/
SHA_FILE = '.changelog_sha'

# Regex: type(scope)!: message  or  type!: message  or  type: message
COMMIT_RE = re.compile(
    r'^(?P<type>[a-zA-Z]+)'
    r'(?:\((?P<scope>[^)]+)\))?'
    r'(?P<breaking>!)?'
    r':\s*(?P<message>.+)$'
)

# ─── Multi-language commit support ────────────────────────────────────────────

# Maps flag marker (alone on a line) → language code used in this script
FLAG_LANG_MAP: dict[str, str] = {
    # Real Unicode flag emoji
    '🇺🇸': 'en',
    '🇬🇧': 'en',
    '🇧🇷': 'pt',
    '🇵🇹': 'pt',
    '🇪🇸': 'es',
    # Discord-style shortcodes (typed in terminal / commit tools)
    ':flag_us:': 'en',
    ':flag_gb:': 'en',
    ':flag_br:': 'pt',
    ':flag_pt:': 'pt',
    ':flag_es:': 'es',
}


def parse_multilang(text: str) -> dict[str, str] | None:
    """
    Detect and parse a multi-language commit message.

    Returns a dict {'en': ..., 'pt': ..., 'es': ...} (any subset) when the
    text contains two or more flag-delimited sections, otherwise None.
    """
    # Fast path: no known flag marker present
    if not any(flag in text for flag in FLAG_LANG_MAP):
        return None

    sections: dict[str, list[str]] = {}
    current_lang: str | None = None

    for line in text.splitlines():
        stripped = line.strip()
        matched_lang: str | None = None
        for flag, lang in FLAG_LANG_MAP.items():
            if stripped == flag:
                matched_lang = lang
                break

        if matched_lang is not None:
            current_lang = matched_lang
            sections.setdefault(current_lang, [])
        elif current_lang is not None:
            sections[current_lang].append(line)

    # Strip blank lines at start/end of each section, drop empty ones
    result: dict[str, str] = {}
    for lang, lines in sections.items():
        content = '\n'.join(lines).strip()
        if content:
            result[lang] = content

    # Require at least two distinct language sections to avoid false positives
    # (e.g., a conventional commit body that happens to mention a country flag)
    return result if len(result) >= 2 else None


# ─── Git helpers ───────────────────────────────────────────────────────────────

def git_log(repo_path: Path, from_sha: str | None) -> list[dict]:
    """Return commits oldest-first, optionally starting after from_sha.

    Each entry has: sha, date, subject, body
    body is the commit message body (everything after the blank line).
    """
    field_sep = '\x1F'   # unit separator  — rare in commit messages
    rec_sep   = '\x1E'   # record separator — rare in commit messages
    # %s = subject, %b = body (blank-line separated from subject by git)
    fmt = f'%H{field_sep}%aI{field_sep}%s{field_sep}%b{rec_sep}'
    cmd = ['git', '-C', str(repo_path), 'log', f'--format={fmt}', '--reverse']
    if from_sha:
        cmd.append(f'{from_sha}..HEAD')
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)

    commits = []
    for record in result.stdout.split(rec_sep):
        record = record.strip()
        if not record:
            continue
        # maxsplit=3 so the body (field 4) can contain field_sep without harm
        parts = record.split(field_sep, 3)
        if len(parts) < 3:
            continue
        sha      = parts[0].strip()
        date_iso = parts[1].strip()
        subject  = parts[2].strip()
        body     = parts[3].strip() if len(parts) > 3 else ''
        try:
            dt = datetime.fromisoformat(date_iso.replace('Z', '+00:00'))
            date_str = dt.strftime('%Y-%m-%d')
        except Exception:
            date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')
        commits.append({
            'sha': sha, 'date': date_str,
            'subject': subject, 'body': body,
        })
    return commits


def get_latest_sha(repo_path: Path) -> str | None:
    result = subprocess.run(
        ['git', '-C', str(repo_path), 'rev-parse', 'HEAD'],
        capture_output=True, text=True
    )
    return result.stdout.strip() if result.returncode == 0 else None


# ─── Commit parsing ────────────────────────────────────────────────────────────

def parse_commit(commit: dict) -> dict:
    m = COMMIT_RE.match(commit['subject'])
    if not m:
        return {**commit, 'ctype': 'chore', 'scope': None,
                'breaking': False, 'desc': commit['subject']}
    ctype = m.group('type').lower()
    scope = m.group('scope')
    breaking = bool(m.group('breaking'))
    desc = m.group('message').strip()
    desc = desc[0].upper() + desc[1:] if desc else desc
    return {**commit, 'ctype': ctype, 'scope': scope,
            'breaking': breaking, 'desc': desc}


# ─── Rendering ────────────────────────────────────────────────────────────────

def render_item(c: dict) -> str:
    prefix = f'**{c["scope"]}**: ' if c.get('scope') else ''
    return f'- {prefix}{c["desc"]}'


def render_date_block(date: str, sha: str, type_groups: dict[str, list],
                      lang: str = 'en') -> str:
    """Render one date block.

    Section headings are emitted in *lang* using SECTION_LABELS so they are
    never sent to the machine translator (which would produce unreliable results
    and corrupt the placeholders used to protect markdown structure).
    """
    labels = SECTION_LABELS.get(lang, SECTION_LABELS['en'])
    fallback_en = SECTION_LABELS['en']

    lines = [f'\n## [{date}] · `{sha[:7]}`\n']

    seen: set[str] = set()
    for key in TYPE_ORDER:
        if key in type_groups:
            seen.add(key)
            icon, label = labels.get(key, fallback_en.get(key, ('🔧', 'Maintenance')))
            lines.append(f'\n### {icon} {label}\n')
            for c in type_groups[key]:
                lines.append(render_item(c))

    # Any type not covered by TYPE_ORDER
    for key, entries in type_groups.items():
        if key not in seen:
            icon, label = labels.get(key, fallback_en.get(key, ('🔧', 'Maintenance')))
            lines.append(f'\n### {icon} {label}\n')
            for c in entries:
                lines.append(render_item(c))

    return '\n'.join(lines)


def render_multilang_block(date: str, sha: str, sections: dict[str, str],
                            lang: str) -> str:
    """Render one date block for a multi-language commit, for the given lang.

    Falls back to 'en' if the requested language is absent.
    """
    content = sections.get(lang) or sections.get('en', '')
    header = f'\n## [{date}] · `{sha[:7]}`\n'
    return header + '\n' + content


# ─── Translation ──────────────────────────────────────────────────────────────

# Things we want to keep verbatim through the translator.
# Note: section headings and date/sha lines are no longer included here —
# they are rendered directly in the target language by render_date_block()
# so they never need to pass through translation at all.
_PROTECT_PATTERNS = [
    r'`[^`\n]+`',                    # inline code  e.g. `nexusprism-core`
    r'\*\*[^*\n]+\*\*:',             # **scope**: prefix  e.g. **tab**:
    r'\[skip ci\]',
]
_PROTECT_RE = re.compile(
    '|'.join('(?:' + p + ')' for p in _PROTECT_PATTERNS),
    flags=re.MULTILINE
)

# Placeholder token format.
# Must survive machine translation without modification.
# We use a long, all-uppercase, underscore-separated token because
# translation services treat such strings as untranslatable identifiers.
# Control characters (\x02/\x03) are stripped by Google Translate — do NOT use them.
_PH_PREFIX = 'NXWIKI__PH'
_PH_SUFFIX = '__NXWIKIEND'


def protect(text: str) -> tuple[str, dict]:
    holders: dict[str, str] = {}
    counter = [0]

    def _replace(m: re.Match) -> str:
        key = f'{_PH_PREFIX}{counter[0]}{_PH_SUFFIX}'
        holders[key] = m.group(0)
        counter[0] += 1
        return key

    return _PROTECT_RE.sub(_replace, text), holders


def restore(text: str, holders: dict) -> str:
    for key, val in holders.items():
        text = text.replace(key, val)
    return text


def _chunk_text(text: str, limit: int = 4500) -> list[str]:
    """Split text at blank lines keeping chunks under limit chars."""
    chunks, current = [], ''
    for para in text.split('\n\n'):
        if len(current) + len(para) + 2 > limit:
            if current:
                chunks.append(current.strip())
            current = para
        else:
            current = (current + '\n\n' + para) if current else para
    if current:
        chunks.append(current.strip())
    return chunks or [text]


def translate_text(text: str, target: str) -> str:
    """Translate text via DeepL (if key set) or Google Translate (free)."""
    deepl_key = os.environ.get('DEEPL_API_KEY', '').strip()

    if deepl_key:
        try:
            from deep_translator import DeeplTranslator
            lang_map = {'pt': 'PT-BR', 'es': 'ES'}
            t = DeeplTranslator(api_key=deepl_key, source='en',
                                target=lang_map.get(target, target))
            return t.translate(text) or text
        except Exception as e:
            print(f'[WARN] DeepL failed ({e}), falling back to Google.', file=sys.stderr)

    try:
        from deep_translator import GoogleTranslator
        lang_map = {'pt': 'pt', 'es': 'es'}
        gt = GoogleTranslator(source='en', target=lang_map.get(target, target))
        chunks = _chunk_text(text)
        return '\n\n'.join(gt.translate(c) or c for c in chunks)
    except Exception as e:
        print(f'[WARN] Google Translate failed ({e}). Using English.', file=sys.stderr)
        return text


def translate_section(section_en: str, target: str) -> str:
    protected, holders = protect(section_en)
    translated = translate_text(protected, target)
    return restore(translated, holders)


# ─── File helpers ──────────────────────────────────────────────────────────────

def read_sha_state(wiki_docs: Path) -> str | None:
    p = wiki_docs / SHA_FILE
    return p.read_text().strip() or None if p.exists() else None


def write_sha_state(wiki_docs: Path, sha: str) -> None:
    (wiki_docs / SHA_FILE).write_text(sha + '\n', encoding='utf-8')


def prepend_to_file(path: Path, new_content: str) -> None:
    """Insert new_content right after the opening h1 + --- separator."""
    existing = path.read_text(encoding='utf-8') if path.exists() else ''
    lines = existing.split('\n')

    # Find insertion point: after h1 line and optional '---' separator
    insert_at = 1  # default: after first line
    for i, line in enumerate(lines):
        if line.startswith('# '):
            insert_at = i + 1
        elif i > 0 and line.strip() == '---' and insert_at > 0:
            insert_at = i + 1
            break

    before = '\n'.join(lines[:insert_at])
    after  = '\n'.join(lines[insert_at:])
    combined = before + '\n' + new_content.rstrip() + '\n\n---\n\n' + after.lstrip()
    path.write_text(combined, encoding='utf-8')


# ─── Changelog file headers ────────────────────────────────────────────────────
# These are written once if the file is empty / missing.

HEADER_EN = """\
# Changelog

> Auto-generated from [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism) commits.
> Translated automatically — minor phrasing differences are expected.

---
"""

HEADER_PT = """\
# Histórico de Alterações

> Gerado automaticamente a partir dos commits do [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism).
> Traduzido automaticamente — pequenas diferenças de fraseado são esperadas.

---
"""

HEADER_ES = """\
# Historial de Cambios

> Generado automáticamente desde los commits de [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism).
> Traducido automáticamente — pueden esperarse pequeñas diferencias de redacción.

---
"""


def ensure_header(path: Path, header: str) -> None:
    if not path.exists() or path.stat().st_size < 10:
        path.write_text(header, encoding='utf-8')


# ─── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    ap = argparse.ArgumentParser(description='NexusPrism dynamic changelog generator')
    ap.add_argument('--repo-path', required=True,
                    help='Path to the NexusPrism plugin git repository')
    ap.add_argument('--wiki-path', required=True,
                    help='Path to the wiki docs/ directory')
    ap.add_argument('--from-sha',
                    help='Re-process commits starting after this SHA (overrides state file)')
    ap.add_argument('--dry-run', action='store_true',
                    help='Print generated output without writing any files')
    args = ap.parse_args()

    repo_path = Path(args.repo_path).resolve()
    wiki_docs = Path(args.wiki_path).resolve()
    from_sha  = args.from_sha or read_sha_state(wiki_docs)

    print(f'Repo:       {repo_path}')
    print(f'Wiki docs:  {wiki_docs}')
    print(f'From SHA:   {from_sha or "(beginning)"}')

    raw = git_log(repo_path, from_sha)
    if not raw:
        print('No new commits — changelog is up to date.')
        return

    # Skip pure merge commits and bot commits
    raw = [c for c in raw
           if not c['subject'].startswith('Merge ')
           and '[skip ci]' not in c['subject']
           and 'chore(changelog)' not in c['subject']]

    if not raw:
        print('No qualifying commits after filtering.')
        return

    # ── Separate multi-language commits from conventional ones ─────────────────
    ml_commits:   list[dict] = []   # have hand-written per-lang sections
    conv_commits: list[dict] = []   # conventional commits → need translation

    for c in raw:
        # Check the full message (subject + body) for flag sections
        full_msg = c['subject'] + ('\n' + c['body'] if c['body'] else '')
        ml = parse_multilang(full_msg)
        if ml:
            c['_multilang'] = ml
            ml_commits.append(c)
            print(f'  [multilang] {c["sha"][:7]} — langs: {sorted(ml.keys())}')
        else:
            conv_commits.append(c)

    print(f'Processing {len(conv_commits)} conventional + {len(ml_commits)} multi-lang commit(s)...')

    # ── Parse conventional commits ─────────────────────────────────────────────
    parsed_conv = [parse_commit(c) for c in conv_commits]

    # Group conventional commits by date → type → list
    conv_by_date: dict[str, dict[str, list]] = {}
    for c in parsed_conv:
        date = c['date']
        conv_by_date.setdefault(date, {})
        key = 'breaking' if c['breaking'] else c['ctype']
        conv_by_date[date].setdefault(key, []).append(c)

    # ── Build per-language output, one date at a time ─────────────────────────
    all_dates = sorted(set(c['date'] for c in raw), reverse=True)
    en_parts: list[str] = []
    pt_parts: list[str] = []
    es_parts: list[str] = []

    for date in all_dates:
        # --- Conventional block for this date ---
        if date in conv_by_date:
            sha = [c for c in conv_commits if c['date'] == date][-1]['sha']
            en_block = render_date_block(date, sha, conv_by_date[date], lang='en')
            # PT and ES blocks have section headings rendered in target language
            # directly — only the bullet text is sent to the translator.
            pt_block = render_date_block(date, sha, conv_by_date[date], lang='pt')
            es_block = render_date_block(date, sha, conv_by_date[date], lang='es')
            en_parts.append(en_block)

            if not args.dry_run:
                print(f'  Translating {date} → PT-BR...')
                pt_parts.append(translate_section(pt_block, 'pt'))
                print(f'  Translating {date} → ES...')
                es_parts.append(translate_section(es_block, 'es'))
            else:
                # Dry run: show language-specific blocks without translation
                pt_parts.append(pt_block)
                es_parts.append(es_block)

        # --- Multi-language blocks for this date ---
        for c in ml_commits:
            if c['date'] != date:
                continue
            ml = c['_multilang']
            en_parts.append(render_multilang_block(date, c['sha'], ml, 'en'))
            pt_parts.append(render_multilang_block(date, c['sha'], ml, 'pt'))
            es_parts.append(render_multilang_block(date, c['sha'], ml, 'es'))

    en_out = '\n'.join(en_parts)
    pt_out = '\n'.join(pt_parts)
    es_out = '\n'.join(es_parts)

    latest_sha = raw[-1]['sha']

    if args.dry_run:
        print('\n' + '─' * 60 + '\n[EN]\n' + en_out)
        print('\n' + '─' * 60 + '\n[PT]\n' + pt_out)
        print('\n' + '─' * 60 + '\n[ES]\n' + es_out)
        print(f'\nLast SHA would be recorded: {latest_sha[:7]}')
        return

    # Ensure changelog files have proper headers
    ensure_header(wiki_docs / 'changelog.en.md', HEADER_EN)
    ensure_header(wiki_docs / 'changelog.md',    HEADER_PT)
    ensure_header(wiki_docs / 'changelog.es.md', HEADER_ES)

    prepend_to_file(wiki_docs / 'changelog.en.md', en_out)
    prepend_to_file(wiki_docs / 'changelog.md',    pt_out)
    prepend_to_file(wiki_docs / 'changelog.es.md', es_out)

    write_sha_state(wiki_docs, latest_sha)

    dates = sorted(set(c['date'] for c in raw), reverse=True)
    print(f'Done. Recorded SHA: {latest_sha[:7]}')
    print(f'Dates covered: {", ".join(dates)}')
    ml_count = len(ml_commits)
    if ml_count:
        print(f'Multi-language commits (no translation needed): {ml_count}')


if __name__ == '__main__':
    main()
