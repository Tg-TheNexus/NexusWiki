# Security Module

The Security module provides **BCrypt-based player authentication**, CAPTCHA anti-bot protection, session management, anti-duplication, anti-lag tools, and network-level DDoS hardening — designed for **offline/cracked servers running Geyser+Floodgate**.

---

## Sub-systems

| Sub-system | Description |
|---|---|
| **Auth** | Register/login with BCrypt passwords, persistent sessions, Postgres or SQLite storage |
| **Anti-Bot** | IP rate-limiting, CAPTCHA map challenge, name blacklisting, VPN detection, Bedrock bypass |
| **Short-Session Detection** | Flags players who disconnect in < 30 seconds as likely scanners/bots; sends Discord alert |
| **Premium IP Whitelist** | Blocks premium accounts connecting from unknown IPs; optional manual first-approval |
| **Mod Detection** | Plugin-channel scanner — kicks hacked clients, alerts staff on Forge/NeoForge |
| **Anti-Dupe** | Detects and prevents common item duplication exploits |
| **Anti-Lag** | Scheduled world cleaner, entity stacker, leveled mobs |

---

## Authentication

Players on cracked servers must `/register` on first join and `/login` on subsequent joins.
Bedrock players (via Geyser+Floodgate) are authenticated by Xbox Live and **bypass all Java auth** entirely.
Premium Java accounts are verified via the Mojang API and also bypass auth.

### Commands

| Command | Usage | Permission |
|---|---|---|
| `/register <password> <confirm>` | Register an account | *(all players)* |
| `/login <password>` | Log into your account | *(all players)* |
| `/changepassword <old> <new>` | Change password | *(authenticated)* |
| `/auth trustip <player> <ip>` | Manually approve a new IP for a premium player | OP |

### Auth Configuration (`security/auth.yml`)

```yaml
storage: sqlite           # sqlite | postgres

postgres:
  url: "jdbc:postgresql://localhost:5432/nexusprism"
  user: nexus
  password: changeme

# In-memory idle timeout — re-login required after N minutes of inactivity
session-timeout-minutes: 30

# Reconnect window — players who rejoin within N hours are auto-logged in
# 0 = always require /login on every join
persistent-session-hours: 2

max-failed-attempts: 5    # Lockout after N wrong passwords
lockout-minutes: 10

login-spawn:
  enabled: false          # Teleport to safe spot while unauthenticated
  world: world
  x: 0.0
  y: 64.0
  z: 0.0
  yaw: 0.0
  pitch: 0.0

# ── Premium IP Whitelist ─────────────────────────────────────────────
premium-ip-whitelist:
  enabled: true           # Kick premium accounts on unknown IPs

# ── First-Connection Policy (BOT scanner hardening) ──────────────────
ip-whitelist:
  # false (default): first IP is auto-trusted
  # true: first connection is DENIED — admin must run /auth trustip <player> <ip>
  # Enable this on public servers being targeted by scanners (e.g. BOT_32 pattern)
  require-manual-first-approval: false
```

### Bedrock / Geyser+Floodgate

Bedrock players connect through Geyser. Floodgate assigns them UUIDs where
`getMostSignificantBits() == 0` — NexusPrism detects this at `AsyncPlayerPreLoginEvent`
and immediately marks the player as premium (Xbox-authenticated), skipping:

- CAPTCHA
- `/register` and `/login` requirements
- Mojang API lookup
- Premium IP whitelist checks

This is correct: Bedrock accounts require a real Microsoft/Xbox account with Geyser's
online-mode enforcement, so they are inherently more trusted than cracked Java clients.

### Premium Verification (Java)

When `premium-check.enabled` is `true`, NexusPrism validates premium Java accounts:

1. **UUID version check** — FastLogin assigns real Mojang UUIDs (v4). Offline UUIDs are v3. Mismatch → cracked.
2. **Mojang API comparison** — the player name is looked up and the returned UUID is compared against the actual UUID. Mismatch → flagged as impersonation attempt.

#### Cache & Resilience

| Layer | Detail |
|---|---|
| **In-memory cache** | 24-hour TTL; cleared on restart |
| **SQLite persistent cache** | Survives restarts — `security/premium-cache.db` |
| **Rate limiter** | Max 50 Mojang API calls per 10-minute window |
| **Exponential backoff** | Backs off up to 60s on repeated API failures |
| **Fallback** | Uses last cached result when the API is unreachable |

---

## Anti-Bot

### How It Works

Connection flow at `AsyncPlayerPreLoginEvent`:

```
1. Bedrock UUID check (getMostSignificantBits == 0) → auto-trust, skip all checks
2. Join rate limiter → blocks IPs exceeding max-joins per window
3. Name blacklist → regex patterns block scanner-like usernames
4. VPN detection → optional proxycheck.io / iphub.info integration
5. Premium check → Mojang UUID verification
6. Alt detection → alerts if one IP has too many linked accounts
```

On join: CAPTCHA map challenge (skipped for premium and Bedrock players).

!!! warning "What anti-bot does NOT protect against"
    Attacks that send malformed packets (like the April 2026 `ServerboundHelloPacket +1 byte` flood)
    are rejected by Netty **before** `AsyncPlayerPreLoginEvent` fires. All plugin-level checks above
    are bypassed. See the **Network-Level DDoS Hardening** section below.

### Short-Session Detection

When a player disconnects in under **30 seconds**, the system logs a warning and sends a
Discord alert to the `security` channel:

```
⚡ Short Session | `PlayerName` (`1.2.3.4`) disconnected after 7s — possible scanner/bot.
```

This catches bots that pass the handshake but disconnect immediately after joining,
which evades rate-limit windows.

To receive these alerts, add a `security` entry to `discord/channels.yml`:

```yaml
bot:
  security:
    targets:
      - id: "https://discord.com/api/webhooks/WEBHOOK_ID/WEBHOOK_TOKEN"
        isWebhook: true
    useEmbed: false
```

### Anti-Bot Configuration (`security/antibot.yml`)

```yaml
rate-limit:
  window-seconds: 10      # Sliding window for IP join tracking
  max-joins: 3            # Block if same IP joins more than N times per window

# Regex patterns matched against the player's username at AsyncPlayerPreLoginEvent.
# Supports Java regex. Use (?i) for case-insensitive matching.
name-blacklist-patterns:
  - "(?i)^BOT_\\d+$"       # BOT_1, BOT_32 (Mineflyer/scanner bots)
  - "(?i)^bot\\d+$"        # bot1, bot99
  - "(?i)^scanner.*$"      # scanner, scanner01
  - "(?i)^crawler.*$"      # crawler, webcrawler
  - "(?i)^test\\d*$"       # test, test1, test123
  - "[A-Za-z]{1,3}[0-9]{5,}"  # abc12345 (short prefix + long number)
  - "^[0-9]+$"             # purely numeric names

vpn-detection:
  enabled: false
  api-url: "https://proxycheck.io/v2/{ip}?key={key}&vpn=1"
  api-key: ""
  cache-minutes: 60

captcha:
  enabled: true
  timeout-seconds: 60
  session-hours: 24        # Skip CAPTCHA for 24h after first successful pass

premium-check:
  enabled: true            # Query Mojang API to verify premium accounts

alt-detection:
  max-accounts-per-ip: 3   # Alert admins if one IP has 3+ accounts (0 = disable)
```

---

## Network-Level DDoS Hardening

Attacks that operate below the plugin layer (malformed packets, connection floods) require
OS and proxy-level defenses. NexusPrism provides operational runbooks in `ops/`.

### Defense Layers (ordered by where they apply)

```
Internet → [TCPShield/Cloudflare] → [iptables/Fail2Ban] → [bukkit.yml throttle] → [Netty] → [Plugin events]
```

| Layer | Tool | Config location |
|---|---|---|
| Proxy filtering | TCPShield / Cloudflare Spectrum | `ops/server/tcpshield-cloudflare.md` |
| Host firewall | iptables + script | `ops/firewall/block-attacker.sh` |
| Auto-ban | Fail2Ban | `ops/fail2ban/` |
| Bukkit throttle | `connection-throttle` in `bukkit.yml` | `ops/server/bukkit-connection-throttle.md` |
| Plugin layer | NexusPrism anti-bot | `security/antibot.yml` |

### Recommended quick setup

```bash
# 1. Block a known attacker IP immediately
sudo bash ops/firewall/block-attacker.sh 15.237.177.126

# 2. Deploy Fail2Ban rules (auto-blocks future offenders)
sudo cp ops/fail2ban/filter.d/minecraft-malformed.conf /etc/fail2ban/filter.d/
sudo cp ops/fail2ban/jail.local /etc/fail2ban/jail.d/minecraft.conf
sudo systemctl reload fail2ban

# 3. Set connection-throttle in bukkit.yml (see ops/server/bukkit-connection-throttle.md)
# 4. Evaluate TCPShield for long-term proxy protection (see ops/server/tcpshield-cloudflare.md)
```

### April 2026 Incident

On **2026-04-20**, IP `15.237.177.126` (AWS EC2) sent a malformed `ServerboundHelloPacket`
(1 byte extra) every ~5 minutes for 17 hours. This caused a confirmed Paper Watchdog freeze
at 19:35 UTC. Full details in `ATTACKS.md` (gitignored).

---

## Anti-Lag

### World Cleaner

Automatically removes old ground items and excess entities on a schedule.

### Command

| Command | Usage | Permission |
|---|---|---|
| `/cleanworld` | Manually trigger a world clean | `nexusprism.security.cleanworld` |

### Anti-Lag Configuration (`security/antilag.yml`)

```yaml
cleaner:
  interval-seconds: 300
  warn-seconds: 5
  item-age-ticks: 6000
  worlds:
    - world
    - world_nether
    - world_the_end

stacker:
  radius: 5.0
  max-stack: 50
  entity-types:
    types: ["*"]
    named: false          # Don't stack named mobs

leveled-mobs:
  enabled: true
  max-level: 20
  xp-multiplier-per-level: 0.20
  damage-multiplier-per-level: 0.15
  health-multiplier-per-level: 0.10

backup:
  enabled: true
  interval-hours: 6
  keep-last: 5
  worlds:
    - world
    - world_nether
    - world_the_end
```

---

## Leveled Mobs

Every hostile mob that spawns is assigned a **level** based on depth, dimension, and biome.

### Level Roll Table

| Condition | Level Range / Bonus |
|---|---|
| Y > 64 (surface) | Lv. 1–4 |
| Y ≤ 64 | Lv. 3–6 |
| Y ≤ 30 | Lv. 5–8 |
| Y ≤ 0 (deep underground) | Lv. 8–12 |
| Nether dimension | +3 to roll |
| The End dimension | +4 to roll |
| Deep Dark biome | +5 to roll |
| Blood Moon active | +2 to all rolls |

### Stat Formulas

| Stat | Formula |
|---|---|
| **Damage** | `baseDamage × (1 + (level-1) × damageMultiplierPerLevel) × stackCount` |
| **XP** | `baseXP × stackCount × (1 + (level-1) × xpMultiplierPerLevel)` |
| **Health** | Scaled by `healthMultiplierPerLevel` per level above 1 |

---

## Mod Detection

Scans **plugin-message channels** registered during login to detect hacked clients.

- **Blacklisted channels** → player is kicked immediately and staff are notified
- **Watch-list channels** → staff are notified, player is never kicked (e.g. Forge — may be legitimate)

### Configuration (`security/mods.yml`)

```yaml
mod-detector:
  enabled: true
  action: KICK           # LOG | NOTIFY | KICK
  notify-staff: true
  kick-message: "§cYou are using a blacklisted modification."
  blacklisted-channels:
    - "wurst:*"
    - "meteor-client:*"
    - "liquidbounce:*"
  watch-channels:
    - "forge:*"
    - "fml:*"
    - "neoforge:*"
```

---

## Anti-Dupe

```yaml
# security/antidupe.yml
log-attempts: true
punish-on-detect: false
```

---

## Staff Commands

| Command | Usage | Permission |
|---|---|---|
| `/vanish` | Toggle visibility | `nexusprism.staff.vanish` |
| `/vanish <player>` | Vanish another player | `nexusprism.staff.vanish.others` |
| `/invsee <player>` | Inspect a player's inventory | `nexusprism.staff.invsee` |
| `/spy` | Toggle chat spy mode | `nexusprism.staff.spy` |

---

## Permissions

| Permission | Description | Default |
|---|---|---|
| `nexusprism.security.cleanworld` | Manual world clean | OP |
| `nexusprism.staff.vanish` | Vanish yourself | OP |
| `nexusprism.staff.vanish.others` | Vanish other players | OP |
| `nexusprism.staff.vanish.see` | See vanished players | OP |
| `nexusprism.staff.invsee` | Inspect inventories | OP |
| `nexusprism.staff.spy` | Chat spy mode | OP |

---

## PlaceholderAPI

| Placeholder | Description |
|---|---|
| `%nexusprism_authenticated%` | `true` / `false` — is the player logged in? |
| `%nexusprism_auth_status%` | Human-readable: `Authenticated`, `Pending` |
