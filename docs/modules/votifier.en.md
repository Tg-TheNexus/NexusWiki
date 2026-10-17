# Votifier Module

The Votifier module is a **standalone Votifier V1 and V2 server** built directly into NexusPrism. It handles incoming votes from server listing websites, distributes configurable rewards, and tracks player vote streaks on a leaderboard.

---

## How It Works

```flow
Vote Site  ──► Votifier Server (port 8192)  ──► VoteManager  ──► Rewards + Streak
                (V1 RSA / V2 token-based)
```

1. Register your server on voting sites (Minecraftservers.org, etc.)
2. Point each site to your server IP and Votifier port (default `8192`)
3. When a player votes, the site sends a payload to your Votifier server
4. NexusPrism processes the vote, runs reward commands, and updates the streak

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/vote` | Show voting links and your current streak | `nexusprism.vote` |
| `/votetop` | Show the vote leaderboard | `nexusprism.vote.top` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.vote` | Use `/vote` | true |
| `nexusprism.vote.top` | Use `/votetop` | true |

---

## Configuration (`votifier/config.yml`)

```yaml
host: "0.0.0.0"       # Listen on all interfaces
port: 8192             # Votifier port (open this in your firewall)
token: "change-this-token"   # Shared secret for V2 authentication

vote-links:
  - "https://minecraftservers.org/vote/YOUR_SERVER_ID"
  - "https://minecraft-server-list.com/server/YOUR_SERVER_ID/vote/"

rewards:
  - type: COMMAND
    value: "eco give {player} 500"
  - type: COMMAND
    value: "crates key give {player} VOTE 1"
  - type: MESSAGE
    value: "&aThank you for voting, {player}! You received $500 and a crate key."

streak:
  enabled: true
  max-gap-hours: 36    # Votes more than 36h apart reset the streak
  multipliers:
    5:  1.5            # 5-vote streak = 1.5× rewards
    10: 2.0            # 10-vote streak = 2× rewards
    30: 3.0            # 30-vote streak = 3× rewards
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `host` | IP to bind the vote server. Use `0.0.0.0` for all interfaces. |
| `port` | TCP port. Must be open in your firewall and forwarded if behind NAT. |
| `token` | Secret token for V2 authentication. Change this immediately. |
| `vote-links` | List of URLs displayed by `/vote`. |
| `rewards[].type` | `COMMAND` (runs a console command) or `MESSAGE` (sends player a message). |
| `rewards[].value` | Command/message string. Use `{player}` for the voter's username. |
| `streak.max-gap-hours` | How many hours can pass between votes before the streak resets. |
| `streak.multipliers` | Map of streak length → reward multiplier. |

---

## Protocol Support

| Protocol | Description |
| --- | --- |
| **V1** | Legacy RSA-encrypted Votifier protocol. Compatible with most older vote sites. |
| **V2** | Modern HMAC-SHA256 token-based protocol. Preferred — more secure and reliable. |

RSA keys for V1 are automatically generated on first start and stored as `votifier/rsa/public.key` and `votifier/rsa/private.key`.

---

## Registering on Vote Sites

When registering on a vote site, you will need:

- **Server IP** — your server's public IP address
- **Votifier Port** — `8192` (or whatever you set in `config.yml`)
- **Public Key** — copy from `plugins/NexusPrism/votifier/rsa/public.key` (V1 sites)
- **Token** — the `token` value from `config.yml` (V2 sites)

---

## Streak System

| Streak | Multiplier |
| --- | --- |
| 1–4 votes | 1× (base) |
| 5–9 votes | 1.5× |
| 10–29 votes | 2× |
| 30+ votes | 3× |

When the multiplier is active, reward `COMMAND` values are executed multiple times equal to the multiplier (rounded to nearest integer), or you can implement custom multiplier logic using the `%nexusprism_vote_streak%` placeholder in external plugins.

---

## PlaceholderAPI

| Placeholder | Description |
| --- | --- |
| `%nexusprism_votes_total%` | Total lifetime votes by the player |
| `%nexusprism_vote_streak%` | Player's current vote streak |
