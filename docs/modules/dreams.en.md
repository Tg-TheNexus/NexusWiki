# Dreams Module

The Dreams module triggers a **cinematic sleep experience** when a player sleeps in a bed. With a configurable chance, players are transported to a dream or nightmare dimension cutscene before waking back up at their original location.

---

## How It Works

1. A player sleeps in a bed
2. There is a configurable chance (`dream_trigger_chance`) that a cutscene triggers
3. The player is teleported to the dream or nightmare world
4. Potion effects, messages, and a timer create an atmospheric sequence
5. After the duration, the player is returned to their original bed location

---

## Dream vs Nightmare

| Type | Chance | Default Effects | Mood |
| --- | --- | --- | --- |
| **Dream** | 40% (of trigger chance) | Night Vision, Slowness | Peaceful, ethereal |
| **Nightmare** | 60% (of trigger chance) | Blindness, Nausea, Slowness | Dark, unsettling |

---

## Commands

| Command | Usage | Permission |
| --- | --- | --- |
| `/dreams reload` | Reload dreams configuration | `nexusprism.dreams.admin` |
| `/dreams trigger <player>` | Force-trigger a dream for a player | `nexusprism.dreams.admin` |
| `/dreams trigger <player> nightmare` | Force a nightmare | `nexusprism.dreams.admin` |

---

## Permissions

| Permission | Description | Default |
| --- | --- | --- |
| `nexusprism.dreams.admin` | Admin dream commands | OP |

---

## Configuration (`dreams/config.yml`)

```yaml
# Base chance (%) that sleeping triggers the cutscene
dream_trigger_chance: 25

dimension:
  enabled: true

  nightmare:
    world: ""              # World name — leave empty to use main world
    x: 0.0
    y: 64.0
    z: 0.0
    yaw: 0.0
    pitch: 0.0
    chance: 60             # Probability (%) of nightmare vs dream
    duration: 300          # Duration in ticks (300 = 15 seconds)
    effects:
      - BLINDNESS:1
      - NAUSEA:1
      - SLOWNESS:1

  dreams:
    world: ""
    x: 0.0
    y: 64.0
    z: 0.0
    yaw: 0.0
    pitch: 0.0
    duration: 300
    effects:
      - NIGHT_VISION:1
      - SLOWNESS:0

messages:
  dream:
    flashback_init:   "&9You drift off peacefully..."
    flashback_middle: "&9So peaceful..."
    end:              "&7You slowly wake up."
  nightmare:
    flashback_init:   "&8A dark memory surfaces..."
    flashback_middle: "&8You can't look away..."
    flashback_scream: "&8!"
    end:              "&7You wake up in a cold sweat."
```

### Configuration Fields

| Field | Description |
| --- | --- |
| `dream_trigger_chance` | Percentage chance a sleep triggers the system. |
| `dimension.enabled` | Enable the teleport cutscene. |
| `nightmare.chance` | Of triggered cutscenes, what % are nightmares. |
| `duration` | How long (ticks) the player stays in the dimension. 20 ticks = 1 second. |
| `effects` | List of potion effects in `EFFECT:AMPLIFIER` format (amplifier 0 = level I). |
| `messages.*` | Cinematic messages shown during the sequence. Supports `&` color codes. |

---

## Setting Up Dream Worlds

For the best experience, create dedicated flat or atmospheric worlds for dreams and nightmares:

1. Create the world (with a world manager plugin or Multiverse)
2. Set the coordinates in `dreams/config.yml` under `dimension.dreams.world` and `dimension.nightmare.world`
3. Build atmospheric scenery at those coordinates
4. Reload with `/dreams reload`

!!! tip
    Leave `world` empty to use the main overworld. Players will be teleported to the configured XYZ coordinates in the default world.

---

## Sacrifice Arc Integration

When the **Events** module is loaded, the **Sacrifice Arc** can suppress the normal dream cutscene entirely.

If a player's Blood Moon survival streak has reached a multiple of 7 (7, 14, 21, 28...) and they enter a bed, the Sacrifice Arc intercepts the sleep event **before** any dream or nightmare is chosen. The player is shown a choice GUI instead of entering the cutscene.

!!! info
    This behaviour is controlled by `DreamsManager.SACRIFICE_HOOK` — a hook set by the Events module at load time and cleared on shutdown. If the Events module is disabled, dreams work exactly as described above with no changes.

See the [Events module](events.md) for full details on the Sacrifice Arc.
