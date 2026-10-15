# Historial de Cambios

> Generado automáticamente desde los commits de [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism).
> Traducido automáticamente — pueden esperarse pequeñas diferencias de redacción.

---

## [2026-10-14] · `64bc66f`


### ✨ Añadido

- **store**: Cosmetic-only default sku-map and supporter titles (#51)

---

## [2026-10-14] · `41a480b`


### 📚 Documentación

- How to turn the delivery bridge on in a server (#50)

---

## [2026-10-14] · `abfc6dc`


### 🐛 Corregido

- **delivery**: Bind timestamptz values when marking an order delivered (#49)

---

## [2026-10-14] · `222e5f3`


### ✨ Añadido

- **delivery**: Bridge database from key_configs, fix item keys, unmapped skus and mark-delivered path (#48)

---

## [2026-10-14] · `2aa89fa`


### 🐛 Corregido

- **web**: Unify the lynx address and move the webhook secret to key_configs

### 🔧 Mantenimiento

- Rename GitHub org to Tg-TheNexus
- Rename org to Tg-TheNexus and unify lynx and webhook config keys (#47)

## [2026-10-03] · `780b8af`


### 🔧 Mantenimiento

- **config**: Point defaults at the nexusheim.com hosts

---

## [2026-09-28] · `c392ae4`


### 🐛 Corregido

- **ci**: Drop dev branch trigger, NexusPrism doesn't use one

---

## [2026-09-28] · `3b2579e`


### 🐛 Corregido

- **ci**: Don't fail the whole build when artifact upload hits storage quota

---

## [2026-09-28] · `60616b0`


### 📚 Documentación

- **changelog**: Note the link/linkstreamer split

---

## [2026-09-28] · `2d9c95d`


### ✨ Añadido

- **twitch**: Split /twitch link into /twitch link and /twitch linkstreamer

---

## [2026-09-27] · `18cd012`


### 🐛 Corregido

- **events,quests**: Raise Groq max_tokens for gpt-oss-120b's reasoning overhead

---

## [2026-09-27] · `037e895`


### 🐛 Corregido

- **events,quests**: Groq/compound-mini was also removed from Groq's catalog

---

## [2026-09-26] · `4b18be4`


### 🐛 Corregido

- **events,quests**: Replace deprecated Groq model in BossTitle/DailyQuests

---

## [2026-09-23] · `17c3478`


### ✨ Añadido

- **economy**: Publish vanilla sell-prices to shared DB for nexus-bot's /market

---

## [2026-08-09] · `632d673`


### 🔧Mantenimiento

- **deps**: Mejora el controlador JDBC postgresql 42.7.11 -> 42.7.12

---

## [2026-08-09] · `9f261ed`


### ✨Añadido See More

- **economy**: Agregar puente de moneda basado en encuestas
- **discord**: Enlaces de cuenta espejo a nexus-bot

### 🐛 Corregido See More

- **config**: Eliminar estructuras colgantes/entradas de investigación

---

## [2026-08-06] · `ab72213`


### ✨Añadido See More

- **events**: Externaliza el equilibrio del juego codificado en la configuración

### 🐛 Corregido See More

- **security**: Elimina la IP/nombre de usuario real del ejemplo de javadoc, elimina la URL de reserva de nexus-bot codificada

### ♻️ Modificado

- **core**: Eliminar elemento/máquina/energía/dominio de investigación confirmado-muerto

### 📚 Documentación

- Actualizar los documentos de referencia para que coincidan con el módulo/superficie API actual

---

## [2026-07-11] · `36e78ff`


### 🐛 Corregido See More

- **waila**: Extraer formatoSnakeName para la cadena EntityType, corregir error de compilación
## [2026-07-10] · `0d08f3e`


### ✨Añadido See More

- **waila**: Detección de entidades y coloración basada en rarezas

---

## [2026-07-09] · `0283136`


### ✨Añadido See More

- **mmo**: Agregar superficie de gancho NexusATS (T1 cableado, terminales T2/T3)

### 🐛 Corregido See More

- **lang**: Elimina claves YAML duplicadas en en_US y pt_BR
## [2026-07-06] · `32d26d9`


### ✨Añadido See More

- **discord**: Notificaciones de eliminación masiva de grupos con rebote de 1 segundo
- **discord**: Resolución de mención bidireccional — @@ MC→Discord, # Discord→MC

### 🐛 Corregido See More

- **discord**: Webhook tiene prioridad para los mensajes del jugador, JDA para los mensajes del sistema: evita publicaciones duplicadas
- **discord**: Cargar todos los miembros del gremio en la barra de acción de mención listo + arreglar
- **mmo**: Restaurar MmoListener eliminado por error en la extracción de slimefun

### ♻️ Modificado

- **discord**: Elimina DiscordChatListener muerto, elimina el comentario engañoso de chat.webhookUrl
- **discord**: Eliminar @PlayerName heredado → Resolución de mención de Discord

### 📚 Documentación

- **discord**: Aclarar que el canal predeterminado necesita ID de JDA para Discord → MC Relay

### 🔧Mantenimiento

- **config**: Eliminar secciones muertas, arreglar lista de módulos
- **discord**: Elimina la clave de webhook de chat inactiva de key_configs.yml

---

## [2026-07-03] · `ef78584`


### 🔧Mantenimiento

- **ci**: Eliminar el paso validar_items movido a NexusATS

---

## [2026-07-03] · `2786877`


### ♻️ Modificado

- **events**: Cambie el nombre de Sacrifice Arc a The Convergence en todos los archivos y códigos de idiomas

---

## [2026-06-19] · `d04c992`


### ✨Añadido See More

- **integration**: Agregue una superficie de gancho NexusATS para el bloque de la máquina y el cableado Waila

---

## [2026-06-19] · `06bfe20`


### ✨Añadido See More

- **waila**: Agregar reconocimiento de bloque básico

### 🐛 Corregido See More

- **startup**: Reduce la verbosidad del registro y corrige prefijos duplicados y fugas de color.
- **twitch**: Deja de reconectarse después de 3 fallas de IRC consecutivas

### ♻️ Modificado

- **slimefun**: Extraiga máquinas, energía, elementos y elementos para el futuro complemento NexusItems.
## [2026-06-17] · `ce58736`


### ✨Añadido See More

- **machines**: Agregar sistema de máquina multibloque impulsado por YAML

### 🐛 Corregido See More

- **items**: Cambie el nombre de los elementos de aleación simple al sufijo _INGOT y elimine los marcadores de posición de PAPEL
## [2026-06-16] · `cfd4b44`


### 🐛 Corregido See More

- **recipes**: Ingredientes ENHANCED_CRAFTING sin forma analizados como sección, no como lista de cadenas

### ♻️ Modificado

- **machines**: Reemplace el bloque de máquina de la Mesa de elaboración mejorada con un multibloque estilo Slimefun
- **machines**: Reescribe la mesa de elaboración mejorada en un verdadero multibloque estilo Slimefun

### 🔧Mantenimiento

- **items**: Reemplazar nexo:COPPER_INGOT con vainilla COPPER_INGOT
- **items**: Arreglar la categorización: cambiar el nombre de los minerales en bruto, eliminar duplicados de vainilla, arreglar la coincidencia de aleación/placa
- **items**: Cambie el nombre de DUST_AMETHYST/DUST_NETHERITE a una convención *_DUST consistente
## [2026-06-15] · `dd8cee0`


### ✨Añadido See More

- **machines**: Agregar máquina de mesa de elaboración y sistema de recetas mejorados

### 🐛 Corregido See More

- **machines**: Resolve MachineCatalog ENHANCED_CRAFTING_TABLE advertencia de entrada de elemento
- **machines**: Corrige la advertencia ENHANCED_CRAFTING_TABLE MachineCatalog

### ♻️ Modificado

- **recipes**: Migre todas las recetas de creación de complementos a la tabla de creación mejorada
## [2026-06-14] · `f52e15d`


### 🐛 Corregido See More

- **machines**: Resolve 3 advertencias entre capas de MachineCatalog
- **machines**: Elimina el código auxiliar HOLOGRAM_PROJECTOR duplicado de basic_machines.yml

---

## [2026-06-14] · `a434364`


### ✨Añadido See More

- **crafting**: Agrega recetas para 37 elementos que antes no se podían crear

### 🐛 Corregido See More

- **items**: Mover SINGULARITY_CONSTRUCTOR a nexus_machines.yml; agregar definición de máquina + recetas de singularidad

---

## [2026-06-14] · `76b04ab`


### ✨Añadido See More

- **crafting**: Agregar cadena de recetas infinita en Infinity Table

### 🐛 Corregido See More

- **events**: Registra los 6 jefes de desafío que faltan en DEFAULT_BOSS_FILES

### ♻️ Modificado

- **crafting**: Migrar equipo infinito a Infinity Table; arreglar INFINITY_APPLE

---

## [2026-06-14] · `8b862fc`


### ✨Añadido See More

- **items/tinkers**: Agregue la categoría TINKERS, migre 137 elementos CAST, corrija INGOT_FORMER a MACHINE
- **tools,ci**: Agregue validar_items.py (conflictos CMD + reglas de categoría) y conéctelo a CI

### 🐛 Corregido See More

- **mmo**: Guard null customName() antes de ConcurrentHashMap.putIfAbsent en MobHealthDisplay

### ♻️ Modificado

- **lang**: Cambie el nombre de las claves de idioma de security.world-cleaner y sincronice los archivos de idioma
- **events/challenge**: Agregue CMD de visualización a los YAML del jefe, actualice las clases de ChallengeBoss
- **items/cobblestone**: Reemplace COMPRESSED_COBBLESTONE de 5 niveles con 8 elementos explícitos (x9..x43M), elimine COBBLE_1-5 duplicados y GUI de máquinas obsoletas

### 🔧Mantenimiento

- **tools**: Elimina artefactos rp_prompts obsoletos, permite herramientas/*.py en gitignore
- **items**: Asignar CMD faltantes a las variantes ITEM_BAND y NETWORK_POWER_DISPLAY en gear.yml
## [2026-06-09] · `ca942b3`


### 🐛 Corregido See More

- **events**: Cambiar el nombre del directorio de recursos JAR de Challenge_bosses (era anime_bosses)
- **energy,ae**: Puente del consumidor + retroalimentación de inserción del terminal ME

### ♻️ Modificado

- **lang**: Migrar mensajes codificados a claves de idioma (lote 1)
- **lang**: Migrar cadenas codificadas del complemento nexusprism a claves de idioma
- **lang**: Reemplace todos los § literales con & en archivos lang
- **lang**: Migrar las cadenas restantes del complemento nexusprism a claves de idioma
- **lang**: Migrar cadenas en eventos/mmo/rng/security/discord/quests a claves de idioma
- **lang**: Migrar las cadenas § restantes en chat/core/crates/mmo/machines/enchants a las claves de idioma y ChatColor
## [2026-06-08] · `d1b12d2`


### ✨Añadido See More

- **items,ae**: Niveles de martillo, capacidad de bytes AE2, corrección de persistencia ME
- **vfx,mmo,crates**: VFXUtil, placas de identificación de salud de la mafia, VFX de habilidad, VFX de caja

### 🐛 Corregido See More

- **machines**: Infraestructura energética exenta del catálogo Verificación de capa GUI
- Teclas de idioma de estado de **ae,gui,energy**: AE, colorear la historia de la GUI, búfer de generación creativa
- **ae,gui,commands**: Canales de cable de vidrio, GUI creativas, finalización de pestañas
- El controlador **ae**: proporciona 8 canales base para que funcionen las redes sin cables
- **mmo**: Soluciona el conflicto de la barra de acciones entre las notificaciones de HUD y XP

### ♻️ Modificado

- **display**: Centraliza la barra de acciones a través de ActionBarManager
- **events**: Cambiar el nombre del paquete de anime y las clases para desafiar
- **events**: Termina el anime → cambia el nombre del desafío en documentos, idiomas y recursos

### 🔧Mantenimiento

- **cleanup**: Eliminar copias archivadas y eliminar banners CUT obsoletos
- **cleanup**: Elimina los banners CUT obsoletos restantes y actualiza los ejemplos/cajas
## [2026-06-07] · `c2888ce`


### 🐛 Corregido See More

- **machines**: Omitir claves de plantilla/campos en el cargador; soltar el archivo de elementos generados obsoletos
- **items**: Propagar colocables a través de plantillas + podar elementos de máquina generados duplicados
- **machines**: Agregar definición de comportamiento de ALMACENAMIENTO CREATIVE_CAPACITOR
- **machines**: Agregue generadores AVANZADOS + ELECTRIC_BLAST_FURNACE, alinee los identificadores FAL/MOB
## [2026-06-06] · `e7a40f7`


### ✨Añadido See More

- **api**: Reconstruir la superficie API de artículo/máquina/receta
- **core**: MachineManager respaldado por PDC + registro/resolvedores de elementos
- **machines**: Motor tipificado, registro, definiciones, cargador + validador de catálogo
- **ae**: Reconstruir la red ME como máquinas controladas por MachineContext
- **storage**: Persiste las ubicaciones de las máquinas a través de DataManager (SQLite/MySQL/YAML)
- **machines**: Pegamento de complemento, oyentes divididos, controlador GUI, cargadores, cableado
- **recipes**: Migrar red ME, celda de almacenamiento + elaboración de mochila a YAML
- **machines**: Hacer que todas las máquinas estén disponibles + proporcionar GUI basadas en tipos
- **energy**: Infinite CREATIVE_CAPACITOR + solo marca los bloques controlados por el motor
- **energy**: Conectar los generadores del motor a la red de cable + alternar el modo de exportación

### 🐛 Corregido See More

- **machines**: Cambie el nombre de la clave GUI de CRUSHER a ORE_CRUSHER; dedup CREATIVE_CAPACITOR
- **items**: Fusionar CREATIVE_GENERATOR_BLOCK perdido en CREATIVE_GENERATOR

### ♻️ Modificado

- **energy,mmo,systems,items**: Vuelva a conectar a los consumidores a la nueva API de artículo/máquina
- **machines**: Fusionar elementos generados en machine_blocks + GUI con reconocimiento de subtipos

### 📚 Documentación

- **recipes**: Documento codificado de RecipeLoader a las brechas de migración de YAML
- **recipes**: Marcar recetas ME/celdas de almacenamiento/mochila como migradas

### 🔧Mantenimiento

- Gitignore actualizado
## [2026-06-04] · `6256f98`


### 🔧Mantenimiento

- **machines,items**: Archivar elemento/máquina/ME Java (sin eliminar) + consumidores de código auxiliar
## [2026-06-03] · `7213cc6`


### ✨Añadido See More

- **waila**: Estadísticas de la máquina en vivo en HUD a través del motor compartido (Error 5)

### 🐛 Corregido See More

- **machines**: Break arroja un elemento de máquina personalizado, no el bloque básico
- **machines**: Persiste las ubicaciones para que las máquinas sobrevivan al reinicio (Error 3)
- **machines**: Un único motor compartido activa todas las máquinas (Error 4)

### ♻️ Modificado

- **machines**: Typed MachineContext + oyentes divididos (reescritura de la Sección 10)

---

## [2026-06-03] · `6d5654a`


### ✨Añadido See More

- **events**: Título de Groq por retador al aparecer el jefe
- **vip**: Alinee los kits VIP del juego con los niveles de la tienda web + entrega por cable
- Las redes **ae**: ME ahora realmente requieren energía
- **items**: Agregar categoría de elemento HERRAMIENTAS + actualizaciones de SubCategoryMatcher

### 🐛 Corregido See More

- Sistema **ae**: ME no funcional: ID de bloque en mayúsculas + materiales no funcionales
- **data**: Consolidar QUANTUM_STORAGE_CELL id + arreglar TOME_OF_ENLIGHTENMENT + mensaje de jefe

### 🔧Mantenimiento

- **lang**: Renombrar Arco de Sacrificio -> Arco de Desafío, Jefe de Anime -> Retador del Más Allá
## [2026-06-02] · `3ac9c37`


### ✨Añadido See More

- **twitch**: Comentarios visuales en el juego para eventos de sub/animación/incursión
- Registro **machines**: MachineComponent para anular el comportamiento de ID por máquina
- Sistema de impulso de XP global estilo SimpleXPBoosts
- Comportamiento de acción/disparador estilo ExecutableItems de **items**:
- **items**: /itemedit editor de elementos en vivo (inspirado en ItemEdit)
- **mmo**: Combinación de teclas en modo captura: presione una tecla para vincular una habilidad
- **events**: Realmente otorga bonificaciones MMO en recompensa de sacrificio

### 🐛 Corregido See More

- **items**: Eliminar definición ME_NETWORK_ACCESS_TERMINAL duplicada
- Cambio de nombre de carpeta de paquete de datos **advancements**: 1.21 + extracción con reconocimiento de versión
- **gui**: StatsGUI/KeyBindGUI se bloquea, questnpc UX, prefijo de guía del centro de comandos

### 🔧Mantenimiento

- Carpeta del complemento de referencia de Gitignore/inspirations

---

## [2026-06-02] · `d2ba3e7`


### ✨Añadido See More

- **discord**: Sistema de combate de bonificación de roles
- ConfigMigrator auto-merge + comando de migración MySQL (Fase 3)
- **mmo**: Rediseño de GUI inspirado en AuraSkills + HUD de enfriamiento de ataque
- **essentials**: El personal desaparece + recompensas por hitos del tiempo de juego

### 🐛 Corregido See More

- Conflictos de ME CMD, elementos faltantes de NETWORK_CAPACITOR, ID de recetas, ejecutor de combinación de teclas, circuitos.yml

### ♻️ Modificado

- **ae**: Rediseño de GUI de unidad/terminal ME + corrección de errores críticos

---

## [2026-06-02] · `19ac7e8`


### 🐛 Corregido See More

- Trabajos NPE + dejar UX, elementos ME, comando de combinación de teclas, argumentos del centro de comando
## [2026-06-01] · `f0cc6ca`


### ✨Añadido See More

- **mmo**: Sistema de daño de arma por elemento con seguimiento de proyectiles
- **advancements**: Sistema de avance personalizado mediante paquete de datos + activadores de complementos

---

## [2026-06-01] · `b86702c`


### ✨Añadido See More

- **quests**: Agregue sistema de misiones, otorgadores de NPC, GUI del centro de comando y expansión de combinación de teclas
- **discord**: Bot de Discord y actualizaciones de integración
- **energy**: Agregar componente generador creativo

### ♻️ Modificado

- **core**: Migrar recursos del complemento a datos/subcarpeta

### 🔧Mantenimiento

- Mejoras en la GUI, MMO, economía y otras mejoras en todo el módulo
- Eliminar archivos basura obsoletos, actualizar gitignore y actualizar CHANGELOG

---

## [2026-05-29] · `1985014`


### 🐛 Corregido See More

- **ci**: Fuerza PT-BR en el mensaje Groq, elimina las comillas circundantes de la respuesta

---

## [2026-05-29] · `7fcaa1d`


### 🐛 Corregido See More

- Mensaje AI **ci**: en portugués, muévase al contenido de arriba para insertar con formato de encabezado de Discord

---

## [2026-05-29] · `3d42824`


### 🐛 Corregido See More

- **discord**: Messages.yml se guardó en una ruta incorrecta, lo que provocó que todas las claves regresaran [Mensaje faltante]

---

## [2026-05-29] · `8709b16`


### ✨Añadido See More

- **ci**: Mensaje generado por IA a través de Groq en notificaciones de compilación de Discord

---

## [2026-05-29] · `8ba64aa`


### 🔧Mantenimiento

- **ci**: Avatar de robot aleatorio por compilación en notificaciones de Discord

---

## [2026-05-29] · `6b528c3`


### 🐛 Corregido See More

- **ci**: Ejecute pruebas en CI, elimine el flujo de trabajo de compilación redundante, agrupe el registro de cambios por tipo de confirmación

---

## [2026-05-28] · `b3be732`


### 🐛 Corregido See More

- **machines-gui**: Extraiga máquinas-gui.yml a la carpeta de datos al iniciar

---

## [2026-05-28] · `329fd92`


### 🐛 Corregido See More

- **gui**: Guía de navegación, diseño de recetas, rango de paginación

---

## [2026-05-28] · `ec4b039`


### ✨Añadido See More

- **api**: Expone campos colocables/multibloque, agrega VariantDefinition, corrige la referencia del tipo de máquina
- **machines**: Agregar niveles de expansión automática y subtipo de procesamiento al cargador de la máquina
- **plugin**: Fase 7: puente multibloque, actualizaciones del cargador DataDriven, cambios de nombre de ID de receta

### 🐛 Corregido See More

- **plugin**: El comando Give muestra nombres para mostrar, alternancia de mensajes de interrupción, registro de implementación de API

### 🔧Mantenimiento

- **items**: Fase 6: cambio de nombre masivo de _BLOCK, limpieza nativa de la máquina, variantes predeterminadas
- **plugin**: Actualizaciones de idioma/configuración: mensajes multibloque, alternancia de mensajes de interrupción, valores predeterminados económicos
- **modules**: Actualizaciones en economía, mmo, seguridad, eventos, interfaz gráfica de usuario, rasgos, discordia, web, ss, pestañas
- **ops**: Filtros Fail2ban y reglas de firewall para el bloqueo de atacantes y paquetes mal formados
## [2026-05-23] · `5cc6c1c`


### ✨Añadido See More

- **tab**: Agregar /nexus marcador alternar comando por jugador
## [2026-05-22] · `70a3df5`


### ✨Añadido See More

- **guide**: Fase 4 completa: recategorización masiva de 404 elementos + eliminación de 10 ID corruptos
- **machines**: Agregar campo de subtipo de procesamiento a MachineDefinition

### 🐛 Corregido See More

- **gui**: Desorden del diseño de la receta + código de color sin formato en el título
- **guide**: Ampliar los espacios de categoría a 28 y agregar paginación

### 🔧Mantenimiento

- **items**: Eliminar 31 SV_* heredados y duplicados de limo camelCase
- **guide**: Elimina 4 elementos auxiliares heredados de Slimefun + agrega 15 íconos de categorías faltantes

---

## [2026-05-22] · `3ceeabf`


### ✨Añadido See More

- **gui**: Agregue GUI de máquina de tipo específico y envío de cables

### 🐛 Corregido See More

- **gui**: Evite el robo de elementos de las GUI de habilidades/rasgos mediante orden de apertura → registro

### ♻️ Modificado

- **items**: Cambiar el nombre de la llave inglesa + infinity_crafting_* ID a mayúsculas
- **items**: Propagar nexus_crafting_node → NEXUS_CRAFTING_NODE cambiar nombre

### 🔧Mantenimiento

- **items**: Eliminar 85 elementos YAML heredados/duplicados (Fase 1)
- **items**: Cambiar el nombre de nexus_crafting_node_block → NEXUS_CRAFTING_NODE_BLOCK

---

## [2026-05-22] · `4172dec`


### ✨Añadido See More

- **modules**: Activación/desactivación por módulo mediante config.yml y GUI

---

## [2026-05-21] · `208b215`


### 🐛 Corregido See More

- **ci**: Pasa GH_PAT como entrada de token a action-gh-release

---

## [2026-05-21] · `a43cc50`


### 🐛 Corregido See More

- **ci**: Utilice GH_PAT para la creación de versiones (GITHUB_TOKEN no tiene acceso de escritura de organización)

---

## [2026-05-21] · `69ac4f3`


### 🐛 Corregido See More

- **ci**: Pase el registro de cambios a través de env var para evitar errores de sintaxis de bash

---

## [2026-05-21] · `cf363dd`


### 🐛 Corregido See More

- **ci**: Corrige 403 push, versiones de acción incorrecta y activadores de rama incorrectos

---

## [2026-05-21] · `e488545`


### 🔧Mantenimiento

- Se eliminó la lista de materiales al inicio del archivo.

---

## [2026-05-21] · `2f25103`


### ✨Añadido See More

- **plugin**: Fase 2 NexusLynxReporter: enviar latidos/registros/config a Railway
- Filtro **reporter**: REDACT + niveles de registro/alerta configurables
- **anti-dupe**: Prevención de engaños de ruptura de bloques en rng/mmo/traits

### 🐛 Corregido See More

- **reporter**: Ampliar el filtro REDACT para cubrir las URL de conexión JDBC
- **discord**: Traducir mensajes de estado del servidor al portugués

### ♻️ Modificado

- **config**: Centraliza todos los secretos en key_configs.yml
- **reporter**: Elimina el filtro por clave de pushConfig: key_configs.yml es el único archivo omitido
- **config**: Key_configs.yml solo contiene secretos: las claves no confidenciales se mueven a archivos de módulo

---

## [2026-05-14] · `bab3917`


### ✨Añadido See More

- **i18n**: Conecte LanguageManager a módulos de seguridad, protecciones y clanes
- **i18n**: Conecte LanguageManager a MachineManager, SilkSpawners, Twitch; agregue todas las claves de idioma nuevas a 4 configuraciones regionales
- **i18n**: Migrar gui/mmo/web/ae/energy/essentials/protections a LanguageManager
## [2026-05-13] · `3cfce4c`


### ✨Añadido See More

- **i18n**: Conecte TagGUI/RtpWorldGUI a LanguageManager + agregue LanguageSelectGUI

---

## [2026-05-13] · `2201b42`


### 📚 Documentación

- **config**: Anota key_configs.yml con la var env fuente para cada clave

---

## [2026-05-13] · `191f461`


### 🔧Mantenimiento

- **deps**: Mejora de acciones/carga de artefacto de 4 a 7
- Migrar referencias de organizaciones de O-Tiger a Tg-TheNexus
## [2026-05-02] · `ba0ebd5`


### 🔧Mantenimiento

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### ✨Añadido See More

- **logger**: Colorea las etiquetas del módulo por prefijo

### 🐛 Corregido See More

- Protocolo de actualización **deps**:Lib 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)
- **config**: Conecte todos los campos key_configs.yml a las configuraciones del módulo
- **machines**: Implementar TODOs obsoletos de MachineEngine
- **integrations**: Elimina el campo de complemento no utilizado y registra errores de LuckPerms

### 📚 Documentación

- Actualización README, CONTRIBUCIONES, CRÉDITOS, ECOSISTEMA
- Agregue ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

### 🔧Mantenimiento

- Simplifique el registro de inicio, elimine ProGuard, reduzca el ruido del Dependabot
- **deps**: Acciones de mejora/carga de artefacto de 4 a 7
- Se agregó una advertencia al personal sobre Pr de riesgo medio.

### 🔧Mantenimiento

- **dependabot**: Clasificación de riesgo + PR de bajo riesgo de cierre automático
## [2026-05-12] · `13f15da`


### 🔧Mantenimiento

- Carácter BOM despojado
## [2026-05-11] · `bcdd189`


### ✨Añadido See More

- **events**: Agregue 6 jefes de anime, cambie el nombre de isekai → anime, AddonLoader, corrección de BOM

### 🐛 Corregido See More

- **tools**: Clasifique los 2696 elementos: expanda CMD_MODULES, agregue estilos de categoría MÁGICO/SEED/MOB; regenerar todos los lotes rápidos
## [2026-04-29] · `bbac1d1`


### 📚 Documentación

- Actualizar CONFIGURACIONES: sección key_configs.yml, sección de lista negra, claves nexus-lynx/nexus-bot
## [2026-04-28] · `40babb7`


### ✨Añadido See More

- **security**: Lista negra de autenticación + archivo de credenciales central KeyConfig

### 🐛 Corregido See More

- **chat**: Extracto finalReason para la captura lambda en MuteCommand

---

## [2026-05-02] · `ba0ebd5`


### 🔧Mantenimiento

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### 🔧Mantenimiento

- Se agregó una advertencia al personal sobre Pr de riesgo medio.

---

## [2026-05-13] · `9479dbc`


### 🔧Mantenimiento

- **dependabot**: Clasificación de riesgo + cierre automático de relaciones públicas de bajo riesgo

---

## [2026-05-13] · `f22c9c1`


### 📚 Documentación

- Agregue ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

---

## [2026-05-13] · `f5aa66a`


### 🐛 Corregido See More

- **config**: Conecte todos los campos key_configs.yml a las configuraciones del módulo
- **machines**: Implementar TODOs obsoletos de MachineEngine
- **integrations**: Elimina el campo de complemento no utilizado y registra errores de LuckPerms

### 📚 Documentación

- Actualización README, CONTRIBUCIONES, CRÉDITOS, ECOSISTEMA

---

## [2026-05-13] · `552aa62`


### ✨Añadido See More

- **logger**: Colorea las etiquetas del módulo por prefijo

---

## [2026-05-13] · `c5966c3`


### 🐛 Corregido See More

- Protocolo de actualización **deps**:Lib 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)

---

## [2026-05-13] · `74b3432`


### 🔧Mantenimiento

- Simplifique el registro de inicio, elimine ProGuard, reduzca el ruido del Dependabot

---

## [2026-05-12] · `13f15da`


### 🔧Mantenimiento

- Carácter BOM despojado

---

## [2026-05-11] · `bcdd189`


### 🐛 Corregido See More

- **tools**: Clasifique los 2696 elementos: expanda CMD_MODULES, agregue estilos de categoría MÁGICO/SEED/MOB; regenerar todos los lotes rápidos

---

## [2026-05-11] · `7ac6735`


### ✨Añadido See More

- **events**: Agregue 6 jefes de anime, cambie el nombre de isekai → anime, AddonLoader, corrección de BOM

---

## [2026-04-29] · `bbac1d1`


### 📚 Documentación

- Actualizar CONFIGURACIONES: sección key_configs.yml, sección de lista negra, claves nexus-lynx/nexus-bot
## [2026-04-28] · `40babb7`


### ✨Añadido See More

- **security**: Lista negra de autenticación + archivo de credenciales central KeyConfig

### 🐛 Corregido See More

- **chat**: Extracto finalReason para la captura lambda en MuteCommand

---

## [2026-04-26] · `792efb0`


### ✨Añadido See More

- **discord**: Reenviar eventos de moderación a nexus-bot /api/moderation a través de HTTP

### 🔧Mantenimiento

- Agrega .rtk/ a gitignore

---

## [22/04/2026] · `3782900`


### ✨Añadido See More

- **web**: Reemplazar el receptor HTTP entrante con sondeo saliente

---

## [22/04/2026] · `762a968`


### 📚 Documentación

- Corregir la ruta de configuración de autenticación, agregar la sección canales.yml, expandir la lista de verificación

---

## [2026-04-21] · `984477f`


### 🔧 Mantenimiento

- Agregue la entrada del canal de seguridad comentada a los canales predeterminados.yml

---

## [2026-04-21] · `ddb3481`


### 🔒Seguridad

- Alerta de Discord de sesión corta por cable + agregar runbooks de operaciones/DDoS

---

## [2026-04-20] · `b322900`


### 🐛 Corregido See More

- **auth**: Omitir la autenticación de Java para reproductores Bedrock/Floodgate

### 🔒Seguridad

- Refuerzo de bot/escáner: detección de sesiones cortas, puerta de confianza automática de IP, corrección de sesión de Postgres

---

## [2026-04-20] · `a998d1f`


### 📚 Documentación

- Agregar referencia web/web-config.yml + registro de cambios de refuerzo de seguridad

---

## [2026-04-18] · `7f36abc`


### 🔒Seguridad

- Persistencia de clave AES-CBC, autenticación secreta del receptor, validación del nombre del jugador, columnas de sesión

---

## [2026-04-12] · `f52f78d`


### ✨Añadido See More

- Manejo de eventos IRC **twitch**:, recompensas de sub/animación/incursión, puerta de rifa clave
- Punto final **web**: TwitchEventReceiver para la integración del Stream Panel
- Comando **essentials**: RTP con GUI de selector mundial

### 🐛 Corregido See More

- **security**: Confirmación premium FastLogin + refuerzo de autenticación

### 🔧Mantenimiento

- **data**: Actualizaciones YAML de artículo/máquina/receta + cableado de complementos
## [2026-03-24] · `cc57494`


### ✨Añadido See More

- **fastlogin**: Scaffolda módulo nexusprism-fastlogin con autenticación premium a través de ProtocolLib

### 🐛 Corregido See More

- **mmo/segurança/encantamentos**: Corrige mensajes MMO, verificación premium y Auto Smelt
- **lang**: Mover mmo para nivel raíz de YAML (estava aninhado em economía)
- **plugin**: califica ProtectionHandler como MachineManager.ProtectionHandler
- **fastlogin**: Sustituye el protocolo de enlace RSA/AES por búsqueda en el nombre sincronizado→UUID
- **fastlogin**: Injeta UUID vía reflexão de campo (compatível Spigot e Paper)
- **fastlogin**: Injeta UUID a través de PlayerProfile en Paper, reflejo de campo en Spigot

### 🔧Mantenimiento

- Se movió el mensaje de bloqueo mmo anidado a la raíz.

---

## [2026-03-24] · `94b05a7`


### 🐛 Corregido See More

- **items**: Adiciona _templates.yml con item_template base para data/items/
- **data**: Corrección de errores de inicialización del servidor
- **items**: Corrige conflictos de CMD dos artículos comprimidos (30000-30002)

### 🔧Mantenimiento

- Corrección de escape inválido '\$" para "$"

---

## [2026-03-24] · `39476a5`

### ✨ Añadido

- **research**: Sistema de árbol de investigación basado en `researches.yml` — las entradas tienen tier (BASIC/ADVANCED/INFINITY), costo en pergaminos, dependencias y desbloqueos
- **research**: Progreso de investigación persistido en SQLite, MySQL y YAML
- **guide**: Las recetas de la Infinity Table ahora se registran automáticamente en la guía del juego
- **machines**: VOID_COLLECTOR_BLOCK y VOID_SMELTER_BLOCK añadidos (tier Infinity)
- **items**: SIGNALUM_INGOT y COMPRESSED_DIAMOND añadidos a items.yml
- **discord**: ConsoleLogHandler — reenvía la salida de la consola del servidor a un canal de Discord
- **guide**: Los íconos de categoría y tier de la guía ahora son configurables mediante `gui_items.yml`; los desarrolladores de addons pueden registrar íconos de categoría personalizados sin modificar Java

### 🔧 Mantenimiento

- **config**: Todos los archivos de datos reestructurados bajo la jerarquía `data/` (`data/items/`, `data/machines/<tier>/`, `data/crafting/`, `data/smelting/`, `data/crafting/infinity_table/`)
- **config**: Archivos `items.yml`, `machines.yml` y `recipes.yml` en la raíz eliminados — reemplazados por la estructura `data/`
- **recipes**: Las recetas de máquinas ahora se definen en línea dentro del bloque de la máquina bajo la clave `recipes:`
- **recipes**: El prefijo `nexus:ITEM_ID` ahora está soportado en todos los archivos YAML de recetas para referenciar ítems personalizados

### 🐛 Corregido

- **storage**: Claves de configuración renombradas de `storage.*` a `database.*` para coincidir con `config.yml`
- **storage**: La migración de MySQL < 8 (`ALTER TABLE ADD COLUMN`) ya no usa `IF NOT EXISTS` — captura el código de error 1060
- **research**: ResearchManager ahora se recarga correctamente con `/nexus reload`

### ⚖️ Legal

- Licencia cambiada de MIT a propietaria — Todos los derechos reservados

---

## [22/03/2026] · `7260628`


### 🔧Mantenimiento

- **release**: Agregar versión de entradas y lista de cambios a flujo de trabajo_dispatch

---

## [22/03/2026] · `1a79a0f`


### ✨Añadido See More

- **tab,protections,essentials**: Animações nomeadas, ordenação por grupo, GUI de banderas, casas dinámicas

---

## [2026-03-22] · `5b49358`


### ✨ Añadido

- **discord,events**: GamePresence TYPE|texto, probabilidad de Blood Moon, incrustaciones de muerte/logro

### 🐛 Corregido

- **enchantments**: Agregar dependencia nexusprism-core para LanguageManager
- **tab**: Parámetro corregido ausente en el constructor TabCommand

### 📚 Documentación

- Actualización del registro de cambios, configuraciones y marcadores de posición (22/03/2026)

### 🔧 Mantenimiento

- Modificación general: LanguageManager integrado en todos los módulos

---

## [2026-03-21] · `83b864b`


### 🔧 Mantenimiento

- Se agregó la opción de votación del servidor para restablecer el servidor MC. Basado en el trabajo de gnomomuitoloco (en Discord)

## [2026-03-20] · `e6356c5`


### ✨ Añadido

- **discord,integrations**: Agregar control de panel, votación de servidor y proveedores PAPI

---

## [2026-03-19] · `bb5ecb9`


### ✨ Añadido

- **energy**: Exponer API de energía mediante EnergyProvider/EnergyRegistry
- **addon-example**: Agregar ejemplo de uso de EnergyRegistry

### 🐛 Corregido

- **economy**: Usar campo público def.id en lugar del inexistente getId() en JobProviderImpl
- **protections**: Usar Region.getFlag(RegionFlag) y API DuelManager correctos en ProtectionsProviderImpl
- **providers**: Corregir HologramLine, BloodMoonManager.getWorldName y verificación de mundo en EventsProviderImpl
- **plugin**: Resolver errores de compilación en BackpackProviderImpl y MachineRegistrarImpl

---

## [2026-03-19] · `1875bb0`


### 🐛 Corregido

- **chat**: Usar los nombres correctos de métodos ChannelRegistry y ChatChannel en ChatProviderImpl

---

## [2026-03-19] · `55c634e`


### ✨ Añadido

- **security**: Verificación premium basada en UUID con caché persistente
- **events**: Comando admin /isekai con inicio forzado y selección de jefe
- **mmo**: Sistema dinámico de coste de maná y nueva habilidad de doble hoja
- **mmo**: Sistema de asignación de teclas de habilidades con GUI y atajos en el juego
- **api**: Agregar 9 interfaces de proveedor, registros y MachineProcessingRegistry
- **modules**: Cablear proveedores en constructores de módulos y paradas
- **machines**: Conectar MachineProcessingRegistry al MachineEngine
- **addon-example**: Agregar proyecto de plantilla pública con README y flujo de publicación
- **api**: Agregar cargador de contenido, registro de recetas infinitas e interfaces de registro de máquinas

### ♻️ Modificado

- Renombrar nexusslime → nexusprism en todas las capas

### 🔧 Mantenimiento

- Refactorizando todas las referencias de nexusslime a nexusprism
- Se corrigió el job de notificación en el flujo de trabajo dependabot-discord. Causa raíz: mis células cerebrales olvidaron agregar los secretos del dependabot

## [2026-03-18] · `ca5db45`


### ✨ Añadido

- **security**: Mobs nivelados y mejoras en el apilador de mobs
- **economy**: Jobs, tienda, casa de subastas y warps de jugadores
- **events**: Blood Moon, Arco del Sacrificio y sistema de Jefe Isekai
- **mmo**: Estadísticas, árboles de habilidades, habilidades, profesiones y sistema de maná

### 🐛 Corregido

- **tab**: Corregir los valores predeterminados de configuración del TAB

### 🔧 Mantenimiento

- Se agregó un respaldo para evitar falsos positivos al iniciar sesión/registrarse
- Registrar módulos Events y MMO, renombrar el plugin a NexusPrism

## [2026-03-16] · `cc4853a`


### 🔧 Mantenimiento

- Se agregaron marcadores y personalizaciones de MOTD al módulo TAB
- Se agregó forge/neoforge a la lista de vigilancia para evitar explotadores, mayor tiempo para limpiar el mundo y verificación de jugadores. Si no se encontró ninguno, se omite la limpieza

## [2026-03-10] · `a92e2ee`


### 🔧 Mantenimiento

- Se agregó soporte jitpack a la API
- Actualizado jitpack.yml para forzar el uso de maven 3.9
- no sé
- Corrección menor: agregar definición yaml al bloque de código

## [2026-03-09] · `e5a7a7f`


### 🔧 Mantenimiento

- Se ha mejorado el flujo de autenticación, verificando ahora el tipo de cuenta (premium o crackeada) y las IP asociadas. Para el primer acceso, un administrador deberá otorgar confianza a la IP.

## [2026-03-08] · `6676d8d`


### 🔧 Mantenimiento

- Agregar módulo de hologramas, detector de mod/mineral, antilag configurable y mejoras de spawner.
- Referencias de crédito eliminadas (no es un servidor p2w)

## [2026-03-04] · `b9749a0`


### 🔧 Mantenimiento

- Flujo de autenticación mejorado para detectar también IP y bloquear las no reconocidas
- Nuevas correcciones conectadas para flujos de autenticación y seguridad

## [2026-03-02] · `e5562d2`


### 🔧 Mantenimiento

- Archivos de documentación actualizados
- Se agregó soporte para SkinsRestorer a las cuentas premium; las crackeadas deben usar comandos.
- Olvidé agregar los archivos al .gitignore

## [2026-03-01] · `f5f4ee5`


### 🔧 Mantenimiento

- Se cambió el flujo de autenticación a basado en mapas

## [2026-02-28] · `bfc7f2f`


### 🔧 Mantenimiento

- Bump actions/upload-artifact de 6 a 7 en el grupo gha-major
- Flujo de autenticación mejorado: ahora se basa en sesiones, tiempo predeterminado 2 horas

## [2026-02-27] · `4b773aa`


### 🔧 Mantenimiento

- Añadido:
- registro de cambios agregado

## [2026-02-26] · `8d8020d`


### 🔧 Mantenimiento

- Actualizados algunos archivos
- Poms.xml actualizado de cada módulo
- Módulo de protecciones mejorado para ser como RedProtection. También agregué algunos de mis proyectos antiguos, como el boss Echoes y la experiencia de ensueño
- Eliminada completamente la antigua dependencia del nuvotifier y agregada una imagen pública como avatar del flujo de trabajo
- Se corrigió sed que causaba que la URL tuviera un formato incorrecto
- Se agregó soporte para ejecutar acciones desde Discord

## [2026-02-25] · `9b39ccd`


### 🔧 Mantenimiento

- Se corrigió la descarga de importación de nuvotifier maven, agregándola localmente
- Crear SECURITY.md
- Votificador deshabilitado por ahora. Planificando agregar nuevamente, pero como código interno, no solo como una llamada API.
- Me olvidé de la dependencia
- Votificador desactivado en Nexus.....

### 🔧 Mantenimiento

- Se agregó compatibilidad con emoji al módulo de chat; ahora será posible mencionar a alguien entre discord <-> minecraft, usando sus nombres actuales en cada plataforma. El usuario mencionado debe estar verificado en el servidor de Discord para recibir una notificación. Se agregaron claves de idioma a los nuevos módulos.

## [2026-02-24] · `6b1c020`


### 🔧 Mantenimiento

- Bump org.postgresql:postgresql de 42.7.4 a 42.7.7

## [2026-02-23] · `93ac56c`


### 🔧 Mantenimiento

- Se agregó formateador de chat y redirecciones de canales
- Flujo de trabajo dependabot-discord actualizado
- Se agregó soporte de crafteo múltiple para tiers de ítems infinitos
- Cambiado a payloads jq para un uso más seguro
- Corregir la sangría en README y deshacer los cambios de merge pull del dependabot (provoca incompatibilidad)

## [2026-02-21] · `265156e`


### 🔧 Mantenimiento

- Bump com.sk89q.worldguard:worldguard-bukkit

## [2026-02-11] · `7681a88`


### 🔧 Mantenimiento

- Tienda web vinculada con el módulo nexusslime-web. Mejorado aún más el módulo discord, permitiendo configuraciones a través de archivos yml.

## [2026-02-07] · `1600a94`


### 🔧 Mantenimiento

- Bump del grupo maven-major en 1 directorio con 2 actualizaciones

## [2026-02-04] · `7dc0811`


### 🔧 Mantenimiento

- Implementación de la API de Discord

## [2026-01-28] · `955cfc5`


### 🔧 Mantenimiento

- Pruebas de integración de Discord

## [2026-01-20] · `fe77e92`


### 🔧 Mantenimiento

- Actualizar plantillas de issues
- ItemYamlLoader: admite plantillas con nombre

### 🔧 Mantenimiento

- Evitar la descarga de ProtocolLib durante la compilación (opcional en tiempo de ejecución)

## [2026-01-19] · `06bbb4b`


### 🔧 Mantenimiento

- Flujos de trabajo actualizados y agregado CONTRIBUTING.md

## [2026-01-18] · `7d5b8ab`


### 🔧 Mantenimiento

- .gitignore actualizado
- Flujo de trabajo release.yml actualizado

## [2026-01-17] · `3fcae81`


### ✨ Añadido

- Implementar máquinas de procesamiento escalonado e infraestructura de sistemas principales

### 🔧 Mantenimiento

- Creados flujos de trabajo para compilaciones y lanzamientos
- release.yml actualizado
- Bump del grupo gha-major con 3 actualizaciones
- No sé, me perdí algunos campos en la notificación de Discord

## [2026-01-16] · `5771bc7`


### 🔧 Mantenimiento

- Confirmación inicial — Marcadores de posición de ítems funcionando

---

## [2.0.0-BETA] — Lanzamiento Inicial

### ✨ Añadido

- Reescritura completa como un **proyecto Maven multi-módulo con +25 módulos**
- Nuevo módulo `nexusprism-api` que proporciona una API pública para desarrolladores de addons
- Todos los sistemas de funciones ahora son módulos independientes con su propio ciclo de vida
- Migración de persistencia YAML a **SQLite / PostgreSQL** mediante `nexusprism-storage`
- `CustomItemRegistry` con etiquetado de ítems via PDC (`nexusprism:id`)
- 500+ ítems basados en datos definidos en `items.yml`
- Sistema de tier de ítems: Básico → Avanzado → Infinito
- Árbol de investigación con desbloqueos por XP
- Soporte multi-idioma: Inglés, Portugués Brasileño, Español, Chino Simplificado
- **nexusprism-essentials** — 40+ comandos QoL (homes, warps, TPA, AFK, prisión, utilidades)
- **nexusprism-economy** — Sistema de moneda dual, `/sell`, `/baltop`, precios de venta configurables
- **nexusprism-clans** — Reclamación de territorio, árbol de mejoras, cofre de clan, chat de clan
- **nexusprism-security** — Autenticación BCrypt, anti-bot CAPTCHA, detección de VPN, anti-lag, anti-dupe
- **nexusprism-discord** — Bot JDA, vinculación de cuentas, sincronización de roles, webhooks
- **nexusprism-crystaldefense** — Minijuego cooperativo por oleadas
- **nexusprism-votifier** — Servidor Votifier V1/V2 independiente con rachas y clasificación
- **nexusprism-dreams** — Sistema de cinemática al dormir (sueños y pesadillas)
- **nexusprism-protections** — Reclamación de regiones, flags, sistema de duelo 1v1
- **nexusprism-custommobs** — Jefes definidos en YAML con formas de IA y tablas de botín
- **nexusprism-twitch** — Vinculación de cuenta, alertas en vivo, relay de chat, sorteos
- **nexusprism-ae** — Almacenamiento en red ME (estilo Applied Energistics)
- **nexusprism-energy** — Generación de energía y redes de cables
- **nexusprism-chat** — Chat de 4 canales (global, local, staff, comercio) con moderación
- **nexusprism-events** — Luna de Sangre, Arco del Sacrificio y sistema de Jefe Isekai
- **nexusprism-mmo** — Estadísticas, árboles de habilidades, habilidades, profesiones y sistema de maná
- **nexusprism-tab** — Encabezado/pie de página de la lista TAB personalizado con prefijo LuckPerms
- **nexusprism-holograms** — Hologramas de texto flotante basados en YAML
- **nexusprism-traits** — Sistema de traits con cartas de Tarot e integración con economía
- **nexusprism-rng** — Ruleta diaria, bloques de suerte, gacha, niveles de investigación
- **nexusprism-crates** — Cofres de botín con apertura animada y llaves
- **nexusprism-enchantments** — 175 encantamientos personalizados (6 rarezas, 10 tipos de activación)
- **nexusprism-structures** — Inyección de botín en estructuras (11 estructuras vanilla + API de addon)
- **nexusprism-waila** — Tooltips de máquinas WAILA/HUD
- **nexusprism-web** — Bridge de tienda web, kits VIP, procesamiento de pagos, RGPD
- **PlaceholderAPI** — 14 proveedores, 30+ placeholders en todos los módulos
- **LuckPerms** — Permisos y placeholders basados en grupo
- `MachineYamlLoader` — máquinas definidas en `machines.yml`, sin necesidad de Java
- `MachineEngine` — procesamiento asíncrono de máquinas
- Estaciones de crafteo multibloques con formato de receta YAML (`infinity_recipes/`)
- Generadores de energía: Paneles Solares, Generadores de Carbón
- Transporte de energía por cables con pérdida configurable por bloque
