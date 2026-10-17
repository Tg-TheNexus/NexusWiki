# PlaceholderAPI Reference

NexusPrism registers its own PlaceholderAPI expansion under the `nexusprism` identifier. All placeholders follow the pattern `%nexusprism_<name>%`.

**Requires:** [PlaceholderAPI](https://www.spigotmc.org/resources/placeholderapi.6245/) (soft dependency — install separately)

---

## Economy

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_money%` | Player's current money balance | `12500.00` |

---

## Essentials

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_playtime%` | Total playtime (formatted) | `3d 12h 45m` |
| `%nexusprism_playtime_minutes%` | Total playtime in minutes | `5085` |
| `%nexusprism_homes%` | Number of homes set | `3` |
| `%nexusprism_afk%` | `true` if player is AFK | `false` |
| `%nexusprism_afk_status%` | Human-readable AFK status | `AFK` / `Online` |

---

## Clans

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_clan_name%` | Player's clan name | `Shadowborn` |
| `%nexusprism_clan_tag%` | Clan tag | `SHD` |
| `%nexusprism_clan_role%` | Player's role in clan | `Owner` / `Officer` / `Member` |
| `%nexusprism_clan_level%` | Clan's current level | `5` |
| `%nexusprism_clan_members%` | Online member count | `8` |
| `%nexusprism_clan_bank%` | Clan bank balance | `75000.00` |

Returns empty string if the player is not in a clan.

---

## Crystal Defense

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_crystal_wave%` | Current wave number | `7` |
| `%nexusprism_crystal_health%` | Crystal HP remaining | `680.0` |
| `%nexusprism_crystal_points%` | Player's kill points in current game | `145` |
| `%nexusprism_crystal_arena%` | Arena name the player is in | `arena1` |

Returns empty string if the player is not in a Crystal Defense game.

---

## Security

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_authenticated%` | `true` if the player is logged in | `true` |
| `%nexusprism_auth_status%` | Human-readable auth status | `Authenticated` / `Pending` |

---

## Votifier

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_votes_total%` | Total lifetime votes | `127` |
| `%nexusprism_vote_streak%` | Current vote streak length | `12` |

---

## Player Stats

⚠️ Item/machine/energy/research stat placeholders (blocks broken, machines placed, items
crafted, energy generated, research unlocked) were removed 2026-08-06 — the underlying
`player_stats` table and the systems that would feed it were confirmed dead (no code ever
persisted or fed those values; see `ECOSYSTEM.md`). Only generic player-level stats remain:

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_player_level%` | Player NexusPrism level | `15` |

---

## LuckPerms

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_lp_prefix%` | Player's LuckPerms prefix | `&6[VIP]` |
| `%nexusprism_lp_suffix%` | Player's LuckPerms suffix | `&7✦` |

These require LuckPerms to be installed.

---

## MMO

**Module required** (`nexusprism-mmo`).

| Placeholder | Returns | Notes |
| --- | --- | --- |
| `%nexusprism_mmo_level%` | MMO character level | integer |
| `%nexusprism_mmo_mana%` | Current mana | integer |
| `%nexusprism_mmo_mana_max%` | Maximum mana | integer |
| `%nexusprism_mmo_stat_points%` | Unspent stat points | integer |
| `%nexusprism_mmo_stat_strength%` | STRENGTH value | integer |
| `%nexusprism_mmo_stat_dexterity%` | DEXTERITY value | integer |
| `%nexusprism_mmo_stat_intelligence%` | INTELLIGENCE value | integer |
| `%nexusprism_mmo_stat_vitality%` | VITALITY value | integer |
| `%nexusprism_mmo_stat_endurance%` | ENDURANCE value | integer |
| `%nexusprism_mmo_stat_luck%` | LUCK value | integer |
| `%nexusprism_mmo_skill_<treeid>%` | Skill tree level | e.g. `mmo_skill_warrior` |
| `%nexusprism_mmo_profession_<profid>%` | Profession level | e.g. `mmo_profession_mining` |

---

## Events

`bloodmoon_*` resolve even without the Events module (returning `false` / `1.00`).

| Placeholder | Returns | Notes |
| --- | --- | --- |
| `%nexusprism_bloodmoon_active%` | `true` / `false` | server-wide |
| `%nexusprism_bloodmoon_multiplier%` | Kill-pay multiplier | `1.00` when inactive |
| `%nexusprism_sacrifice_streak%` | Survival streak | **Module required** |
| `%nexusprism_in_sacrifice%` | `true` / `false` | **Module required** |
| `%nexusprism_isekai_active%` | `true` / `false` | **Module required** |

---

## Traits & RNG

**Module required** (`nexusprism-traits`).

| Placeholder | Returns | Notes |
| --- | --- | --- |
| `%nexusprism_traits_research%` | Research/gacha level | integer |
| `%nexusprism_traits_count%` | Number of assigned trait cards | integer |
| `%nexusprism_traits_cards%` | Comma-separated card names | `none` if empty |

---

## Jobs

**Module required** (`nexusprism-economy`).

| Placeholder | Returns | Notes |
| --- | --- | --- |
| `%nexusprism_job%` | Active job ID | `none` if no job |
| `%nexusprism_job_level%` | Level in active job | `0` if no job |
| `%nexusprism_job_xp%` | XP in active job | `0` if no job |

---

## Discord

**Module required** (`nexusprism-discord`).

| Placeholder | Returns | Notes |
| --- | --- | --- |
| `%nexusprism_discord_linked%` | `true` / `false` | — |
| `%nexusprism_discord_id%` | Discord snowflake ID | empty string if not linked |

---

## Core / Misc

| Placeholder | Description | Example |
| --- | --- | --- |
| `%nexusprism_version%` | Plugin version string | `2.0.0-BETA` |
| `%nexusprism_player%` | Player username | `Steve` |
| `%nexusprism_uuid%` | Player UUID | `069a79f4-...` |

---

## Usage in Scoreboards / TAB

```yaml
# Example with TAB plugin
header: "&bNexusPrism &7%nexusprism_version%"
tablist-name: "%nexusprism_lp_prefix%%player_name%"
scoreboard:
  title: "&b&lYour Stats"
  lines:
    - "&7Money: &a$%nexusprism_money%"
    - "&7Votes: &e%nexusprism_votes_total% &7(streak: %nexusprism_vote_streak%)"
    - "&7Clan: &f%nexusprism_clan_name%"
    - "&7Playtime: &f%nexusprism_playtime%"
```
