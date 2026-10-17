# Módulo Custom Mobs

O módulo Custom Mobs permite que administradores de servidores definam **bosses baseados em YAML** com saúde, equipamento, efeitos de poção, formas de IA, tabelas de loot e ovos de spawn personalizados — tudo sem escrever código Java.

---

## Visão Geral

| Funcionalidade | Descrição |
| --- | --- |
| **Definições em YAML** | Cada boss é um único arquivo `.yml` em `custommobs/bosses/` |
| **Formas de IA** | Bosses alternam entre estilos de combate (SWORD, DAGGER, GLADIUS…) |
| **Equipamento** | Conjunto completo de armadura e armas |
| **Efeitos de Poção** | Efeitos permanentes aplicados ao boss |
| **Tabelas de Loot** | Drops garantidos e drops por chance |
| **Ovos de Spawn** | Ovos de spawn personalizados criados ou fornecidos com `/bossegg` |
| **Persistente** | Bosses sobrevivem a reinicializações do servidor |

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/boss spawn <id>` | Invocar um boss na sua localização | `nexusprism.boss.admin` |
| `/boss spawn <id> <mundo> <x> <y> <z>` | Invocar em coordenadas | `nexusprism.boss.admin` |
| `/boss list` | Listar todos os bosses registrados | `nexusprism.boss.admin` |
| `/boss info <id>` | Mostrar detalhes da definição do boss | `nexusprism.boss.admin` |
| `/boss kill <id>` | Matar todas as instâncias ativas de um boss | `nexusprism.boss.admin` |
| `/bossegg give <jogador> <id>` | Dar um ovo de spawn de boss | `nexusprism.boss.admin` |
| `/bossegg <id>` | Obter seu próprio ovo de spawn de boss | `nexusprism.boss.admin` |

---

## Formato YAML de Boss

Os arquivos de boss são colocados em `plugins/NexusPrism/custommobs/bosses/<id>.yml`.

### Exemplo Completo (`white_death.yml`)

```yaml
name: "§uEchoes §tof §sthe §bWhite §fDeath"
entity: WITHER_SKELETON
health: 200.0
persistent: true

equipment:
  helmet:     GOLDEN_HELMET
  chestplate: GOLDEN_CHESTPLATE
  leggings:   GOLDEN_LEGGINGS
  boots:      GOLDEN_BOOTS
  main_hand:  DIAMOND_SWORD
  off_hand:   SHIELD

potion_effects:
  - SPEED:2

ai_forms:
  - type: SWORD
    weight: 5
  - type: DAGGER
    weight: 3
  - type: GLADIUS
    weight: 2

loot:
  always:
    - SHADOW_SHARD:1
    - SNOWBALL:5
    - ENCHANTED_BOOK:1
  chance:
    - item: FROZEN_DAGGER
      chance: 0.20
    - item: GLADIUS
      chance: 0.10

form_switch_interval_ticks: 300
```

### Referência de Campos

| Campo | Tipo | Descrição |
| --- | --- | --- |
| `name` | String | Nome de exibição com códigos de cor `&`/`§` |
| `entity` | EntityType do Bukkit | Tipo de entidade base (ex: `WITHER_SKELETON`, `ZOMBIE`) |
| `health` | Double | Saúde máxima em meias vidas |
| `persistent` | Boolean | Se `true`, o boss persiste após descarregamento de chunks/reinicializações |
| `equipment.*` | Material | Slots de equipamento: `helmet`, `chestplate`, `leggings`, `boots`, `main_hand`, `off_hand` |
| `potion_effects` | Lista | Efeitos permanentes no formato `EFEITO:AMPLIFICADOR` |
| `ai_forms` | Lista | Estilos de combate que o boss alterna |
| `ai_forms[].type` | String | ID da forma de IA (`SWORD`, `DAGGER`, `GLADIUS`, etc.) |
| `ai_forms[].weight` | Integer | Peso relativo para seleção aleatória |
| `loot.always` | Lista | Drops garantidos no formato `ID_ITEM:quantidade` |
| `loot.chance` | Lista | Drops por chance com `item` e `chance` (0.0–1.0) |
| `form_switch_interval_ticks` | Integer | Ticks entre trocas de forma de IA (300 = 15 segundos) |

### Itens de Loot

Tanto nomes de `Material` do Bukkit quanto IDs de itens personalizados do NexusPrism podem ser usados nas tabelas de loot:

```yaml
loot:
  always:
    - DIAMOND:3           # Material vanilla
    - NEXUS_SHARD:1       # ID de item personalizado do NexusPrism
  chance:
    - item: BOSS_TROPHY
      chance: 0.05        # 5% de chance de drop
```

---

## Tipos de Forma de IA

| Forma | Descrição |
| --- | --- |
| `SWORD` | Corpo a corpo agressivo, avança em direção ao alvo |
| `DAGGER` | Ataques rápidos de hit-and-run |
| `GLADIUS` | Ataque equilibrado com ataques de escudo |

Formas de IA personalizadas podem ser adicionadas criando módulos addon usando a `nexusprism-api`.

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.boss.admin` | Todos os comandos de boss e ovo de spawn | OP |

---

## Uso do Ovo de Spawn

Ovos de spawn fornecidos com `/bossegg give <jogador> <id>` podem ser clicados com o botão direito no mundo para invocar o boss. O item de ovo mostra o nome do boss e uma prévia de sua saúde no lore.
