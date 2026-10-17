# Módulo Essenciais

O módulo Essenciais fornece **+40 comandos de qualidade de vida** cobrindo homes, warps, waypoints, teleporte, detecção de AFK, prisão e comandos utilitários do dia a dia.

---

## Homes

Jogadores podem definir homes com nome e se teletransportar para elas.

### Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/home [nome]` | Teletransportar para uma home | `nexusprism.essentials.home` |
| `/home list` | Listar todas as homes | `nexusprism.essentials.home` |
| `/sethome <nome>` | Definir home na posição atual | `nexusprism.essentials.home` |
| `/delhome <nome>` | Deletar uma home | `nexusprism.essentials.home` |

### Permissões de Slots de Home

| Permissão | Slots |
| --- | --- |
| `nexusprism.essentials.homes.1` | 1 (padrão) |
| `nexusprism.essentials.homes.3` | 3 |
| `nexusprism.essentials.homes.10` | 10 |
| `nexusprism.essentials.homes.unlimited` | Ilimitado (OP) |

---

## Warps

Destinos de teletransporte públicos em todo o servidor gerenciados por admins.

### Comandos de Warps

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/warp <nome>` | Teletransportar para um warp | `nexusprism.essentials.warp.use` |
| `/warp list` | Listar todos os warps | `nexusprism.essentials.warp.use` |
| `/setwarp <nome>` | Criar um warp (OP) | `nexusprism.essentials.warp.admin` |
| `/delwarp <nome>` | Deletar um warp (OP) | `nexusprism.essentials.warp.admin` |

---

## TPA (Pedidos de Teletransporte)

### Comandos TPA

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/tpa <jogador>` | Enviar pedido de teletransporte | `nexusprism.essentials.tpa` |
| `/tpaccept` | Aceitar pedido de teletransporte | `nexusprism.essentials.tpa` |
| `/tpdeny` | Recusar pedido de teletransporte | `nexusprism.essentials.tpa` |
| `/tphere <jogador>` | Teletransportar jogador até você (OP) | `nexusprism.essentials.tphere` |
| `/tppos <x> <y> <z>` | Teletransportar para coordenadas (OP) | `nexusprism.essentials.tppos` |
| `/spawn` | Teletransportar para o spawn | `nexusprism.essentials.spawn` |
| `/setspawn` | Definir o spawn do servidor (OP) | `nexusprism.essentials.setspawn` |
| `/back` | Voltar para localização anterior | `nexusprism.essentials.back` |

### Configuração (`essentials/config.yml`)

```yaml
tpa:
  expiry-seconds: 60       # Pedido expira após este tempo

back:
  save-on-death: true      # Salvar localização de morte para /back
  save-on-any-teleport: false

spawn:
  respawn-at-spawn: false  # Forçar respawn no spawn (vs. cama)
```

---

## Sistema AFK

### Comandos AFK

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/afk` | Alternar status AFK | `nexusprism.essentials.afk` |

### Configuração AFK

```yaml
afk:
  idle-seconds: 300        # AFK automático após 5 minutos inativo
  broadcast: true          # Anunciar quando um jogador ficar AFK
```

---

## Prisão

Admins podem enviar jogadores para uma localização de prisão predefinida.

### Comandos de Prisão

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/jail <jogador> [duração]` | Prender um jogador (OP) | `nexusprism.essentials.jail.admin` |
| `/unjail <jogador>` | Soltar um jogador (OP) | `nexusprism.essentials.jail.admin` |
| `/setjail` | Definir localização da prisão (OP) | `nexusprism.essentials.jail.admin` |

---

## Comandos Utilitários

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/fly` | Alternar modo de voo | `nexusprism.essentials.fly` |
| `/fly <jogador>` | Alternar voo para outro jogador (OP) | `nexusprism.essentials.fly.others` |
| `/god` | Alternar modo deus | `nexusprism.essentials.god` |
| `/heal` | Curar a si mesmo (OP) | `nexusprism.essentials.heal` |
| `/feed` | Alimentar a si mesmo (OP) | `nexusprism.essentials.feed` |
| `/nick <nome>` | Definir apelido | `nexusprism.essentials.nick` |
| `/workbench` | Bancada portátil | `nexusprism.essentials.workbench` |
| `/trash` | Lixeira portátil | `nexusprism.essentials.trash` |
| `/anvil` | Bigorna portátil (OP) | `nexusprism.essentials.anvil` |
| `/speed <valor>` | Definir velocidade de movimento (OP) | `nexusprism.essentials.speed` |
| `/near` | Listar jogadores próximos | `nexusprism.essentials.near` |
| `/seen <jogador>` | Última vez visto | `nexusprism.essentials.seen` |
| `/getpos` | Mostrar suas coordenadas | `nexusprism.essentials.getpos` |
| `/playtime` | Verificar tempo de jogo | `nexusprism.essentials.playtime` |
| `/gamemode <modo>` | Alterar modo de jogo (OP) | `nexusprism.essentials.gamemode` |
| `/enderchest` | Abrir seu baú de ender | `nexusprism.essentials.enderchest` |
| `/repair` | Reparar item segurado (OP) | `nexusprism.essentials.repair` |
| `/ext` | Apagar a si mesmo (OP) | `nexusprism.essentials.ext` |
| `/hat` | Usar item como chapéu | `nexusprism.essentials.hat` |
| `/rules` | Mostrar regras do servidor | `nexusprism.essentials.rules` |
| `/worth [item]` | Verificar valor de venda | `nexusprism.essentials.worth` |
