# Módulo Dreams

O módulo Dreams aciona uma **experiência cinematográfica ao dormir** quando um jogador deita em uma cama. Com uma chance configurável, os jogadores são transportados para uma cutscene de sonho ou pesadelo antes de acordar no local original.

---

## Como Funciona

1. Um jogador deita em uma cama
2. Há uma chance configurável (`dream_trigger_chance`) de que uma cutscene seja acionada
3. O jogador é teleportado para o mundo de sonho ou pesadelo
4. Efeitos de poção, mensagens e um temporizador criam uma sequência atmosférica
5. Após a duração, o jogador é retornado à sua localização original na cama

---

## Sonho vs. Pesadelo

| Tipo | Chance | Efeitos Padrão | Clima |
| --- | --- | --- | --- |
| **Sonho** | 40% (da chance de ativação) | Visão Noturna, Lentidão | Pacífico, etéreo |
| **Pesadelo** | 60% (da chance de ativação) | Cegueira, Náusea, Lentidão | Sombrio, perturbador |

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/dreams reload` | Recarregar configuração dos sonhos | `nexusprism.dreams.admin` |
| `/dreams trigger <player>` | Forçar um sonho para um jogador | `nexusprism.dreams.admin` |
| `/dreams trigger <player> nightmare` | Forçar um pesadelo | `nexusprism.dreams.admin` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.dreams.admin` | Comandos administrativos de sonhos | OP |

---

## Configuração (`dreams/config.yml`)

```yaml
# Chance base (%) de que dormir acione a cutscene
dream_trigger_chance: 25

dimension:
  enabled: true

  nightmare:
    world: ""              # Nome do mundo — deixe vazio para usar o mundo principal
    x: 0.0
    y: 64.0
    z: 0.0
    yaw: 0.0
    pitch: 0.0
    chance: 60             # Probabilidade (%) de pesadelo em relação a sonho
    duration: 300          # Duração em ticks (300 = 15 segundos)
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

### Campos de Configuração

| Campo | Descrição |
| --- | --- |
| `dream_trigger_chance` | Porcentagem de chance de que um sono acione o sistema. |
| `dimension.enabled` | Ativa a cutscene de teleporte. |
| `nightmare.chance` | Das cutscenes acionadas, qual % são pesadelos. |
| `duration` | Por quanto tempo (ticks) o jogador permanece na dimensão. 20 ticks = 1 segundo. |
| `effects` | Lista de efeitos de poção no formato `EFEITO:AMPLIFICADOR` (amplificador 0 = nível I). |
| `messages.*` | Mensagens cinematográficas exibidas durante a sequência. Suporta códigos de cor `&`. |

---

## Configurando Mundos de Sonho

Para a melhor experiência, crie mundos planos ou atmosféricos dedicados para sonhos e pesadelos:

1. Crie o mundo (com um plugin de gerenciamento de mundos ou Multiverse)
2. Defina as coordenadas em `dreams/config.yml` em `dimension.dreams.world` e `dimension.nightmare.world`
3. Construa cenários atmosféricos nessas coordenadas
4. Recarregue com `/dreams reload`

!!! tip
    Deixe `world` vazio para usar o mundo principal. Os jogadores serão teleportados para as coordenadas XYZ configuradas no mundo padrão.

---

## Integração com o Arco do Sacrifício

Quando o módulo **Events** está ativo, o **Arco do Sacrifício** pode suprimir completamente a cutscene normal de sonho.

Se a sequência de sobrevivência à Lua de Sangue de um jogador atingir um múltiplo de 7 (7, 14, 21, 28...) e o jogador entrar em uma cama, o Arco do Sacrifício intercepta o evento de dormir **antes** de qualquer sonho ou pesadelo ser sorteado. Em vez disso, é exibida uma GUI de escolha.

!!! info
    Este comportamento é controlado pelo `DreamsManager.SACRIFICE_HOOK` — um hook definido pelo módulo Events no carregamento e removido no desligamento. Se o módulo Events estiver desativado, os sonhos funcionam exatamente como descrito acima, sem alterações.

Veja o [módulo Events](events.md) para mais detalhes sobre o Arco do Sacrifício.
