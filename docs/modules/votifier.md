# Módulo Votifier

O módulo Votifier é um **servidor Votifier V1 e V2 autônomo** embutido diretamente no NexusPrism. Ele processa votos recebidos de sites de listagem de servidores, distribui recompensas configuráveis e acompanha sequências de votos dos jogadores em um placar.

---

## Como Funciona

```flow
Site de Votação  ──► Servidor Votifier (porta 8192)  ──► VoteManager  ──► Recompensas + Sequência
                      (V1 RSA / V2 baseado em token)
```

1. Cadastre seu servidor em sites de votação (Minecraftservers.org, etc.)
2. Aponte cada site para o IP do seu servidor e a porta do Votifier (padrão `8192`)
3. Quando um jogador votar, o site envia um payload para o seu servidor Votifier
4. O NexusPrism processa o voto, executa os comandos de recompensa e atualiza a sequência

---

## Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/vote` | Exibir links de votação e sua sequência atual | `nexusprism.vote` |
| `/votetop` | Exibir o placar de votos | `nexusprism.vote.top` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.vote` | Usar `/vote` | true |
| `nexusprism.vote.top` | Usar `/votetop` | true |

---

## Configuração (`votifier/config.yml`)

```yaml
host: "0.0.0.0"       # Ouvir em todas as interfaces
port: 8192             # Porta do Votifier (abra no firewall)
token: "change-this-token"   # Segredo compartilhado para autenticação V2

vote-links:
  - "https://minecraftservers.org/vote/YOUR_SERVER_ID"
  - "https://minecraft-server-list.com/server/YOUR_SERVER_ID/vote/"

rewards:
  - type: COMMAND
    value: "eco give {player} 500"
  - type: COMMAND
    value: "crates key give {player} VOTE 1"
  - type: MESSAGE
    value: "&aThank you for voting, {player}! You received $500 and a crate key."

streak:
  enabled: true
  max-gap-hours: 36    # Votos com mais de 36h de intervalo reiniciam a sequência
  multipliers:
    5:  1.5            # Sequência de 5 votos = 1.5× recompensas
    10: 2.0            # Sequência de 10 votos = 2× recompensas
    30: 3.0            # Sequência de 30 votos = 3× recompensas
```

### Campos de Configuração

| Campo | Descrição |
| --- | --- |
| `host` | IP para vincular o servidor de votos. Use `0.0.0.0` para todas as interfaces. |
| `port` | Porta TCP. Deve estar aberta no firewall e redirecionada se estiver atrás de NAT. |
| `token` | Token secreto para autenticação V2. Altere imediatamente. |
| `vote-links` | Lista de URLs exibidas pelo `/vote`. |
| `rewards[].type` | `COMMAND` (executa um comando no console) ou `MESSAGE` (envia mensagem ao jogador). |
| `rewards[].value` | String de comando/mensagem. Use `{player}` para o nome do votante. |
| `streak.max-gap-hours` | Quantas horas podem passar entre votos antes de a sequência ser reiniciada. |
| `streak.multipliers` | Mapa de tamanho da sequência → multiplicador de recompensas. |

---

## Suporte a Protocolos

| Protocolo | Descrição |
| --- | --- |
| **V1** | Protocolo Votifier legado com criptografia RSA. Compatível com a maioria dos sites mais antigos. |
| **V2** | Protocolo moderno baseado em token HMAC-SHA256. Preferido — mais seguro e confiável. |

As chaves RSA para V1 são geradas automaticamente na primeira inicialização e armazenadas como `votifier/rsa/public.key` e `votifier/rsa/private.key`.

---

## Cadastro em Sites de Votação

Ao se cadastrar em um site de votação, você precisará de:

- **IP do Servidor** — o endereço IP público do seu servidor
- **Porta do Votifier** — `8192` (ou o valor definido em `config.yml`)
- **Chave Pública** — copie de `plugins/NexusPrism/votifier/rsa/public.key` (sites V1)
- **Token** — o valor de `token` em `config.yml` (sites V2)

---

## Sistema de Sequência

| Sequência | Multiplicador |
| --- | --- |
| 1–4 votos | 1× (base) |
| 5–9 votos | 1.5× |
| 10–29 votos | 2× |
| 30+ votos | 3× |

Quando o multiplicador está ativo, os valores `COMMAND` de recompensa são executados múltiplas vezes de acordo com o multiplicador (arredondado para o inteiro mais próximo). Você também pode implementar lógica de multiplicador personalizada usando o placeholder `%nexusprism_vote_streak%` em plugins externos.

---

## PlaceholderAPI

| Placeholder | Descrição |
| --- | --- |
| `%nexusprism_votes_total%` | Total de votos acumulados do jogador |
| `%nexusprism_vote_streak%` | Sequência de votos atual do jogador |
