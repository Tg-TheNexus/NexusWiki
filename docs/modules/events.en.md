# Events Module

*Last updated: 2026-03-22*

The Events module adds **world-scale dynamic events** that affect all players simultaneously — starting with the **Blood Moon**, which transforms nights into increasingly dangerous survival challenges tied to a per-player streak and a **Sacrifice Arc**.

---

## Blood Moon

The Blood Moon automatically activates each night when world time crosses **tick 13000** and deactivates at dawn (**tick 23000**). Server operators can also control it manually.

### Effects While Active

| Effect | Detail |
| --- | --- |
| Mob level bonus | All Leveled Mob rolls receive **+2** |
| Hunter job pay | Multiplied by the configured `kill-pay-multiplier` (default ×1.5) |
| Particle rain | Red DUST particles spawn around every online player every 3 seconds |
| Horde waves | A mob horde spawns every `horde-interval-ticks` (default 5 min) |

At **dawn** (deactivation), every online player who survived earns **+1** to their survival streak.

### Horde Waves

Each horde interval, a random online player is chosen as the target. **30 mobs** spawn in a ring 18 blocks around them from this pool: Zombie, Skeleton, Creeper, Spider, Witch, Husk, Drowned. All horde mobs are named `[Blood Moon]` in dark red.

### Commands

| Command | Description | Permission |
| --- | --- | --- |
| `/bloodmoon` | Show current Blood Moon status | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon start` | Force-activate the Blood Moon | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon stop` | Force-deactivate the Blood Moon | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon status` | Detailed status output | `nexusprism.events.bloodmoon.admin` |

### Configuration (`events/config.yml`)

```yaml
blood-moon:
  enabled: true
  world: world                     # The world to watch for time changes
  schedule: RANDOM                 # RANDOM (chance per night) or ALWAYS
  random-chance-per-night: 15      # Chance (%) a Blood Moon occurs each night (RANDOM only)
  kill-pay-multiplier: 1.5         # Hunter job pay multiplier during Blood Moon
  particle-interval-ticks: 60     # How often (ticks) to spawn particles per player
  horde-interval-ticks: 6000      # How often (ticks) to fire a horde wave (6000 = 5 min)
  horde-size: 30                   # Number of mobs per horde wave
```

---

## Survival Streak

Every player has a personal **Blood Moon survival streak** stored persistently in SQLite (`events/events.db`).

| Event | Streak Change |
| --- | --- |
| Survive a full Blood Moon night | **+1** (awarded at dawn) |
| Die during a Blood Moon | **Reset to 0** |

When the streak reaches a **multiple of 7** (7, 14, 21, 28...), the player receives a **Sacrifice Invitation** the next time they sleep.

### Streak Difficulty Scaling

Higher streaks make every Blood Moon harder — more mob levels, more spawns, and additional mini-boss events.

| Streak Range | Level Bonus | Spawn Rate Bonus | Elite Multiplier | Extra Events |
| --- | --- | --- | --- | --- |
| 1–6 | Base | Base | Base | — |
| 7–13 | +4 | +500% | ×3 | — |
| 14–20 | +7 | +700% | ×5 | Mid-event boss spawn |
| 21+ | +10 | +900% | Unlimited | Mini-bosses every 5 min |

---

## Sacrifice Arc

The Sacrifice Arc is a high-stakes optional challenge triggered by the survival streak. It hooks into the [Dreams module](dreams.md): when the streak qualifies, sleeping opens a **choice GUI** instead of a dream cutscene.

### Choice GUI

A 3-row GUI with two options:

| Slot | Item | Action |
| --- | --- | --- |
| 11 | Green Wool — **Accept** | Teleport to arena, 90-second survival trial |
| 15 | Red Wool — **Decline** | Reset streak, no other penalty |

Closing the GUI without clicking counts as **Decline**.

### Arena Trial

1. The player is teleported to the configured arena (or stays in their current location if unconfigured)
2. A random **Anime Boss** is summoned — selected from the pool eligible for the player's streak
3. A **180-second countdown** begins with warnings at 60s, 30s, 10s, and 5s

### Outcomes

| Outcome | Result |
| --- | --- |
| **Survive** | Reward granted (default: 3 Diamond Blocks), server-wide broadcast, streak reset |
| **Die** | Streak reset to 0 |
| **Quit/disconnect** | Session cleaned up, treated as failure |

### Sacrifice Reward Tiers

Rewards scale with how many Sacrifices you have completed (every 7 streak milestones).

| Streak Milestone | Rewards |
| --- | --- |
| **7** | Tier 1 MMO item + permanent **+5 Max HP** |
| **14** | Tier 2 MMO item + permanent **+10 Max HP** + **1 stat point** |
| **21** | Tier 3 MMO item + permanent **+2 stat points** + cosmetic effect |
| **28** | Tier 4 MMO item + permanent **+3 stat points** + title + boss egg |
| **35+** | Multiplying stat points + exclusive anime cosmetic per milestone |

!!! warning "Streak Reset After Sacrifice"
    Completing a Sacrifice — win or lose — resets your streak to 0. Your **best streak** is recorded separately and never resets.

### Configuration (`events/config.yml`)

```yaml
sacrifice:
  arena:
    world: ""    # Leave blank to use the player's current world
    x: 0.0
    y: 64.0
    z: 0.0
```

!!! tip "Setting Up the Arena"
    Build a dedicated PvE arena and set its coordinates under `sacrifice.arena`. Leave `world` blank to fight in place — useful for testing.

---

## Anime Boss Codex

When a Sacrifice is accepted, a random **Anime Boss** is summoned in the arena. The boss pool available depends on the player's current streak. Each boss has multiple phases, unique mechanics, and a unique drop.

Boss definitions live in `events/anime_bosses/*.yml`. Health and damage scale with streak:

```
finalStat = baseStat × (1 + (streak - 7) × 0.2)
```

### Boss Pool

| Boss | Min Streak | Base Entity | Spawn Weight |
| --- | --- | --- | --- |
| Rimuru Tempest | 7 | Giant Slime | 10 |
| Kazuma Satou | 7 | Villager | 9 |
| Subaru Natsuki | 7 | Zombie | 8 |
| Ainz Ooal Gown | 14 | Wither Skeleton | 7 |
| Itadori Yuji | 14 | Piglin Brute | 6 |
| Kirito | 14 | Zombie | 6 |
| Gojo Satoru | 21 | Phantom / Vex | 5 |
| Levi Ackermann | 21 | Vindicator | 4 |

---

=== "Rimuru Tempest"

    **Min Streak:** 7 · **Base Entity:** Giant Slime

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Predator Aura (absorbs projectiles), Slime Split (mini-slimes at 80%/70%) |
    | 2 | 60% → 25% | Storm of Steel (12 arrows 360°), Predator Drain (heals on hit) — swaps to Guardian |
    | 3 | 25% → 0% | Void Collapse (8-block pull AoE, 3 dmg/tick), Infinite Regen (2 HP/2 ticks) — immune to knockback |

    **Transitions:** Blue nova + Wither sound (→ Phase 2). Black collapse + Dragon Death sound + 2s Blindness (→ Phase 3).

    **Drop:** Slime-core fragment · Blue shimmer aura cosmetic

=== "Kazuma Satou"

    **Min Streak:** 7 · **Base Entity:** Villager

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Steal (removes random hotbar item every 12s), Lucky Trigger (15% crit for 5× dmg, no tell) |
    | 2 | 60% → 25% | Drain Touch (drains XP levels), Party Command (2 "Aqua" + 1 "Darkness" entity), Megumin Explosion (one-time at phase transition) |
    | 3 | 25% → 0% | Lucky Trigger rises to 35% but same damage reflects to Kazuma; Final Steal (attempts to steal weapon); Aqua Call (one-time full HP restore) |

    **Drop:** Adventurer's card · "Adventurer" rank item · Stolen items returned doubled

=== "Subaru Natsuki"

    **Min Streak:** 7 · **Base Entity:** Zombie

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 50% | Ground Slam, Desperate Call (spawns "Rem" zombie at 60%) |
    | **Return by Death** | At 0 HP (once) | Resets to 100% HP, player HP restored to pre-killing-blow, title: `⟳ RETURN BY DEATH` |
    | Post-RBD | 100% → 0% | Witch Factor (Wither I + Hunger II every 20s), Last Stand (below 25%: +40% speed, +50% dmg) |

    !!! danger "Return by Death"
        Subaru cannot be killed the first time. The mechanic fires exactly **once per fight** — if you don't account for it, you'll lose your killing-blow window.

    **Drop:** Silver coin cosmetic · "Witch's Scent" aura

=== "Ainz Ooal Gown"

    **Min Streak:** 14 · **Base Entity:** Wither Skeleton

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 70% | Summon Floor Guardians (3 zombies every 30s), Negative Burst (wither skull → Wither II + Weakness) |
    | 2 | 70% → 30% | Grasp of Death (delayed 10 true dmg 4s after hit), Dark Wisdom (15s immunity to repeated damage type) |
    | 3 | 30% → 0% | Touch of Ainz (3s standing still = instant kill), Soul Eater (heals 5 HP per killed entity) |

    !!! warning "Cannot be killed below 1 HP while summoned entities are alive."

    **Drop:** Undead Crown cosmetic · "§8Overlord" title fragment

=== "Itadori Yuji"

    **Min Streak:** 14 · **Base Entity:** Piglin Brute

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 50% | Divergent Fist (8% Black Flash proc = 10× dmg), Rush Down (3-hit combo telegraphed by orange pulse) |
    | 2 — **Sukuna Awakens** | 50% → 0% | Dismantle (3 shulker bullets in V + bleed), Cleave (5-block AoE melee), Malevolent Shrine (below 20%: 20 slashes in 3s), Black Flash rises to 15% |

    **Drop:** Curse energy crystal · "§4Cursed" title · Tattoo cosmetic

=== "Kirito"

    **Min Streak:** 14 · **Base Entity:** Zombie

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 40% | Sword Skill Vorpal (straight-line 5-hit charge), Parry (20% negate incoming hit) |
    | 2 — **???** | 40% → 0% | *Something awakens at 40% HP. Figure it out.* |

    **Drop:** Black coat elytra cosmetic · "§7Solo Player" title · *something else*

    !!! quote "Lore"
        *He who bests the Black Swordsman inherits more than a title.*

    !!! note ""
        `NjZhNzY2NjU3NTZlNzQ2YTZiNjM2YTZiNjM2YTZiNjM2YTZiNjM2YTZi`

=== "Gojo Satoru"

    **Min Streak:** 21 · **Base Entity:** Phantom / Vex

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Infinity (70% of all attacks deal 1 dmg), Phase Shift (invisible every 8s for 4s) |
    | 2 | 60% → 25% | Blue Pull (yanks player), Purple Hollow (straight beam AoE — 1s warning, 15 dmg + Levitation) |
    | 3 — **Domain Expansion** | 25% → 0% | Darkness every 2s, Total Information (confusion bursts), Domain Strike (instant directional hit +50%), Infinity FULLY active |

    !!! tip "Mage abilities and fire damage bypass Infinity."

    **Drop:** Blindfold cosmetic · "§b∞ Limitless" title

=== "Levi Ackermann"

    **Min Streak:** 21 · **Base Entity:** Vindicator

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 50% | ODM Charge (teleports to wall → instant dash to player), Clean Cut (bypasses 50% defense), Vertical Manoeuvre (SPEED IV circles for 3s) |
    | 2 | 50% → 0% | Wall to Wall (4 chained charges, decreasing telegraph), Titan Killer Form (below 25%: 5s stance — one-hit-to-0.5-hearts on connection, white outline tell) |

    !!! danger "Cannot be stunned, knocked back, or slowed — ever."

    **Drop:** ODM gear elytra cosmetic · "§8Survey Corps" title · Titan-slayer blade CMD

---

=== "Goku"

    **Min Streak:** 28 · **Base Entity:** Zombie

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 70% | Ki Blast (long-range projectile), Kaio-Ken (SPEED III + STRENGTH II burst) |
    | 2 | 70% → 40% | Super Saiyan (strength surge, speed surge, glowing aura), Ki Barrage (5 rapid projectiles) |
    | 3 — **Ultra Instinct** | 40% → 0% | Ultra Instinct Dodge (dodge chance), Ultra Instinct Strike (teleport behind player + heavy hit) |

    **Drop:** "§fSaiyan" title · Power Aura cosmetic

=== "Naruto Uzumaki"

    **Min Streak:** 28 · **Base Entity:** Zombie

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 70% | Shadow Clone (2 decoy zombies summoned), Rasengan (direct melee burst + knockback) |
    | 2 | 70% → 40% | Nine-Tails Cloak (SPEED II + STRENGTH I, orange aura), Rasenshuriken (wide AoE projectile) |
    | 3 — **Baryon Mode** | 40% → 0% | Baryon Mode (STRENGTH III + SPEED III, each hit costs player XP) |

    **Drop:** "§eKage" title · Sage eye cosmetic

=== "Aizen Sosuke"

    **Min Streak:** 28 · **Base Entity:** Wither Skeleton

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Kyoka Suigetsu (random blindness on hit), Spiritual Pressure (Slowness + Weakness aura) |
    | 2 | 60% → 30% | Transcendence (15s immunity shield), Illusion Step (teleport behind player with no tell) |
    | 3 — **Hogyoku** | 30% → 0% | Hogyoku Ascension (all stats maxed), Reiatsu Burst (AoE wither + Darkness + 10 true dmg) |

    !!! warning "Transcendence is immunity — not a dodge. All damage is absorbed for 15 seconds."

    **Drop:** "§8Hogyoku" title · Soul Reaper cloak cosmetic

=== "Natsu Dragneel"

    **Min Streak:** 28 · **Base Entity:** Blaze

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 70% | Fire Dragon Roar (fireball cone), Eat Fire (heals when hit by fire damage) |
    | 2 | 70% → 40% | Fire Dragon Iron Fist (charged melee + FIRE II), Flame Cloak (contact damage) |
    | 3 — **Dragon Force** | 40% → 0% | Dragon Force (STRENGTH II + RESISTANCE I — power doubles), Fire Nova (AoE explosion at feet) |

    !!! tip "Fire damage heals Natsu — use physical attacks only."

    **Drop:** "§cDragon Slayer" title · Fairy Tail guild cosmetic

=== "Sung Jin-Woo"

    **Min Streak:** 28 · **Base Entity:** Warden

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Shadow Soldier (summons 2 zombie soldiers), Tenacity (50% chance to ignore stagger) |
    | 2 | 60% → 30% | Ruler's Authority (pulls player toward boss), Stealth (brief vanish + ambush strike) |
    | 3 — **Shadow Monarch** | 30% → 0% | Shadow Monarch Form (RESISTANCE I + SPEED II), Arise (killed player summons shadow soldier for 30s) |

    !!! danger "Shadow soldiers persist until killed. Clear them before focusing the boss."

    **Drop:** "§8Shadow Monarch" title · Monarch's aura cosmetic

=== "Giorno Giovanna"

    **Min Streak:** 28 · **Base Entity:** Zombie

    | Phase | HP Range | Key Abilities |
    | --- | --- | --- |
    | 1 | 100% → 60% | Life Shot (projectile applies Poison + Wither), Golden Experience (converts player hits into nature damage) |
    | 2 | 60% → 30% | Infinite Death Loop (SLOW IV + Weakness until dispelled by retreat), Restoration (heals 5 HP on melee kill) |
    | 3 — **Requiem** | 30% → 0% | Requiem Loop (all player attacks heal Giorno for 5s), Gold Experience Requiem (resets hit to zero — one-time negation) |

    !!! warning "During Requiem Loop, dealing damage heals the boss. Stop attacking and wait it out."

    **Drop:** "§6Golden Wind" title · GER aura cosmetic

---

## Admin Commands

| Command | Description | Permission |
| --- | --- | --- |
| `/bloodmoon` | Show Blood Moon status | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon start` | Force-activate Blood Moon | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon stop` | Force-deactivate Blood Moon | `nexusprism.events.bloodmoon.admin` |
| `/isekai` | Show active Isekai boss fights | `nexusprism.events.isekai.admin` |
| `/isekai force <player>` | Force-start an Isekai boss fight for a player | `nexusprism.events.isekai.admin` |
| `/isekai force <player> <bossId>` | Force-start with a specific boss | `nexusprism.events.isekai.admin` |
| `/isekai stop <player>` | End an active boss fight | `nexusprism.events.isekai.admin` |
| `/isekai list` | List all available boss IDs | `nexusprism.events.isekai.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.events.bloodmoon.admin` | Control Blood Moon manually | OP |
| `nexusprism.events.isekai.admin` | Control Isekai boss fights manually | OP |
