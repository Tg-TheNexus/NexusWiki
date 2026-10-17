# Custom Mobs Module

The Custom Mobs module lets server admins define **YAML-based bosses** with custom health, equipment, potion effects, AI combat forms, loot tables, and spawn eggs — all without writing Java code.

---

## Overview

| Feature | Description |
| --- | --- |
| **YAML definitions** | Each boss is a single `.yml` file in `custommobs/bosses/` |
| **AI Forms** | Bosses switch between combat styles (SWORD, DAGGER, GLADIUS…) |
| **Equipment** | Full armor and weapon loadout |
| **Potion Effects** | Permanent effects applied to the boss |
| **Loot Tables** | Guaranteed drops and chance-based drops |
| **Spawn Eggs** | Custom spawn eggs crafted or given with `/bossegg` |
| **Persistent** | Bosses survive server restarts |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/boss spawn <id>` | Spawn a boss at your location | `nexusprism.boss.admin` |
| `/boss spawn <id> <world> <x> <y> <z>` | Spawn at coordinates | `nexusprism.boss.admin` |
| `/boss list` | List all registered bosses | `nexusprism.boss.admin` |
| `/boss info <id>` | Show boss definition details | `nexusprism.boss.admin` |
| `/boss kill <id>` | Kill all active instances of a boss | `nexusprism.boss.admin` |
| `/bossegg give <player> <id>` | Give a boss spawn egg | `nexusprism.boss.admin` |
| `/bossegg <id>` | Get your own boss spawn egg | `nexusprism.boss.admin` |

---

## Boss YAML Format

Boss files are placed in `plugins/NexusPrism/custommobs/bosses/<id>.yml`.

### Full Example (`white_death.yml`)

```yaml
name: "§uEchoes §tof §sthe §bWhite §fDeath"
entity: WITHER_SKELETON
health: 200.0
persistent: true

equipment:
  helmet:     GOLDEN_HELMET
  chestplate: GOLDEN_CHESTPLATE
  leggings:   GOLDEN_LEGGINGS
  boots:      GOLDEN_BOOTS
  main_hand:  DIAMOND_SWORD
  off_hand:   SHIELD

potion_effects:
  - SPEED:2

ai_forms:
  - type: SWORD
    weight: 5
  - type: DAGGER
    weight: 3
  - type: GLADIUS
    weight: 2

loot:
  always:
    - SHADOW_SHARD:1
    - SNOWBALL:5
    - ENCHANTED_BOOK:1
  chance:
    - item: FROZEN_DAGGER
      chance: 0.20
    - item: GLADIUS
      chance: 0.10

form_switch_interval_ticks: 300
```

### Field Reference

| Field | Type | Description |
| --- | --- | --- |
| `name` | String | Display name with `&`/`§` color codes |
| `entity` | Bukkit EntityType | Base entity type (e.g. `WITHER_SKELETON`, `ZOMBIE`) |
| `health` | Double | Max health in half-hearts |
| `persistent` | Boolean | If `true`, boss persists through chunk unloads/restarts |
| `equipment.*` | Material | Equipment slots: `helmet`, `chestplate`, `leggings`, `boots`, `main_hand`, `off_hand` |
| `potion_effects` | List | Permanent effects in `EFFECT:AMPLIFIER` format |
| `ai_forms` | List | Combat styles the boss alternates between |
| `ai_forms[].type` | String | AI form ID (`SWORD`, `DAGGER`, `GLADIUS`, etc.) |
| `ai_forms[].weight` | Integer | Relative weight for random selection |
| `loot.always` | List | Guaranteed drops in `ITEM_ID:amount` format |
| `loot.chance` | List | Chance-based drops with `item` and `chance` (0.0–1.0) |
| `form_switch_interval_ticks` | Integer | Ticks between AI form switches (300 = 15 seconds) |

### Loot Items

Both Bukkit `Material` names and NexusPrism custom item IDs can be used in loot tables:

```yaml
loot:
  always:
    - DIAMOND:3           # Vanilla material
    - NEXUS_SHARD:1       # Custom NexusPrism item ID
  chance:
    - item: BOSS_TROPHY
      chance: 0.05        # 5% drop chance
```

---

## AI Form Types

| Form | Description |
| --- | --- |
| `SWORD` | Aggressive melee, charges toward target |
| `DAGGER` | Fast hit-and-run attacks |
| `GLADIUS` | Balanced attack with shield bashing |

Custom AI forms can be added by creating addon modules using the `nexusprism-api`.

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.boss.admin` | All boss and spawn egg commands | OP |

---

## Spawn Egg Usage

Spawn eggs given with `/bossegg give <player> <id>` can be right-clicked in the world to spawn the boss. The egg item shows the boss name and a preview of its health in the lore.
