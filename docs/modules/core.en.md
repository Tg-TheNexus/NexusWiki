# Core Module

The Core module is the foundation of NexusPrism: language system (i18n), the GUI framework,
per-player data storage (with a generic extension API for addons), the structure-loot event
hook, and the personal waypoint system.

> **Item/machine/energy/research content has moved to NexusATS.** NexusPrism itself no
> longer ships a custom item registry, machine engine, energy network, or research tree —
> that entire domain lives in the separate NexusATS plugin now. If NexusATS is installed,
> its commands are exposed under `/nexusprism <subcommand>` (see below); without NexusATS,
> those subcommands are unavailable.

---

## PDC System

NexusPrism uses Minecraft's **PersistentDataContainer** for its own player/machine-placement
bookkeeping. Addon plugins (like NexusATS) use the same pattern for their own items and
blocks under their own PDC namespace.

---

## Addon Extension Hooks

NexusPrism exposes a small set of generic hooks so addon plugins (NexusATS, and any future
addon) can integrate without NexusPrism needing to know about them ahead of time:

| Hook | Purpose |
| --- | --- |
| `NexusPrism.registerBlockClassifier(isAddonBlock, addonBlockIdLookup)` | Lets an addon mark its own blocks so RNG/traits/MMO/Waila skip or redirect on them |
| `NexusPrism.registerAddonCommand(subCommand, handler)` | Registers a `/nexusprism <subCommand>` handler owned by the addon |
| `NexusPrism.registerAddonTabCompleter(subCommand, completer)` | Tab-completion for an addon-registered subcommand |
| `DataManager.setPlayerField(playerId, namespace, key, value)` / `getPlayerField(...)` / `getPlayerFields(...)` | Generic per-player key/value storage, scoped by namespace, for addons that need to persist their own data through NexusPrism's database without a schema migration |

---

## Waypoints

Waypoints are personal fast-travel points saved by the player.

### Waypoints Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/waypoint create <name>` | Create a waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint delete <name>` | Delete a waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint list` | List all waypoints | `nexusprism.essentials.waypoint` |
| `/waypoint tp <name>` | Teleport to a waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint info <name>` | Show waypoint details | `nexusprism.essentials.waypoint` |

Aliases: `/wp`

### Slot Limit Permissions

| Permission | Slots |
| --- | --- |
| `nexusprism.essentials.waypoints.1` | 1 (default) |
| `nexusprism.essentials.waypoints.5` | 5 |
| `nexusprism.essentials.waypoints.25` | 25 |
| `nexusprism.essentials.waypoints.unlimited` | Unlimited (OP) |

---

## Main Plugin Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/nexusprism help` | Show help | `nexusprism.command` |
| `/nexusprism info` | Plugin info | `nexusprism.command` |
| `/nexusprism reload` | Reload all configs | `nexusprism.admin.reload` |
| `/nexusprism modules` | List loaded modules | `nexusprism.command` |
| `/nexusprism give <player> <item>` | Give an item — requires NexusATS | `nexusprism.admin.give` |
| `/nexusprism guide` | Open the item guide — requires NexusATS | `nexusprism.command` |
| `/nexusprism machines` | Machine info — requires NexusATS | `nexusprism.command` |
| `/nexusprism research` | Research menu — requires NexusATS | `nexusprism.command` |
| `/nexusprism recipe` | Recipe lookup — requires NexusATS | `nexusprism.command` |

Aliases: `/ns`, `/nexus`, `/slime`, `/nslime`

---

## Language Support

NexusPrism ships with four language files:

| File | Language |
| --- | --- |
| `lang/en_US.yml` | English (default) |
| `lang/pt_BR.yml` | Brazilian Portuguese |
| `lang/es_ES.yml` | Spanish |
| `lang/zh_CN.yml` | Chinese (Simplified) |

Set the active language in `config.yml`:

```yaml
settings:
  language: en_US
```
