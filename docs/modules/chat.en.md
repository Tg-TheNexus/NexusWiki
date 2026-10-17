# Chat Module

The Chat module replaces the default Minecraft chat with a **4-channel system** — local, global, staff, and report — each with configurable radius, format, and LuckPerms rank prefix integration.

---

## Channels

| Channel | Trigger | Audience | Description |
| --- | --- | --- | --- |
| **Local** | Default (no prefix) | Players within radius | Standard proximity-based chat |
| **Global** | `!<message>` or `/g` | All online players | Server-wide broadcast |
| **Staff** | `/staffchat` or `/sc` | Staff only | Private staff communication channel |
| **Report** | `/report <player> <reason>` | Staff only | Player-submitted reports, delivered to staff |

---

## Commands

| Command | Aliases | Usage | Permission |
| --- | --- | --- | --- |
| `/globalchat <message>` | `/g`, `/gc` | Send a message to all players | `nexusprism.chat.global` |
| `/staffchat <message>` | `/sc` | Send a message to staff | `nexusprism.chat.staff` |
| `/report <player> <reason>` | — | Report a player to staff | `nexusprism.chat.report` |
| `/chat reload` | — | Reload chat configuration | `nexusprism.chat.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.chat.global` | Use global chat channel | true |
| `nexusprism.chat.staff` | Access staff chat channel | OP |
| `nexusprism.chat.report` | Submit player reports | true |
| `nexusprism.chat.admin` | Reload chat configuration | OP |

---

## Configuration (`chat/config.yml`)

```yaml
chat:
  local:
    radius: 100          # Blocks — 0 for global local chat (same as global)
    format: "{prefix}&f{name}&7: &f{message}"

  global:
    format: "&8[&bGlobal&8] {prefix}&f{name}&7: &f{message}"
    trigger-prefix: "!"  # Start a message with ! to send globally

  staff:
    format: "&8[&cStaff&8] &7{name}&7: &c{message}"

  report:
    format: "&8[&6Report&8] &e{reporter}&7 reported &c{target}&7: &f{reason}"

  # Integrate LuckPerms rank prefixes into chat format
  luckperms-prefix:
    enabled: true
    # {prefix} in format strings is replaced with the player's LuckPerms prefix
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `local.radius` | Maximum distance (blocks) for local chat. Set to `0` to make local reach all players. |
| `local.format` | Chat format for local messages. Supports `{prefix}`, `{name}`, `{message}`. |
| `global.trigger-prefix` | Character(s) that switch a local message to global (e.g. `!hello` → global). |
| `luckperms-prefix.enabled` | When `true`, `{prefix}` in format strings is replaced with the LuckPerms rank prefix. |

---

## LuckPerms Integration

When LuckPerms is installed and `luckperms-prefix.enabled: true`, each player's rank prefix is automatically injected into the `{prefix}` placeholder in chat format strings. No extra configuration is needed — the module reads the prefix from LuckPerms at chat time.
