# Módulo Web & GDPR

O módulo Web gerencia a **integração com a loja virtual**, **entrega de kits VIP**, **webhooks de pagamento** e **conformidade com a LGPD/GDPR** — dando aos jogadores controle sobre seus dados pessoais.

---

## Conformidade com LGPD/GDPR

Os jogadores podem exportar, deletar e gerenciar o consentimento de seus dados armazenados diretamente no jogo.

### Comandos

Todos os comandos GDPR são exclusivos para jogadores e não requerem permissão especial.

| Comando | Descrição |
| --- | --- |
| `/nexus gdpr` | Mostrar informações de GDPR e configurações de consentimento atuais |
| `/nexus gdpr export` | Exportar todos os dados pessoais para um arquivo JSON em `gdpr/` |
| `/nexus gdpr delete` | Deletar todos os dados pessoais (direito ao esquecimento) |
| `/nexus consent <tipo> <accept\|deny>` | Conceder ou negar um tipo específico de consentimento |

### Tipos de Consentimento

| Tipo | O que Cobre |
| --- | --- |
| `activity_tracking` | Dados de entrada/saída e tempo de jogo |
| `purchase_history` | Registros de transações |
| `discord_notifications` | Ações do jogador vinculadas ao Discord |
| `statistics` | Estatísticas e conquistas do jogador |
| `marketing` | Anúncios e promoções do servidor |

!!! info "Exclusão de dados"
    Registros financeiros mais recentes que `gdpr.legal-retention-years` são **anonimizados** em vez de deletados, para cumprir os requisitos legais mínimos de retenção. Todos os outros dados são removidos imediatamente.

---

## Integração com Loja Virtual

### Entrega de Kits VIP

Quando um jogador compra um rank ou kit na loja virtual, o pedido é colocado em fila. No próximo acesso do jogador, `auto-deliver: true` entrega o kit automaticamente.

```yaml
kits:
  VIP:
    items:
      - material: DIAMOND
        amount: 5
    commands:
      - "lp user {player} group set vip"
      - "tell {player} Bem-vindo ao VIP!"
```

---

## Segurança

### Criptografia de Dados

Com `security.enable-encryption: true` (padrão), dados sensíveis são criptografados com **AES-256-CBC** com IV aleatório por entrada. A chave é gerada uma vez e salva em `plugins/NexusPrism/web/encryption.key`.

!!! warning "Faça backup de encryption.key"
    Se este arquivo for perdido, os dados previamente criptografados não poderão ser recuperados. Inclua-o nos backups do servidor. Nunca o commite em um repositório git.

### Segredo do Receiver (Stream Panel)

O plugin abre uma porta HTTP (`nexus-tools.receiver-port`, padrão `8080`) para receber eventos Twitch do Stream Panel. Configure `nexus-tools.receiver-secret` com um segredo compartilhado e use o mesmo valor no Stream Panel. Requisições sem o header `Authorization: Bearer <secret>` correto são rejeitadas com 401.

---

## Configuração (`web-config.yml`)

```yaml
discord:
  webhook-url: ""
  server-invite: "https://discord.gg/seu-invite"
  notifications-enabled: false

api:
  enabled: false
  endpoint: "https://seu-site.com/api"
  key: ""                          # Gerado automaticamente na primeira execução
  rate-limit: 60

security:
  require-api-key: true
  enable-ip-whitelist: false
  whitelisted-ips:
    - "127.0.0.1"
    - "seu-ip-do-servidor"
  enable-encryption: true          # AES-256-CBC; chave em web/encryption.key

gdpr:
  enabled: true
  log-transactions: true
  data-retention-days: 365
  legal-retention-years: 7
  allow-data-export: true
  allow-data-deletion: true

payments:
  enabled: false
  provider: "custom"               # stripe | paypal | mercadopago | custom
  webhook-secret: ""               # Gerado automaticamente na primeira execução
  currency: "BRL"

nexus-tools:
  receiver-port: 8080              # Porta HTTP para eventos do Stream Panel
  receiver-secret: ""              # Segredo compartilhado — deve coincidir com o Stream Panel

vip-kits:
  enabled: true
  auto-deliver: true
  verify-payment: true
```

### Campos de Configuração

| Campo | Padrão | Descrição |
| --- | --- | --- |
| `api.endpoint` | — | URL base da loja virtual para verificação de pedidos |
| `api.key` | *(auto-gerado)* | Copie para a variável de ambiente `NEXUS_API_KEY` da loja |
| `security.require-api-key` | `true` | Rejeita requisições sem API key válida — nunca desabilite em produção |
| `security.enable-encryption` | `true` | Criptografia AES-256-CBC para dados sensíveis armazenados |
| `payments.webhook-secret` | *(auto-gerado)* | Deve coincidir com o segredo configurado no painel do provedor de pagamento |
| `nexus-tools.receiver-secret` | `` | Segredo compartilhado para autenticação HTTP Stream Panel → plugin |
| `vip-kits.auto-deliver` | `true` | Entrega kits pendentes automaticamente ao jogador entrar |
| `vip-kits.verify-payment` | `true` | Verifica status do pagamento via API antes de entregar o kit |
