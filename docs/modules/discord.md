# Módulo Discord

O módulo Discord fornece um **bot com JDA** com ponte de chat Minecraft ↔ Discord, vinculação de contas de jogadores, sincronização de cargos, entrega por webhooks e monitoramento de GitHub Actions.

---

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Ponte de Chat** | Retransmite o chat do jogo para canais do Discord e vice-versa |
| **Vinculação de Contas** | Vincula contas do Discord a contas do Minecraft via DM |
| **Sincronização de Cargos** | Atribui cargos do Discord com base nos grupos do LuckPerms |
| **Webhooks** | Envia eventos de jogadores (entrada, morte, conquista) para o Discord |
| **Alertas de Menção** | Notifica jogadores no jogo quando são mencionados no Discord |
| **GitHub Actions** | Monitora e aciona fluxos de CI/CD a partir do Discord |
| **Voto do Servidor** | Votação da comunidade para reiniciar o servidor via slash command |
| **Controle do Painel** | Comandos admin de iniciar/parar via API do Pterodactyl |

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/discord` | Exibe o link de convite do Discord | *(todos os jogadores)* |
| `/discord link` | Inicia o processo de vinculação de conta | *(todos os jogadores)* |
| `/discord unlink` | Desvincula sua conta do Discord | *(todos os jogadores)* |
| `/discord info` | Exibe sua conta do Discord vinculada | *(todos os jogadores)* |
| `/discordrr` | Gerencia mensagens de reação-cargo | `nexusprism.admin` |

---

## Configuração

### 1. Criar um Bot no Discord

1. Acesse [discord.com/developers/applications](https://discord.com/developers/applications)
2. Crie uma nova Aplicação → Bot
3. Copie o **Token do Bot**
4. Ative **Message Content Intent** e **Server Members Intent**
5. Convide o bot para o seu servidor com os escopos `bot` + `applications.commands`

### 2. Configurar o Bot (`discord/config.yml`)

```yaml
enabled: true

default-webhook: "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"

admin:
  enabled: false
  port: 8765
  token: ""

mentions:
  style: actionbar           # chat | actionbar | bossbar
  message: "&e&l[Discord] &b{sender} &7mentioned you!"
  bossbar:
    color: YELLOW
    duration: 5

bot:
  enabled: true
```

### 3. Configurar Definições do Bot (`discord/bot.yml`)

```yaml
token: "YOUR_BOT_TOKEN_HERE"
guild-id: "YOUR_GUILD_ID"

# IDs de canais para a ponte
channels:
  global-chat: "CHANNEL_ID"
  announcements: "CHANNEL_ID"
  staff: "CHANNEL_ID"
```

### 4. Configurar Canais (`discord/channels.yml`)

```yaml
# Mapeia canais de chat do jogo para IDs de canais do Discord
global:
  discord-id: "123456789012345678"
  webhook: "https://discord.com/api/webhooks/..."
  relay-to-game: true
  relay-to-discord: true

staff:
  discord-id: "123456789012345679"
  relay-to-game: true
  relay-to-discord: true
```

---

## Webhooks de Eventos de Jogadores (`discord/playerEvents.yml`)

```yaml
join:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** joined the server!"

quit:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** left the server."

death:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** died: {death_message}"

achievement:
  enabled: true
  webhook: "https://discord.com/api/webhooks/..."
  message: "**{player}** earned **{achievement}**!"
```

---

## Mapeamento de Cargos (`discord/roles.yml`)

```yaml
# Grupo do LuckPerms → ID de Cargo do Discord
mappings:
  vip: "DISCORD_ROLE_ID"
  mvp: "DISCORD_ROLE_ID"
  staff: "DISCORD_ROLE_ID"
  admin: "DISCORD_ROLE_ID"
```

---

## Webhooks de Saída (`discord/outbound.yml`)

```yaml
webhooks:
  default: "https://discord.com/api/webhooks/..."
  deaths: "https://discord.com/api/webhooks/..."
  votes: "https://discord.com/api/webhooks/..."
```

---

## Integração com Loja (`discord/webstore.yml`)

```yaml
enabled: true
webhook: "https://discord.com/api/webhooks/..."
message: "**{player}** just purchased **{package}** from the store! Thank you!"
```

---

## Integração com GitHub Actions

O módulo Discord pode monitorar fluxos de trabalho do GitHub Actions e permitir que a equipe os acione a partir do Discord.

Classes principais: `GitHubActionsManager`, `WorkflowPoller`, `WorkflowTriggerRecord`

---

## Voto do Servidor e Controle do Painel

### `/server vote` — Votação da Comunidade

Qualquer membro do Discord (opcionalmente restrito a cargos específicos) pode iniciar uma votação para reiniciar o servidor.

1. O membro executa `/server vote` no Discord.
2. O bot posta um embed com botões **✅ Sim** e **❌ Não**.
3. Cada membro pode mudar seu voto durante a janela de votação.
4. Ao encerrar a janela, o bot avalia o resultado:
   - Requer `min-votes` votos **e** `threshold`% de sim para aprovar.
   - Se aprovado: RCON transmite aviso no jogo, depois o Pterodactyl envia sinal `restart` após `warn-seconds`.
   - Se reprovado: embed é atualizado com o resultado, nenhuma ação é tomada.
5. Um cooldown configurável impede votações consecutivas.

### `/server start` / `/server stop` — Comandos Admin

Restrito a cargos listados em `server-vote.admin-roles` (ou permissão de Administrador do Discord se a lista estiver vazia).

| Slash Command Discord | Ação |
| --- | --- |
| `/server vote` | Iniciar votação comunitária de reinicialização |
| `/server start` | Enviar sinal `start` ao Pterodactyl |
| `/server stop` | Transmitir aviso RCON e enviar sinal `stop` |

### Configuração — `discord/panel.yml`

```yaml
panel: pterodactyl

pterodactyl:
  base-url: "https://panel.example.com"
  client-api-key: ""
  server-uuid: ""

rcon:
  host: "127.0.0.1"
  port: 25575
  password: ""
  timeout-seconds: 5

server-vote:
  enabled: true
  voter-roles: []
  admin-roles: []
  min-votes: 3
  threshold: 0.6
  window-seconds: 120
  cooldown-minutes: 30
  warn-seconds: 60
  channel: "default"
```

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.discord.link` | Vincular conta do Discord | true |
| `nexusprism.admin` | Comandos administrativos do Discord | OP |
