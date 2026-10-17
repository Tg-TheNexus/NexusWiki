# Web & GDPR Module

The Web module handles **webstore integration**, **VIP kit delivery**, **payment webhooks**, and **GDPR compliance** — giving players control over their personal data.

---

## GDPR Compliance

Players can export, delete, and manage consent for their stored data directly in-game.

### Commands

All GDPR commands are player-only and require no special permission (GDPR compliance requires they be accessible to all players).

| Command | Description |
| --- | --- |
| `/nexus gdpr` | Show GDPR info and current consent settings |
| `/nexus gdpr export` | Export all personal data to a JSON file in `gdpr/` |
| `/nexus gdpr delete` | Delete all personal data (right to erasure) |
| `/nexus consent <type> <accept\|deny>` | Grant or deny a specific consent type |

### Consent Types

| Consent Type | What It Covers |
| --- | --- |
| `activity_tracking` | Join/leave/playtime data |
| `purchase_history` | Transaction records |
| `discord_notifications` | Discord-linked player actions |
| `statistics` | Player stats and achievements |
| `marketing` | Server announcements and promotions |

On first join, players receive a prompt to accept or deny `activity_tracking`. Other consent types can be managed anytime via `/nexus consent`.

!!! info "Data deletion"
    Financial records newer than `gdpr.legal-retention-years` are **anonymised** rather than deleted, to comply with legal minimum retention requirements. All other data is removed immediately.

---

## Webstore Integration

The module bridges an external webstore with the plugin for **automatic kit delivery** and **payment verification**.

### VIP Kit Delivery

When a player purchases a rank or kit on the webstore, the order is queued. On the player's next join, `auto-deliver: true` delivers the kit automatically.

Kits are defined in `kits.yml`:

```yaml
kits:
  VIP:
    items:
      - material: DIAMOND
        amount: 5
      - material: GOLDEN_APPLE
        amount: 1
    commands:
      - "lp user {player} group set vip"
      - "tell {player} Welcome to VIP!"
  MVP:
    items:
      - material: NETHERITE_INGOT
        amount: 3
    commands:
      - "lp user {player} group set mvp"
```

---

## Security

### Data Encryption

When `security.enable-encryption: true` (default), sensitive data stored by the web module is encrypted with **AES-256-CBC** using a random IV per entry. The key is generated once and persisted to `plugins/NexusPrism/web/encryption.key`.

!!! warning "Back up encryption.key"
    If this file is lost, previously encrypted data cannot be decrypted. Include it in your server backups. Never commit it to a git repository.

### Stream Panel Integration (polling model)

The plugin polls the Stream Panel outbound — **no open port on the Minecraft server is needed**.

Every `nexus-tools.poll-interval-seconds` (default: `5`) the plugin sends a `GET` to the Stream Panel's `/api/nexus/events/pending` endpoint, consumes any queued Twitch events (raid, sub, cheer), then `POST`s the consumed IDs to `/api/nexus/events/ack`.

Set `nexus-tools.panel-url` to your Stream Panel Railway URL and `nexus-tools.receiver-secret` to match the `NEXUS_TOOLS_SECRET` env var on Railway. Requests without a matching `Authorization: Bearer <secret>` header are rejected with 401.

Leave `receiver-secret` empty only in isolated local development environments.

---

## Configuration (`web-config.yml`)

```yaml
discord:
  webhook-url: ""                  # Webhook for delivery notifications
  server-invite: "https://discord.gg/your-invite"
  notifications-enabled: false

api:
  enabled: false
  endpoint: "https://your-website.com/api"
  key: ""                          # Auto-generated 64-char hex on first run
  rate-limit: 60                   # Requests per minute

security:
  require-api-key: true
  enable-ip-whitelist: false
  whitelisted-ips:
    - "127.0.0.1"
    - "your-server-ip"
  enable-encryption: true          # AES-256-CBC; key stored in web/encryption.key

gdpr:
  enabled: true
  log-transactions: true
  data-retention-days: 365
  legal-retention-years: 7
  allow-data-export: true
  allow-data-deletion: true

payments:
  enabled: false
  provider: "custom"               # stripe | paypal | mercadopago | custom
  webhook-secret: ""               # Auto-generated UUID on first run
  currency: "USD"

nexus-tools:
  panel-url: ""                    # Stream Panel Railway URL (e.g. https://your-panel.up.railway.app)
  receiver-secret: ""              # Shared secret — must match NEXUS_TOOLS_SECRET on Railway
  poll-interval-seconds: 5        # How often the plugin fetches events

vip-kits:
  enabled: true
  auto-deliver: true
  verify-payment: true
```

### Configuration Fields

| Field | Default | Description |
| --- | --- | --- |
| `api.endpoint` | — | Webstore API base URL for order verification |
| `api.key` | *(auto-generated)* | Copy to webstore's `NEXUS_API_KEY` env var |
| `security.require-api-key` | `true` | Reject requests without a valid API key — never disable in production |
| `security.enable-encryption` | `true` | AES-256-CBC encryption for stored sensitive data |
| `payments.webhook-secret` | *(auto-generated)* | Must match the secret set in your payment provider's webhook dashboard |
| `nexus-tools.panel-url` | `` | Stream Panel Railway URL the plugin polls for events |
| `nexus-tools.receiver-secret` | `` | Shared bearer secret; must match `NEXUS_TOOLS_SECRET` on Railway |
| `nexus-tools.poll-interval-seconds` | `5` | Polling frequency in seconds |
| `vip-kits.auto-deliver` | `true` | Deliver pending kits automatically on player join |
| `vip-kits.verify-payment` | `true` | Verify payment status via API before delivery |
