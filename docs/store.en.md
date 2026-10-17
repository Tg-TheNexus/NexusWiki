# Store / Webstore

NexusPrism includes a built-in webstore bridge that delivers purchased packages to players automatically, even while they are offline.

!!! warning "EULA Compliance"
    All store packages must comply with the [Minecraft Commercial Usage Guidelines](https://www.minecraft.net/en-us/eula). Selling gameplay advantages that cannot be earned in-game through normal play is **not permitted** on servers accessible to the public. The features listed below follow EULA-compliant design principles.

---

## EULA-Compliant Features

The following features are safely offered in a store under the Minecraft EULA:

| Feature | Notes |
| --- | --- |
| **Cosmetic nicknames** | `/nick` — visual only, no gameplay advantage |
| **Cosmetic hats** | `/hat` — visual only |
| **Additional homes** | Extra home slots (convenience, not power) |
| **Fly in non-PvP zones** | Cosmetic convenience; disabled in PvP regions |
| **Resource pack access** | Server resource pack (cosmetic) |
| **Extra waypoint slots** | Convenience — see `nexusprism.essentials.waypoints.*` |
| **VIP kit (cosmetic)** | Cosmetic items, vanity gear — no enchanted diamond armor |
| **Crate keys** | As long as all crate rewards can also be earned in-game |
| **Colored name tags** | Visual only |
| **Discord role** | Access to a special Discord channel |
| **Custom join messages** | Visual/cosmetic |

---

## Delivery System

NexusPrism's webstore bridge (`nexusprism-web`) uses a delivery queue. When a player purchases a package:

1. The webstore posts a delivery request to the plugin via the delivery bridge
2. The delivery is queued in `delivery.yml` (persistent)
3. On the player's next login, all pending deliveries are processed
4. Commands are run on their behalf automatically

This means **offline delivery** is supported — the player does not need to be online at the time of purchase.

### `delivery.yml` Configuration

```yaml
# Delivery bridge configuration
enabled: true

# HTTP endpoint the webstore POSTs delivery requests to
# Leave empty to disable HTTP ingestion (use file-based delivery instead)
endpoint:
  host: "0.0.0.0"
  port: 9090
  token: "change-this-delivery-token"

# Fallback: read deliveries from this file (one JSON object per line)
file-fallback: "pending_deliveries.jsonl"
```

---

## VIP Kits (`kits.yml`)

VIP kits are given to players on purchase or via `/kit <name>`. Configure them in `kits.yml`:

```yaml
kits:
  vip:
    display-name: "&6VIP Kit"
    permission: "nexusprism.kit.vip"
    cooldown-hours: 24
    items:
      - material: GOLDEN_APPLE
        amount: 5
      - material: FIREWORK_ROCKET
        amount: 16
      - nexusprism-id: SERVER_KEY    # Custom NexusPrism item
        amount: 1
    commands:
      - "eco give {player} 1000"

  mvp:
    display-name: "&bMVP Kit"
    permission: "nexusprism.kit.mvp"
    cooldown-hours: 24
    items:
      - material: GOLDEN_APPLE
        amount: 16
      - nexusprism-id: SERVER_KEY
        amount: 2
    commands:
      - "eco give {player} 2500"
```

---

## GDPR / Consent

NexusPrism includes a GDPR consent system (`GDPRManager`) for servers operating in the EU. Players can be prompted to consent to data collection on first join.

```yaml
# web-config.yml
gdpr:
  enabled: false
  consent-on-join: true
  consent-types:
    - ANALYTICS
    - MARKETING
```

---

## Recommended Store Platforms

NexusPrism's delivery system is compatible with any store platform that can make HTTP POST requests or write to a shared file. Commonly used platforms include:

- **Tebex** (formerly Buycraft) — EULA-certified
- **CraftingStore** — EULA-certified
- **Custom panel** — Use the HTTP delivery endpoint

!!! tip "Test your delivery"
    Use `/nexusprism reload` after editing `delivery.yml`. Test a delivery manually by writing a delivery JSON to the file-fallback and relogging.
