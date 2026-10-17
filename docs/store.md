# Loja / Webstore

O NexusPrism inclui uma bridge de loja web integrada que entrega pacotes comprados aos jogadores automaticamente, mesmo quando estão offline.

!!! warning "Conformidade com o EULA"
    Todos os pacotes da loja devem estar em conformidade com as [Diretrizes de Uso Comercial do Minecraft](https://www.minecraft.net/en-us/eula). A venda de vantagens de jogo que não possam ser obtidas normalmente **não é permitida** em servidores acessíveis ao público.

---

## Funcionalidades Conformes ao EULA

| Funcionalidade | Observações |
| --- | --- |
| **Nicknames cosméticos** | `/nick` — apenas visual, sem vantagem |
| **Chapéus cosméticos** | `/hat` — apenas visual |
| **Homes adicionais** | Slots extras de home (conveniência) |
| **Voar fora de zonas PvP** | Conveniência cosmética; desabilitado em regiões PvP |
| **Acesso ao resource pack** | Resource pack do servidor (cosmético) |
| **Slots extras de ponto de viagem** | Conveniência — veja `nexusprism.essentials.waypoints.*` |
| **Kit VIP (cosmético)** | Itens cosméticos, equipamento de vaidade |
| **Chaves de crate** | Desde que todas as recompensas também possam ser obtidas em jogo |
| **Tags de nome coloridas** | Apenas visual |
| **Cargo no Discord** | Acesso a um canal especial do Discord |
| **Mensagens de entrada personalizadas** | Visual/cosmético |

---

## Sistema de Entrega

A bridge de webstore do NexusPrism usa uma fila de entrega. Quando um jogador compra um pacote:

1. A loja envia uma solicitação de entrega ao plugin via bridge
2. A entrega é enfileirada em `delivery.yml` (persistente)
3. No próximo login do jogador, todas as entregas pendentes são processadas
4. Os comandos são executados automaticamente em seu nome

Isso significa que a **entrega offline é suportada** — o jogador não precisa estar online no momento da compra.

### Configuração (`delivery.yml`)

```yaml
enabled: true

endpoint:
  host: "0.0.0.0"
  port: 9090
  token: "mude-este-token-de-entrega"

file-fallback: "pending_deliveries.jsonl"
```

---

## Kits VIP (`kits.yml`)

```yaml
kits:
  vip:
    display-name: "&6Kit VIP"
    permission: "nexusprism.kit.vip"
    cooldown-hours: 24
    items:
      - material: GOLDEN_APPLE
        amount: 5
      - nexusprism-id: SERVER_KEY
        amount: 1
    commands:
      - "eco give {player} 1000"

  mvp:
    display-name: "&bKit MVP"
    permission: "nexusprism.kit.mvp"
    cooldown-hours: 24
    items:
      - material: GOLDEN_APPLE
        amount: 16
      - nexusprism-id: SERVER_KEY
        amount: 2
    commands:
      - "eco give {player} 2500"
```

---

## Plataformas de Loja Recomendadas

- **Tebex** (antigo Buycraft) — certificado pelo EULA
- **CraftingStore** — certificado pelo EULA
- **Painel personalizado** — use o endpoint HTTP de entrega
