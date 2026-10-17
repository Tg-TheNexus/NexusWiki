# Módulo Traits

O módulo Traits atribui a cada jogador um conjunto de **3 Cartas de Tarô** que concedem efeitos passivos e reativos. As cartas são sorteadas aleatoriamente no primeiro acesso e podem ser reroladas com custo em dinheiro.

---

## Como Funciona

1. No **primeiro acesso**, três cartas únicas são sorteadas do pool ponderado e atribuídas ao jogador
2. O jogador abre o menu de traits com `/traits` para ver as cartas ativas e rerolar
3. Cada carta aplica seus efeitos passivamente (tarefa de tick) ou de forma reativa (listeners de eventos)
4. O reroll custa dinheiro e tem cooldown — **reroll completo** substitui as 3, **reroll único** substitui uma

---

## Cartas de Tarô

As cartas são sorteadas dos 22 Arcanos Maiores em 4 níveis de raridade.

| Raridade | Peso | Exemplos |
| --- | --- | --- |
| **Comum** | 10 | O Louco, O Mago, A Sacerdotisa, A Imperatriz, O Carro, A Força, O Eremita, A Roda da Fortuna, A Justiça, O Mundo |
| **Incomum** | 6 | O Imperador, O Hierofante, Os Amantes, A Lua, O Sol, A Temperança, A Estrela |
| **Raro** | 3 | A Torre, O Diabo, O Rei Eremita |
| **Lendário** | 1 | O Julgamento, A Morte |

---

## Comandos

| Comando | Permissão | Descrição |
| --- | --- | --- |
| `/traits` | *(todos os jogadores)* | Abrir o GUI de Traits de Tarô |
| `/traits info` | *(todos os jogadores)* | Listar as cartas atuais no chat |
| `/traits admin set <jogador> <slot 1-3> <NOME_DA_CARTA>` | `nexusprism.traits.admin` | Forçar a definição de uma carta (ignora custo e cooldown) |
| `/traits admin reload` | `nexusprism.traits.admin` | Recarregar `traits/config.yml` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.traits.admin` | Comandos administrativos de traits | OP |

---

## Configuração (`traits/config.yml`)

```yaml
reroll:
  full-cost: 5000.0                 # Custo em dinheiro para rerolar as 3 cartas
  single-cost: 2000.0               # Custo para rerolar uma única carta
  full-cooldown-seconds: 604800     # 7 dias entre rerolls completos
  single-cooldown-seconds: 86400    # 24 horas entre rerolls únicos
```

!!! info "Exclusão no reroll único"
    Ao rerolar uma única carta, todas as cartas atualmente equipadas são excluídas do pool de sorteio — a substituição será sempre uma carta diferente.
