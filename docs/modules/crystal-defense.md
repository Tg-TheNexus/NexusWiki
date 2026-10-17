# Módulo Crystal Defense

Crystal Defense é um **minigame cooperativo em ondas** onde os jogadores defendem Ender Crystals contra hordas de mobs cada vez mais difíceis. Os jogadores ganham pontos por morte e os gastam em melhorias da arena.

---

## Como Jogar

1. Um administrador cria uma arena com `/crystal create <nome>`
2. Os jogadores entram na arena com `/crystal join <nome>`
3. O jogo começa automaticamente quando houver jogadores suficientes prontos (ou manualmente com `/crystal start`)
4. Mobs surgem em ondas — elimine-os antes que destruam o cristal
5. Gaste os pontos de abate em melhorias entre as ondas
6. O jogo termina quando o HP do cristal chega a zero

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/crystal join <arena>` | Entrar em uma arena | `nexusprism.crystaldefense.use` |
| `/crystal leave` | Sair da arena atual | `nexusprism.crystaldefense.use` |
| `/crystal list` | Listar arenas disponíveis | `nexusprism.crystaldefense.use` |
| `/crystal status` | Exibir onda atual e HP do cristal | `nexusprism.crystaldefense.use` |
| `/crystal create <nome>` | Criar uma nova arena | `nexusprism.crystaldefense.admin` |
| `/crystal delete <nome>` | Excluir uma arena | `nexusprism.crystaldefense.admin` |
| `/crystal setcrystal <arena>` | Definir localização do cristal | `nexusprism.crystaldefense.admin` |
| `/crystal setspawn <arena>` | Definir ponto de spawn dos jogadores | `nexusprism.crystaldefense.admin` |
| `/crystal start [arena]` | Forçar início de um jogo | `nexusprism.crystaldefense.admin` |
| `/crystal stop [arena]` | Parar um jogo | `nexusprism.crystaldefense.admin` |
| `/crystal reload` | Recarregar configurações das arenas | `nexusprism.crystaldefense.admin` |

---

## Configuração da Arena

1. Construa sua arena no mundo
2. Execute `/crystal create <nome>`
3. Fique na posição do Ender Crystal → `/crystal setcrystal <nome>`
4. Fique no ponto de spawn dos jogadores → `/crystal setspawn <nome>`
5. (Opcional) Edite `crystaldefense/config.yml` para configurar ondas e custos de melhorias

---

## Configuração Principal (`crystaldefense/config.yml`)

```yaml
arena:
  crystal-max-health: 1000.0    # HP padrão do cristal para novas arenas

points:
  per-kill: 5                   # Pontos ganhos por abate de mob

upgrades:
  crystal_health:
    base_cost: 20
    step_percent: 20            # HP máximo do cristal aumenta 20% por compra

  crystal_defense:
    base_cost: 25
    duration_seconds: 30        # Duração de RESISTANCE II aplicada a todos os jogadores

  player_attack_buff:
    base_cost: 30
    damage_percent: 20          # % de aumento no dano base de ataque do jogador
    duration_seconds: 60
```

---

## Definição de Ondas (`crystaldefense/waves.yml`)

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

## Melhorias

| Melhoria | Efeito | Custo Base |
| --- | --- | --- |
| **Crystal Health** | Aumenta o HP máximo do cristal em 20% por nível | 20 pontos |
| **Crystal Defense** | Aplica RESISTANCE II a todos os jogadores por 30s | 25 pontos |
| **Player Attack Buff** | +20% de dano por 60s | 30 pontos |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.crystaldefense.use` | Entrar em arenas e jogar | true |
| `nexusprism.crystaldefense.admin` | Criar/gerenciar arenas | OP |

---

## PlaceholderAPI

| Placeholder | Descrição |
| --- | --- |
| `%nexusprism_crystal_wave%` | Número da onda atual |
| `%nexusprism_crystal_health%` | HP restante do cristal |
| `%nexusprism_crystal_points%` | Pontos do jogador no jogo atual |
| `%nexusprism_crystal_arena%` | Arena em que o jogador está |
