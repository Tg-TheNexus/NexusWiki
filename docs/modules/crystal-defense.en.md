# Crystal Defense Module

Crystal Defense is a **wave-based cooperative minigame** where players defend Ender Crystals against increasingly difficult mob waves. Players earn points per kill and spend them on arena upgrades.

---

## How to Play

1. An admin creates an arena with `/crystal create <name>`
2. Players join the arena with `/crystal join <name>`
3. The game starts automatically when enough players are ready (or manually via `/crystal start`)
4. Mobs spawn in waves — kill them before they destroy the crystal
5. Spend kill-earned points on upgrades between waves
6. The game ends when the crystal's HP reaches zero

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/crystal join <arena>` | Join an arena | `nexusprism.crystaldefense.use` |
| `/crystal leave` | Leave the current arena | `nexusprism.crystaldefense.use` |
| `/crystal list` | List available arenas | `nexusprism.crystaldefense.use` |
| `/crystal status` | Show current wave and crystal HP | `nexusprism.crystaldefense.use` |
| `/crystal create <name>` | Create a new arena | `nexusprism.crystaldefense.admin` |
| `/crystal delete <name>` | Delete an arena | `nexusprism.crystaldefense.admin` |
| `/crystal setcrystal <arena>` | Set crystal location | `nexusprism.crystaldefense.admin` |
| `/crystal setspawn <arena>` | Set player spawn for arena | `nexusprism.crystaldefense.admin` |
| `/crystal start [arena]` | Force-start a game | `nexusprism.crystaldefense.admin` |
| `/crystal stop [arena]` | Stop a game | `nexusprism.crystaldefense.admin` |
| `/crystal reload` | Reload arena configs | `nexusprism.crystaldefense.admin` |

---

## Arena Setup

1. Build your arena in the world
2. Run `/crystal create <name>`
3. Stand at the Ender Crystal position → `/crystal setcrystal <name>`
4. Stand at the player spawn → `/crystal setspawn <name>`
5. (Optional) Edit `crystaldefense/config.yml` to configure waves and upgrade costs

---

## Main Configuration (`crystaldefense/config.yml`)

```yaml
arena:
  crystal-max-health: 1000.0    # Default crystal HP for new arenas

points:
  per-kill: 5                   # Points earned per mob kill

upgrades:
  crystal_health:
    base_cost: 20
    step_percent: 20            # Crystal max-HP increases by 20% per purchase

  crystal_defense:
    base_cost: 25
    duration_seconds: 30        # RESISTANCE II duration applied to all players

  player_attack_buff:
    base_cost: 30
    damage_percent: 20          # % increase to player base attack damage
    duration_seconds: 60
```

---

## Wave Definitions (`crystaldefense/waves.yml`)

```yaml
waves:
  1:
    mobs:
      - type: ZOMBIE
        count: 10
        health-multiplier: 1.0
      - type: SKELETON
        count: 5
        health-multiplier: 1.0
    delay-seconds: 3

  2:
    mobs:
      - type: ZOMBIE
        count: 15
        health-multiplier: 1.2
      - type: SKELETON
        count: 8
        health-multiplier: 1.1
      - type: CREEPER
        count: 3
        health-multiplier: 1.0
    delay-seconds: 3

  5:
    mobs:
      - type: WITHER_SKELETON
        count: 5
        health-multiplier: 1.5
      - type: BLAZE
        count: 10
        health-multiplier: 1.3
    delay-seconds: 5
    boss:
      type: WITHER
      health: 300.0
```

---

## Upgrades

| Upgrade | Effect | Base Cost |
| --- | --- | --- |
| **Crystal Health** | Increases crystal max HP by 20% per level | 20 points |
| **Crystal Defense** | Applies RESISTANCE II to all players for 30s | 25 points |
| **Player Attack Buff** | +20% damage for 60s | 30 points |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.crystaldefense.use` | Join arenas and play | true |
| `nexusprism.crystaldefense.admin` | Create/manage arenas | OP |

---

## PlaceholderAPI

| Placeholder | Description |
| --- | --- |
| `%nexusprism_crystal_wave%` | Current wave number |
| `%nexusprism_crystal_health%` | Crystal HP remaining |
| `%nexusprism_crystal_points%` | Player's points in current game |
| `%nexusprism_crystal_arena%` | Arena the player is in |
