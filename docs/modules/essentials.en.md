# Essentials Module

The Essentials module provides **40+ quality-of-life commands** covering homes, warps, waypoints, teleportation, AFK detection, jail, and everyday utility commands.

---

## Homes

Players can set named homes and teleport back to them.

### Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/home [name]` | Teleport to a home | `nexusprism.essentials.home` |
| `/home list` | List all homes | `nexusprism.essentials.home` |
| `/sethome <name>` | Set a home at your location | `nexusprism.essentials.home` |
| `/delhome <name>` | Delete a home | `nexusprism.essentials.home` |

### Home Slot Permissions

| Permission | Slots |
| --- | --- |
| `nexusprism.essentials.homes.1` | 1 (default: true) |
| `nexusprism.essentials.homes.3` | 3 |
| `nexusprism.essentials.homes.10` | 10 |
| `nexusprism.essentials.homes.unlimited` | Unlimited (OP) |

---

## Warps

Server-wide public teleport destinations managed by admins.

## Warps Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/warp <name>` | Teleport to a warp | `nexusprism.essentials.warp.use` |
| `/warp list` | List all warps | `nexusprism.essentials.warp.use` |
| `/setwarp <name>` | Create a warp | `nexusprism.essentials.warp.admin` |
| `/delwarp <name>` | Delete a warp | `nexusprism.essentials.warp.admin` |

---

## TPA (Teleport Requests)

### TPA Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/tpa <player>` | Send a teleport request | `nexusprism.essentials.tpa` |
| `/tpaccept` | Accept a teleport request | `nexusprism.essentials.tpa` |
| `/tpdeny` | Deny a teleport request | `nexusprism.essentials.tpa` |
| `/tphere <player>` | Teleport a player to you | `nexusprism.essentials.tphere` |
| `/tppos <x> <y> <z>` | Teleport to coordinates | `nexusprism.essentials.tppos` |
| `/spawn` | Teleport to spawn | `nexusprism.essentials.spawn` |
| `/setspawn` | Set the server spawn | `nexusprism.essentials.setspawn` |
| `/back` | Return to previous location | `nexusprism.essentials.back` |

### TPA Configuration (`essentials/config.yml`)

```yaml
tpa:
  expiry-seconds: 60       # Request expires after this many seconds

back:
  save-on-death: true      # Save death location for /back
  save-on-any-teleport: false

spawn:
  respawn-at-spawn: false  # Force respawn at spawn (vs. bed)
```

---

## AFK System

### AFK Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/afk` | Toggle AFK status | `nexusprism.essentials.afk` |

### AFK Configuration

```yaml
afk:
  idle-seconds: 300        # Auto-AFK after 5 minutes of inactivity
  broadcast: true          # Announce when a player goes AFK
```

---

## Jail

Admins can send players to a predefined jail location.

### Jail Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/jail <player> [duration]` | Jail a player | `nexusprism.essentials.jail.admin` |
| `/unjail <player>` | Release a player | `nexusprism.essentials.jail.admin` |
| `/setjail` | Set the jail location | `nexusprism.essentials.jail.admin` |

---

## Utility Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/fly` | Toggle fly mode | `nexusprism.essentials.fly` |
| `/fly <player>` | Toggle fly for another player | `nexusprism.essentials.fly.others` |
| `/god` | Toggle god mode | `nexusprism.essentials.god` |
| `/god <player>` | Toggle god for another player | `nexusprism.essentials.god.others` |
| `/heal` | Heal yourself | `nexusprism.essentials.heal` |
| `/heal <player>` | Heal another player | `nexusprism.essentials.heal.others` |
| `/feed` | Feed yourself | `nexusprism.essentials.feed` |
| `/feed <player>` | Feed another player | `nexusprism.essentials.feed.others` |
| `/nick <name>` | Set your nickname | `nexusprism.essentials.nick` |
| `/nick <player> <name>` | Set another player's nick | `nexusprism.essentials.nick.others` |
| `/workbench` | Open a portable workbench | `nexusprism.essentials.workbench` |
| `/trash` | Open a portable trash bin | `nexusprism.essentials.trash` |
| `/anvil` | Open a portable anvil | `nexusprism.essentials.anvil` |
| `/grindstone` | Open a portable grindstone | `nexusprism.essentials.grindstone` |
| `/stonecutter` | Open a portable stonecutter | `nexusprism.essentials.stonecutter` |
| `/speed <value>` | Set walk/fly speed | `nexusprism.essentials.speed` |
| `/near` | List nearby players | `nexusprism.essentials.near` |
| `/seen <player>` | Last seen info | `nexusprism.essentials.seen` |
| `/clearinventory` | Clear your inventory | `nexusprism.essentials.clearinventory` |
| `/clearinventory <player>` | Clear another's inventory | `nexusprism.essentials.clearinventory.others` |
| `/getpos` | Show your coordinates | `nexusprism.essentials.getpos` |
| `/playtime` | Check your playtime | `nexusprism.essentials.playtime` |
| `/gamemode <mode>` | Change gamemode | `nexusprism.essentials.gamemode` |
| `/enderchest` | Open your ender chest | `nexusprism.essentials.enderchest` |
| `/enderchest <player>` | Open another's ender chest | `nexusprism.essentials.enderchest.others` |
| `/repair` | Repair held item | `nexusprism.essentials.repair` |
| `/ext` | Extinguish yourself | `nexusprism.essentials.ext` |
| `/exp <amount>` | Give yourself XP | `nexusprism.essentials.exp` |
| `/hat` | Wear held item as hat | `nexusprism.essentials.hat` |
| `/skull <player>` | Get a player's head | `nexusprism.essentials.skull` |
| `/rules` | Show server rules | `nexusprism.essentials.rules` |
| `/worth [item]` | Check item sell value | `nexusprism.essentials.worth` |

### Server Rules Configuration

```yaml
rules:
  - "&7 1. Respect all players."
  - "&7 2. No griefing or stealing."
  - "&7 3. No hacking or exploiting."
  - "&7 4. Have fun!"
```

### Fly Configuration

```yaml
fly:
  deny-in-pvp-regions: true   # Disable /fly when entering PvP regions
```
