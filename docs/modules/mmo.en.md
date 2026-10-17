# MMO Module

The MMO module transforms NexusPrism into a light RPG experience. Players earn an **MMO level**, allocate **stat points**, level up **six skill trees**, unlock and use **abilities**, and progress through **eight professions** — each with a unique mastery passive.

---

## MMO Level & Stat Points

Players earn MMO XP from any in-game activity (combat, professions, skill trees). Leveling up grants **1 unspent stat point** to spend freely.

### XP to Level Formula

```
xpToLevel(n) = 100 × 2^((n-1) / 10)
```

The XP requirement doubles every 10 levels.

### Stats

| Stat | Effect |
| --- | --- |
| `MAX_HEALTH` | Increases maximum hearts |
| `STRENGTH` | +1.5% melee damage per point |
| `DEFENSE` | -0.8% damage taken per point (max 80% reduction) |
| `AGILITY` | +0.5% dodge chance per point (hit cancelled, "Dodged!" in actionbar) |
| `INTELLIGENCE` | Increases magic ability power |
| `WISDOM` | Affects healing effectiveness and mana-equivalent costs |
| `LUCK` | Improves drop rates and random outcomes |
| `CRIT_CHANCE` | +1% critical hit chance per point (max 95%) |
| `CRIT_DAMAGE` | Crit multiplier = `1.5 + (critDamage × 0.01)` |
| `MAGIC_POWER` | Amplifies magic ability damage |
| `MINING_SPEED` | Increases block break speed |
| `FISHING_LUCK` | Improves fishing treasure quality |

**Final stat value** = base (player-allocated) + skill tree bonuses + future equipment bonuses.

### Commands

| Command | Description |
| --- | --- |
| `/stats` | View your stat sheet and unspent points |
| `/stats add <stat>` | Spend 1 stat point (e.g. `/stats add strength`) |

---

## Skill Trees

Six independent skill trees, each leveled through specific activities. Leveling grants passive stat bonuses and unlocks abilities at milestones.

### Tree Overview

| Tree | Primary Stats | XP Source | Abilities |
| --- | --- | --- | --- |
| **Warrior** | Strength, Defense, Max Health | Melee kills | Shield Bash (10), Berserker Rage (25), Warlord Aura (50) |
| **Rogue** | Agility, Crit Chance, Crit Damage | Kills | Shadow Step (10), Backstab (25), Phantom Form (50) |
| **Mage** | Intelligence, Magic Power, Wisdom | Enchanting | Fireball (10), Arcane Shield (25), Nova Burst (50) |
| **Archer** | Agility, Crit Chance, Luck | Kills | Rain of Arrows (10), Eagle Eye (25), Piercing Shot (50) |
| **Healer** | Wisdom, Max Health, Defense | Healing | Holy Aura (10), Revive (25), Sanctuary (50) |
| **Alchemist** | Luck, Intelligence, Wisdom | Brewing | Toxic Cloud (10), Elixir Surge (25), Philosopher's Touch (50) |

!!! warning "Hidden abilities"
    Some abilities are not listed here. They exist — but their conditions, costs, and names are for you to discover.

### Ability Descriptions

=== "Warrior"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Shield Bash** | Deals cone damage and knockback in front of the player |
    | 25 | **Berserker Rage** | Melee damage ×2 for 8 seconds |
    | 50 | **Warlord Aura** | Passive +30% melee damage permanently |

=== "Rogue"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Shadow Step** | Blink 6 blocks in the direction you're looking |
    | 25 | **Backstab** | Deal 4× damage when hitting a target from behind |
    | 50 | **Phantom Form** | 5 seconds of invisibility + +200% damage |

=== "Mage"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Fireball** | Launch an explosive projectile with a FLAME particle trail |
    | 25 | **Arcane Shield** | 3 orbiting orbs, each absorbing 1 incoming hit |
    | 50 | **Nova Burst** | AoE arcane explosion centred on the player |

=== "Archer"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Rain of Arrows** | Fire 9 critical arrows in a radial arc |
    | 25 | **Eagle Eye** | Fire a single piercing arrow that passes through mobs |
    | 50 | **Piercing Shot** | 5× damage arrow that ignores all defense |

=== "Healer"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Holy Aura** | Restore 6 hearts to all nearby allies |
    | 25 | **Revive** | Prevents the next fatal hit (one-time shield) |
    | 50 | **Sanctuary** | Create a 10-block healing zone lasting 15 seconds |

=== "Alchemist"

    | Level | Ability | Description |
    | --- | --- | --- |
    | 10 | **Toxic Cloud** | Deploy a lingering poison area effect cloud |
    | 25 | **Elixir Surge** | Share all your currently active potions with nearby allies |
    | 50 | **Philosopher's Touch** | Passive chance to duplicate any potion you brew |

### Using Abilities

```
/skill use <abilityId>
```

Or open `/skill`, click a tree, then click the ability icon. Cooldowns are tracked per player per ability.

### Ability Key Bindings

Players can bind unlocked abilities to hotbar slots for quick activation without typing commands. Open `/skill keybind` to configure bindings via GUI — each slot shows the ability name, mana cost, and current cooldown. Pressing the bound hotbar key activates the ability instantly.

### Commands

| Command | Description | Permission |
| --- | --- | --- |
| `/skill` | Open Skill Tree Browser GUI | `nexusprism.mmo.use` |
| `/skill use <id>` | Activate an unlocked ability | `nexusprism.mmo.use` |
| `/skill keybind` | Open the key binding GUI | `nexusprism.mmo.use` |

---

## Mana

Each player has a **mana pool** that abilities draw from. Mana regenerates passively based on the **Wisdom** stat.

| Mechanic | Detail |
| --- | --- |
| Base pool | Scales with MMO level |
| Regen | Wisdom-based, always active |
| On insufficient mana | Action bar: `§cNot enough mana!` — ability is blocked |
| Cost display | Shown on ability icons and in the key binding GUI |

The mana pool is also accessible from the [Addon API](../developer/api.md): `MmoRegistry.get()` → `getCurrentMana()`, `hasMana()`, `consumeMana()`.

---

## Professions

Eight professions level independently from skill trees. Each has a **mastery passive** that grows stronger with profession level.

### XP Formula

```
xpToLevel(n) = baseXp × 1.8^(level / 10)
```

### Profession Table

| Profession | XP Source | Mastery Passive | Max Bonus |
| --- | --- | --- | --- |
| **Mining** | Breaking ores | Vein Miner — double ore drop chance | 50% |
| **Farming** | Breaking crops | Bountiful Harvest — double crop drop | 60% |
| **Fishing** | Catching fish | Lucky Cast — extra treasure chance | 40% |
| **Lumberjack** | Breaking logs | Wood Splitter — double log drop | 50% |
| **Blacksmithing** | Crafting/smelting tools & armor | Master Craft — duplicate crafted tool/armor | 30% |
| **Alchemy** | Brewing potions | Potion Duplication — duplicate brewed potions | 50% |
| **Enchanting** | Enchanting items | Arcane Efficiency — save XP levels on enchant | 40% |
| **Cooking** | Crafting/smelting food | Gourmet — duplicate cooked food | 70% |

---

## Storage & Permissions

| Detail | Value |
| --- | --- |
| Database | SQLite — `mmo/mmo.db` |
| Tables | `player_mmo`, `player_skills`, `player_professions` |
| Permission | `nexusprism.mmo.use` (default: **true**) |
