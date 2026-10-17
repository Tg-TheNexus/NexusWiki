# Módulo Crates

O módulo Crates oferece **caixas de loot baseadas em chaves** com animações de abertura, efeitos de partículas em idle e tabelas de recompensas configuráveis por caixa.

---

## Como Funciona

1. Um admin coloca um bloco e o registra como caixa com `/crate setblock <id>`
2. O jogador recebe chaves (virtuais ou físicas) via `/crate give`
3. O jogador clica com botão direito no bloco da caixa — a chave é consumida e a animação de abertura começa
4. Uma recompensa aleatória é selecionada e entregue

---

## Modos de Chave

| Modo | Descrição |
| --- | --- |
| `VIRTUAL` *(padrão)* | Chaves armazenadas no banco de dados — sem risco de duplicação, sem item no inventário |
| `PHYSICAL` | Chaves são itens `TRIPWIRE_HOOK` com tag PDC correspondendo ao ID da caixa |

---

## Comandos

| Comando | Permissão | Descrição |
| --- | --- | --- |
| `/crate give <jogador> <caixa> [quantidade]` | `nexusprism.crates.admin` | Dar chaves de caixa a um jogador |
| `/crate keys [jogador]` | `nexusprism.crates.use` | Ver saldo de chaves virtuais |
| `/crate setblock <caixa>` | `nexusprism.crates.admin` | Registrar o bloco mirado como uma caixa |
| `/crate removeblock` | `nexusprism.crates.admin` | Desregistrar o bloco mirado |
| `/crate preview <caixa>` | *(todos os jogadores)* | Visualizar possíveis recompensas |
| `/crate list` | *(todos os jogadores)* | Listar todos os tipos de caixa |
| `/crate reload` | `nexusprism.crates.admin` | Recarregar todas as definições de caixas |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.crates.admin` | Criar, remover e dar caixas | OP |
| `nexusprism.crates.use` | Verificar saldo de chaves | true |

---

## Configuração

### Config Global (`crates/config.yml`)

```yaml
key-mode: VIRTUAL        # VIRTUAL | PHYSICAL
```

### Definição de Caixa (`crates/<id>.yml`)

```yaml
display-name: "&aCaixa Comum"
block-material: WHITE_SHULKER_BOX

broadcast-wins: false
preview: true

opening:
  mode: SPIN          # SPIN | INSTANT
  firework: false

particles:
  idle:
    type: END_ROD
    count: 5
  win:
    type: FIREWORK
    count: 30

rewards:
  - type: ITEM
    data: IRON_INGOT
    amount: 8
    weight: 30
    display-name: "&78x Lingote de Ferro"
  - type: MONEY
    data: "500"
    weight: 25
    display-name: "&a$500"
  - type: COMMAND
    data: "give {player} minecraft:diamond 1"
    weight: 5
    display-name: "&bDiamante Bônus"
```
