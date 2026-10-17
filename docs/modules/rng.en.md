# RNG Module

The RNG module provides **daily spin rewards**, **lucky blocks**, **gacha pulls** via Research Parchments, and **automatic server events** — all driven by configurable reward pools.

---

## Features

| Feature | Description |
| --- | --- |
| **Daily Spin** | Once-per-day reward wheel (`/spin`) |
| **Lucky Blocks** | Placeable PDC-tagged blocks that execute a random reward on break |
| **Gacha** | Right-click a Research Parchment to pull from a tier-gated reward pool |
| **Server Events** | Automatic timed buffs (Double Drops, Double XP, Mining Rush, etc.) |

---

## Commands

| Command | Permission | Description |
| --- | --- | --- |
| `/spin` | `nexusprism.rng.spin` | Open the daily spin GUI |
| `/rng event start <id>` | `nexusprism.rng.admin` | Force-start a server event |
| `/rng event stop` | `nexusprism.rng.admin` | Stop the active event |
| `/rng event list` | `nexusprism.rng.admin` | List all defined events |
| `/rng giveblock <player> [pool] [amount]` | `nexusprism.rng.admin` | Give lucky block items |
| `/rng giveparchment <player> <BASIC\|ADVANCED\|INFINITY>` | `nexusprism.rng.admin` | Give a Research Parchment |
| `/rng research get <player>` | `nexusprism.rng.admin` | Check a player's research level |
| `/rng research set <player> <level>` | `nexusprism.rng.admin` | Set a player's research level |
| `/rng reload` | `nexusprism.rng.admin` | Reload config, events, and reward pools |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.rng.spin` | Use the daily spin | true |
| `nexusprism.rng.admin` | All admin RNG commands | OP |

---

## Configuration (`rng/config.yml`)

```yaml
daily-spin:
  cooldown-seconds: 86400    # 24 hours between spins
  pool: daily                # Reward pool ID used for the spin

server-events:
  enabled: true
  interval-minutes: 90       # Random event fires every ~90 minutes

gacha:
  xp-per-pull: 1             # Research XP gained per gacha pull
```

---

## Reward Pools (`rng/pools/*.yml`)

All `.yml` files in the `pools/` folder are loaded automatically. Default pools: `daily` (for `/spin`) and `lucky` (for lucky blocks).

```yaml
pool-id: daily
rewards:
  - type: MONEY
    data: "500"
    weight: 30
    display-name: "&a$500"
  - type: ITEM
    data: DIAMOND
    amount: 3
    weight: 5
    display-name: "&b3x Diamond"
  - type: COMMAND
    data: "give {player} minecraft:totem_of_undying 1"
    weight: 1
    display-name: "&6Totem of Undying"
```

| Reward Type | `data` field | Notes |
| --- | --- | --- |
| `MONEY` | Amount as string (e.g. `"500"`) | Requires Economy module |
| `ITEM` | `Material` name | `amount` field sets quantity |
| `COMMAND` | Command string | `{player}` replaced with the player's name |

---

## Server Events (`rng/events.yml`)

```yaml
events:
  double_drops:
    display-name: "&a⚡ Double Drops!"
    type: DOUBLE_DROPS
    duration-seconds: 1800
    weight: 20
```

| Event Type | Effect |
| --- | --- |
| `DOUBLE_DROPS` | All block/mob drops are doubled |
| `DOUBLE_XP` | All XP gains are doubled |
| `MOB_RUSH` | Increased mob spawn rate server-wide |
| `MINING_RUSH` | Bonus drops from mining ores |
| `TRADING_BOOST` | Better villager trade prices |
| `HAPPY_HOUR` | Combined bonus (drops + XP) |
| `CUSTOM` | Triggers a custom command/broadcast only |

---

## Gacha (Research Parchments)

Research Parchments are items obtained from structure loot or given by admins. Right-clicking one triggers a gacha pull from a tier-gated pool.

| Parchment Tier | Pool | Min Research Level |
| --- | --- | --- |
| `BASIC` | `gacha_basic` | 0 |
| `ADVANCED` | `gacha_advanced` | 5 |
| `INFINITY` | `gacha_infinity` | 10 |

Each pull grants `gacha.xp-per-pull` Research XP. Reaching Research Level 5 and 10 unlocks higher-tier parchments. Gacha reward pools are defined in `rng/gacha.yml` under the `basic:`, `advanced:`, and `infinity:` sections (same format as reward pools above).
