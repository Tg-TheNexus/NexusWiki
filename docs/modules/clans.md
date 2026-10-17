# Módulo Clãs

O módulo Clãs permite que jogadores criem equipes persistentes com **conquista de território**, **árvore de melhorias**, um **baú compartilhado** e **chat de clã**.

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/clan create <nome> <tag>` | Criar um novo clã | `nexusprism.clan.use` |
| `/clan disband` | Dissolver o clã | `nexusprism.clan.use` |
| `/clan invite <jogador>` | Convidar um jogador | `nexusprism.clan.use` |
| `/clan join <nome>` | Entrar em um clã | `nexusprism.clan.use` |
| `/clan leave` | Sair do clã | `nexusprism.clan.use` |
| `/clan kick <jogador>` | Expulsar um membro | `nexusprism.clan.use` |
| `/clan promote <jogador>` | Promover a oficial | `nexusprism.clan.use` |
| `/clan demote <jogador>` | Rebaixar a membro | `nexusprism.clan.use` |
| `/clan info [nome]` | Ver informações do clã | `nexusprism.clan.use` |
| `/clan list` | Listar todos os clãs | `nexusprism.clan.use` |
| `/clan chat` | Alternar chat de clã | `nexusprism.clan.use` |
| `/clan claim` | Reivindicar chunk atual | `nexusprism.clan.use` |
| `/clan unclaim` | Liberar chunk atual | `nexusprism.clan.use` |
| `/clan map` | Mostrar mapa de território | `nexusprism.clan.use` |
| `/clan chest` | Abrir baú do clã | `nexusprism.clan.use` |
| `/clan upgrade` | Abrir menu de melhorias | `nexusprism.clan.use` |
| `/clan top` | Placar de clãs | `nexusprism.clan.use` |
| `/clan admin disband <nome>` | Forçar dissolução (admin) | `nexusprism.clan.admin` |

---

## Cargos

| Cargo | Permissões |
| --- | --- |
| **Líder** | Todas as ações, dissolver, melhorar |
| **Oficial** | Convidar, expulsar membros, gerenciar território |
| **Membro** | Acessar baú, chat, usar território |

---

## Sistema de Território

Clãs reivindicam chunks como território. Membros podem construir livremente; não-membros são bloqueados (quando a proteção está ativada).

### Configuração (`clans/config.yml`)

```yaml
pvp-friendly-fire: false       # Membros não podem se atacar

clan-name-min-length: 3
clan-name-max-length: 16
clan-tag-min-length: 2
clan-tag-max-length: 4

base-member-cap: 10            # Membros no nível 1
base-territory-cap: 10         # Chunks reivindicáveis no nível 1

neutral-chunk-protection: false

territory-worlds:
  - world
  - world_nether
```

---

## Árvore de Melhorias (`clans/upgrades.yml`)

```yaml
upgrades:
  member_cap:
    display-name: "&aExpansão de Membros"
    description: "Aumenta o máximo de membros em 5."
    max-level: 5
    cost-per-level:
      money: 5000
    bonus-per-level:
      members: 5

  territory_cap:
    display-name: "&aExpansão de Território"
    description: "Reivindique 10 chunks adicionais por nível."
    max-level: 10
    cost-per-level:
      money: 3000
    bonus-per-level:
      chunks: 10
```

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.clan.use` | Usar comandos de clã | true |
| `nexusprism.clan.admin` | Gerenciamento admin de clãs | OP |
| `nexusprism.clan.bypass-protection` | Ignorar proteção de território | OP |

---

## PlaceholderAPI

| Placeholder | Descrição |
| --- | --- |
| `%nexusprism_clan_name%` | Nome do clã do jogador |
| `%nexusprism_clan_tag%` | Tag do clã |
| `%nexusprism_clan_role%` | Cargo do jogador no clã |
| `%nexusprism_clan_level%` | Nível do clã |
| `%nexusprism_clan_members%` | Contagem de membros online |
| `%nexusprism_clan_bank%` | Saldo do banco do clã |
