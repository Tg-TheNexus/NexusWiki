# Commands Reference

Complete list of all commands registered by NexusPrism, organized by module.

**Legend:**

- `<arg>` — required argument
- `[arg]` — optional argument
- `(OP)` — operator-only by default
- `(true)` — available to all players by default

---

## Core / Plugin

| Command | Aliases | Description | Permission |
| --- | --- | --- | --- |
| `/nexusprism help` | `/ns`, `/nexus`, `/slime` | Show help | `nexusprism.command` |
| `/nexusprism info` | | Plugin version and status | `nexusprism.command` |
| `/nexusprism reload` | | Reload all configs | `nexusprism.admin.reload` |
| `/nexusprism give <player> <item>` | | Give a custom item | `nexusprism.admin.give` |
| `/nexusprism give <player> <item>` | | Give an item — requires NexusATS | `nexusprism.admin.give` |
| `/nexusprism guide` | | Open item guide — requires NexusATS | `nexusprism.command` |
| `/nexusprism modules` | | List all loaded modules | `nexusprism.command` |
| `/nexusprism machines` | | Machine info — requires NexusATS | `nexusprism.command` |
| `/nexusprism research` | | Research menu — requires NexusATS | `nexusprism.command` |
| `/recipe <item>` | | Show crafting recipe(s) | `nexusprism.recipe` |

> **Removed 2026-08-06:** standalone `/research`, `/nexusprism machine info/list`,
> `/nexusprism energy info/network`, and `/backpack` commands described dead systems with no
> remaining code. See `modules/core.md`.

---

## Waypoints

| Command | Aliases | Description | Permission |
| --- | --- | --- | --- |
| `/waypoint create <name>` | `/wp` | Create a waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint delete <name>` | `/wp` | Delete a waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint list` | `/wp` | List all waypoints | `nexusprism.essentials.waypoint` |
| `/waypoint tp <name>` | `/wp` | Teleport to waypoint | `nexusprism.essentials.waypoint` |
| `/waypoint info <name>` | `/wp` | Waypoint info | `nexusprism.essentials.waypoint` |

---

## Essentials — Homes

| Command | Description | Permission |
| --- | --- | --- |
| `/home [name]` | Teleport to a home | `nexusprism.essentials.home` |
| `/home list` | List all homes | `nexusprism.essentials.home` |
| `/sethome <name>` | Set home at current location | `nexusprism.essentials.home` |
| `/delhome <name>` | Delete a home | `nexusprism.essentials.home` |

---

## Essentials — Warps

| Command | Description | Permission |
| --- | --- | --- |
| `/warp <name>` | Teleport to a warp | `nexusprism.essentials.warp.use` |
| `/warp list` | List all warps | `nexusprism.essentials.warp.use` |
| `/setwarp <name>` | Create a warp (OP) | `nexusprism.essentials.warp.admin` |
| `/delwarp <name>` | Delete a warp (OP) | `nexusprism.essentials.warp.admin` |

---

## Essentials — Teleportation

| Command | Description | Permission |
| --- | --- | --- |
| `/tpa <player>` | Send teleport request | `nexusprism.essentials.tpa` |
| `/tpaccept` | Accept teleport request | `nexusprism.essentials.tpa` |
| `/tpdeny` | Deny teleport request | `nexusprism.essentials.tpa` |
| `/tphere <player>` | Summon a player (OP) | `nexusprism.essentials.tphere` |
| `/tppos <x> <y> <z>` | Teleport to coordinates (OP) | `nexusprism.essentials.tppos` |
| `/spawn` | Teleport to spawn | `nexusprism.essentials.spawn` |
| `/setspawn` | Set server spawn (OP) | `nexusprism.essentials.setspawn` |
| `/back` | Return to previous location | `nexusprism.essentials.back` |

---

## Essentials — Utility

| Command | Description | Permission |
| --- | --- | --- |
| `/afk` | Toggle AFK | `nexusprism.essentials.afk` |
| `/fly` | Toggle fly (self) | `nexusprism.essentials.fly` |
| `/fly <player>` | Toggle fly (other, OP) | `nexusprism.essentials.fly.others` |
| `/god` | Toggle god mode | `nexusprism.essentials.god` |
| `/god <player>` | Toggle god (other, OP) | `nexusprism.essentials.god.others` |
| `/heal` | Heal yourself (OP) | `nexusprism.essentials.heal` |
| `/heal <player>` | Heal another (OP) | `nexusprism.essentials.heal.others` |
| `/feed` | Feed yourself (OP) | `nexusprism.essentials.feed` |
| `/feed <player>` | Feed another (OP) | `nexusprism.essentials.feed.others` |
| `/nick <name>` | Set nickname | `nexusprism.essentials.nick` |
| `/nick <player> <name>` | Set nickname (other, OP) | `nexusprism.essentials.nick.others` |
| `/hat` | Wear item as hat | `nexusprism.essentials.hat` |
| `/speed <value>` | Set walk/fly speed (OP) | `nexusprism.essentials.speed` |
| `/workbench` | Portable workbench | `nexusprism.essentials.workbench` |
| `/anvil` | Portable anvil (OP) | `nexusprism.essentials.anvil` |
| `/grindstone` | Portable grindstone (OP) | `nexusprism.essentials.grindstone` |
| `/stonecutter` | Portable stonecutter (OP) | `nexusprism.essentials.stonecutter` |
| `/trash` | Portable trash bin | `nexusprism.essentials.trash` |
| `/near` | List nearby players | `nexusprism.essentials.near` |
| `/seen <player>` | Last seen info | `nexusprism.essentials.seen` |
| `/getpos` | Show coordinates | `nexusprism.essentials.getpos` |
| `/playtime` | Check playtime | `nexusprism.essentials.playtime` |
| `/gamemode <mode>` | Change gamemode (OP) | `nexusprism.essentials.gamemode` |
| `/enderchest` | Open ender chest | `nexusprism.essentials.enderchest` |
| `/enderchest <player>` | Open other's ender chest (OP) | `nexusprism.essentials.enderchest.others` |
| `/clearinventory` | Clear own inventory (OP) | `nexusprism.essentials.clearinventory` |
| `/clearinventory <player>` | Clear other's inventory (OP) | `nexusprism.essentials.clearinventory.others` |
| `/repair` | Repair held item (OP) | `nexusprism.essentials.repair` |
| `/ext` | Extinguish yourself (OP) | `nexusprism.essentials.ext` |
| `/exp <amount>` | Give XP (OP) | `nexusprism.essentials.exp` |
| `/skull [player]` | Get player head (OP) | `nexusprism.essentials.skull` |
| `/rules` | Show server rules | `nexusprism.essentials.rules` |
| `/worth [item]` | Item sell value | `nexusprism.essentials.worth` |

---

## Essentials — Jail

| Command | Description | Permission |
| --- | --- | --- |
| `/jail <player> [duration]` | Jail a player (OP) | `nexusprism.essentials.jail.admin` |
| `/unjail <player>` | Release a player (OP) | `nexusprism.essentials.jail.admin` |
| `/setjail` | Set jail location (OP) | `nexusprism.essentials.jail.admin` |

---

## Economy

| Command | Description | Permission |
| --- | --- | --- |
| `/money [player]` | Check balance | `nexusprism.economy.money` |
| `/baltop` | Top 10 richest | `nexusprism.economy.baltop` |
| `/sell hand` | Sell item in hand | `nexusprism.economy.sell` |
| `/sell all` | Sell all sellable items | `nexusprism.economy.sell` |
| `/sell inventory` | Sell entire inventory | `nexusprism.economy.sell` |
| `/worth [item]` | Check sell value | `nexusprism.essentials.worth` |
| `/eco give <player> <amount>` | Give money (OP) | `nexusprism.economy.admin` |
| `/eco take <player> <amount>` | Take money (OP) | `nexusprism.economy.admin` |
| `/eco set <player> <amount>` | Set balance (OP) | `nexusprism.economy.admin` |
| `/eco reset <player>` | Reset balance (OP) | `nexusprism.economy.admin` |

---

## Clans

| Command | Description | Permission |
| --- | --- | --- |
| `/clan create <name> <tag>` | Create a clan | `nexusprism.clan.use` |
| `/clan disband` | Disband clan | `nexusprism.clan.use` |
| `/clan invite <player>` | Invite a player | `nexusprism.clan.use` |
| `/clan join <name>` | Join a clan | `nexusprism.clan.use` |
| `/clan leave` | Leave clan | `nexusprism.clan.use` |
| `/clan kick <player>` | Kick a member | `nexusprism.clan.use` |
| `/clan promote <player>` | Promote to officer | `nexusprism.clan.use` |
| `/clan demote <player>` | Demote to member | `nexusprism.clan.use` |
| `/clan info [name]` | Clan info | `nexusprism.clan.use` |
| `/clan list` | List all clans | `nexusprism.clan.use` |
| `/clan chat` | Toggle clan chat | `nexusprism.clan.use` |
| `/clan claim` | Claim current chunk | `nexusprism.clan.use` |
| `/clan unclaim` | Unclaim current chunk | `nexusprism.clan.use` |
| `/clan map` | Show territory map | `nexusprism.clan.use` |
| `/clan chest` | Open clan chest | `nexusprism.clan.use` |
| `/clan upgrade` | Open upgrade menu | `nexusprism.clan.use` |
| `/clan top` | Clan leaderboard | `nexusprism.clan.use` |
| `/clan admin disband <name>` | Force disband (OP) | `nexusprism.clan.admin` |
| `/clan admin unclaim <name>` | Force unclaim (OP) | `nexusprism.clan.admin` |

---

## Security & Staff

| Command | Description | Permission |
| --- | --- | --- |
| `/register <password> <confirm>` | Register account | *(all)* |
| `/login <password>` | Login | *(all)* |
| `/changepassword <old> <new>` | Change password | *(authenticated)* |
| `/vanish` | Toggle vanish (OP) | `nexusprism.staff.vanish` |
| `/vanish <player>` | Vanish other (OP) | `nexusprism.staff.vanish.others` |
| `/invsee <player>` | Inspect inventory (OP) | `nexusprism.staff.invsee` |
| `/spy` | Toggle chat spy (OP) | `nexusprism.staff.spy` |
| `/cleanworld` | Run world cleaner (OP) | `nexusprism.security.cleanworld` |

---

## Discord

| Command | Description | Permission |
| --- | --- | --- |
| `/discord` | Discord invite link | *(all)* |
| `/discord link` | Start account linking | *(all)* |
| `/discord unlink` | Unlink account | *(all)* |
| `/discord info` | Show linked account | *(all)* |
| `/discordrr` | Manage reaction roles (OP) | `nexusprism.admin` |

---

## Protections & Duel

| Command | Description | Permission |
| --- | --- | --- |
| `/region claim <name>` | Claim selected area | `nexusprism.region.use` |
| `/region delete <name>` | Delete region | `nexusprism.region.use` |
| `/region list` | List your regions | `nexusprism.region.use` |
| `/region info [name]` | Region details | `nexusprism.region.use` |
| `/region addmember <region> <player>` | Add member | `nexusprism.region.use` |
| `/region removemember <region> <player>` | Remove member | `nexusprism.region.use` |
| `/region setflag <region> <flag> <val>` | Set a flag | `nexusprism.region.use` |
| `/region flags <region>` | View flags | `nexusprism.region.use` |
| `/protect <name>` | Quick chunk protection | `nexusprism.region.use` |
| `/region admin list` | Admin: all regions (OP) | `nexusprism.protect.admin` |
| `/region admin delete <name>` | Admin: delete region (OP) | `nexusprism.protect.admin` |
| `/duel <player>` | Challenge to duel | `nexusprism.duel.use` |
| `/duel accept` | Accept duel | `nexusprism.duel.use` |
| `/duel deny` | Deny duel | `nexusprism.duel.use` |
| `/duel spectate <player>` | Spectate duel | `nexusprism.duel.use` |
| `/duel stats` | Duel stats | `nexusprism.duel.use` |
| `/duel setarena` | Set duel arena (OP) | `nexusprism.protect.admin` |

---

## Crystal Defense

| Command | Description | Permission |
| --- | --- | --- |
| `/crystal join <arena>` | Join an arena | `nexusprism.crystaldefense.use` |
| `/crystal leave` | Leave arena | `nexusprism.crystaldefense.use` |
| `/crystal list` | List arenas | `nexusprism.crystaldefense.use` |
| `/crystal status` | Wave and crystal HP | `nexusprism.crystaldefense.use` |
| `/crystal create <name>` | Create arena (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal delete <name>` | Delete arena (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal setcrystal <arena>` | Set crystal loc (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal setspawn <arena>` | Set spawn (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal start [arena]` | Force-start (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal stop [arena]` | Stop game (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal reload` | Reload configs (OP) | `nexusprism.crystaldefense.admin` |

---

## Votifier

| Command | Description | Permission |
| --- | --- | --- |
| `/vote` | Show vote links and streak | `nexusprism.vote` |
| `/votetop` | Vote leaderboard | `nexusprism.vote.top` |

---

## Custom Mobs

| Command | Description | Permission |
| --- | --- | --- |
| `/boss spawn <id>` | Spawn a boss | `nexusprism.boss.admin` |
| `/boss spawn <id> <w> <x> <y> <z>` | Spawn at coords | `nexusprism.boss.admin` |
| `/boss list` | List all bosses | `nexusprism.boss.admin` |
| `/boss info <id>` | Boss definition | `nexusprism.boss.admin` |
| `/boss kill <id>` | Kill all boss instances | `nexusprism.boss.admin` |
| `/bossegg give <player> <id>` | Give spawn egg | `nexusprism.boss.admin` |

---

## Dreams

| Command | Description | Permission |
| --- | --- | --- |
| `/dreams reload` | Reload config | `nexusprism.dreams.admin` |
| `/dreams trigger <player>` | Force dream | `nexusprism.dreams.admin` |
| `/dreams trigger <player> nightmare` | Force nightmare | `nexusprism.dreams.admin` |

---

## Twitch

| Command | Description | Permission |
| --- | --- | --- |
| `/twitch link <username>` | Start linking | `nexusprism.twitch.use` |
| `/twitch unlink` | Unlink account | `nexusprism.twitch.use` |
| `/twitch status` | Link status | `nexusprism.twitch.use` |
| `/twitch approve <player>` | Approve link (OP) | `nexusprism.twitch.staff` |
| `/twitch reject <player>` | Reject link (OP) | `nexusprism.twitch.staff` |
| `/twitch pending` | Pending requests (OP) | `nexusprism.twitch.staff` |
| `/twitch giveaway <streamer>` | Draw winner (OP) | `nexusprism.twitch.staff` |
| `/twitch reload` | Reload config (OP) | `nexusprism.twitch.admin` |
