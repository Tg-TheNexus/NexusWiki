# Economy Module

The Economy module provides a **single-currency system** (money), sell commands, a wealth leaderboard, and per-item sell price configuration.

---

## Overview

| Currency | Description |
| --- | --- |
| **Money** (`$`) | In-game currency earned from selling items, voting, jobs, etc. |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/money` | Check your balance | `nexusprism.economy.money` |
| `/money <player>` | Check another player's balance | `nexusprism.economy.money` |
| `/baltop` | Top 10 richest players | `nexusprism.economy.baltop` |
| `/sell hand` | Sell item in hand | `nexusprism.economy.sell` |
| `/sell all` | Sell all sellable items | `nexusprism.economy.sell` |
| `/sell inventory` | Sell entire inventory | `nexusprism.economy.sell` |
| `/worth [item]` | Check sell value of item | `nexusprism.essentials.worth` |
| `/eco give <player> <amount>` | Give money (admin) | `nexusprism.economy.admin` |
| `/eco take <player> <amount>` | Take money (admin) | `nexusprism.economy.admin` |
| `/eco set <player> <amount>` | Set balance (admin) | `nexusprism.economy.admin` |
| `/eco reset <player>` | Reset balance (admin) | `nexusprism.economy.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.economy.money` | Check balances | true |
| `nexusprism.economy.baltop` | View leaderboard | true |
| `nexusprism.economy.sell` | Use /sell commands | true |
| `nexusprism.economy.admin` | Admin eco commands | OP |

---

## Sell Prices (`economy/sell-prices.yml`)

Configure per-material sell prices used by `/sell` and `/worth`.

```yaml
prices:
  # ── Stone & Earth ──────────────────────────────────────────────
  COBBLESTONE:       2.0
  STONE:             3.0
  DIRT:              1.0
  GRAVEL:            1.5
  SAND:              2.0

  # ── Wood & Plants ──────────────────────────────────────────────
  OAK_LOG:           6.0
  SPRUCE_LOG:        6.0
  WHEAT:             4.0
  SUGAR_CANE:        3.0

  # ── Ores & Metals ──────────────────────────────────────────────
  COAL:             10.0
  RAW_IRON:         15.0
  IRON_INGOT:       25.0
  RAW_GOLD:         30.0
  GOLD_INGOT:       50.0
  DIAMOND:         200.0
  EMERALD:         100.0
  NETHERITE_INGOT: 1200.0

  # ── Mob Drops ──────────────────────────────────────────────────
  BONE:              5.0
  ROTTEN_FLESH:      2.0
  BLAZE_ROD:        20.0
  ENDER_PEARL:      25.0
  SHULKER_SHELL:   150.0
  HEART_OF_THE_SEA: 500.0

  # Set to 0 or omit to make an item unsellable
  BEDROCK:           0.0
```

!!! tip
    Use Material names (Bukkit uppercase). Items not listed in `sell-prices.yml` cannot be sold. Custom NexusPrism items can also be added by their item ID.

---

## PlaceholderAPI

| Placeholder | Description |
| --- | --- |
| `%nexusprism_money%` | Player's money balance |


See the full [PlaceholderAPI reference](../reference/placeholders.md).

---

## Jobs

Players choose a job and earn money and XP by performing related in-game activities.

### Available Jobs

| Job | Primary Activities |
| --- | --- |
| **Miner** | Breaking ores and stone |
| **Hunter** | Killing hostile mobs |
| **Farmer** | Breaking crops |
| **Fisher** | Catching fish |
| **Smith** | Smelting ingots, crafting tools/armor |
| **Enchanter** | Enchanting items |
| **Alchemist** | Brewing potions |
| **Lumberjack** | Chopping logs |

Players can only hold **one job at a time**. Job configurations are YAML files under `economy/jobs/`.

### Pay & XP Formulas

| Value | Formula |
| --- | --- |
| **Pay per action** | `base × (1 + level × payScalePerLevel)` |
| **XP to next level** | `baseXpToLevel × 2^((level-1)/10)` *(doubles every 10 levels)* |

### Commands

| Command | Description | Permission |
| --- | --- | --- |
| `/job` | Open Job Browser GUI | `nexusprism.economy.job.use` |
| `/job join <id>` | Join a job | `nexusprism.economy.job.use` |
| `/job leave` | Leave current job | `nexusprism.economy.job.use` |
| `/job info [id]` | View job stats | `nexusprism.economy.job.use` |
| `/job top` | Job leaderboard | `nexusprism.economy.job.use` |

!!! note "Blood Moon Bonus"
    During a Blood Moon, the **Hunter** job's kill-pay is multiplied (default ×1.5). See the [Events module](events.md).

---

## Chest Shops

Players can create in-world shops by placing a sign on (or adjacent to) a chest.

### Creating a Shop

1. Place a chest
2. Place a sign on the front face, top face, or an adjacent block
3. Write `[Shop]` on the **first line**
4. Write `BUY <price>` on line 2 (optional)
5. Write `SELL <price>` on line 3 (optional)

The plugin auto-detects the chest below or wall-adjacent to the sign. Stock level is shown automatically on line 4.

### Sign Format

```
[Shop]
BUY 50
SELL 25
[12 in stock]
```

### Shop GUI

A 3-row GUI opens when a player right-clicks the sign:

| Slot | Contents |
| --- | --- |
| Centre (slot 13) | Item preview |
| Slots 19–21 | Buy ×1 / ×8 / ×64 |
| Slots 23–25 | Sell ×1 / ×8 / ×64 |

### Admin Shops

Admin shops have **unlimited stock** and are created by setting the owner UUID to `null` internally. Use `nexusprism.economy.shop.admin` to create them.

### Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.economy.shop.create` | Create player chest shops | true |
| `nexusprism.economy.shop.admin` | Create admin (unlimited stock) shops | OP |

---

## Player Warps

Players can set named warp points that any other player can visit.

### Commands

| Command | Description |
| --- | --- |
| `/pw set <name>` | Create a warp at your current location |
| `/pw delete <name>` | Remove one of your warps |
| `/pw desc <name> <text>` | Set a description for the warp |
| `/pw icon <name> <material>` | Set the icon shown in the GUI |
| `/pw list` | Browse all player warps (paginated 6-row GUI) |
| `/pw visit <player> <name>` | Teleport to another player's warp |

### Warp Limits

| Permission | Max Warps |
| --- | --- |
| `nexusprism.economy.playerwarp.unlimited` | Unlimited |
| `nexusprism.economy.playerwarp.10` | 10 |
| `nexusprism.economy.playerwarp.3` | 3 |
| *(default)* | 1 |

---

## Auction House

A global listing board where players buy and sell items with each other.

### How It Works

- List any item from your hand with `/ah sell <price>`
- Listings expire after **7 days** if unsold
- Expired or cancelled items are returned to the owner (hourly cleanup)
- Each player can have up to **10 active listings** at once

### Commands

| Command | Description | Permission |
| --- | --- | --- |
| `/ah` | Browse active listings (6-row paginated GUI) | `nexusprism.economy.ah.use` |
| `/ah sell <price>` | List held item at a price | `nexusprism.economy.ah.use` |
| `/ah own` | View your listings; cancel active or reclaim expired | `nexusprism.economy.ah.use` |
| `/ah cancel <id>` | Cancel a listing by its ID | `nexusprism.economy.ah.use` |
