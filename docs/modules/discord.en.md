# Discord Module

The Discord module provides a **JDA-powered bot** with Minecraft ↔ Discord chat bridging, player account linking, role synchronization, webhook delivery, and GitHub Actions monitoring.

---

## Features

| Feature | Description |
| --- | --- |
| **Chat Bridge** | Relay in-game chat to Discord channels and vice versa |
| **Account Linking** | Link Discord accounts to Minecraft accounts via DM |
| **Role Sync** | Assign Discord roles based on LuckPerms groups |
| **Webhooks** | Push player events (join, death, achievement) to Discord |
| **Mention Alerts** | Notify in-game players when mentioned on Discord |
| **GitHub Actions** | Monitor and trigger CI/CD workflows from Discord |
| **Server Vote** | Community-driven restart vote via Discord slash command |
| **Panel Control** | Admin start/stop commands via Pterodactyl API |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/discord` | Show Discord invite link | *(all players)* |
| `/discord link` | Start account linking process | *(all players)* |
| `/discord unlink` | Unlink your Discord account | *(all players)* |
| `/discord info` | Show your linked Discord account | *(all players)* |
| `/discordrr` | Manage reaction-role messages | `nexusprism.admin` |

---

## Setup

### 1. Create a Discord Bot

1. Go to [discord.com/developers/applications](https://discord.com/developers/applications)
2. Create a new Application → Bot
3. Copy the **Bot Token**
4. Enable **Message Content Intent** and **Server Members Intent**
5. Invite the bot to your server with `bot` + `applications.commands` scopes

### 2. Configure the Bot (`discord/config.yml`)

```yaml
enabled: true

default-webhook: "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"

admin:
  enabled: false
  port: 8765
  token: ""

mentions:
  style: actionbar           # chat | actionbar | bossbar
  message: "&e&l[Discord] &b{sender} &7mentioned you!"
  bossbar:
    color: YELLOW
    duration: 5

bot:
  enabled: true
```

### 3. Configure Bot Settings (`discord/bot.yml`)

```yaml
token: "YOUR_BOT_TOKEN_HERE"
guild-id: "YOUR_GUILD_ID"

# Channel IDs for bridging
channels:
  global-chat: "CHANNEL_ID"
  announcements: "CHANNEL_ID"
  staff: "CHANNEL_ID"
```

### 4. Configure Channels (`discord/channels.yml`)

```yaml
# Map in-game chat channels to Discord channel IDs
global:
  discord-id: "123456789012345678"
  webhook: "https://discord.com/api/webhooks/..."
  relay-to-game: true
  relay-to-discord: true

staff:
  discord-id: "123456789012345679"
  relay-to-game: true
  relay-to-discord: true
```

---

## Player Event Webhooks (`discord/playerEvents.yml`)

```yaml
join:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** joined the server!"

quit:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** left the server."

death:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** died: {death_message}"

achievement:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** earned **{achievement}**!"
```

---

## Role Mappings (`discord/roles.yml`)

```yaml
# LuckPerms group → Discord Role ID
mappings:
  vip: "DISCORD_ROLE_ID"
  mvp: "DISCORD_ROLE_ID"
  staff: "DISCORD_ROLE_ID"
  admin: "DISCORD_ROLE_ID"
```

---

## Outbound Webhooks (`discord/outbound.yml`)

```yaml
webhooks:
  default: "https://discord.com/api/webhooks/..."
  deaths: "https://discord.com/api/webhooks/..."
  votes: "https://discord.com/api/webhooks/..."
```

---

## Webstore Integration (`discord/webstore.yml`)

```yaml
enabled: true
webhook: "https://discord.com/api/webhooks/..."
message: "**{player}** just purchased **{package}** from the store! Thank you!"
```

---

## Server Vote & Panel Control

### `/server vote` — Community Restart Vote

Any Discord member (optionally restricted to specific roles) can start a vote to restart the server.

1. Member runs `/server vote` in Discord.
2. Bot posts an embed with **✅ Yes** and **❌ No** buttons.
3. Each member can change their vote at any time during the window.
4. When the window closes the bot evaluates the result:
   - Requires `min-votes` cast **and** `threshold`% yes to pass.
   - On pass: RCON broadcasts an in-game warning, then Pterodactyl sends a `restart` signal after `warn-seconds`.
   - On fail: embed is updated with the result, no action is taken.
5. A configurable cooldown prevents back-to-back votes.

### `/server start` / `/server stop` — Admin Commands

Restricted to roles listed under `server-vote.admin-roles` (or Discord Administrator permission if the list is empty).

| Discord Slash Command | Action |
| --- | --- |
| `/server vote` | Start a community restart vote |
| `/server start` | Send `start` signal to Pterodactyl (server offline → online) |
| `/server stop` | Broadcast RCON warning then send `stop` signal |

### Configuration — `discord/panel.yml`

```yaml
panel: pterodactyl          # panel type (only pterodactyl supported)

pterodactyl:
  base-url: "https://panel.example.com"
  client-api-key: ""        # Account → API Credentials in your panel
  server-uuid: ""           # Server UUID from the panel URL

rcon:
  host: "127.0.0.1"
  port: 25575
  password: ""
  timeout-seconds: 5

server-vote:
  enabled: true
  voter-roles: []           # role IDs/names allowed to start a vote (empty = anyone)
  admin-roles: []           # role IDs/names for /server start|stop (empty = ADMINISTRATOR perm)
  min-votes: 3              # minimum votes before threshold is evaluated
  threshold: 0.6            # 60% yes required to pass
  window-seconds: 120       # voting window
  cooldown-minutes: 30      # cooldown between votes
  warn-seconds: 60          # RCON warning time before restart executes
  channel: "default"        # channel key or numeric Discord channel ID
```

---

## GitHub Actions Integration

The Discord module can monitor GitHub Actions workflows and allow staff to trigger them from Discord.

Key classes: `GitHubActionsManager`, `WorkflowPoller`, `WorkflowTriggerRecord`

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.discord.link` | Link Discord account | true |
| `nexusprism.admin` | Admin Discord commands | OP |
