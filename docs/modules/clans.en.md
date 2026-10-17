# Clans Module

The Clans module lets players create persistent teams with **territory claiming**, **upgrade trees**, a **shared clan chest**, and **clan chat**.

---

## Overview

- Players create or join clans using `/clan`
- Clans can claim chunks as territory
- Territory protects against non-member interaction (configurable)
- Clans level up through the upgrade tree (more members, more chunks)
- A shared clan chest GUI stores items for all members

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/clan create <name> <tag>` | Create a new clan | `nexusprism.clan.use` |
| `/clan disband` | Disband your clan | `nexusprism.clan.use` |
| `/clan invite <player>` | Invite a player | `nexusprism.clan.use` |
| `/clan join <name>` | Join a clan by invite | `nexusprism.clan.use` |
| `/clan leave` | Leave your clan | `nexusprism.clan.use` |
| `/clan kick <player>` | Kick a member | `nexusprism.clan.use` |
| `/clan promote <player>` | Promote to officer | `nexusprism.clan.use` |
| `/clan demote <player>` | Demote to member | `nexusprism.clan.use` |
| `/clan info [name]` | View clan info | `nexusprism.clan.use` |
| `/clan list` | List all clans | `nexusprism.clan.use` |
| `/clan chat` | Toggle clan chat | `nexusprism.clan.use` |
| `/clan claim` | Claim current chunk | `nexusprism.clan.use` |
| `/clan unclaim` | Unclaim current chunk | `nexusprism.clan.use` |
| `/clan map` | Show territory map | `nexusprism.clan.use` |
| `/clan chest` | Open clan chest | `nexusprism.clan.use` |
| `/clan upgrade` | Open upgrade menu | `nexusprism.clan.use` |
| `/clan top` | Clan leaderboard | `nexusprism.clan.use` |
| `/clan ally <clan>` | Send or accept an alliance request | `nexusprism.clan.use` |
| `/clan ally remove <clan>` | Remove an alliance | `nexusprism.clan.use` |
| `/clan enemy <clan>` | Mark a clan as an enemy | `nexusprism.clan.use` |
| `/clan enemy remove <clan>` | Remove enemy status | `nexusprism.clan.use` |
| `/clan admin disband <name>` | Force-disband (admin) | `nexusprism.clan.admin` |
| `/clan admin unclaim <name>` | Force-unclaim (admin) | `nexusprism.clan.admin` |

---

## Roles

| Role | Permissions |
| --- | --- |
| **Owner** | All actions, disband, upgrade |
| **Officer** | Invite, kick members, manage territory |
| **Member** | Access chest, chat, use territory |

---

## Territory System

Clans claim chunks as territory. Members can build freely; non-members are blocked (when protection is enabled).

### Territory Configuration (`clans/config.yml`)

```yaml
pvp-friendly-fire: false       # Members cannot damage each other

clan-name-min-length: 3
clan-name-max-length: 16
clan-tag-min-length: 2
clan-tag-max-length: 4

base-member-cap: 10            # Members at level 1
base-territory-cap: 10         # Claimable chunks at level 1

neutral-chunk-protection: false # Protect unclaimed chunks from outsiders

territory-worlds:
  - world
  - world_nether
```

---

## Upgrade Tree (`clans/upgrades.yml`)

Clans spend resources to unlock upgrades across **8 upgrade paths**.

| Upgrade Key | Description |
| --- | --- |
| `member_cap` | Increase the maximum number of clan members |
| `territory_cap` | Claim additional chunks as territory |
| `chest_size` | Expand the shared clan chest capacity |
| `home_warps` | Unlock additional clan home warp points |
| `exp_boost` | Bonus XP multiplier for all clan members |
| `stacker_bonus` | Increased mob stacker drops for clan members |
| `bank_cap` | Raise the maximum clan bank balance |
| `ally_cap` | Allow more simultaneous alliances |

```yaml
upgrades:
  member_cap:
    display-name: "&aMember Expansion"
    description: "Increase maximum members by 5."
    max-level: 5
    cost-per-level:
      money: 5000
    bonus-per-level:
      members: 5

  territory_cap:
    display-name: "&aTerritory Expansion"
    description: "Claim 10 additional chunks per level."
    max-level: 10
    cost-per-level:
      money: 3000
    bonus-per-level:
      chunks: 10

  chest_size:
    display-name: "&aClan Chest Expansion"
    description: "Add 9 more slots to the clan chest."
    max-level: 6
    cost-per-level:
      money: 2000
    bonus-per-level:
      slots: 9

  home_warps:
    display-name: "&aHome Warps"
    description: "Unlock an additional clan home location."
    max-level: 3
    cost-per-level:
      money: 4000

  exp_boost:
    display-name: "&aEXP Boost"
    description: "Grant all members a bonus XP multiplier."
    max-level: 5
    cost-per-level:
      money: 6000

  stacker_bonus:
    display-name: "&aStacker Bonus"
    description: "Increase mob stacker loot drops for members."
    max-level: 5
    cost-per-level:
      money: 4000

  bank_cap:
    display-name: "&aBank Capacity"
    description: "Raise the maximum balance of the clan bank."
    max-level: 5
    cost-per-level:
      money: 8000

  ally_cap:
    display-name: "&aAlliance Slots"
    description: "Allow one additional clan alliance."
    max-level: 3
    cost-per-level:
      money: 5000
```

---

## Alliances & Enemies

Clans can form **alliances** (allied members can build in each other's territory) or declare **enemies** (for display and future PvP mechanics).

- Alliance requests must be accepted by the other clan leader/officer with `/clan ally <requesting-clan>`
- The number of simultaneous alliances is capped by the `ally_cap` upgrade
- Enemy status is one-sided and does not require confirmation

---

## Clan Chest

The clan chest is a shared GUI inventory accessible to all clan members. Its size grows with the `chest_slots` upgrade.

---

## Clan Chat

Toggle clan-only chat with `/clan chat`. Messages sent while in clan chat mode are only visible to clan members.

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.clan.use` | Use clan commands | true |
| `nexusprism.clan.admin` | Admin clan management | OP |
| `nexusprism.clan.bypass-protection` | Bypass clan territory protection | OP |

---

## PlaceholderAPI

| Placeholder | Description |
| --- | --- |
| `%nexusprism_clan_name%` | Player's clan name |
| `%nexusprism_clan_tag%` | Clan tag (e.g. `[TAG]`) |
| `%nexusprism_clan_role%` | Player's role in clan |
| `%nexusprism_clan_level%` | Clan level |
| `%nexusprism_clan_members%` | Online member count |
| `%nexusprism_clan_bank%` | Clan bank balance |

See the full [PlaceholderAPI reference](../reference/placeholders.md).
