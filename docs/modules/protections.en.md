# Protections Module

The Protections module provides **WorldGuard-style cuboid region claiming**, 28 configurable protection flags, and a **1v1 duel system**.

!!! info "This is not Towny"
    `nexusprism-protections` is a cuboid region system similar to **WorldGuard or GriefPrevention** — players define a 3D area and set flags on it. It has **no cities, nations, taxes, or diplomacy**. If you want Towny-style chunk-based territory with clan governance, see the [Clans module](clans.md) instead.

---

## Region Claiming

Players select two corners of a cuboid region with the selection wand, then claim it as their protected area. Non-members cannot build, break, or interact within the region by default.

### How to Claim a Region

1. Hold a **Golden Axe** (default wand)
2. Left-click one corner of your region → right-click the opposite corner
3. Run `/region claim <name>` to claim the selection

### Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/region claim <name>` | Claim selected area | `nexusprism.region.use` |
| `/region delete <name>` | Delete a region | `nexusprism.region.use` |
| `/region list` | List your regions | `nexusprism.region.use` |
| `/region info [name]` | View region details | `nexusprism.region.use` |
| `/region addmember <region> <player>` | Add a member | `nexusprism.region.use` |
| `/region removemember <region> <player>` | Remove a member | `nexusprism.region.use` |
| `/region setflag <region> <flag> <value>` | Set a flag | `nexusprism.region.use` |
| `/region flags <region>` | View all flags | `nexusprism.region.use` |
| `/protect <name>` | Quick-protect current chunk | `nexusprism.region.use` |
| `/region admin list [player]` | Admin: list all regions | `nexusprism.protect.admin` |
| `/region admin delete <name>` | Admin: force-delete region | `nexusprism.protect.admin` |
| `/region admin setowner <region> <player>` | Admin: change owner | `nexusprism.protect.admin` |

---

## Region Flags

Flags control what is and isn't allowed within a region. Regions have two types: **PLAYER** (priority 0, created by players) and **ADMIN** (priority 100, created by staff — always overrides player regions).

| Flag | Values | Default | Description |
| --- | --- | --- | --- |
| `pvp` | `true` / `false` | `false` | Allow PvP inside the region |
| `build` | `true` / `false` | `false` | Allow non-members to build/break blocks |
| `interact` | `true` / `false` | `false` | Allow non-members to interact (chests, buttons…) |
| `mob-spawning` | `true` / `false` | `true` | Allow hostile mobs to spawn |
| `animal-spawning` | `true` / `false` | `true` | Allow passive animals to spawn |
| `monster-attack` | `true` / `false` | `true` | Allow mobs to attack players |
| `explosions` | `true` / `false` | `false` | Allow TNT / creeper explosions |
| `fire` | `true` / `false` | `false` | Allow fire spread |
| `fly` | `true` / `false` | `false` | Allow flight inside the region |
| `keep-inventory` | `true` / `false` | `false` | Keep inventory on death inside the region |
| `keep-exp` | `true` / `false` | `false` | Keep experience on death |
| `entry` | `true` / `false` | `true` | Allow non-members to enter the region |
| `deny-sleep` | `true` / `false` | `false` | Prevent players from sleeping in beds |
| `smart-door` | `true` / `false` | `false` | Doors auto-close after a short delay |
| `greeting` | `<text>` | — | Message shown when entering the region |
| `farewell` | `<text>` | — | Message shown when leaving the region |

```bash
# Example: enable PvP in an arena region
/region setflag my-arena pvp true
/region setflag my-arena greeting "&cYou entered a PvP zone!"
```

---

## Configuration (`protections/config.yml`)

```yaml
selection-wand: GOLDEN_AXE     # Item used to select region corners

max-regions-per-player: 5      # Max regions per player
max-region-volume: 100000      # Max region size in blocks

pvp-in-wilderness: true        # Allow PvP outside any region

duel-request-timeout-seconds: 30

economy:
  enabled: false               # Charge players to claim regions
  base-cost: 100.0             # Flat fee per claim
  cost-per-block: 0.01         # Additional cost × region volume
  refund-percent: 50           # % refunded when a region is deleted
```

---

## Duel System

The duel system lets players challenge each other to a 1v1 fight in a safe duel arena. Deaths during duels do not drop items.

### Duel Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/duel <player>` | Challenge a player to a duel | `nexusprism.duel.use` |
| `/duel accept` | Accept a duel challenge | `nexusprism.duel.use` |
| `/duel deny` | Deny a duel challenge | `nexusprism.duel.use` |
| `/duel spectate <player>` | Spectate a duel | `nexusprism.duel.use` |
| `/duel stats` | View your duel stats | `nexusprism.duel.use` |
| `/duel setarena` | Set duel arena at your location | `nexusprism.protect.admin` |

### Duel Rules

- Duel requests expire after `duel-request-timeout-seconds` (default: 30)
- Items are saved and restored after the duel ends
- The winner receives configurable rewards (set in the economy bridge)
- Both players are teleported to the duel arena on accept

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.region.use` | Create and manage own regions | true |
| `nexusprism.protect.admin` | Admin region management | OP |
| `nexusprism.bypass.protection` | Bypass all region protections | OP |
| `nexusprism.duel.use` | Challenge and accept duels | true |
