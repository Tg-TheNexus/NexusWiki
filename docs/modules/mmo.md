# Módulo MMO

O módulo MMO transforma o NexusPrism em uma experiência leve de RPG. Os jogadores ganham um **nível MMO**, alocam **pontos de atributo**, sobem de nível em **seis árvores de habilidades**, desbloqueiam e usam **habilidades**, e progridem por **oito profissões** — cada uma com uma passiva de maestria única.

---

## Nível MMO e Pontos de Atributo

Os jogadores ganham XP MMO de qualquer atividade no jogo (combate, profissões, árvores de habilidades). Subir de nível concede **1 ponto de atributo** não gasto para usar livremente.

### Fórmula de XP para Nível

```
xpParaNível(n) = 100 × 2^((n-1) / 10)
```

O requisito de XP dobra a cada 10 níveis.

### Atributos

| Atributo | Efeito |
| --- | --- |
| `MAX_HEALTH` | Aumenta os corações máximos |
| `STRENGTH` | +1,5% de dano corpo a corpo por ponto |
| `DEFENSE` | -0,8% de dano recebido por ponto (máx. 80% de redução) |
| `AGILITY` | +0,5% de chance de esquiva por ponto (golpe cancelado, "Esquivou!" na actionbar) |
| `INTELLIGENCE` | Aumenta o poder das habilidades mágicas |
| `WISDOM` | Afeta a eficácia de cura e custos equivalentes a mana |
| `LUCK` | Melhora as taxas de drop e resultados aleatórios |
| `CRIT_CHANCE` | +1% de chance de acerto crítico por ponto (máx. 95%) |
| `CRIT_DAMAGE` | Multiplicador de crítico = `1,5 + (critDano × 0,01)` |
| `MAGIC_POWER` | Amplifica o dano das habilidades mágicas |
| `MINING_SPEED` | Aumenta a velocidade de quebrar blocos |
| `FISHING_LUCK` | Melhora a qualidade do tesouro da pesca |

**Valor final do atributo** = base (alocado pelo jogador) + bônus da árvore de habilidades + bônus futuros de equipamentos.

### Comandos

| Comando | Descrição |
| --- | --- |
| `/stats` | Ver sua ficha de atributos e pontos não gastos |
| `/stats add <atributo>` | Gastar 1 ponto de atributo (ex.: `/stats add strength`) |

---

## Árvores de Habilidades

Seis árvores de habilidades independentes, cada uma aumentada de nível por atividades específicas. Subir de nível concede bônus passivos de atributos e desbloqueia habilidades em marcos.

### Visão Geral das Árvores

| Árvore | Atributos Principais | Fonte de XP | Habilidades |
| --- | --- | --- | --- |
| **Guerreiro** | Força, Defesa, Vida Máxima | Abates corpo a corpo | Golpe de Escudo (10), Fúria Berserker (25), Aura de Senhor da Guerra (50) |
| **Ladino** | Agilidade, Chance Crítica, Dano Crítico | Abates | Passo Sombrio (10), Ataque nas Costas (25), Forma Fantasma (50) |
| **Mago** | Inteligência, Poder Mágico, Sabedoria | Encantamentos | Bola de Fogo (10), Escudo Arcano (25), Explosão Nova (50) |
| **Arqueiro** | Agilidade, Chance Crítica, Sorte | Abates | Chuva de Flechas (10), Olho de Águia (25), Tiro Perfurante (50) |
| **Curandeiro** | Sabedoria, Vida Máxima, Defesa | Cura | Aura Sagrada (10), Ressuscitar (25), Santuário (50) |
| **Alquimista** | Sorte, Inteligência, Sabedoria | Preparo de poções | Nuvem Tóxica (10), Surto de Elixir (25), Toque do Filósofo (50) |

### Descrições das Habilidades

=== "Guerreiro"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Golpe de Escudo** | Causa dano em cone e empurrão à frente do jogador |
    | 25 | **Fúria Berserker** | Dano corpo a corpo ×2 por 8 segundos |
    | 50 | **Aura de Senhor da Guerra** | Passiva: +30% de dano corpo a corpo permanentemente |

=== "Ladino"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Passo Sombrio** | Teleportar 6 blocos na direção em que está olhando |
    | 25 | **Ataque nas Costas** | Causa 4× de dano ao acertar um alvo pelas costas |
    | 50 | **Forma Fantasma** | 5 segundos de invisibilidade + +200% de dano |

=== "Mago"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Bola de Fogo** | Lança um projétil explosivo com rastro de partículas de chama |
    | 25 | **Escudo Arcano** | 3 orbes orbitando, cada um absorvendo 1 golpe recebido |
    | 50 | **Explosão Nova** | Explosão arcana em área centrada no jogador |

=== "Arqueiro"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Chuva de Flechas** | Disparar 9 flechas críticas em arco radial |
    | 25 | **Olho de Águia** | Disparar uma única flecha perfurante que passa pelos mobs |
    | 50 | **Tiro Perfurante** | Flecha com 5× de dano que ignora toda defesa |

=== "Curandeiro"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Aura Sagrada** | Restaurar 6 corações em todos os aliados próximos |
    | 25 | **Ressuscitar** | Previne o próximo golpe fatal (escudo único) |
    | 50 | **Santuário** | Criar uma zona de cura de 10 blocos com duração de 15 segundos |

=== "Alquimista"

    | Nível | Habilidade | Descrição |
    | --- | --- | --- |
    | 10 | **Nuvem Tóxica** | Implantar uma nuvem de veneno persistente |
    | 25 | **Surto de Elixir** | Compartilhar todas as suas poções ativas com aliados próximos |
    | 50 | **Toque do Filósofo** | Chance passiva de duplicar qualquer poção preparada |

!!! warning "Habilidades ocultas"
    Algumas habilidades não estão listadas aqui. Elas existem — mas suas condições, custos e nomes são para você descobrir.

### Usando Habilidades

```
/skill use <idHabilidade>
```

Ou abra `/skill`, clique em uma árvore e depois clique no ícone da habilidade. Os tempos de recarga são rastreados por jogador por habilidade.

### Vinculação de Teclas de Habilidades

Jogadores podem vincular habilidades desbloqueadas a slots da hotbar para ativação rápida sem digitar comandos. Abra `/skill keybind` para configurar os vínculos via GUI — cada slot mostra o nome da habilidade, o custo de mana e o cooldown atual. Pressionar a tecla da hotbar vinculada ativa a habilidade instantaneamente.

### Comandos

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/skill` | Abrir o GUI do Navegador de Árvores de Habilidades | `nexusprism.mmo.use` |
| `/skill use <id>` | Ativar uma habilidade desbloqueada | `nexusprism.mmo.use` |
| `/skill keybind` | Abrir o GUI de vinculação de teclas | `nexusprism.mmo.use` |

---

## Mana

Cada jogador possui uma **reserva de mana** que as habilidades consomem. O mana regenera passivamente com base no atributo **Sabedoria**.

| Mecânica | Detalhe |
| --- | --- |
| Reserva base | Escala com o nível MMO |
| Regeneração | Baseada em Sabedoria, sempre ativa |
| Mana insuficiente | Barra de ação: `§cMana insuficiente!` — habilidade bloqueada |
| Exibição do custo | Mostrado nos ícones de habilidade e no GUI de vinculação de teclas |

O pool de mana também está acessível pela [API de Addon](../developer/api.pt.md): `MmoRegistry.get()` → `getCurrentMana()`, `hasMana()`, `consumeMana()`.

---

## Profissões

Oito profissões sobem de nível independentemente das árvores de habilidades. Cada uma tem uma **passiva de maestria** que fica mais forte com o nível da profissão.

### Fórmula de XP

```
xpParaNível(n) = xpBase × 1,8^(nível / 10)
```

### Tabela de Profissões

| Profissão | Fonte de XP | Passiva de Maestria | Bônus Máx. |
| --- | --- | --- | --- |
| **Mineração** | Quebrar minérios | Minerador de Veio — dobrar chance de drop de minério | 50% |
| **Agricultura** | Quebrar plantações | Colheita Abundante — dobrar drop de colheita | 60% |
| **Pesca** | Pescar | Lançamento Sortudo — chance extra de tesouro | 40% |
| **Lenhador** | Quebrar troncos | Rachador de Madeira — dobrar drop de tronco | 50% |
| **Ferraria** | Criar/fundir ferramentas e armaduras | Artesão Mestre — duplicar ferramenta/armadura criada | 30% |
| **Alquimia** | Preparar poções | Duplicação de Poções — duplicar poções preparadas | 50% |
| **Encantamento** | Encantar itens | Eficiência Arcana — economizar níveis de XP ao encantar | 40% |
| **Culinária** | Criar/fundir alimentos | Gourmet — duplicar alimentos cozidos | 70% |

---

## Armazenamento e Permissões

| Detalhe | Valor |
| --- | --- |
| Banco de dados | SQLite — `mmo/mmo.db` |
| Tabelas | `player_mmo`, `player_skills`, `player_professions` |
| Permissão | `nexusprism.mmo.use` (padrão: **true**) |
