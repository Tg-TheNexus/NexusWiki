# NexusPrism

> **A comprehensive reimplementation and evolution of Slimefun4** — next-generation tech, magic, and quality-of-life systems for Minecraft servers.

NexusPrism is a modular Spigot plugin built on a +25-module Maven architecture.
It brings custom items, machines, energy networks, clans, economy, minigames, and deep integrations all under a single, lightweight plugin JAR.

---

## Key Features

| Category | Highlights |
| --- | --- |
| **Custom Items** | 2,700+ data-driven items defined in YAML |
| **Machines** | Multiblock crafting, energy networks, ME storage |
| **Economy** | Single currency (money), /sell, /baltop |
| **Clans** | Territory claiming, upgrades, clan chest, clan chat |
| **Essentials** | 40+ QoL commands — homes, warps, TPA, AFK, jail |
| **Security** | BCrypt auth, CAPTCHA anti-bot, anti-dupe, anti-lag |
| **Discord** | Bot integration, account linking, role sync |
| **Crystal Defense** | Wave-based minigame protecting Ender Crystals |
| **Custom Mobs** | YAML-defined bosses with loot tables and AI forms |
| **Votifier** | Standalone V1/V2 vote server, streaks, leaderboards |
| **Dreams** | Sleep cutscene system with nightmare variants |
| **Protections** | Region claims, flags, duel arena system |
| **Twitch** | Account linking, live alerts, chat relay, giveaways |
| **PlaceholderAPI** | 30+ placeholders across all modules |

---

## Module Overview

```text
NexusPrism
├── nexusprism-api          Public API for addon developers
├── nexusprism-core         Core managers, PDC registry, language
├── nexusprism-items        Custom item storage (2,700+ items)
├── nexusprism-machines     Machine definitions, processing engine
├── nexusprism-systems      Energy network implementation
├── nexusprism-integrations PlaceholderAPI, LuckPerms, SkinsRestorer
├── nexusprism-storage      SQLite / PostgreSQL persistence
├── nexusprism-gui          GUI framework
├── nexusprism-utils        Utility helpers
├── nexusprism-web          Webstore delivery, VIP kits, payments
├── nexusprism-plugin       Main entry point (Spigot)
├── nexusprism-discord      JDA bot, webhooks, account linking
├── nexusprism-chat         4-channel chat system
├── nexusprism-ae           ME (Applied Energistics-style) storage
├── nexusprism-energy       Energy generation and cable networks
├── nexusprism-waila        WAILA/HUD integration
├── nexusprism-security     Auth, anti-bot, anti-lag, anti-dupe
├── nexusprism-clans        Clans, territory, upgrades
├── nexusprism-economy      Money, sell prices
├── nexusprism-essentials   40+ QoL commands
├── nexusprism-crystaldefense Wave-based Crystal Defense minigame
├── nexusprism-custommobs   YAML-defined bosses
├── nexusprism-dreams       Sleep cutscene system
├── nexusprism-protections  Region protection, duel system
├── nexusprism-ss           Silk Spawner support
├── nexusprism-votifier     Standalone Votifier V1/V2 server
└── nexusprism-twitch       Twitch integration
```

---

## Quick Navigation

| | |
| --- | --- |
| **[Getting Started](getting-started.md)** | Installation, requirements, and first steps |
| **[Core Module](modules/core.md)** | Items, PDC system, custom item registry |
| **[All Modules](modules/index.md)** | Browse all 13 feature modules |
| **[Commands Reference](reference/commands.md)** | All 40+ commands with usage and permissions |
| **[Permissions Reference](reference/permissions.md)** | Complete permission node list |
| **[PlaceholderAPI](reference/placeholders.md)** | All `%nexusprism_*%` placeholders |

---

## Author

NexusPrism is developed by **O-Tiger**

- API version: `1.21`
- Soft dependencies: `PlaceholderAPI`, `LuckPerms`, `SkinsRestorer`
