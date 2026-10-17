# Referência de Comandos

Lista completa de todos os comandos registrados pelo NexusPrism, organizados por módulo.

**Legenda:**

- `<arg>` — argumento obrigatório
- `[arg]` — argumento opcional
- `(OP)` — apenas para operadores por padrão
- `(true)` — disponível para todos os jogadores por padrão

---

## Core / Plugin

| Comando | Aliases | Descrição | Permissão |
| --- | --- | --- | --- |
| `/nexusprism help` | `/ns`, `/nexus`, `/slime` | Mostrar ajuda | `nexusprism.command` |
| `/nexusprism info` | | Versão e status do plugin | `nexusprism.command` |
| `/nexusprism reload` | | Recarregar todas as configurações | `nexusprism.admin.reload` |
| `/nexusprism give <player> <item>` | | Dar um item — requer NexusATS | `nexusprism.admin.give` |
| `/nexusprism guide` | | Abrir guia de itens — requer NexusATS | `nexusprism.command` |
| `/nexusprism modules` | | Listar todos os módulos carregados | `nexusprism.command` |
| `/nexusprism machines` | | Informações de máquina — requer NexusATS | `nexusprism.command` |
| `/nexusprism research` | | Menu de pesquisa — requer NexusATS | `nexusprism.command` |
| `/recipe <item>` | | Mostrar receita(s) de crafting | `nexusprism.recipe` |

> **Removido em 2026-08-06:** `/research` avulso, `/nexusprism machine info/list`,
> `/nexusprism energy info/network` e comandos `/backpack` descreviam sistemas mortos, sem
> nenhum código restante. Veja `modules/core.md`.

---

## Pontos de Viagem

| Comando | Aliases | Descrição | Permissão |
| --- | --- | --- | --- |
| `/waypoint create <name>` | `/wp` | Criar um ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint delete <name>` | `/wp` | Excluir um ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint list` | `/wp` | Listar todos os pontos de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint tp <name>` | `/wp` | Teleportar para ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint info <name>` | `/wp` | Informações do ponto de viagem | `nexusprism.essentials.waypoint` |

---

## Essenciais — Homes

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/home [name]` | Teleportar para um home | `nexusprism.essentials.home` |
| `/home list` | Listar todos os homes | `nexusprism.essentials.home` |
| `/sethome <name>` | Definir home na localização atual | `nexusprism.essentials.home` |
| `/delhome <name>` | Excluir um home | `nexusprism.essentials.home` |

---

## Essenciais — Warps

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/warp <name>` | Teleportar para um warp | `nexusprism.essentials.warp.use` |
| `/warp list` | Listar todos os warps | `nexusprism.essentials.warp.use` |
| `/setwarp <name>` | Criar um warp (OP) | `nexusprism.essentials.warp.admin` |
| `/delwarp <name>` | Excluir um warp (OP) | `nexusprism.essentials.warp.admin` |

---

## Essenciais — Teleportação

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/tpa <player>` | Enviar solicitação de teleporte | `nexusprism.essentials.tpa` |
| `/tpaccept` | Aceitar solicitação de teleporte | `nexusprism.essentials.tpa` |
| `/tpdeny` | Recusar solicitação de teleporte | `nexusprism.essentials.tpa` |
| `/tphere <player>` | Convocar um jogador (OP) | `nexusprism.essentials.tphere` |
| `/tppos <x> <y> <z>` | Teleportar para coordenadas (OP) | `nexusprism.essentials.tppos` |
| `/spawn` | Teleportar para o spawn | `nexusprism.essentials.spawn` |
| `/setspawn` | Definir spawn do servidor (OP) | `nexusprism.essentials.setspawn` |
| `/back` | Retornar à localização anterior | `nexusprism.essentials.back` |

---

## Essenciais — Utilidades

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/afk` | Alternar AFK | `nexusprism.essentials.afk` |
| `/fly` | Alternar voo (próprio) | `nexusprism.essentials.fly` |
| `/fly <player>` | Alternar voo (outro, OP) | `nexusprism.essentials.fly.others` |
| `/god` | Alternar modo deus | `nexusprism.essentials.god` |
| `/god <player>` | Alternar deus (outro, OP) | `nexusprism.essentials.god.others` |
| `/heal` | Curar a si mesmo (OP) | `nexusprism.essentials.heal` |
| `/heal <player>` | Curar outro (OP) | `nexusprism.essentials.heal.others` |
| `/feed` | Alimentar a si mesmo (OP) | `nexusprism.essentials.feed` |
| `/feed <player>` | Alimentar outro (OP) | `nexusprism.essentials.feed.others` |
| `/nick <name>` | Definir apelido | `nexusprism.essentials.nick` |
| `/nick <player> <name>` | Definir apelido (outro, OP) | `nexusprism.essentials.nick.others` |
| `/hat` | Usar item como chapéu | `nexusprism.essentials.hat` |
| `/speed <value>` | Definir velocidade de caminhada/voo (OP) | `nexusprism.essentials.speed` |
| `/workbench` | Bancada de trabalho portátil | `nexusprism.essentials.workbench` |
| `/anvil` | Bigorna portátil (OP) | `nexusprism.essentials.anvil` |
| `/grindstone` | Pedra de amolar portátil (OP) | `nexusprism.essentials.grindstone` |
| `/stonecutter` | Cortador de pedra portátil (OP) | `nexusprism.essentials.stonecutter` |
| `/trash` | Lixeira portátil | `nexusprism.essentials.trash` |
| `/near` | Listar jogadores próximos | `nexusprism.essentials.near` |
| `/seen <player>` | Informações da última vez online | `nexusprism.essentials.seen` |
| `/getpos` | Mostrar coordenadas | `nexusprism.essentials.getpos` |
| `/playtime` | Verificar tempo de jogo | `nexusprism.essentials.playtime` |
| `/gamemode <mode>` | Mudar modo de jogo (OP) | `nexusprism.essentials.gamemode` |
| `/enderchest` | Abrir baú do end | `nexusprism.essentials.enderchest` |
| `/enderchest <player>` | Abrir baú do end de outro (OP) | `nexusprism.essentials.enderchest.others` |
| `/clearinventory` | Limpar inventário próprio (OP) | `nexusprism.essentials.clearinventory` |
| `/clearinventory <player>` | Limpar inventário de outro (OP) | `nexusprism.essentials.clearinventory.others` |
| `/repair` | Reparar item na mão (OP) | `nexusprism.essentials.repair` |
| `/ext` | Apagar a si mesmo (OP) | `nexusprism.essentials.ext` |
| `/exp <amount>` | Dar XP (OP) | `nexusprism.essentials.exp` |
| `/skull [player]` | Obter cabeça de jogador (OP) | `nexusprism.essentials.skull` |
| `/rules` | Mostrar regras do servidor | `nexusprism.essentials.rules` |
| `/worth [item]` | Valor de venda do item | `nexusprism.essentials.worth` |

---

## Essenciais — Prisão

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/jail <player> [duration]` | Prender um jogador (OP) | `nexusprism.essentials.jail.admin` |
| `/unjail <player>` | Soltar um jogador (OP) | `nexusprism.essentials.jail.admin` |
| `/setjail` | Definir localização da prisão (OP) | `nexusprism.essentials.jail.admin` |

---

## Economia

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/money [player]` | Verificar saldo | `nexusprism.economy.money` |
| `/baltop` | Top 10 mais ricos | `nexusprism.economy.baltop` |
| `/sell hand` | Vender item na mão | `nexusprism.economy.sell` |
| `/sell all` | Vender todos os itens vendáveis | `nexusprism.economy.sell` |
| `/sell inventory` | Vender inventário inteiro | `nexusprism.economy.sell` |
| `/worth [item]` | Verificar valor de venda | `nexusprism.essentials.worth` |
| `/eco give <player> <amount>` | Dar dinheiro (OP) | `nexusprism.economy.admin` |
| `/eco take <player> <amount>` | Retirar dinheiro (OP) | `nexusprism.economy.admin` |
| `/eco set <player> <amount>` | Definir saldo (OP) | `nexusprism.economy.admin` |
| `/eco reset <player>` | Redefinir saldo (OP) | `nexusprism.economy.admin` |

---

## Clãs

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/clan create <name> <tag>` | Criar um clã | `nexusprism.clan.use` |
| `/clan disband` | Dissolver clã | `nexusprism.clan.use` |
| `/clan invite <player>` | Convidar um jogador | `nexusprism.clan.use` |
| `/clan join <name>` | Entrar em um clã | `nexusprism.clan.use` |
| `/clan leave` | Sair do clã | `nexusprism.clan.use` |
| `/clan kick <player>` | Expulsar um membro | `nexusprism.clan.use` |
| `/clan promote <player>` | Promover a oficial | `nexusprism.clan.use` |
| `/clan demote <player>` | Rebaixar a membro | `nexusprism.clan.use` |
| `/clan info [name]` | Informações do clã | `nexusprism.clan.use` |
| `/clan list` | Listar todos os clãs | `nexusprism.clan.use` |
| `/clan chat` | Alternar chat de clã | `nexusprism.clan.use` |
| `/clan claim` | Reivindicar chunk atual | `nexusprism.clan.use` |
| `/clan unclaim` | Liberar chunk atual | `nexusprism.clan.use` |
| `/clan map` | Mostrar mapa de território | `nexusprism.clan.use` |
| `/clan chest` | Abrir baú do clã | `nexusprism.clan.use` |
| `/clan upgrade` | Abrir menu de melhorias | `nexusprism.clan.use` |
| `/clan top` | Placar de clãs | `nexusprism.clan.use` |
| `/clan admin disband <name>` | Forçar dissolução (OP) | `nexusprism.clan.admin` |
| `/clan admin unclaim <name>` | Forçar liberação (OP) | `nexusprism.clan.admin` |

---

## Segurança & Equipe

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/register <password> <confirm>` | Registrar conta | *(todos)* |
| `/login <password>` | Fazer login | *(todos)* |
| `/changepassword <old> <new>` | Alterar senha | *(autenticado)* |
| `/vanish` | Alternar invisibilidade (OP) | `nexusprism.staff.vanish` |
| `/vanish <player>` | Tornar outro invisível (OP) | `nexusprism.staff.vanish.others` |
| `/invsee <player>` | Inspecionar inventário (OP) | `nexusprism.staff.invsee` |
| `/spy` | Alternar espionagem de chat (OP) | `nexusprism.staff.spy` |
| `/cleanworld` | Executar limpador de mundo (OP) | `nexusprism.security.cleanworld` |

---

## Discord

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/discord` | Link de convite do Discord | *(todos)* |
| `/discord link` | Iniciar vinculação de conta | *(todos)* |
| `/discord unlink` | Desvincular conta | *(todos)* |
| `/discord info` | Mostrar conta vinculada | *(todos)* |
| `/discordrr` | Gerenciar cargos de reação (OP) | `nexusprism.admin` |

---

## Proteções & Duelo

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/region claim <name>` | Reivindicar área selecionada | `nexusprism.region.use` |
| `/region delete <name>` | Excluir região | `nexusprism.region.use` |
| `/region list` | Listar suas regiões | `nexusprism.region.use` |
| `/region info [name]` | Detalhes da região | `nexusprism.region.use` |
| `/region addmember <region> <player>` | Adicionar membro | `nexusprism.region.use` |
| `/region removemember <region> <player>` | Remover membro | `nexusprism.region.use` |
| `/region setflag <region> <flag> <val>` | Definir uma flag | `nexusprism.region.use` |
| `/region flags <region>` | Ver flags | `nexusprism.region.use` |
| `/protect <name>` | Proteção rápida de chunk | `nexusprism.region.use` |
| `/region admin list` | Admin: todas as regiões (OP) | `nexusprism.protect.admin` |
| `/region admin delete <name>` | Admin: excluir região (OP) | `nexusprism.protect.admin` |
| `/duel <player>` | Desafiar para duelo | `nexusprism.duel.use` |
| `/duel accept` | Aceitar duelo | `nexusprism.duel.use` |
| `/duel deny` | Recusar duelo | `nexusprism.duel.use` |
| `/duel spectate <player>` | Espectador de duelo | `nexusprism.duel.use` |
| `/duel stats` | Estatísticas de duelo | `nexusprism.duel.use` |
| `/duel setarena` | Definir arena de duelo (OP) | `nexusprism.protect.admin` |

---

## Crystal Defense

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/crystal join <arena>` | Entrar em uma arena | `nexusprism.crystaldefense.use` |
| `/crystal leave` | Sair da arena | `nexusprism.crystaldefense.use` |
| `/crystal list` | Listar arenas | `nexusprism.crystaldefense.use` |
| `/crystal status` | Onda e HP do cristal | `nexusprism.crystaldefense.use` |
| `/crystal create <name>` | Criar arena (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal delete <name>` | Excluir arena (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal setcrystal <arena>` | Definir localização do cristal (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal setspawn <arena>` | Definir spawn (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal start [arena]` | Forçar início (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal stop [arena]` | Parar jogo (OP) | `nexusprism.crystaldefense.admin` |
| `/crystal reload` | Recarregar configurações (OP) | `nexusprism.crystaldefense.admin` |

---

## Votifier

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/vote` | Mostrar links de votação e sequência | `nexusprism.vote` |
| `/votetop` | Placar de votos | `nexusprism.vote.top` |

---

## Custom Mobs

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/boss spawn <id>` | Invocar um boss | `nexusprism.boss.admin` |
| `/boss spawn <id> <w> <x> <y> <z>` | Invocar em coordenadas | `nexusprism.boss.admin` |
| `/boss list` | Listar todos os bosses | `nexusprism.boss.admin` |
| `/boss info <id>` | Definição do boss | `nexusprism.boss.admin` |
| `/boss kill <id>` | Matar todas as instâncias do boss | `nexusprism.boss.admin` |
| `/bossegg give <player> <id>` | Dar ovo de spawn | `nexusprism.boss.admin` |

---

## Dreams

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/dreams reload` | Recarregar configuração | `nexusprism.dreams.admin` |
| `/dreams trigger <player>` | Forçar sonho | `nexusprism.dreams.admin` |
| `/dreams trigger <player> nightmare` | Forçar pesadelo | `nexusprism.dreams.admin` |

---

## Twitch

| Comando | Descrição | Permissão |
| --- | --- | --- |
| `/twitch link <username>` | Iniciar vinculação | `nexusprism.twitch.use` |
| `/twitch unlink` | Desvincular conta | `nexusprism.twitch.use` |
| `/twitch status` | Status da vinculação | `nexusprism.twitch.use` |
| `/twitch approve <player>` | Aprovar vinculação (OP) | `nexusprism.twitch.staff` |
| `/twitch reject <player>` | Rejeitar vinculação (OP) | `nexusprism.twitch.staff` |
| `/twitch pending` | Solicitações pendentes (OP) | `nexusprism.twitch.staff` |
| `/twitch giveaway <streamer>` | Sortear vencedor (OP) | `nexusprism.twitch.staff` |
| `/twitch reload` | Recarregar configuração (OP) | `nexusprism.twitch.admin` |
