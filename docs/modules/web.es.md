# Módulo Web & GDPR

El módulo Web gestiona la **integración con la tienda virtual**, **entrega de kits VIP**, **webhooks de pago** y **cumplimiento del RGPD** — dando a los jugadores control sobre sus datos personales.

---

## Cumplimiento del RGPD

| Comando | Descripción |
| --- | --- |
| `/nexus gdpr` | Mostrar información de RGPD y configuración de consentimiento |
| `/nexus gdpr export` | Exportar todos los datos personales a un archivo JSON |
| `/nexus gdpr delete` | Eliminar todos los datos personales (derecho al olvido) |
| `/nexus consent <tipo> <accept\|deny>` | Otorgar o denegar un tipo de consentimiento |

### Tipos de Consentimiento

| Tipo | Qué cubre |
| --- | --- |
| `activity_tracking` | Datos de conexión y tiempo de juego |
| `purchase_history` | Registros de transacciones |
| `discord_notifications` | Acciones del jugador vinculadas a Discord |
| `statistics` | Estadísticas y logros del jugador |
| `marketing` | Anuncios y promociones del servidor |

---

## Seguridad

### Cifrado de Datos

Con `security.enable-encryption: true` (predeterminado), los datos sensibles se cifran con **AES-256-CBC** con IV aleatorio por entrada. La clave se genera una vez y se guarda en `plugins/NexusPrism/web/encryption.key`.

!!! warning "Haz copia de seguridad de encryption.key"
    Si se pierde este archivo, los datos cifrados no podrán recuperarse. Inclúyelo en las copias de seguridad del servidor. Nunca lo subas a un repositorio git.

### Secreto del Receiver (Stream Panel)

El plugin abre un puerto HTTP (`nexus-tools.receiver-port`, predeterminado `8080`) para recibir eventos de Twitch del Stream Panel. Configura `nexus-tools.receiver-secret` con un secreto compartido y usa el mismo valor en el Stream Panel. Las solicitudes sin el header `Authorization: Bearer <secret>` correcto son rechazadas con 401.

---

## Configuración (`web-config.yml`)

```yaml
discord:
  webhook-url: ""
  server-invite: "https://discord.gg/tu-invite"
  notifications-enabled: false

api:
  enabled: false
  endpoint: "https://tu-sitio.com/api"
  key: ""                          # Generado automáticamente en el primer inicio
  rate-limit: 60

security:
  require-api-key: true
  enable-ip-whitelist: false
  whitelisted-ips:
    - "127.0.0.1"
    - "tu-ip-del-servidor"
  enable-encryption: true          # AES-256-CBC; clave en web/encryption.key

gdpr:
  enabled: true
  data-retention-days: 365
  legal-retention-years: 7
  allow-data-export: true
  allow-data-deletion: true

payments:
  enabled: false
  provider: "custom"               # stripe | mercadopago | custom
  webhook-secret: ""               # Generado automáticamente en el primer inicio
  currency: "USD"

nexus-tools:
  receiver-port: 8080              # Puerto HTTP para eventos del Stream Panel
  receiver-secret: ""              # Secreto compartido — debe coincidir con Stream Panel

vip-kits:
  enabled: true
  auto-deliver: true
  verify-payment: true
```

### Campos de Configuración

| Campo | Predeterminado | Descripción |
| --- | --- | --- |
| `api.endpoint` | — | URL base de la tienda para verificación de pedidos |
| `api.key` | *(auto-generado)* | Cópialo a la variable de entorno `NEXUS_API_KEY` de la tienda |
| `security.require-api-key` | `true` | Rechaza solicitudes sin API key válida — nunca deshabilites en producción |
| `security.enable-encryption` | `true` | Cifrado AES-256-CBC para datos sensibles almacenados |
| `payments.webhook-secret` | *(auto-generado)* | Debe coincidir con el secreto configurado en el panel del proveedor de pago |
| `nexus-tools.receiver-secret` | `` | Secreto compartido para autenticación HTTP Stream Panel → plugin |
| `vip-kits.auto-deliver` | `true` | Entrega kits pendientes automáticamente cuando el jugador se conecta |
| `vip-kits.verify-payment` | `true` | Verifica el estado del pago vía API antes de entregar el kit |
