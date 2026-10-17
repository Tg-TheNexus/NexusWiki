# Módulo Segurança

O módulo Segurança fornece **autenticação BCrypt**, proteção anti-bot com CAPTCHA, gerenciamento de sessões, anti-duplicação e ferramentas anti-lag — projetado para **servidores offline/cracked**.

---

## Sub-sistemas

| Sub-sistema | Descrição |
| --- | --- |
| **Auth** | Registro/login com senhas BCrypt, sessões persistentes |
| **Anti-Bot** | Limitação de taxa por IP, CAPTCHA em mapa, blacklist de nomes, detecção de VPN |
| **Anti-Dupe** | Detecta e previne exploits comuns de duplicação de itens |
| **Anti-Lag** | Limpador de mundo agendado, empilhador de entidades |

---

## Autenticação

Jogadores em servidores cracked devem `/register` no primeiro acesso e `/login` nos acessos seguintes. Contas premium são verificadas via API Mojang e ignoram a autenticação.

### Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/register <senha> <confirmar>` | Registrar uma conta | *(todos)* |
| `/login <senha>` | Entrar na conta | *(todos)* |
| `/changepassword <antiga> <nova>` | Alterar senha | *(autenticado)* |

### Configuração Auth (`security/auth.yml`)

```yaml
storage: sqlite           # sqlite | postgres

session-timeout-minutes: 30      # Re-login após 30min inativo
persistent-session-hours: 2      # Auto-login em 2h após última sessão

max-failed-attempts: 5           # Bloqueio após 5 senhas erradas
lockout-minutes: 10

login-spawn:
  enabled: false                 # Teleportar para lobby enquanto não autenticado
```

### Verificação Premium

Quando `premium-check.enabled` é `true`, o NexusPrism valida contas premium com um processo de duas etapas para que jogadores cracked não possam se passar por contas pagas:

1. **Verificação da versão do UUID** — servidores offline atribuem UUIDs versão 3 a todos os jogadores. Um jogador premium autenticado via FastLogin/JPremium recebe seu UUID real da Mojang (versão 4). Versão 3 = cracked, rejeitado imediatamente.
2. **Comparação com a API da Mojang** — mesmo para UUIDs versão 4, o nome é consultado em `api.mojang.com` e o UUID retornado é comparado com o UUID real do jogador. Qualquer discrepância é sinalizada como tentativa de impersonação.

#### Cache e Resiliência

| Camada | Detalhe |
| --- | --- |
| **Cache em memória** | TTL de 24 horas; limpo ao reiniciar |
| **Cache persistente SQLite** | Sobrevive a reinicializações — arquivo: `security/premium-cache.db` |
| **Limitador de taxa** | Máx. 50 chamadas à API da Mojang por janela de 10 minutos |
| **Backoff exponencial** | Recua até 60 s em caso de falhas repetidas na API |
| **Fallback** | Usa o último resultado em cache quando a API estiver inacessível |

!!! warning "Detecção de impersonação"
    Se um jogador se conectar com um UUID versão 3 (offline) mas o cache indicar que aquele nome possui uma conta Mojang, um aviso é registrado: `IMPERSONATION DETECTED`. O jogador ainda pode entrar, mas é tratado como cracked (deve usar `/login`).

---

## Anti-Bot

### Configuração (`security/antibot.yml`)

```yaml
rate-limit:
  window-seconds: 10
  max-joins: 3            # Máximo de entradas por IP na janela

name-blacklist-patterns:
  - "[A-Za-z]{1,3}[0-9]{5,}"
  - "bot[0-9]+"

captcha:
  enabled: true
  timeout-seconds: 60
  session-hours: 24       # Pular CAPTCHA por 24h após aprovação

premium-check:
  enabled: true           # Contas premium ignoram o CAPTCHA

alt-detection:
  max-accounts-per-ip: 3  # Alertar admins se um IP tiver 3+ contas
```

---

## Anti-Lag

### Comandos

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/cleanworld` | Executar limpeza manual do mundo | `nexusprism.security.cleanworld` |

### Configuração (`security/antilag.yml`)

```yaml
cleaner:
  interval-seconds: 300   # Limpeza automática a cada 5 minutos
  warn-seconds: 5          # Aviso antes da limpeza
  item-age-ticks: 6000     # Remover itens com mais de 5 minutos
  worlds:
    - world
    - world_nether
    - world_the_end

stacker:
  radius: 5.0              # Fundir mobs em raio de 5 blocos
  max-stack: 50            # Máximo de 50 mobs por pilha
```

---

## Comandos de Staff

| Comando | Uso | Permissão |
| --- | --- | --- |
| `/vanish` | Alternar invisibilidade (OP) | `nexusprism.staff.vanish` |
| `/invsee <jogador>` | Inspecionar inventário (OP) | `nexusprism.staff.invsee` |
| `/spy` | Alternar espionagem de chat (OP) | `nexusprism.staff.spy` |

---

## Permissões

| Permissão | Descrição | Padrão |
| --- | --- | --- |
| `nexusprism.security.cleanworld` | Limpeza manual do mundo | OP |
| `nexusprism.staff.vanish` | Ficar invisível | OP |
| `nexusprism.staff.invsee` | Inspecionar inventários | OP |
| `nexusprism.staff.spy` | Modo spy de chat | OP |

---

## Mobs com Nível

Todo mob hostil que aparece no mundo recebe automaticamente um **nível** que escala de acordo com o perigo do ambiente. Mobs de nível mais alto causam mais dano, têm mais vida e concedem mais XP.

### Tabela de Rolagem de Nível

Os níveis são rolados no spawn com base na altura Y, dimensão e bioma. Os bônus se acumulam.

| Condição | Faixa / Bônus |
| --- | --- |
| Y > 64 (superfície) | Nv. 1–4 |
| Y ≤ 64 | Nv. 3–6 |
| Y ≤ 30 | Nv. 5–8 |
| Y ≤ 0 (subterrâneo profundo) | Nv. 8–12 |
| Dimensão Nether | +3 ao resultado |
| The End | +4 ao resultado |
| Bioma Deep Dark | +5 ao resultado |
| Lua de Sangue ativa | +2 a todos os resultados |

Todos os resultados são limitados ao intervalo `[1, max-level]` da configuração.

### Formato do Nome

| Situação | Nome exibido |
| --- | --- |
| Empilhado + com nível | `3x [Nv.5] Zumbi` |
| Único + com nível | `[Nv.5] Zumbi` |
| Nível 1 (qualquer pilha) | `3x Zumbi` *(sem tag de nível)* |

### Fórmulas de Atributo

| Atributo | Fórmula |
| --- | --- |
| **Dano** | `danoBase × (1 + (nível-1) × multiplicadorDanoPorNível) × contadorPilha` |
| **XP** | `xpBase × contadorPilha × (1 + (nível-1) × multiplicadorXPPorNível)` |
| **Vida** | Escalada por `multiplicadorVidaPorNível` por nível acima de 1 |

### Configuração (`security/antilag.yml`)

```yaml
leveled-mobs:
  enabled: true
  max-level: 20
  xp-multiplier-per-level: 0.20      # +20% XP por nível acima de 1
  damage-multiplier-per-level: 0.15  # +15% dano por nível acima de 1
  health-multiplier-per-level: 0.10  # +10% vida por nível acima de 1
```

!!! note "Integração com Lua de Sangue"
    Quando a **Lua de Sangue** está ativa (veja o [módulo Events](events.md)), todas as rolagens de nível recebem um bônus de **+2**, tornando os mobs de superfície significativamente mais perigosos à noite.

---

## PlaceholderAPI

| Placeholder | Descrição |
| --- | --- |
| `%nexusprism_authenticated%` | `true` se o jogador está autenticado |
| `%nexusprism_auth_status%` | Status de auth legível (`Autenticado`, `Pendente`) |
