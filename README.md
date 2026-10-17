# NexusPrism Wiki

Official documentation for the [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism) Minecraft plugin — a modular Paper 1.21.4 plugin with 36 modules covering economy, clans, MMO, custom mobs, crates, Discord integration, Twitch integration, and more.

**Live site:** https://wiki.nexusheim.com/

---

## Stack

- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) — static site generator
- [Railway](https://railway.app) + Cloudflare — hosting and DNS
- `mkdocs-i18n` — trilingual docs (EN / PT-BR / ES)

## Local Development

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000

## Contributing

Docs live in `docs/`. Each page has three variants:

| File | Language |
|---|---|
| `page.md` | Português (BR), the default language |
| `page.en.md` | English |
| `page.es.md` | Español |

Edit all three when adding or updating content. See [CONTRIBUTING](https://github.com/Tg-TheNexus/NexusPrism/blob/main/CONTRIBUTING.md) for guidelines.

## License

Documentation is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
