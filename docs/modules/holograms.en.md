# Holograms Module

The Holograms module creates **floating text and item displays** in the world, backed by `TextDisplay` and `ItemDisplay` entities. All holograms are defined in `holograms.yml` and survive server restarts.

---

## Line Types

| Type | Description |
| --- | --- |
| `TEXT` | Formatted text line. Supports `&` color codes and PlaceholderAPI. |
| `ITEM` | Floating item icon (any `Material`). |
| `HEAD` | Player skull (fetches skin asynchronously). |

Lines are stacked upward with 0.3-block spacing. Line `0` is the topmost line.

---

## Commands

All subcommands require `nexusprism.holograms.admin`.

| Command | Description |
| --- | --- |
| `/holo create <id>` | Create a hologram at your location |
| `/holo delete <id>` | Delete a hologram |
| `/holo addline <id> text <text…>` | Append a text line |
| `/holo addline <id> item <MATERIAL>` | Append an item display line |
| `/holo addline <id> head <player>` | Append a player skull line |
| `/holo setline <id> <line#> <text…>` | Replace a text line (0-based index) |
| `/holo removeline <id> <line#>` | Remove a line (0-based index) |
| `/holo move <id>` | Move hologram to your current location |
| `/holo list` | List all hologram IDs |
| `/holo info <id>` | Show world, coordinates, visibility, and lines |
| `/holo show <id> <player>` | Force a player to see a `PLAYERS`-mode hologram |
| `/holo hide <id> <player>` | Remove a player from the `PLAYERS` allowlist |
| `/holo reload` | Reload all holograms from `holograms.yml` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.holograms.admin` | All hologram management commands | OP |

---

## Visibility Modes

| Mode | Behavior |
| --- | --- |
| `GLOBAL` | Visible to all players |
| `PERMISSION` | Visible only to players with the node set in `permission:` |
| `PLAYERS` | Visible only to UUIDs listed in `allowed-players:` |

---

## Configuration (`holograms.yml`)

All holograms are stored and managed in a single `holograms.yml` file. Use commands to edit; the file is saved automatically on every change.

```yaml
# Example hologram
lobby-board:
  world: world
  x: 0.5
  y: 65.0
  z: 0.5
  visibility: GLOBAL        # GLOBAL | PERMISSION | PLAYERS
  permission: ""            # Required when visibility: PERMISSION
  allowed-players:          # UUIDs; required when visibility: PLAYERS
    - "550e8400-e29b-41d4-a716-446655440000"
  lines:
    - type: TEXT
      content: "&b&lTop Players"
    - type: HEAD
      player: "Notch"
    - type: TEXT
      content: "&71. &fNotch &7— &a1,200pts"
    - type: ITEM
      material: DIAMOND
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `world` | World name where the hologram is spawned |
| `x` / `y` / `z` | Position of the bottommost line |
| `visibility` | `GLOBAL`, `PERMISSION`, or `PLAYERS` |
| `permission` | Permission node (used when `visibility: PERMISSION`) |
| `allowed-players` | List of UUID strings (used when `visibility: PLAYERS`) |
| `lines[].type` | `TEXT`, `ITEM`, or `HEAD` |
| `lines[].content` | Text content (for `TEXT` lines); supports `&` color codes |
| `lines[].material` | Material name (for `ITEM` lines) |
| `lines[].player` | Player name (for `HEAD` lines) |

!!! tip
    Holograms are re-spawned from scratch on `/holo reload` and on server start. They use display entities — no armor stands involved.
