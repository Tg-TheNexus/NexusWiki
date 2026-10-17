# Twitch Integration Module

The Twitch module connects your Minecraft server to Twitch. Players can **link their Twitch accounts**, staff are notified when linked players go live, the Twitch chat is relayed in-game, and admins can run **viewer giveaways**.

---

## Features

| Feature | Description |
| --- | --- |
| **Account Linking** | Link Minecraft ↔ Twitch via an in-chat verification code |
| **Live Tag** | Prefixes the chat with `[LIVE]` when a player is streaming |
| **Go-Live Announcements** | Broadcasts when a linked player starts/stops streaming |
| **Chat Relay** | Twitch chat messages appear in-game |
| **Giveaways** | Draw a random eligible linked viewer and reward them |
| **Viewer Rewards** | Automatic periodic raffle for viewers watching linked streamers |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/twitch link <username>` | Start linking your Twitch account | `nexusprism.twitch.use` |
| `/twitch unlink` | Unlink your Twitch account | `nexusprism.twitch.use` |
| `/twitch status` | Check your link status | `nexusprism.twitch.use` |
| `/twitch approve <player>` | Approve a pending link | `nexusprism.twitch.staff` |
| `/twitch reject <player>` | Reject a pending link | `nexusprism.twitch.staff` |
| `/twitch pending` | List pending link requests | `nexusprism.twitch.staff` |
| `/twitch giveaway <streamer>` | Draw a giveaway winner | `nexusprism.twitch.staff` |
| `/twitch reload` | Reload Twitch config | `nexusprism.twitch.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.twitch.use` | Basic Twitch commands | true |
| `nexusprism.twitch.staff` | Approve links, run giveaways | OP |
| `nexusprism.twitch.admin` | Reload config | OP |

---

## Setup

### 1. Create a Twitch Application

1. Go to [dev.twitch.tv/console](https://dev.twitch.tv/console) and create an application
2. Set the OAuth redirect to `http://localhost`
3. Copy the **Client ID** and **Client Secret**

### 2. Create a Bot Account

1. Create a Twitch account for the bot (or use your own)
2. Go to [twitchapps.com/tmi/](https://twitchapps.com/tmi/) to get an OAuth token
3. Add the bot as a moderator in your verification channel

### 3. Configure (`twitch/config.yml`)

```yaml
bot:
  enabled: true
  oauth-token: "oauth:your_token_here"
  client-id: "your_client_id"
  client-secret: "your_client_secret"
  bot-username: "your_bot_account"
  verification-channel: "your_server_twitch_channel"

link:
  require-staff-approval: true  # Staff must approve before link activates
  code-expiry-seconds: 300

stream-poll:
  interval-seconds: 60          # Check if streamers are live every 60s

live-tag:
  enabled: true
  format: "§c[LIVE] §r"         # Prepended to chat format when streaming

announcements:
  go-live:
    enabled: true
    message: "§6[Twitch] §e{player} §7is now live! §f{title} §7— §fttwitch.tv/{channel}"
    discord-channel: "announcements"   # Discord channel key for cross-posting
  go-offline:
    enabled: false
    message: "§6[Twitch] §e{player} §7finished their stream."

chat-relay:
  enabled: true
  format: "§6[Twitch] §b{user}§7: {message}"

giveaway:
  command: "crates key give {player} VOTE 1"
  key-item: "SERVER_KEY"
  active-viewer-window-minutes: 10
  announce-winner: "§6[Giveaway] §e{player} §7won a key! Congrats to @{twitch_name}!"
  twitch-announce: "Congrats @{twitch_name}! You won a key on our Minecraft server!"

viewer-reward:
  enabled: false
  interval-minutes: 30
  command: "crates key give {player} VOTE 1"
```

---

## Account Linking Flow

```cs
Player runs /twitch link <username>
        │
        ▼
Bot sends a 5-character code in the verification Twitch channel
        │
        ▼
Player types !verify <code> in the Twitch chat
        │
        ▼
[If require-staff-approval: true]
Staff approves with /twitch approve <player>
        │
        ▼
Link is active — live tag and announcements apply
```

---

## Giveaway System

Staff can run `/twitch giveaway <streamer>` to:

1. Fetch all currently linked viewers watching that streamer's channel
2. Filter to viewers who sent a message in the last `active-viewer-window-minutes`
3. Randomly select one eligible viewer
4. Execute the configured `command` (or give the `key-item`) to the winner
5. Announce the winner in-game and in Twitch chat

!!! note "Bot Permissions Required"
    For the viewer reward system to fetch the chatters list, the bot account must have the `moderator:read:chatters` OAuth scope and be a moderator in the streamer's channel.

---

## Message Placeholders

| Placeholder | Description |
| --- | --- |
| `{player}` | Minecraft username |
| `{twitch_name}` | Twitch display name |
| `{title}` | Stream title |
| `{channel}` | Twitch channel name |
| `{user}` | Twitch chatter display name |
| `{message}` | Twitch chat message content |
