# Módulo RNG

O módulo RNG oferece **giro diário de recompensas**, **blocos de sorte**, **pulls de gacha** via Pergaminhos de Pesquisa e **eventos automáticos de servidor** — tudo impulsionado por pools de recompensas configuráveis.

---

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Giro Diário** | Roleta de recompensas uma vez por dia (`/spin`) |
| **Blocos de Sorte** | Blocos colocáveis com tag PDC que executam uma recompensa aleatória ao quebrar |
| **Gacha** | Clique com botão direito em um Pergaminho de Pesquisa para fazer um pull do pool correspondente |
| **Eventos de Servidor** | Buffs automáticos cronometrados (Drops Duplos, XP Duplo, Corrida de Mineração, etc.) |

---

## Comandos

| Comando | Permissão | Descrição |
| --- | --- | --- |
| `/spin` | `nexusprism.rng.spin` | Abrir o GUI de giro diário |
| `/rng event start <id>` | `nexusprism.rng.admin` | Forçar início de um evento de servidor |
| `/rng event stop` | `nexusprism.rng.admin` | Parar o evento ativo |
| `/rng event list` | `nexusprism.rng.admin` | Listar todos os eventos definidos |
| `/rng giveblock <jogador> [pool] [quantidade]` | `nexusprism.rng.admin` | Dar itens de bloco de sorte |
| `/rng giveparchment <jogador> <BASIC\|ADVANCED\|INFINITY>` | `nexusprism.rng.admin` | Dar um Pergaminho de Pesquisa |
| `/rng research get <jogador>` | `nexusprism.rng.admin` | Verificar o nível de pesquisa de um jogador |
| `/rng research set <jogador> <nível>` | `nexusprism.rng.admin` | Definir o nível de pesquisa de um jogador |
| `/rng reload` | `nexusprism.rng.admin` | Recarregar configuração, eventos e pools |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.rng.spin` | Usar o giro diário | true |
| `nexusprism.rng.admin` | Todos os comandos administrativos de RNG | OP |

---

## Configuração (`rng/config.yml`)

```yaml
daily-spin:
  cooldown-seconds: 86400    # 24 horas entre giros
  pool: daily                # ID do pool de recompensas usado para o giro

server-events:
  enabled: true
  interval-minutes: 90       # Evento aleatório a cada ~90 minutos

gacha:
  xp-per-pull: 1             # XP de pesquisa ganho por pull de gacha
```

---

## Pools de Recompensas (`rng/pools/*.yml`)

```yaml
pool-id: daily
rewards:
  - type: MONEY
    data: "500"
    weight: 30
    display-name: "&a$500"
  - type: ITEM
    data: DIAMOND
    amount: 3
    weight: 5
    display-name: "&b3x Diamante"
  - type: COMMAND
    data: "give {player} minecraft:totem_of_undying 1"
    weight: 1
    display-name: "&6Totem da Imortalidade"
```

---

## Eventos de Servidor (`rng/events.yml`)

| Tipo de Evento | Efeito |
| --- | --- |
| `DOUBLE_DROPS` | Todos os drops de blocos/mobs são dobrados |
| `DOUBLE_XP` | Todo ganho de XP é dobrado |
| `MOB_RUSH` | Taxa de spawn de mobs aumentada no servidor |
| `MINING_RUSH` | Drops bônus ao minerar minérios |
| `TRADING_BOOST` | Melhores preços de troca com aldeões |
| `HAPPY_HOUR` | Bônus combinado (drops + XP) |
| `CUSTOM` | Executa apenas um comando/transmissão personalizada |

---

## Gacha (Pergaminhos de Pesquisa)

| Nível do Pergaminho | Pool | Nível de Pesquisa Mínimo |
| --- | --- | --- |
| `BASIC` | `gacha_basic` | 0 |
| `ADVANCED` | `gacha_advanced` | 5 |
| `INFINITY` | `gacha_infinity` | 10 |
