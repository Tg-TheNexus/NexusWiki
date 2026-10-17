# Módulo Core

O módulo Core é a base do NexusPrism: sistema de idiomas (i18n), o framework de GUI,
armazenamento de dados por jogador (com uma API genérica de extensão para addons), o hook do
evento de loot de estruturas, e o sistema pessoal de pontos de viagem.

> **O conteúdo de itens/máquinas/energia/pesquisa foi movido para o NexusATS.** O NexusPrism
> em si não fornece mais um registro de itens personalizados, motor de máquinas, rede de
> energia ou árvore de pesquisa — todo esse domínio agora vive no plugin separado NexusATS.
> Se o NexusATS estiver instalado, seus comandos ficam disponíveis sob `/nexusprism
> <subcomando>` (veja abaixo); sem o NexusATS, esses subcomandos ficam indisponíveis.

---

## Sistema PDC

O NexusPrism usa o **PersistentDataContainer** do Minecraft para sua própria gestão de
dados de jogador/posicionamento de máquinas. Addons (como o NexusATS) usam o mesmo padrão
para seus próprios itens e blocos, sob seu próprio namespace de PDC.

---

## Hooks de Extensão para Addons

O NexusPrism expõe um pequeno conjunto de hooks genéricos para que addons (NexusATS, e
qualquer addon futuro) possam se integrar sem que o NexusPrism precise conhecê-los de
antemão:

| Hook | Finalidade |
| --- | --- |
| `NexusPrism.registerBlockClassifier(isAddonBlock, addonBlockIdLookup)` | Permite que um addon marque seus próprios blocos para que RNG/traits/MMO/Waila os ignorem ou redirecionem sobre eles |
| `NexusPrism.registerAddonCommand(subCommand, handler)` | Registra um handler de `/nexusprism <subCommand>` pertencente ao addon |
| `NexusPrism.registerAddonTabCompleter(subCommand, completer)` | Auto-completar para um subcomando registrado por addon |
| `DataManager.setPlayerField(playerId, namespace, key, value)` / `getPlayerField(...)` / `getPlayerFields(...)` | Armazenamento genérico de chave/valor por jogador, isolado por namespace, para addons que precisam persistir seus próprios dados através do banco de dados do NexusPrism sem migração de schema |

---

## Pontos de Viagem

Pontos de viagem são pontos pessoais de teleporte rápido salvos pelo jogador.

### Comandos de Pontos de Viagem

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/waypoint create <nome>` | Criar um ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint delete <nome>` | Excluir um ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint list` | Listar todos os pontos de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint tp <nome>` | Teleportar para um ponto de viagem | `nexusprism.essentials.waypoint` |
| `/waypoint info <nome>` | Mostrar detalhes do ponto de viagem | `nexusprism.essentials.waypoint` |

Aliases: `/wp`

### Permissões de Limite de Slots

| Permissão | Slots |
| --- | --- |
| `nexusprism.essentials.waypoints.1` | 1 (padrão) |
| `nexusprism.essentials.waypoints.5` | 5 |
| `nexusprism.essentials.waypoints.25` | 25 |
| `nexusprism.essentials.waypoints.unlimited` | Ilimitado (OP) |

---

## Comandos Principais do Plugin

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/nexusprism help` | Mostrar ajuda | `nexusprism.command` |
| `/nexusprism info` | Informações do plugin | `nexusprism.command` |
| `/nexusprism reload` | Recarregar todas as configurações | `nexusprism.admin.reload` |
| `/nexusprism modules` | Listar módulos carregados | `nexusprism.command` |
| `/nexusprism give <jogador> <item>` | Dar um item — requer NexusATS | `nexusprism.admin.give` |
| `/nexusprism guide` | Abrir o guia de itens — requer NexusATS | `nexusprism.command` |
| `/nexusprism machines` | Informações de máquina — requer NexusATS | `nexusprism.command` |
| `/nexusprism research` | Menu de pesquisa — requer NexusATS | `nexusprism.command` |
| `/nexusprism recipe` | Consulta de receitas — requer NexusATS | `nexusprism.command` |

Aliases: `/ns`, `/nexus`, `/slime`, `/nslime`

---

## Suporte a Idiomas

O NexusPrism vem com quatro arquivos de idioma:

| Arquivo | Idioma |
| --- | --- |
| `lang/en_US.yml` | Inglês (padrão) |
| `lang/pt_BR.yml` | Português Brasileiro |
| `lang/es_ES.yml` | Espanhol |
| `lang/zh_CN.yml` | Chinês (Simplificado) |

Defina o idioma ativo em `config.yml`:

```yaml
settings:
  language: en_US
```
