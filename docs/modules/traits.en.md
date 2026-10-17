# Traits Module

The Traits module gives each player a set of **3 Tarot Cards** that grant passive and reactive effects. Cards are drawn randomly on first join and can be rerolled at a money cost.

---

## How It Works

1. On **first join**, three unique cards are drawn from the weighted pool and assigned to the player
2. Players open their trait menu with `/traits` to view active cards and reroll
3. Each card applies its effects passively (tick task) or reactively (event listeners)
4. Rerolling costs money and has a cooldown — **full reroll** replaces all 3, **single reroll** replaces one

---

## Tarot Cards

Cards are drawn from 22 Major Arcana across 4 rarity tiers. Higher-rarity cards are significantly rarer.

| Rarity | Weight | Examples |
| --- | --- | --- |
| **Common** | 10 | The Fool, The Magician, The High Priestess, The Empress, The Chariot, Strength, The Hermit, Wheel of Fortune, Justice, The World |
| **Uncommon** | 6 | The Emperor, The Hierophant, The Lovers, The Moon, The Sun, Temperance, The Star |
| **Rare** | 3 | The Tower, The Devil, The Hermit King |
| **Legendary** | 1 | Judgement, Death |

---

## Commands

| Command | Permission | Description |
| --- | --- | --- |
| `/traits` | *(all players)* | Open the Tarot Traits GUI |
| `/traits info` | *(all players)* | List current cards in chat |
| `/traits admin set <player> <slot 1-3> <CARD_NAME>` | `nexusprism.traits.admin` | Force-set a card (bypasses cost and cooldown) |
| `/traits admin reload` | `nexusprism.traits.admin` | Reload `traits/config.yml` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.traits.admin` | Admin trait management commands | OP |

---

## Configuration (`traits/config.yml`)

```yaml
reroll:
  full-cost: 5000.0                 # Money cost to reroll all 3 cards
  single-cost: 2000.0               # Money cost to reroll a single card
  full-cooldown-seconds: 604800     # 7 days between full rerolls
  single-cooldown-seconds: 86400    # 24 hours between single rerolls
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `reroll.full-cost` | Money deducted from the player's balance for a full 3-card reroll |
| `reroll.single-cost` | Money deducted for replacing a single card |
| `reroll.full-cooldown-seconds` | Minimum seconds between full rerolls (default: 7 days) |
| `reroll.single-cooldown-seconds` | Minimum seconds between single rerolls (default: 24 hours) |

!!! info "Single reroll exclusion"
    When a player rerolls a single card, all currently held cards are excluded from the draw pool — the replacement will always be a different card.
