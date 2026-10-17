# Módulo Chat

O módulo Chat substitui o chat padrão do Minecraft por um **sistema de 4 canais** — local, global, staff e report — cada um com raio, formato e integração de prefixo do LuckPerms configuráveis.

---

## Canais

| Canal | Ativação | Audiência | Descrição |
| --- | --- | --- | --- |
| **Local** | Padrão (sem prefixo) | Jogadores dentro do raio | Chat por proximidade |
| **Global** | `!<mensagem>` ou `/g` | Todos os jogadores online | Transmissão para o servidor inteiro |
| **Staff** | `/staffchat` ou `/sc` | Apenas staff | Canal privado de comunicação da equipe |
| **Report** | `/report <jogador> <motivo>` | Apenas staff | Denúncias enviadas por jogadores, entregues à staff |

---

## Comandos

| Comando | Aliases | Uso | Permissão |
| --- | --- | --- | --- |
| `/globalchat <mensagem>` | `/g`, `/gc` | Enviar mensagem para todos | `nexusprism.chat.global` |
| `/staffchat <mensagem>` | `/sc` | Enviar mensagem para a staff | `nexusprism.chat.staff` |
| `/report <jogador> <motivo>` | — | Denunciar um jogador | `nexusprism.chat.report` |
| `/chat reload` | — | Recarregar configuração do chat | `nexusprism.chat.admin` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.chat.global` | Usar o canal de chat global | true |
| `nexusprism.chat.staff` | Acessar o canal de staff | OP |
| `nexusprism.chat.report` | Enviar denúncias de jogadores | true |
| `nexusprism.chat.admin` | Recarregar configuração do chat | OP |

---

## Configuração (`chat/config.yml`)

```yaml
chat:
  local:
    radius: 100          # Blocos — 0 para chat local global (igual ao global)
    format: "{prefix}&f{name}&7: &f{message}"

  global:
    format: "&8[&bGlobal&8] {prefix}&f{name}&7: &f{message}"
    trigger-prefix: "!"  # Inicie a mensagem com ! para enviar globalmente

  staff:
    format: "&8[&cStaff&8] &7{name}&7: &c{message}"

  report:
    format: "&8[&6Report&8] &e{reporter}&7 denunciou &c{target}&7: &f{reason}"

  luckperms-prefix:
    enabled: true
```

### Campos de Configuração

| Campo | Descrição |
| --- | --- |
| `local.radius` | Distância máxima (blocos) para o chat local. `0` para alcançar todos. |
| `local.format` | Formato do chat local. Suporta `{prefix}`, `{name}`, `{message}`. |
| `global.trigger-prefix` | Caractere(s) que transformam uma mensagem local em global (ex: `!oi`). |
| `luckperms-prefix.enabled` | Quando `true`, `{prefix}` é substituído pelo prefixo de rank do LuckPerms. |

---

## Integração com LuckPerms

Com o LuckPerms instalado e `luckperms-prefix.enabled: true`, o prefixo do rank de cada jogador é automaticamente inserido no placeholder `{prefix}` nos formatos de chat. Nenhuma configuração adicional é necessária.
