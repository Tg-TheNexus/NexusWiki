# Módulo Events

*Última atualização: 2026-03-22*

O módulo Events adiciona **eventos dinâmicos em escala mundial** que afetam todos os jogadores simultaneamente — começando com a **Lua de Sangue**, que transforma as noites em desafios de sobrevivência cada vez mais perigosos, vinculados a uma sequência por jogador e a um **Arco do Sacrifício**.

---

## Lua de Sangue

A Lua de Sangue é ativada automaticamente toda noite quando o tempo do mundo ultrapassa o **tick 13000** e é desativada ao amanhecer (**tick 23000**). Operadores do servidor também podem controlá-la manualmente.

### Efeitos Enquanto Ativa

| Efeito | Detalhe |
| --- | --- |
| Bônus de nível de mob | Todas as rolagens de Mobs com Nível recebem **+2** |
| Pagamento do emprego Caçador | Multiplicado pelo `kill-pay-multiplier` configurado (padrão ×1,5) |
| Chuva de partículas | Partículas DUST vermelhas aparecem ao redor de cada jogador online a cada 3 segundos |
| Ondas de horda | Uma horda de mobs aparece a cada `horde-interval-ticks` (padrão 5 min) |

Ao **amanhecer** (desativação), todo jogador online que sobreviveu ganha **+1** em sua sequência de sobrevivência.

### Ondas de Horda

A cada intervalo de horda, um jogador online aleatório é escolhido como alvo. **30 mobs** aparecem em um anel de 18 blocos ao redor dele: Zumbi, Esqueleto, Creeper, Aranha, Bruxa, Husk, Afogado. Todos os mobs da horda são nomeados `[Blood Moon]` em vermelho escuro.

### Comandos

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/bloodmoon` | Exibir status atual da Lua de Sangue | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon start` | Ativar a Lua de Sangue manualmente | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon stop` | Desativar a Lua de Sangue manualmente | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon status` | Saída de status detalhada | `nexusprism.events.bloodmoon.admin` |

### Configuração (`events/config.yml`)

```yaml
blood-moon:
  enabled: true
  world: world                     # O mundo onde as mudanças de tempo são monitoradas
  schedule: RANDOM                 # RANDOM (chance por noite) ou ALWAYS (sempre)
  random-chance-per-night: 15      # Chance (%) de ocorrer uma Lua de Sangue por noite (apenas RANDOM)
  kill-pay-multiplier: 1.5         # Multiplicador de pagamento do Caçador durante a Lua de Sangue
  particle-interval-ticks: 60     # Com que frequência (ticks) gerar partículas por jogador
  horde-interval-ticks: 6000      # Com que frequência (ticks) disparar uma onda de horda (6000 = 5 min)
  horde-size: 30                   # Número de mobs por onda de horda
```

---

## Sequência de Sobrevivência

Cada jogador tem uma **sequência de sobrevivência à Lua de Sangue** armazenada persistentemente em SQLite (`events/events.db`).

| Evento | Mudança na Sequência |
| --- | --- |
| Sobreviver a uma noite completa de Lua de Sangue | **+1** (concedido ao amanhecer) |
| Morrer durante uma Lua de Sangue | **Resetar para 0** |

Quando a sequência atinge um **múltiplo de 7** (7, 14, 21, 28...), o jogador recebe um **Convite de Sacrifício** na próxima vez que dormir.

### Escalonamento de Dificuldade por Sequência

Sequências maiores tornam cada Lua de Sangue mais difícil — mais níveis de mob, mais spawns e eventos de mini-chefe adicionais.

| Faixa de Sequência | Bônus de Nível | Bônus de Taxa de Spawn | Multiplicador Elite | Eventos Extras |
| --- | --- | --- | --- | --- |
| 1–6 | Base | Base | Base | — |
| 7–13 | +4 | +500% | ×3 | — |
| 14–20 | +7 | +700% | ×5 | Spawn de chefe no meio do evento |
| 21+ | +10 | +900% | Ilimitado | Mini-chefes a cada 5 min |

---

## Arco do Sacrifício

O Arco do Sacrifício é um desafio opcional de alto risco acionado pela sequência de sobrevivência. Ele se integra ao [módulo Dreams](dreams.md): quando a sequência se qualifica, dormir abre uma **GUI de escolha** em vez de uma cutscene de sonho.

### GUI de Escolha

Uma GUI de 3 linhas com duas opções:

| Slot | Item | Ação |
| --- | --- | --- |
| 11 | Lã Verde — **Aceitar** | Teleportar para a arena, desafio contra o Chefe Isekai |
| 15 | Lã Vermelha — **Recusar** | Resetar sequência, sem outra penalidade |

Fechar a GUI sem clicar conta como **Recusa**.

### Julgamento na Arena

1. O jogador é teleportado para a arena configurada (ou permanece na localização atual se não configurada)
2. Um **Chefe Isekai** aleatório é invocado — selecionado do pool elegível para a sequência do jogador
3. Uma **contagem regressiva de 180 segundos** começa com avisos em 60s, 30s, 10s e 5s

### Resultados

| Resultado | Consequência |
| --- | --- |
| **Sobreviver** | Recompensa concedida por tier, transmissão para o servidor, sequência resetada |
| **Morrer** | Sequência resetada para 0 |
| **Sair/desconectar** | Sessão encerrada, tratada como falha |

### Tiers de Recompensa do Sacrifício

As recompensas escalam de acordo com quantos Sacrifícios você completou (a cada 7 marcos de sequência).

| Marco de Sequência | Recompensas |
| --- | --- |
| **7** | Item MMO Tier 1 + **+5 HP Máx** permanente |
| **14** | Item MMO Tier 2 + **+10 HP Máx** permanente + **1 ponto de atributo** |
| **21** | Item MMO Tier 3 + **+2 pontos de atributo** permanentes + efeito cosmético |
| **28** | Item MMO Tier 4 + **+3 pontos de atributo** + título + ovo de chefe |
| **35+** | Pontos de atributo multiplicadores + cosmético anime exclusivo por marco |

!!! warning "Sequência Resetada Após o Sacrifício"
    Completar um Sacrifício — ganhar ou perder — reseta sua sequência para 0. Sua **melhor sequência** é registrada separadamente e nunca reseta.

### Configuração (`events/config.yml`)

```yaml
sacrifice:
  arena:
    world: ""    # Deixe em branco para usar o mundo atual do jogador
    x: 0.0
    y: 64.0
    z: 0.0
```

!!! tip "Configurando a Arena"
    Construa uma arena PvE dedicada e defina suas coordenadas em `sacrifice.arena`. Deixe `world` em branco para lutar no lugar — útil para testes.

---

## Codex de Chefes Isekai

Quando um Sacrifício é aceito, um **Chefe Isekai** aleatório é invocado na arena. O pool disponível depende da sequência atual do jogador. Cada chefe tem múltiplas fases, mecânicas únicas e uma drop única.

As definições de chefe ficam em `events/anime_bosses/*.yml`. HP e dano escalam com a sequência:

```
statFinal = statBase × (1 + (sequência - 7) × 0,2)
```

### Pool de Chefes

| Chefe | Sequência Mín. | Entidade Base | Peso de Spawn |
| --- | --- | --- | --- |
| Rimuru Tempest | 7 | Slime Gigante | 10 |
| Kazuma Satou | 7 | Bruxa | 9 |
| Subaru Natsuki | 7 | Zumbi | 8 |
| Ainz Ooal Gown | 14 | Esqueleto Wither | 7 |
| Itadori Yuji | 14 | Piglin Bruto | 6 |
| Kirito | 14 | Zumbi | 6 |
| Gojo Satoru | 21 | Phantom | 5 |
| Levi Ackermann | 21 | Vindicator | 4 |

---

=== "Rimuru Tempest"

    **Sequência Mín.:** 7 · **Entidade Base:** Slime Gigante

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 60% | Aura Predatória (absorve projéteis), Divisão de Slime (mini-slimes em 80%/70%) |
    | 2 | 60% → 25% | Tempestade de Aço (12 flechas em 360°), Dreno Predatório (cura ao acertar) — troca para Guardian |
    | 3 | 25% → 0% | Colapso do Vazio (puxão em AoE de 8 blocos, 3 dmg/tick), Regeneração Infinita (2 HP/2 ticks) — imune a recuo |

    **Drop:** Fragmento de núcleo de slime · Aura brilho azul cosmética

=== "Kazuma Satou"

    **Sequência Mín.:** 7 · **Entidade Base:** Bruxa

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 60% | Roubo (remove item aleatório do hotbar a cada 12s), Gatilho Sortudo (15% crit × 5 dano) |
    | 2 | 60% → 25% | Toque Drenante (drena níveis de XP), Comando de Grupo (2 "Aqua" + 1 "Darkness"), Explosão de Megumin (única na transição) |
    | 3 | 25% → 0% | Gatilho Sortudo sobe para 35% com reflexo de dano; Roubo Final; Chamada de Aqua (restauração de HP única) |

    **Drop:** Cartão de aventureiro · Itens roubados devolvidos em dobro

=== "Subaru Natsuki"

    **Sequência Mín.:** 7 · **Entidade Base:** Zumbi

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 50% | Slam no Chão, Chamado Desesperado (invoca "Rem" em 60%) |
    | **Retorno pela Morte** | Ao chegar a 0 HP (uma vez) | Reseta para 100% HP, HP do jogador restaurado, título: `⟳ RETURN BY DEATH` |
    | Pós-RBD | 100% → 0% | Fator da Bruxa (Wither I + Fome II a cada 20s), Último Ato (abaixo de 25%: +velocidade, +dano) |

    !!! danger "Retorno pela Morte"
        Subaru não pode ser morto na primeira vez. A mecânica dispara exatamente **uma vez por luta**.

    **Drop:** Moeda de prata cosmética · Aura "Cheiro da Bruxa"

=== "Ainz Ooal Gown"

    **Sequência Mín.:** 14 · **Entidade Base:** Esqueleto Wither

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 70% | Convocar Guardiões do Andar (3 zumbis a cada 30s), Explosão Negativa (crânio de wither → Wither II + Fraqueza) |
    | 2 | 70% → 30% | Garra da Morte (10 de dano verdadeiro atrasado 4s), Sabedoria Sombria (15s de imunidade ao tipo de dano repetido) |
    | 3 | 30% → 0% | Toque de Ainz (parado por 3s = morte instantânea), Devorador de Almas (cura 5 HP por entidade morta) |

    !!! warning "Não pode ser morto abaixo de 1 HP enquanto entidades convocadas estiverem vivas."

    **Drop:** Coroa Morta-Viva cosmética · Fragmento de título `§8Overlord`

=== "Itadori Yuji"

    **Sequência Mín.:** 14 · **Entidade Base:** Piglin Bruto

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 50% | Punho Divergente (8% proc Flash Negro = 10× dano), Investida (combo de 3 golpes telegrafado) |
    | 2 — **Sukuna Desperta** | 50% → 0% | Desmantelar (3 projéteis em V + sangramento), Golpe Amplo (AoE corpo a corpo de 5 blocos), Santuário Malevolente (abaixo de 20%: 20 cortes em 3s), Flash Negro sobe para 15% |

    **Drop:** Cristal de energia amaldiçoada · Título `§4Amaldiçoado` · Cosmético de tatuagem

=== "Kirito"

    **Sequência Mínima:** 14 · **Entidade Base:** Zumbi

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 40% | Habilidade de Espada Vorpal (investida de 5 golpes em linha reta), Aparar (20% de chance de negar um golpe) |
    | 2 — **???** | 40% → 0% | *Algo desperta a 40% de HP. Descubra você mesmo.* |

    **Drop:** Cosmético de élitra casaco preto · Título `§7Jogador Solo` · ???

    !!! quote "Lore"
        *Aquele que vence o Espadachim Negro herda mais do que um título.*

    !!! note ""
        `NjZhNzY2NjU3NTZlNzQ2YTZiNjM2YTZiNjM2YTZiNjM2YTZiNjM2YTZi`

=== "Gojo Satoru"

    **Sequência Mín.:** 21 · **Entidade Base:** Phantom

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 60% | Infinidade (70% dos ataques causam 1 dano), Mudança de Fase (invisível a cada 8s por 4s) |
    | 2 | 60% → 25% | Puxão Azul (puxa o jogador), Vazio Roxo (feixe AoE em linha reta — 1s de aviso, 15 dano + Levitação) |
    | 3 — **Expansão de Domínio** | 25% → 0% | Escuridão a cada 2s, Confusão em bursts, Golpe de Domínio (+50%), Infinidade TOTALMENTE ativa |

    !!! tip "Habilidades de mago e dano de fogo ignoram a Infinidade."

    **Drop:** Cosmético de venda · Título `§b∞ Limitless`

=== "Levi Ackermann"

    **Sequência Mín.:** 21 · **Entidade Base:** Vindicator

    | Fase | Faixa de HP | Habilidades Principais |
    | --- | --- | --- |
    | 1 | 100% → 50% | Carga ODM (teleporta para parede → arremessa para o jogador), Corte Limpo (ignora 50% da defesa), Manobra Vertical (VELOCIDADE IV em círculos por 3s) |
    | 2 | 50% → 0% | Parede a Parede (4 cargas encadeadas com tempo de telegrafamento decrescente), Forma Matador de Titã (abaixo de 25%: postura de 5s — um golpe para 0,5 coração, contorno branco telegrafado) |

    !!! danger "Não pode ser atordoado, empurrado ou desacelerado — jamais."

    **Drop:** Cosmético de élitra ODM · Título `§8Survey Corps` · Espada mata-titã CMD

---

### Pool de Chefes Futuros (Sequência 28+)

Chefes planejados para lançamentos futuros: Goku, Naruto Uzumaki, Aizen Sosuke, Natsu Dragneel, Sung Jin-Woo, Giorno Giovanna.

---

## Comandos Administrativos

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/bloodmoon` | Exibir status da Lua de Sangue | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon start` | Forçar a ativação da Lua de Sangue | `nexusprism.events.bloodmoon.admin` |
| `/bloodmoon stop` | Forçar a desativação da Lua de Sangue | `nexusprism.events.bloodmoon.admin` |
| `/isekai` | Exibir lutas ativas do chefe Isekai | `nexusprism.events.isekai.admin` |
| `/isekai force <jogador>` | Forçar o início de uma luta para um jogador | `nexusprism.events.isekai.admin` |
| `/isekai force <jogador> <chefId>` | Forçar com um chefe específico | `nexusprism.events.isekai.admin` |
| `/isekai stop <jogador>` | Encerrar uma luta ativa | `nexusprism.events.isekai.admin` |
| `/isekai list` | Listar todos os IDs de chefes disponíveis | `nexusprism.events.isekai.admin` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.events.bloodmoon.admin` | Controlar a Lua de Sangue manualmente | OP |
| `nexusprism.events.isekai.admin` | Controlar lutas de chefes Isekai manualmente | OP |
