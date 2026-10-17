# Módulo Holograms

O módulo Holograms cria **textos e displays de itens flutuantes** no mundo, usando entidades `TextDisplay` e `ItemDisplay`. Todos os hologramas são definidos em `holograms.yml` e sobrevivem a reinicializações do servidor.

---

## Tipos de Linha

| Tipo | Descrição |
| --- | --- |
| `TEXT` | Linha de texto formatado. Suporta códigos de cor `&` e PlaceholderAPI. |
| `ITEM` | Ícone de item flutuante (qualquer `Material`). |
| `HEAD` | Cabeça de jogador (skin obtida de forma assíncrona). |

As linhas são empilhadas para cima com espaçamento de 0,3 blocos. A linha `0` é a mais alta.

---

## Comandos

Todos os subcomandos requerem `nexusprism.holograms.admin`.

| Comando | Descrição |
| --- | --- |
| `/holo create <id>` | Criar um holograma na sua localização |
| `/holo delete <id>` | Deletar um holograma |
| `/holo addline <id> text <texto…>` | Adicionar uma linha de texto |
| `/holo addline <id> item <MATERIAL>` | Adicionar uma linha de display de item |
| `/holo addline <id> head <jogador>` | Adicionar uma linha de cabeça de jogador |
| `/holo setline <id> <linha#> <texto…>` | Substituir uma linha de texto (índice base 0) |
| `/holo removeline <id> <linha#>` | Remover uma linha (índice base 0) |
| `/holo move <id>` | Mover o holograma para a sua localização atual |
| `/holo list` | Listar todos os IDs de hologramas |
| `/holo info <id>` | Mostrar mundo, coordenadas, visibilidade e linhas |
| `/holo show <id> <jogador>` | Forçar um jogador a ver um holograma no modo `PLAYERS` |
| `/holo hide <id> <jogador>` | Remover um jogador da lista de permissão `PLAYERS` |
| `/holo reload` | Recarregar todos os hologramas de `holograms.yml` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.holograms.admin` | Todos os comandos de gerenciamento de hologramas | OP |

---

## Modos de Visibilidade

| Modo | Comportamento |
| --- | --- |
| `GLOBAL` | Visível para todos os jogadores |
| `PERMISSION` | Visível apenas para jogadores com o nó definido em `permission:` |
| `PLAYERS` | Visível apenas para os UUIDs listados em `allowed-players:` |

---

## Configuração (`holograms.yml`)

```yaml
lobby-board:
  world: world
  x: 0.5
  y: 65.0
  z: 0.5
  visibility: GLOBAL
  permission: ""
  allowed-players:
    - "550e8400-e29b-41d4-a716-446655440000"
  lines:
    - type: TEXT
      content: "&b&lTop Jogadores"
    - type: HEAD
      player: "Notch"
    - type: TEXT
      content: "&71. &fNotch &7— &a1.200pts"
    - type: ITEM
      material: DIAMOND
```

!!! tip
    Os hologramas são recriados do zero ao usar `/holo reload` e ao iniciar o servidor. Eles usam entidades de display — sem armor stands.
