# Crates Module

The Crates module provides **key-based loot crates** with animated openings, idle particle effects, and per-crate configurable reward tables.

---

## How It Works

1. An admin places a block and registers it as a crate with `/crate setblock <id>`
2. A player receives crate keys (virtual or physical) via `/crate give`
3. The player right-clicks the crate block — the key is consumed and the opening animation plays
4. A random reward is selected and delivered

---

## Key Modes

Configured globally in `crates/config.yml`:

| Mode | Description |
| --- | --- |
| `VIRTUAL` *(default)* | Keys stored in the database — dupe-proof, no inventory item |
| `PHYSICAL` | Keys are `TRIPWIRE_HOOK` items with a PDC tag matching the crate ID |

---

## Commands

| Command | Permission | Description |
| --- | --- | --- |
| `/crate give <player> <crate> [amount]` | `nexusprism.crates.admin` | Give crate keys to a player |
| `/crate keys [player]` | `nexusprism.crates.use` | View virtual key balance |
| `/crate setblock <crate>` | `nexusprism.crates.admin` | Register the targeted block as a crate |
| `/crate removeblock` | `nexusprism.crates.admin` | Unregister the targeted block |
| `/crate preview <crate>` | *(all players)* | Preview possible rewards |
| `/crate list` | *(all players)* | List all crate types |
| `/crate reload` | `nexusprism.crates.admin` | Reload all crate definitions |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.crates.admin` | Create, remove, and give crates | OP |
| `nexusprism.crates.use` | Check key balance | true |

---

## Configuration

### Global Config (`crates/config.yml`)

```yaml
key-mode: VIRTUAL        # VIRTUAL | PHYSICAL
```

### Crate Definition (`crates/<id>.yml`)

Each crate has its own YAML file. Default crates bundled: `common.yml`, `rare.yml`, `legendary.yml`.

```yaml
display-name: "&aCommon Crate"
block-material: WHITE_SHULKER_BOX   # Visual block type for the placed crate

broadcast-wins: false               # Announce rare wins server-wide
preview: true                       # Allow /crate preview

opening:
  mode: SPIN                        # SPIN (animated reel) | INSTANT
  firework: false                   # Launch a firework on win

particles:
  idle:
    type: END_ROD
    count: 5
  win:
    type: FIREWORK
    count: 30

rewards:
  - type: ITEM
    data: IRON_INGOT
    amount: 8
    weight: 30
    display-name: "&78x Iron Ingot"
  - type: MONEY
    data: "500"
    weight: 25
    display-name: "&a$500"
  - type: COMMAND
    data: "give {player} minecraft:diamond 1"
    weight: 5
    display-name: "&bBonus Diamond"
```

### Reward Types

| Type | `data` field | Notes |
| --- | --- | --- |
| `ITEM` | `Material` name | `amount` sets quantity |
| `MONEY` | Amount as string | Requires Economy module |
| `COMMAND` | Command string | `{player}` replaced with player name |

!!! info "Placed crate locations"
    Crate block positions are saved in SQLite. They survive server restarts — you only need to run `/crate setblock` once per block.
