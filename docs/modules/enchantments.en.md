# Enchantments Module

The Enchantments module adds **175 custom enchantments** across 6 rarity tiers and 10 trigger types. All enchants are defined in `enchants/config.yml` — no Java code required to add new ones.

---

## Rarities

| Rarity | Color | XP Cost | Weight |
| --- | --- | --- | --- |
| **Common** | White `§f` | 3 XP | 100 |
| **Uncommon** | Green `§a` | 8 XP | 50 |
| **Rare** | Blue `§9` | 15 XP | 20 |
| **Epic** | Purple `§5` | 25 XP | 8 |
| **Legendary** | Gold `§6` | 40 XP | 3 |
| **Mythic** | Red `§c` | 60 XP | 1 |

---

## Trigger Types

| Trigger | When it fires |
| --- | --- |
| `ON_HIT` | When the player deals melee damage |
| `ON_KILL` | When the player kills an entity |
| `ON_MINE` | When the player breaks a block |
| `ON_BREAK` | When the player's item is about to break |
| `ON_DEATH` | When the player dies |
| `ON_DAMAGE_TAKEN` | When the player takes damage |
| `PASSIVE` | Runs continuously on a tick task |
| `ON_JUMP` | When the player jumps |
| `ON_SHOOT` | When the player fires a projectile |
| `VOID` | Fires when the player falls below Y=0 |

---

## Applicable Item Groups

Enchants specify which item types they can be applied to via `applicable-items:`.

`ANY`, `SWORD`, `AXE`, `PICKAXE`, `SHOVEL`, `HOE`, `BOW`, `CROSSBOW`, `TRIDENT`, `FISHING_ROD`, `HELMET`, `CHESTPLATE`, `LEGGINGS`, `BOOTS`, `ARMOR`, `ELYTRA`

---

## Commands

All commands require `nexusprism.enchantments.admin`.

| Command | Description |
| --- | --- |
| `/enchant list` | List all enchants with ID, rarity, and status |
| `/enchant info <id>` | Show details: max level, item groups, conflicts |
| `/enchant give <player> <id> [level]` | Give an enchant book to a player |
| `/enchant apply <id> [level]` | Apply an enchant directly to the held item |
| `/enchant remove <id>` | Remove an enchant from the held item |
| `/enchant reload` | Reload `enchants/config.yml` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.enchantments.admin` | All enchantment management commands | OP |

---

## Configuration (`enchants/config.yml`)

### Rarity Groups

```yaml
groups:
  COMMON:
    color: "§f"
    display: "Common"
    buy-price-xp: 3
    weight: 100
  UNCOMMON:
    color: "§a"
    display: "Uncommon"
    buy-price-xp: 8
    weight: 50
  # RARE, EPIC, LEGENDARY, MYTHIC follow the same format
```

### Obtain Settings

```yaml
obtain-defaults:
  enchanting-table: true    # Can appear in the enchanting table
  random-loot: true         # Can appear in chest loot
  villager-trading: false
  mob-equipment: false
```

### Enchant Definition

```yaml
enchants:
  lifesteal:
    enabled: true
    display-name: "&cLifesteal"
    rarity: UNCOMMON
    trigger: ON_HIT
    max-level: 3
    applicable-items: [SWORD, AXE]
    conflicts: []              # Other custom enchant IDs that conflict
    vanilla-conflicts: []      # Vanilla enchantment names that conflict
    heal-percent-per-level: 0.10   # Custom effect parameter (10% HP per level)
```

| Field | Description |
| --- | --- |
| `enabled` | Set to `false` to disable without removing the entry |
| `rarity` | One of the 6 rarity tiers |
| `trigger` | When the enchant effect fires |
| `max-level` | Highest level the enchant can reach |
| `applicable-items` | List of item group IDs this enchant can be applied to |
| `conflicts` | Custom enchant IDs that cannot coexist with this one |
| `vanilla-conflicts` | Vanilla enchantment names that conflict |

---

## How Enchant Books Work

- Right-clicking an enchant book applies it to the item in the **offhand slot**
- Enchants are stored via **PDC** (Persistent Data Container) with key `enchant_<id>`
- Applied enchants appear in the item lore as `<Color><Name> <Roman numeral> §8[Enchant]`
- The enchanting table can offer custom enchants when `obtain-defaults.enchanting-table: true`
