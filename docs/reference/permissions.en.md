# Permissions Reference

*Last updated: 2026-03-22*

Complete list of all permission nodes registered by NexusPrism. Nodes marked **OP** default to operators only; nodes marked **true** are granted to all players by default; nodes marked **—** must be granted manually.

---

## Core & Admin

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.*` | All permissions | OP |
| `nexusprism.command` | Use basic `/nexusprism` command | true |
| `nexusprism.admin` | General admin access | OP |
| `nexusprism.admin.*` | All admin permissions | OP |
| `nexusprism.admin.reload` | Reload plugin configs | OP |
| `nexusprism.admin.give` | Give custom items | OP |
| `nexusprism.admin.debug` | Toggle debug mode | OP |
| `nexusprism.admin.cleardata` | Clear player data | OP |
| `nexusprism.admin.bypass` | Bypass various admin checks | OP |
| `nexusprism.admin.delivery` | Manage delivery/store orders | OP |
| `nexusprism.admin.recipe` | Admin recipe commands | OP |
| `nexusprism.admin.resourcepack` | Admin resource pack commands | OP |
| `nexusprism.admin.waila` | Admin WAILA tooltip commands | OP |
| `nexusprism.bypass.protection` | Bypass all region protections | OP |
| `nexusprism.bypass.ore-heuristic` | Bypass anti X-ray ore heuristic | OP |
| `nexusprism.db` | DB diagnostic access | OP |

---

> **Removed 2026-08-06:** the old `Research`, `Machines`, and `Backpacks` permission sections
> described dead systems with no remaining code (see `modules/core.md`). Item/machine
> permissions now belong to NexusATS.

---

## Waypoints

| Permission | Slots | Default |
| --- | --- | --- |
| `nexusprism.essentials.waypoints.1` | 1 waypoint | true |
| `nexusprism.essentials.waypoints.5` | 5 waypoints | — |
| `nexusprism.essentials.waypoints.25` | 25 waypoints | — |
| `nexusprism.essentials.waypoints.unlimited` | Unlimited | OP |
| `nexusprism.essentials.waypoint` | Access waypoint commands | true |

---

## Homes

| Permission | Slots | Default |
| --- | --- | --- |
| `nexusprism.essentials.homes.1` | 1 home | true |
| `nexusprism.essentials.homes.3` | 3 homes | — |
| `nexusprism.essentials.homes.10` | 10 homes | — |
| `nexusprism.essentials.homes.unlimited` | Unlimited | OP |
| `nexusprism.essentials.home` | Use /home, /sethome, /delhome | true |

---

## Essentials Commands

| Permission | Command | Default |
| --- | --- | --- |
| `nexusprism.essentials.warp.use` | `/warp` | true |
| `nexusprism.essentials.warp.admin` | `/setwarp`, `/delwarp` | OP |
| `nexusprism.essentials.back` | `/back` | true |
| `nexusprism.essentials.tpa` | `/tpa`, `/tpaccept`, `/tpdeny` | true |
| `nexusprism.essentials.spawn` | `/spawn` | true |
| `nexusprism.essentials.spawn.others` | `/spawn <player>` | OP |
| `nexusprism.essentials.setspawn` | `/setspawn` | OP |
| `nexusprism.essentials.tphere` | `/tphere` | OP |
| `nexusprism.essentials.tppos` | `/tppos` | OP |
| `nexusprism.essentials.near` | `/near` | true |
| `nexusprism.essentials.fly` | `/fly` (self) | false |
| `nexusprism.essentials.fly.others` | `/fly <player>` | OP |
| `nexusprism.essentials.hat` | `/hat` | false |
| `nexusprism.essentials.god` | `/god` (self) | OP |
| `nexusprism.essentials.god.others` | `/god <player>` | OP |
| `nexusprism.essentials.heal` | `/heal` (self) | OP |
| `nexusprism.essentials.heal.others` | `/heal <player>` | OP |
| `nexusprism.essentials.feed` | `/feed` (self) | OP |
| `nexusprism.essentials.feed.others` | `/feed <player>` | OP |
| `nexusprism.essentials.nick` | `/nick` (self) | false |
| `nexusprism.essentials.nick.others` | `/nick <player>` | OP |
| `nexusprism.essentials.afk` | `/afk` | true |
| `nexusprism.essentials.workbench` | `/workbench` | true |
| `nexusprism.essentials.trash` | `/trash` | true |
| `nexusprism.essentials.anvil` | `/anvil` | OP |
| `nexusprism.essentials.grindstone` | `/grindstone` | OP |
| `nexusprism.essentials.stonecutter` | `/stonecutter` | OP |
| `nexusprism.essentials.speed` | `/speed` | OP |
| `nexusprism.essentials.seen` | `/seen` | true |
| `nexusprism.essentials.clearinventory` | `/clearinventory` (self) | OP |
| `nexusprism.essentials.clearinventory.others` | `/clearinventory <player>` | OP |
| `nexusprism.essentials.getpos` | `/getpos` | true |
| `nexusprism.essentials.playtime` | `/playtime` | true |
| `nexusprism.essentials.gamemode` | `/gamemode` | OP |
| `nexusprism.essentials.enderchest` | `/enderchest` (self) | true |
| `nexusprism.essentials.enderchest.others` | `/enderchest <player>` | OP |
| `nexusprism.essentials.repair` | `/repair` (held item) | OP |
| `nexusprism.essentials.repair.all` | `/repair all` (full inventory) | OP |
| `nexusprism.essentials.ext` | `/ext` (self) | OP |
| `nexusprism.essentials.ext.others` | `/ext <player>` | OP |
| `nexusprism.essentials.exp` | `/exp` | OP |
| `nexusprism.essentials.worth` | `/worth` | true |
| `nexusprism.essentials.rules` | `/rules` | true |
| `nexusprism.essentials.skull` | `/skull` | OP |
| `nexusprism.essentials.jail.admin` | Jail management | OP |

---

## Economy

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.economy.money` | View money balance | true |
| `nexusprism.economy.baltop` | View leaderboard | true |
| `nexusprism.economy.sell` | Use `/sell` | true |
| `nexusprism.economy.admin` | Admin eco commands | OP |
| `nexusprism.economy.ah.use` | Use Auction House `/ah` | true |
| `nexusprism.economy.shop.create` | Create chest shops | true |
| `nexusprism.economy.shop.admin` | Admin chest shop management | OP |

### Player Warps

| Permission | Warps | Default |
| --- | --- | --- |
| `nexusprism.economy.playerwarp.use` | Browse and visit player warps | true |
| `nexusprism.economy.playerwarp.3` | Create up to 3 player warps | — |
| `nexusprism.economy.playerwarp.10` | Create up to 10 player warps | — |
| `nexusprism.economy.playerwarp.unlimited` | Unlimited player warps | OP |
| `nexusprism.economy.playerwarp.admin` | Admin player warp management | OP |

---

## Clans

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.clan.use` | Use clan commands | true |
| `nexusprism.clan.admin` | Admin clan management | OP |
| `nexusprism.clan.bypass-protection` | Bypass clan territory protection | OP |
| `nexusprism.clans.bypass` | Bypass all clan checks | OP |

---

## Security

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.security.cleanworld` | Manual world cleaner | OP |
| `nexusprism.security.notify` | Receive security alerts (IP, auth) | OP |
| `nexusprism.staff.vanish` | Vanish yourself | OP |
| `nexusprism.staff.vanish.others` | Vanish another player | OP |
| `nexusprism.staff.vanish.see` | See vanished players | OP |
| `nexusprism.staff.invsee` | Inspect inventories | OP |
| `nexusprism.staff.spy` | Chat spy mode | OP |

---

## Chat

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.chat.staff` | Access staff chat channel | OP |
| `nexusprism.chat.mute` | Mute players | OP |
| `nexusprism.chat.mute.bypass` | Bypass mute | false |
| `nexusprism.chat.filter.bypass` | Bypass word filter | OP |
| `nexusprism.chat.reload` | Reload chat config | OP |
| `nexusprism.chat.color` | Use color codes in chat | OP |

---

## Protections & Duel

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.region.use` | Create and manage own regions | true |
| `nexusprism.region.bypass` | Bypass region build/interact restrictions | OP |
| `nexusprism.protect.admin` | Admin region management | OP |
| `nexusprism.duel.use` | Send and accept duels | true |

---

## Events

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.events.bloodmoon.admin` | Control Blood Moon manually | OP |
| `nexusprism.events.isekai.admin` | Control Isekai boss fights manually | OP |

---

## Crystal Defense

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.crystaldefense.use` | Join arenas | true |
| `nexusprism.crystaldefense.admin` | Create/manage arenas | OP |

---

## Crates

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.crates.use` | Open crates | true |
| `nexusprism.crates.admin` | Admin crate management | OP |

---

## RNG & Daily Spin

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.rng.spin` | Use `/dailyspin` | true |
| `nexusprism.rng.admin` | Admin RNG commands | OP |

---

## Enchantments

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.enchantments.admin` | Admin enchantment commands | OP |

---

## Holograms

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.holograms.admin` | Create/edit/delete holograms | OP |

---

## TAB

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.tab.admin` | Reload TAB config | OP |

---

## Traits

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.traits.admin` | Admin trait management | OP |

---

## Votifier

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.vote` | Use `/vote` | true |
| `nexusprism.vote.top` | Use `/votetop` | true |

---

## Custom Mobs

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.boss.admin` | All boss/spawn-egg commands | OP |

---

## Dreams

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.dreams.admin` | Admin dreams commands | OP |

---

## Twitch

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.twitch.use` | Basic Twitch commands | true |
| `nexusprism.twitch.staff` | Approve links, run giveaways | OP |
| `nexusprism.twitch.admin` | Reload Twitch config | OP |

---

## Silk Spawners

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.silkspawner.use` | Mine spawners with Silk Touch | true |
| `nexusprism.silkspawner.upgrade` | Upgrade spawner mob level | OP |
| `nexusprism.silkspawner.admin` | Admin spawner commands | OP |

---

## Recipes & Kits

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.recipe` | Use `/recipe` | true |
| `nexusprism.command.kit` | Use `/kit` | true |
| `nexusprism.command.vip` | Use `/vip` | true |
| `nexusprism.kit.*` | Access all VIP kits | OP |

---

## Permission Level Nodes

Used by LuckPerms to assign staff ranks. Configure groups in your LP config and assign the appropriate node.

| Permission | Rank |
| --- | --- |
| `nexusprism.level.user` | Regular player |
| `nexusprism.level.helper` | Helper |
| `nexusprism.level.moderator` | Moderator |
| `nexusprism.level.admin` | Admin |
| `nexusprism.level.owner` | Owner |

---

## Tier Nodes

Used to gate store/rank features by tier. Assign in LuckPerms based on the player's purchased rank.

| Permission | Tier |
| --- | --- |
| `nexusprism.tier.basic` | Basic tier |
| `nexusprism.tier.1` | Tier 1 |
| `nexusprism.tier.2` | Tier 2 |
| `nexusprism.tier.3` | Tier 3 |
| `nexusprism.tier.4` | Tier 4 |
| `nexusprism.tier.5` | Tier 5 |
| `nexusprism.tier.intermediate` | Intermediate tier |
| `nexusprism.tier.enhanced` | Enhanced tier |
| `nexusprism.tier.advanced` | Advanced tier |
| `nexusprism.tier.supreme` | Supreme tier |

---

## LuckPerms Suggested Group Setup

Minimal LP group configuration for a typical NexusPrism server:

```yaml
# groups: user → helper → moderator → admin → owner
# Each group inherits from the one below via LP inheritance.

user:
  - nexusprism.level.user
  - nexusprism.tier.basic
  - nexusprism.essentials.homes.1
  - nexusprism.essentials.waypoints.1

vip:
  - nexusprism.level.user
  - nexusprism.tier.1
  - nexusprism.essentials.homes.3
  - nexusprism.essentials.waypoints.5
  - nexusprism.essentials.fly
  - nexusprism.essentials.hat
  - nexusprism.essentials.nick

vip_plus:
  - nexusprism.tier.2
  - nexusprism.essentials.homes.10
  - nexusprism.essentials.waypoints.25
  - nexusprism.economy.playerwarp.3

premium:
  - nexusprism.tier.3
  - nexusprism.essentials.homes.unlimited
  - nexusprism.essentials.waypoints.unlimited
  - nexusprism.economy.playerwarp.10

helper:
  - nexusprism.level.helper
  - nexusprism.chat.mute
  - nexusprism.staff.vanish
  - nexusprism.staff.vanish.see
  - nexusprism.staff.invsee

moderator:
  - nexusprism.level.moderator
  - nexusprism.staff.spy
  - nexusprism.protect.admin
  - nexusprism.security.notify

admin:
  - nexusprism.level.admin
  - nexusprism.admin
  - nexusprism.bypass.protection

owner:
  - nexusprism.level.owner
  - nexusprism.*
```

> **Note:** Inherit groups with `/lp group <child> parent add <parent>` and assign players with `/lp user <player> group set <group>`.
