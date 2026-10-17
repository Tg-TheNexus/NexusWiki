# Módulo Enchantments

O módulo Enchantments adiciona **175 encantamentos personalizados** em 6 níveis de raridade e 10 tipos de gatilho. Todos os encantamentos são definidos em `enchants/config.yml` — nenhum código Java é necessário para adicionar novos.

---

## Raridades

| Raridade | Cor | Custo em XP | Peso |
| --- | --- | --- | --- |
| **Comum** | Branco `§f` | 3 XP | 100 |
| **Incomum** | Verde `§a` | 8 XP | 50 |
| **Raro** | Azul `§9` | 15 XP | 20 |
| **Épico** | Roxo `§5` | 25 XP | 8 |
| **Lendário** | Dourado `§6` | 40 XP | 3 |
| **Mítico** | Vermelho `§c` | 60 XP | 1 |

---

## Tipos de Gatilho

| Gatilho | Quando dispara |
| --- | --- |
| `ON_HIT` | Quando o jogador causa dano corpo a corpo |
| `ON_KILL` | Quando o jogador mata uma entidade |
| `ON_MINE` | Quando o jogador quebra um bloco |
| `ON_BREAK` | Quando o item do jogador está prestes a quebrar |
| `ON_DEATH` | Quando o jogador morre |
| `ON_DAMAGE_TAKEN` | Quando o jogador recebe dano |
| `PASSIVE` | Executado continuamente em uma tarefa de tick |
| `ON_JUMP` | Quando o jogador pula |
| `ON_SHOOT` | Quando o jogador dispara um projétil |
| `VOID` | Quando o jogador cai abaixo de Y=0 |

---

## Comandos

Todos os comandos requerem `nexusprism.enchantments.admin`.

| Comando | Descrição |
| --- | --- |
| `/enchant list` | Listar todos os encantamentos com ID, raridade e status |
| `/enchant info <id>` | Mostrar detalhes: nível máximo, grupos de itens, conflitos |
| `/enchant give <jogador> <id> [nível]` | Dar um livro de encantamento a um jogador |
| `/enchant apply <id> [nível]` | Aplicar um encantamento diretamente no item na mão |
| `/enchant remove <id>` | Remover um encantamento do item na mão |
| `/enchant reload` | Recarregar `enchants/config.yml` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.enchantments.admin` | Todos os comandos de gerenciamento de encantamentos | OP |

---

## Configuração (`enchants/config.yml`)

```yaml
enchants:
  lifesteal:
    enabled: true
    display-name: "&cRoubo de Vida"
    rarity: UNCOMMON
    trigger: ON_HIT
    max-level: 3
    applicable-items: [SWORD, AXE]
    conflicts: []
    vanilla-conflicts: []
    heal-percent-per-level: 0.10
```

---

## Como Funcionam os Livros de Encantamento

- Clicar com botão direito em um livro aplica o encantamento ao item na **mão secundária**
- Encantamentos são armazenados via **PDC** com a chave `enchant_<id>`
- Encantamentos aplicados aparecem no lore do item como `<Cor><Nome> <Algarismo Romano> §8[Enchant]`
