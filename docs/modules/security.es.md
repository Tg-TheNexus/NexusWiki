# Módulo Seguridad

El módulo Seguridad proporciona **autenticación BCrypt**, protección anti-bot con CAPTCHA, gestión de sesiones, anti-duplicación y herramientas anti-lag — diseñado para **servidores offline/crackeados**.

---

## Sub-sistemas

| Sub-sistema | Descripción |
| --- | --- |
| **Auth** | Registro/inicio de sesión con contraseñas BCrypt, sesiones persistentes |
| **Anti-Bot** | Limitación de tasa por IP, CAPTCHA en mapa, lista negra de nombres, detección de VPN |
| **Anti-Dupe** | Detecta y previene exploits comunes de duplicación de ítems |
| **Anti-Lag** | Limpiador de mundo programado, apilador de entidades |

---

## Autenticación

Los jugadores en servidores crackeados deben `/register` en el primer acceso y `/login` en los accesos siguientes. Las cuentas premium omiten la autenticación solo después de que el handshake de sesión de Mojang demuestra que son dueñas del nombre (ver [Verificación Premium](#verificacion-premium)).

### Comandos

| Comando | Uso | Permiso |
| --- | --- | --- |
| `/register <contraseña> <confirmar>` | Registrar una cuenta | *(todos)* |
| `/login <contraseña>` | Iniciar sesión | *(todos)* |
| `/changepassword <antigua> <nueva>` | Cambiar contraseña | *(autenticado)* |
| `/auth premiumclaim <nombre>` | Hace un nombre solo-premium (todo acceso debe pasar el handshake) | OP |
| `/auth premiumunclaim <nombre>` | Quita un claim (el dueño perdió la cuenta, o un nombre reclamado por error) | OP |

### Configuración Auth (`security/auth.yml`)

```yaml
storage: sqlite

session-timeout-minutes: 30      # Re-login tras 30min inactivo
persistent-session-hours: 2      # Auto-login en 2h tras última sesión

max-failed-attempts: 5           # Bloqueo tras 5 contraseñas incorrectas
lockout-minutes: 10

login-spawn:
  enabled: false
```

### Verificación Premium

Un nombre que existe en Mojang no prueba nada: cualquiera puede escribirlo. La única prueba de que el jugador es dueño de la cuenta es el **handshake de sesión de Mojang**, que realiza el módulo FastLogin (requiere ProtocolLib 5.4.0+): el cliente inicia sesión en Mojang y el servidor lo confirma con `sessionserver.mojang.com/session/minecraft/hasJoined`. El resultado vale para un solo acceso y queda ligado al nombre exacto y al UUID real (versión 4) de Mojang.

Un cliente crackeado no puede responder al handshake, así que solo se exige a nombres que el dueño **reclamó** (claim):

1. Un cliente crackeado entra con un nombre que parece premium (sin claim todavía): **no** se le da acceso. Recibe el aviso SÍ/NO y el flujo normal de `/register` y `/login`.
2. El dueño real pulsa **SÍ**. El nombre queda reclamado y el jugador es expulsado para reconectar con el launcher oficial. Un clic nunca da acceso. Un nombre que ya tiene cuenta con contraseña en el servidor no se puede reclamar con un clic; el admin usa `/auth premiumclaim`.
3. A partir de ahí cada acceso de ese nombre debe pasar el handshake. Si lo pasa, omite el CAPTCHA y el `/login` y juega con su UUID real. Quien falla (cliente crackeado, Mojang caído, tiempo agotado) es desconectado y **nunca** cae en `/login`. Sin FastLogin cargado, los nombres reclamados se rechazan.

`premium-uuid-required: false` (premium solo por nombre) fue eliminado; la clave se ignora y el log de inicio lo avisa. Los nombres Bedrock (empiezan con `.`) no se pueden reclamar.

Claves opcionales en el `config.yml` principal: `fastlogin.handshake-timeout-seconds` (20), `fastlogin.mojang-timeout-ms` (5000), `fastlogin.max-handshakes-per-minute-per-ip` (10), `fastlogin.messages.failed|busy|unavailable`.

#### Caché y Resiliencia

| Capa | Detalle |
| --- | --- |
| **Caché en memoria** | TTL de 24 horas; limpiado al reiniciar |
| **Caché persistente SQLite** | Sobrevive a reinicios — archivo: `security/premium-cache.db` |
| **Limitador de tasa** | Máx. 50 llamadas a la API de Mojang por ventana de 10 minutos |
| **Backoff exponencial** | Retrocede hasta 60 s en fallos repetidos de la API |
| **Fallback** | Usa el último resultado en caché cuando la API no está disponible |

!!! note "La caché solo dice si el nombre existe"
    La caché y la API anteriores solo responden si existe una cuenta Mojang con ese nombre. Eso nunca sustituye al `/login`: lo sustituye el handshake.

---

## Anti-Bot

### Configuración (`security/antibot.yml`)

```yaml
rate-limit:
  window-seconds: 10
  max-joins: 3

name-blacklist-patterns:
  - "[A-Za-z]{1,3}[0-9]{5,}"
  - "bot[0-9]+"

captcha:
  enabled: true
  timeout-seconds: 60
  session-hours: 24

premium-check:
  enabled: true

alt-detection:
  max-accounts-per-ip: 3
```

---

## Anti-Lag

### Comandos

| Comando | Uso | Permiso |
| --- | --- | --- |
| `/cleanworld` | Ejecutar limpieza manual del mundo | `nexusprism.security.cleanworld` |

### Configuración (`security/antilag.yml`)

```yaml
cleaner:
  interval-seconds: 300
  warn-seconds: 5
  item-age-ticks: 6000
  worlds:
    - world
    - world_nether

stacker:
  radius: 5.0
  max-stack: 50
```

---

## Comandos de Staff

| Comando | Uso | Permiso |
| --- | --- | --- |
| `/vanish` | Alternar invisibilidad (OP) | `nexusprism.staff.vanish` |
| `/invsee <jugador>` | Inspeccionar inventario (OP) | `nexusprism.staff.invsee` |
| `/spy` | Alternar espionaje de chat (OP) | `nexusprism.staff.spy` |

---

## Permisos

| Permiso | Descripción | Predeterminado |
| --- | --- | --- |
| `nexusprism.security.cleanworld` | Limpieza manual del mundo | OP |
| `nexusprism.staff.vanish` | Volverse invisible | OP |
| `nexusprism.staff.invsee` | Inspeccionar inventarios | OP |
| `nexusprism.staff.spy` | Modo espía de chat | OP |

---

## Mobs con Nivel

Cada mob hostil que aparece en el mundo recibe automáticamente un **nivel** que escala según el peligro del entorno. Los mobs de mayor nivel hacen más daño, tienen más vida y dan más XP.

### Tabla de Tirada de Nivel

Los niveles se tiran al aparecer basándose en la altura Y, dimensión y bioma. Los bonificadores se acumulan.

| Condición | Rango / Bonificador |
| --- | --- |
| Y > 64 (superficie) | Nv. 1–4 |
| Y ≤ 64 | Nv. 3–6 |
| Y ≤ 30 | Nv. 5–8 |
| Y ≤ 0 (subterráneo profundo) | Nv. 8–12 |
| Dimensión Nether | +3 al resultado |
| The End | +4 al resultado |
| Bioma Deep Dark | +5 al resultado |
| Luna de Sangre activa | +2 a todos los resultados |

Todos los resultados se limitan al rango `[1, max-level]` de la configuración.

### Formato del Nombre

| Situación | Nombre mostrado |
| --- | --- |
| Apilado + con nivel | `3x [Nv.5] Zombie` |
| Individual + con nivel | `[Nv.5] Zombie` |
| Nivel 1 (cualquier pila) | `3x Zombie` *(sin etiqueta de nivel)* |

### Fórmulas de Estadísticas

| Estadística | Fórmula |
| --- | --- |
| **Daño** | `dañoBase × (1 + (nivel-1) × multiplicadorDañoPorNivel) × contadorPila` |
| **XP** | `xpBase × contadorPila × (1 + (nivel-1) × multiplicadorXPPorNivel)` |
| **Vida** | Escalada por `multiplicadorVidaPorNivel` por nivel sobre 1 |

### Configuración (`security/antilag.yml`)

```yaml
leveled-mobs:
  enabled: true
  max-level: 20
  xp-multiplier-per-level: 0.20      # +20% XP por nivel sobre 1
  damage-multiplier-per-level: 0.15  # +15% daño por nivel sobre 1
  health-multiplier-per-level: 0.10  # +10% vida por nivel sobre 1
```

!!! note "Integración con Luna de Sangre"
    Cuando la **Luna de Sangre** está activa (ver el [módulo Events](events.md)), todas las tiradas de nivel reciben un bonificador de **+2**, haciendo a los mobs de superficie significativamente más peligrosos de noche.

---

## PlaceholderAPI

| Placeholder | Descripción |
| --- | --- |
| `%nexusprism_authenticated%` | `true` si el jugador está autenticado |
| `%nexusprism_auth_status%` | Estado de auth legible (`Autenticado`, `Pendiente`) |
