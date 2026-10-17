# TAB Module

The TAB module customizes the **player list** (TAB overlay) with formatted headers, footers, ping display, LuckPerms rank prefixes, animated scoreboards, and MOTD customization.

---

## Features

| Feature | Description |
| --- | --- |
| **Header / Footer** | Animated multi-line header and footer with PlaceholderAPI support |
| **Name Formatting** | Player names in the TAB list show their LuckPerms rank prefix and suffix |
| **Ping Display** | Colored ping indicator next to each player's name |
| **Scoreboards** | Per-player sidebar scoreboard with configurable lines and PAPI placeholders |
| **MOTD Customization** | Server list MOTD configurable per-world or globally |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/ntab reload` | Reload TAB configuration | `nexusprism.tab.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.tab.admin` | Reload TAB configuration | OP |

---

## Configuration (`tab/config.yml`)

```yaml
tab:
  enabled: true

  # Header and footer shown in the player list overlay
  # Supports & color codes and PlaceholderAPI placeholders
  header:
    - ""
    - "&b&lNexusPrism &8— &7Skyblock"
    - ""
  footer:
    - ""
    - "&7Online: &f%server_online% &8/ &f%server_max_players%"
    - "&7Ping: &f%player_ping%ms"
    - ""

  # Name format for each player entry in the list
  # {prefix} = LuckPerms rank prefix, {name} = player name, {suffix} = rank suffix
  name-format: "{prefix}&f{name}{suffix}"

  # Show ping as colored text next to the player's name
  ping-display:
    enabled: true
    format: "&8[{ping}ms]"
    thresholds:
      good: 80        # Below this = green
      medium: 150     # Below this = yellow; above = red

scoreboard:
  enabled: true
  title: "&b&lNexusPrism"
  update-ticks: 20   # Refresh rate (20 ticks = 1 second)
  lines:
    - ""
    - "&7Player: &f%player_name%"
    - "&7Money: &a$%nexusprism_money%"
    - "&7Clan: &b%nexusprism_clan_name%"
    - ""
    - "&enexusprism.blazebr.com"
    - ""

motd:
  enabled: false
  lines:
    - "&b&lNexusPrism &r&7— Skyblock MMO"
    - "&7Join and explore!"
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `tab.header` / `tab.footer` | Lines displayed above/below the player list. Supports `&` color codes and PlaceholderAPI. |
| `tab.name-format` | Format for each player's name in the list. Use `{prefix}`, `{name}`, `{suffix}`. |
| `ping-display.thresholds` | Ping values (ms) used to switch between green/yellow/red coloring. |
| `scoreboard.title` | Title text shown at the top of the sidebar scoreboard. |
| `scoreboard.lines` | List of scoreboard lines (top to bottom). Supports PlaceholderAPI. |
| `scoreboard.update-ticks` | How often the scoreboard refreshes. 20 ticks = 1 second. |
| `motd.lines` | Two-line server list description. Supports `&` color codes. |

---

## PlaceholderAPI

The TAB module works with any PlaceholderAPI placeholder in header, footer, and scoreboard lines. See the [PlaceholderAPI reference](../reference/placeholders.md) for all available `%nexusprism_*%` placeholders.
