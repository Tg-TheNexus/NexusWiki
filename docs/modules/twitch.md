# Módulo de Integração Twitch

O módulo Twitch conecta seu servidor Minecraft ao Twitch. Os jogadores podem **vincular suas contas do Twitch**, a equipe é notificada quando jogadores vinculados ficam ao vivo, o chat do Twitch é retransmitido no jogo e os admins podem realizar **sorteios para espectadores**.

---

## Funcionalidades

| Funcionalidade | Descrição |
| --- | --- |
| **Vinculação de Contas** | Vincula Minecraft ↔ Twitch via código de verificação no chat |
| **Tag [LIVE]** | Prefixia o chat com `[LIVE]` quando um jogador está transmitindo |
| **Anúncios de Ao Vivo** | Transmite quando um jogador vinculado inicia/encerra uma transmissão |
| **Retransmissão de Chat** | Mensagens do chat do Twitch aparecem no jogo |
| **Sorteios** | Sorteia um espectador vinculado elegível aleatoriamente e o recompensa |
| **Recompensas para Espectadores** | Sorteio periódico automático para espectadores assistindo a streamers vinculados |

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/twitch link <usuário>` | Iniciar vinculação da conta Twitch | `nexusprism.twitch.use` |
| `/twitch unlink` | Desvincular conta Twitch | `nexusprism.twitch.use` |
| `/twitch status` | Verificar status da vinculação | `nexusprism.twitch.use` |
| `/twitch approve <jogador>` | Aprovar uma vinculação pendente | `nexusprism.twitch.staff` |
| `/twitch reject <jogador>` | Rejeitar uma vinculação pendente | `nexusprism.twitch.staff` |
| `/twitch pending` | Listar solicitações de vinculação pendentes | `nexusprism.twitch.staff` |
| `/twitch giveaway <streamer>` | Sortear um vencedor | `nexusprism.twitch.staff` |
| `/twitch reload` | Recarregar configuração do Twitch | `nexusprism.twitch.admin` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.twitch.use` | Comandos básicos do Twitch | true |
| `nexusprism.twitch.staff` | Aprovar vinculações, realizar sorteios | OP |
| `nexusprism.twitch.admin` | Recarregar configuração | OP |

---

## Configuração

### 1. Criar um Aplicativo Twitch

1. Acesse [dev.twitch.tv/console](https://dev.twitch.tv/console) e crie um aplicativo
2. Defina o redirecionamento OAuth como `http://localhost`
3. Copie o **Client ID** e o **Client Secret**

### 2. Criar uma Conta de Bot

1. Crie uma conta Twitch para o bot (ou use a sua própria)
2. Acesse [twitchapps.com/tmi/](https://twitchapps.com/tmi/) para obter um token OAuth
3. Adicione o bot como moderador no seu canal de verificação

### 3. Configurar (`twitch/config.yml`)

```yaml
bot:
  enabled: true
  oauth-token: "oauth:your_token_here"
  client-id: "your_client_id"
  client-secret: "your_client_secret"
  bot-username: "your_bot_account"
  verification-channel: "your_server_twitch_channel"

link:
  require-staff-approval: true  # A equipe deve aprovar antes de a vinculação ser ativada
  code-expiry-seconds: 300

stream-poll:
  interval-seconds: 60          # Verificar se streamers estão ao vivo a cada 60s

live-tag:
  enabled: true
  format: "§c[LIVE] §r"         # Prefixado ao formato de chat ao transmitir

announcements:
  go-live:
    enabled: true
    message: "§6[Twitch] §e{player} §7is now live! §f{title} §7— §fttwitch.tv/{channel}"
    discord-channel: "announcements"   # Chave de canal do Discord para postagem cruzada
  go-offline:
    enabled: false
    message: "§6[Twitch] §e{player} §7finished their stream."

chat-relay:
  enabled: true
  format: "§6[Twitch] §b{user}§7: {message}"

giveaway:
  command: "crates key give {player} VOTE 1"
  key-item: "SERVER_KEY"
  active-viewer-window-minutes: 10
  announce-winner: "§6[Giveaway] §e{player} §7won a key! Congrats to @{twitch_name}!"
  twitch-announce: "Congrats @{twitch_name}! You won a key on our Minecraft server!"

viewer-reward:
  enabled: false
  interval-minutes: 30
  command: "crates key give {player} VOTE 1"
```

---

## Fluxo de Vinculação de Conta

```cs
Jogador executa /twitch link <usuário>
        │
        ▼
Bot envia um código de 5 caracteres no canal Twitch de verificação
        │
        ▼
Jogador digita !verify <código> no chat do Twitch
        │
        ▼
[Se require-staff-approval: true]
Equipe aprova com /twitch approve <jogador>
        │
        ▼
Vinculação ativa — tag ao vivo e anúncios se aplicam
```

---

## Sistema de Sorteio

A equipe pode executar `/twitch giveaway <streamer>` para:

1. Buscar todos os espectadores vinculados assistindo ao canal daquele streamer
2. Filtrar espectadores que enviaram uma mensagem nos últimos `active-viewer-window-minutes`
3. Selecionar aleatoriamente um espectador elegível
4. Executar o `command` configurado (ou dar o `key-item`) ao vencedor
5. Anunciar o vencedor no jogo e no chat do Twitch

!!! note "Permissões de Bot Necessárias"
    Para que o sistema de recompensas para espectadores busque a lista de chatters, a conta do bot deve ter o escopo OAuth `moderator:read:chatters` e ser moderador no canal do streamer.

---

## Placeholders de Mensagens

| Placeholder | Descrição |
| --- | --- |
| `{player}` | Nome de usuário do Minecraft |
| `{twitch_name}` | Nome de exibição do Twitch |
| `{title}` | Título da transmissão |
| `{channel}` | Nome do canal do Twitch |
| `{user}` | Nome de exibição do espectador no Twitch |
| `{message}` | Conteúdo da mensagem no chat do Twitch |
