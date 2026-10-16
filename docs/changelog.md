# Changelog

> Auto-generated from [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism) commits.
> Translated automatically — minor phrasing differences are expected.

---

## [2026-10-16] · `4a62e51`


### 🐛 Fixed

- **ci**: Skip the Discord notices when the webhook secret is empty (Dependabot runs) (#64)

---

## [2026-10-16] · `2acbad9`


### 📚 Documentation

- Session summary reflects the follow-up fixes (#62)

---

## [2026-10-16] · `447b0d4`


### 🔧 Maintenance

- **deps**: Keep dependabot away from log4j (provided by the server) (#60)

---

## [2026-10-16] · `04b94fb`


### 🐛 Fixed

- **auth**: Prune old name and IP records and uncollected notifications in UUIDConflictResolver (#59)

---

## [2026-10-16] · `396a934`


### 🐛 Fixed

- **auth**: Validate names before the Mojang lookup, shorten demotions, log close errors (#58)

---

## [2026-10-16] · `44787b3`


### 📚 Documentation

- Session summary 2026-10-16 (#57)

---

## [2026-10-16] · `96d8c8c`


### 🐛 Fixed

- **auth**: Mask passwords in logs, BCrypt off the main thread, pre-auth restrictions, per-address lockouts, IP whitelist actually enforced (#55)

---

## [2026-10-16] · `d066a4d`


### 🐛 Fixed

- **auth**: Bind persistent sessions to the IP and review the identity settings at startup (#54)

---

## [2026-10-16] · `e1085d5`


### ✨ Added

- **security**: Trusted test accounts skip the CAPTCHA by name and IP (#53)

---

## [2026-10-14] · `fefe853`


### ✨ Added

- **supporters**: Supporter-pass SKU and the nxsupporter command (#52)

---

## [2026-10-14] · `64bc66f`


### ✨ Added

- **store**: Cosmetic-only default sku-map and supporter titles (#51)

---

## [2026-10-14] · `41a480b`


### 📚 Documentation

- How to turn the delivery bridge on in a server (#50)

---

## [2026-10-14] · `abfc6dc`


### 🐛 Fixed

- **delivery**: Bind timestamptz values when marking an order delivered (#49)

---

## [2026-10-14] · `222e5f3`


### ✨ Added

- **delivery**: Bridge database from key_configs, fix item keys, unmapped skus and mark-delivered path (#48)

---

## [2026-10-14] · `2aa89fa`


### 🐛 Fixed

- **web**: Unify the lynx address and move the webhook secret to key_configs

### 🔧 Maintenance

- Rename GitHub org to Tg-TheNexus
- Rename org to Tg-TheNexus and unify lynx and webhook config keys (#47)

## [2026-10-03] · `780b8af`


### 🔧 Maintenance

- **config**: Point defaults at the nexusheim.com hosts

---

## [2026-09-28] · `c392ae4`


### 🐛 Fixed

- **ci**: Drop dev branch trigger, NexusPrism doesn't use one

---

## [2026-09-28] · `3b2579e`


### 🐛 Fixed

- **ci**: Don't fail the whole build when artifact upload hits storage quota

---

## [2026-09-28] · `60616b0`


### 📚 Documentation

- **changelog**: Note the link/linkstreamer split

---

## [2026-09-28] · `2d9c95d`


### ✨ Added

- **twitch**: Split /twitch link into /twitch link and /twitch linkstreamer

---

## [2026-09-27] · `18cd012`


### 🐛 Fixed

- **events,quests**: Raise Groq max_tokens for gpt-oss-120b's reasoning overhead

---

## [2026-09-27] · `037e895`


### 🐛 Fixed

- **events,quests**: Groq/compound-mini was also removed from Groq's catalog

---

## [2026-09-26] · `4b18be4`


### 🐛 Fixed

- **events,quests**: Replace deprecated Groq model in BossTitle/DailyQuests

---

## [2026-09-23] · `17c3478`


### ✨ Added

- **economy**: Publish vanilla sell-prices to shared DB for nexus-bot's /market

---

## [2026-08-09] · `632d673`


### 🔧 Maintenance

- **deps**: Bump postgresql JDBC driver 42.7.11 -> 42.7.12

---

## [2026-08-09] · `9f261ed`


### ✨ Added

- **economy**: Add polling-based currency bridge
- **discord**: Mirror account links to nexus-bot

### 🐛 Fixed

- **config**: Remove dangling structures/research entries

---

## [2026-08-06] · `ab72213`


### ✨ Added

- **events**: Externalize hardcoded gameplay balance to config

### 🐛 Fixed

- **security**: Scrub real IP/username from javadoc example, remove hardcoded nexus-bot fallback URL

### ♻️ Changed

- **core**: Remove confirmed-dead item/machine/energy/research domain

### 📚 Documentation

- Update reference docs to match current module/API surface

---

## [2026-07-11] · `36e78ff`


### 🐛 Fixed

- **waila**: Extract formatSnakeName for EntityType string, fix compile error

## [2026-07-10] · `0d08f3e`


### ✨ Added

- **waila**: Entity detection and rarity-based coloring

---

## [2026-07-09] · `0283136`


### ✨ Added

- **mmo**: Add NexusATS hook surface (T1 wired, T2/T3 stubs)

### 🐛 Fixed

- **lang**: Remove duplicate YAML keys in en_US and pt_BR

## [2026-07-06] · `32d26d9`


### ✨ Added

- **discord**: Group bulk delete notifications with 1s debounce
- **discord**: Bidirectional mention resolution — @@ MC→Discord, # Discord→MC

### 🐛 Fixed

- **discord**: Webhook takes priority for player messages, JDA for system messages — prevents duplicate posts
- **discord**: Load all guild members on ready + fix mention actionbar
- **mmo**: Restore MmoListener deleted by mistake in slimefun extraction

### ♻️ Changed

- **discord**: Delete dead DiscordChatListener, remove misleading chat.webhookUrl comment
- **discord**: Remove legacy @PlayerName→Discord mention resolution

### 📚 Documentation

- **discord**: Clarify default channel needs JDA id for Discord→MC relay

### 🔧 Maintenance

- **config**: Remove dead sections, fix module list
- **discord**: Remove dead chat-webhook key from key_configs.yml

---

## [2026-07-03] · `ef78584`


### 🔧 Maintenance

- **ci**: Remove validate_items step moved to NexusATS

---

## [2026-07-03] · `2786877`


### ♻️ Changed

- **events**: Rename Sacrifice Arc to The Convergence across all lang files and code

---

## [2026-06-19] · `d04c992`


### ✨ Added

- **integration**: Add NexusATS hook surface for machine block and Waila wiring

---

## [2026-06-19] · `06bfe20`


### ✨ Added

- **waila**: Add vanilla block recognition

### 🐛 Fixed

- **startup**: Reduce log verbosity and fix duplicate prefix and color leaks
- **twitch**: Stop reconnecting after 3 consecutive IRC failures

### ♻️ Changed

- **slimefun**: Extract machines, energy, items, ae to future NexusItems plugin

## [2026-06-17] · `ce58736`


### ✨ Added

- **machines**: Add YAML-driven multiblock machine system

### 🐛 Fixed

- **items**: Rename bare alloy items to _INGOT suffix and remove PAPER placeholders

## [2026-06-16] · `cfd4b44`


### 🐛 Fixed

- **recipes**: Shapeless ENHANCED_CRAFTING ingredients parsed as section not string list

### ♻️ Changed

- **machines**: Replace Enhanced Crafting Table machine block with Slimefun-style multiblock
- **machines**: Rewrite Enhanced Crafting Table to true Slimefun-style multiblock

### 🔧 Maintenance

- **items**: Replace nexus:COPPER_INGOT with vanilla COPPER_INGOT
- **items**: Fix categorization — rename raw ores, remove vanilla duplicates, fix alloy/plate matching
- **items**: Rename DUST_AMETHYST/DUST_NETHERITE to consistent *_DUST convention

## [2026-06-15] · `dd8cee0`


### ✨ Added

- **machines**: Add Enhanced Crafting Table machine and recipe system

### 🐛 Fixed

- **machines**: Resolve MachineCatalog ENHANCED_CRAFTING_TABLE item-entry warning
- **machines**: Fix ENHANCED_CRAFTING_TABLE MachineCatalog warning

### ♻️ Changed

- **recipes**: Migrate all plugin crafting recipes to Enhanced Crafting Table

## [2026-06-14] · `f52e15d`


### 🐛 Fixed

- **machines**: Resolve 3 MachineCatalog cross-layer warnings
- **machines**: Remove duplicate HOLOGRAM_PROJECTOR stub from basic_machines.yml

---

## [2026-06-14] · `a434364`


### ✨ Added

- **crafting**: Add recipes for 37 previously uncraftable items

### 🐛 Fixed

- **items**: Move SINGULARITY_CONSTRUCTOR to nexus_machines.yml; add machine def + singularity recipes

---

## [2026-06-14] · `76b04ab`


### ✨ Added

- **crafting**: Add infinity recipe chain in Infinity Table

### 🐛 Fixed

- **events**: Register missing 6 challenge bosses in DEFAULT_BOSS_FILES

### ♻️ Changed

- **crafting**: Migrate infinity gear to Infinity Table; fix INFINITY_APPLE

---

## [2026-06-14] · `8b862fc`


### ✨ Added

- **items/tinkers**: Add TINKERS category, migrate 137 CAST items, fix INGOT_FORMER to MACHINE
- **tools,ci**: Add validate_items.py (CMD conflicts + category rules) and wire into CI

### 🐛 Fixed

- **mmo**: Guard null customName() before ConcurrentHashMap.putIfAbsent in MobHealthDisplay

### ♻️ Changed

- **lang**: Rename security.world-cleaner lang keys and sync lang files
- **events/challenge**: Add display CMDs to boss YAMLs, update ChallengeBoss classes
- **items/cobblestone**: Replace 5-tier COMPRESSED_COBBLESTONE with 8 explicit items (x9..x43M), remove COBBLE_1-5 duplicates and stale machine GUIs

### 🔧 Maintenance

- **tools**: Remove stale rp_prompts artifacts, allow tools/*.py in gitignore
- **items**: Assign missing CMDs to ITEM_BAND and NETWORK_POWER_DISPLAY variants in gear.yml

## [2026-06-09] · `ca942b3`


### 🐛 Fixed

- **events**: Rename challenge_bosses JAR resource dir (was anime_bosses)
- **energy,ae**: Consumer bridge + ME terminal insert feedback

### ♻️ Changed

- **lang**: Migrate hardcoded messages to lang keys (batch 1)
- **lang**: Migrate nexusprism-plugin hardcoded strings to lang keys
- **lang**: Replace all § literals with & in lang files
- **lang**: Migrate remaining nexusprism-plugin strings to lang keys
- **lang**: Migrate strings in events/mmo/rng/security/discord/quests to lang keys
- **lang**: Migrate remaining § strings in chat/core/crates/mmo/machines/enchants to lang keys and ChatColor

## [2026-06-08] · `d1b12d2`


### ✨ Added

- **items,ae**: Hammer tiers, AE2 byte capacity, ME persistence fix
- **vfx,mmo,crates**: VFXUtil, mob health nameplates, ability VFX, crate VFX

### 🐛 Fixed

- **machines**: Exempt energy infrastructure from catalog GUI-layer check
- **ae,gui,energy**: AE status lang keys, colorize GUI lore, creative gen buffer
- **ae,gui,commands**: Glass cable channels, creative GUIs, give tab-completion
- **ae**: Controller provides 8 base channels so cable-less networks work
- **mmo**: Fix action bar conflict between HUD and XP notification

### ♻️ Changed

- **display**: Centralize action bar through ActionBarManager
- **events**: Rename anime package and classes to challenge
- **events**: Finish anime→challenge rename across docs, lang, and resources

### 🔧 Maintenance

- **cleanup**: Delete archived copies and remove stale CUT banners
- **cleanup**: Remove remaining stale CUT banners and update example/crates

## [2026-06-07] · `c2888ce`


### 🐛 Fixed

- **machines**: Skip template/fields keys in loader; drop obsolete generated items file
- **items**: Propagate placeable via templates + prune duplicate generated machine items
- **machines**: Add CREATIVE_CAPACITOR STORAGE behavior def
- **machines**: Add ADVANCED generators + ELECTRIC_BLAST_FURNACE, align FAL/MOB ids

## [2026-06-06] · `e7a40f7`


### ✨ Added

- **api**: Rebuild item/machine/recipe API surface
- **core**: PDC-backed MachineManager + item registry/resolvers
- **machines**: Typed engine, registry, definitions, loader + catalog validator
- **ae**: Rebuild ME network as MachineContext-driven machines
- **storage**: Persist machine placements via DataManager (SQLite/MySQL/YAML)
- **machines**: Plugin glue, split listeners, GUI handler, loaders, wiring
- **recipes**: Migrate ME network, storage cell + backpack crafting to YAML
- **machines**: Make every machine obtainable + give type-based GUIs
- **energy**: Infinite CREATIVE_CAPACITOR + only tick engine-handled blocks
- **energy**: Bridge engine generators into cable network + export-mode toggle

### 🐛 Fixed

- **machines**: Rename CRUSHER gui key to ORE_CRUSHER; dedup CREATIVE_CAPACITOR
- **items**: Merge stray CREATIVE_GENERATOR_BLOCK into CREATIVE_GENERATOR

### ♻️ Changed

- **energy,mmo,systems,items**: Rewire consumers to new item/machine API
- **machines**: Merge generated items into machine_blocks + subtype-aware GUIs

### 📚 Documentation

- **recipes**: Document hardcoded RecipeLoader to YAML migration gaps
- **recipes**: Mark ME/storage-cell/backpack recipes as migrated

### 🔧 Maintenance

- Updated gitignore

## [2026-06-04] · `6256f98`


### 🔧 Maintenance

- **machines,items**: Archive item/machine/ME Java (no delete) + stub consumers

## [2026-06-03] · `7213cc6`


### ✨ Added

- **waila**: Live machine stats in HUD via shared engine (Bug 5)

### 🐛 Fixed

- **machines**: Break drops custom machine item, not the vanilla block
- **machines**: Persist placements so machines survive restart (Bug 3)
- **machines**: Single shared engine ticks all machines (Bug 4)

### ♻️ Changed

- **machines**: Typed MachineContext + split listeners (Section 10 rewrite)

---

## [2026-06-03] · `6d5654a`


### ✨ Added

- **events**: Per-Challenger Groq title on boss spawn
- **vip**: Align in-game VIP kits with webstore tiers + wire delivery
- **ae**: ME networks now actually require energy
- **items**: Add TOOLS item category + SubCategoryMatcher updates

### 🐛 Fixed

- **ae**: ME system non-functional — uppercase block IDs + non-functional materials
- **data**: Consolidate QUANTUM_STORAGE_CELL id + fix TOME_OF_ENLIGHTENMENT + boss msg

### 🔧 Maintenance

- **lang**: Rename Sacrifice Arc -> Challenge Arc, Anime Boss -> Challenger from Beyond

## [2026-06-02] · `3ac9c37`


### ✨ Added

- **twitch**: In-game visual feedback for sub/cheer/raid events
- **machines**: MachineComponent registry for per-machine-ID behavior override
- SimpleXPBoosts-style global XP boost system
- **items**: ExecutableItems-style trigger/action behavior
- **items**: /itemedit live item editor (ItemEdit-inspired)
- **mmo**: Capture-mode keybinding — press a key to bind an ability
- **events**: Actually grant MMO bonuses on Sacrifice reward

### 🐛 Fixed

- **items**: Remove duplicate ME_NETWORK_ACCESS_TERMINAL definition
- **advancements**: 1.21 datapack folder rename + version-aware extraction
- **gui**: StatsGUI/KeyBindGUI crashes, questnpc UX, command-center guide prefix

### 🔧 Maintenance

- Gitignore /inspirations reference plugin folder

---

## [2026-06-02] · `d2ba3e7`


### ✨ Added

- **discord**: Role bonus combat system
- ConfigMigrator auto-merge + MySQL migration command (Phase 3)
- **mmo**: AuraSkills-inspired GUI redesign + attack cooldown HUD
- **essentials**: Staff vanish + playtime milestone rewards

### 🐛 Fixed

- ME CMD conflicts, missing NETWORK_CAPACITOR items, recipe IDs, keybind executor, circuits.yml

### ♻️ Changed

- **ae**: Redesign ME Terminal/Drive GUIs + fix critical bugs

---

## [2026-06-02] · `19ac7e8`


### 🐛 Fixed

- Jobs NPE + leave UX, ME items, keybind command, command center args

## [2026-06-01] · `f0cc6ca`


### ✨ Added

- **mmo**: Per-item weapon damage system with projectile tracking
- **advancements**: Custom advancement system via datapack + plugin triggers

---

## [2026-06-01] · `b86702c`


### ✨ Added

- **quests**: Add quest system, NPC givers, command center GUI, and keybind expansion
- **discord**: Discord bot and integration updates
- **energy**: Add creative generator component

### ♻️ Changed

- **core**: Migrate plugin resources to data/ subfolder

### 🔧 Maintenance

- Module-wide GUI, MMO, economy, and misc improvements
- Remove stale junk files, update gitignore, and update CHANGELOG

---

## [2026-05-29] · `1985014`


### 🐛 Fixed

- **ci**: Force PT-BR in Groq prompt, strip surrounding quotes from response

---

## [2026-05-29] · `7fcaa1d`


### 🐛 Fixed

- **ci**: AI message in Portuguese, move to content above embed with Discord heading format

---

## [2026-05-29] · `3d42824`


### 🐛 Fixed

- **discord**: Messages.yml saved to wrong path, causing all keys to return [Missing message]

---

## [2026-05-29] · `8709b16`


### ✨ Added

- **ci**: AI-generated message via Groq on Discord build notifications

---

## [2026-05-29] · `8ba64aa`


### 🔧 Maintenance

- **ci**: Random robot avatar per build on Discord notifications

---

## [2026-05-29] · `6b528c3`


### 🐛 Fixed

- **ci**: Run tests in CI, remove redundant build workflow, group changelog by commit type

---

## [2026-05-28] · `b3be732`


### 🐛 Fixed

- **machines-gui**: Extract machines-gui.yml to data folder on startup

---

## [2026-05-28] · `329fd92`


### 🐛 Fixed

- **gui**: Guide navigation, recipe layout, pagination range

---

## [2026-05-28] · `ec4b039`


### ✨ Added

- **api**: Expose placeable/multiblock fields, add VariantDefinition, fix machine type ref
- **machines**: Add tiers auto-expansion and processing-subtype to machine loader
- **plugin**: Phase 7 — multiblock bridge, DataDriven loader updates, recipe ID renames

### 🐛 Fixed

- **plugin**: Give command shows display names, break-message toggle, API impl logging

### 🔧 Maintenance

- **items**: Phase 6 — mass _BLOCK rename, native machine cleanup, variant-defaults
- **plugin**: Lang/config updates — multiblock messages, break-message toggle, economy defaults
- **modules**: Updates across economy, mmo, security, events, gui, traits, discord, web, ss, tab
- **ops**: Fail2ban filters and firewall rules for malformed packet and attacker blocking

## [2026-05-23] · `5cc6c1c`


### ✨ Added

- **tab**: Add /nexus scoreboard toggle per-player command

## [2026-05-22] · `70a3df5`


### ✨ Added

- **guide**: Phase 4 complete — bulk recategorize 404 items + delete 10 corrupted IDs
- **machines**: Add processing-subtype field to MachineDefinition

### 🐛 Fixed

- **gui**: Recipe layout disorder + raw color code in title
- **guide**: Expand category slots to 28 and add pagination

### 🔧 Maintenance

- **items**: Delete 31 legacy SV_* and camelCase slime duplicates
- **guide**: Delete 4 legacy Slimefun stub items + add 15 missing category icons

---

## [2026-05-22] · `3ceeabf`


### ✨ Added

- **gui**: Add type-specific machine GUIs and wire dispatch

### 🐛 Fixed

- **gui**: Prevent item theft from skill/trait GUIs via open→register order

### ♻️ Changed

- **items**: Rename wrench + infinity_crafting_* IDs to uppercase
- **items**: Propagate nexus_crafting_node → NEXUS_CRAFTING_NODE rename

### 🔧 Maintenance

- **items**: Delete 85 legacy/duplicate YAML items (Phase 1)
- **items**: Rename nexus_crafting_node_block → NEXUS_CRAFTING_NODE_BLOCK

---

## [2026-05-22] · `4172dec`


### ✨ Added

- **modules**: Per-module enable/disable toggles via config.yml and GUI

---

## [2026-05-21] · `208b215`


### 🐛 Fixed

- **ci**: Pass GH_PAT as token input to action-gh-release

---

## [2026-05-21] · `a43cc50`


### 🐛 Fixed

- **ci**: Use GH_PAT for release creation (GITHUB_TOKEN has no org write access)

---

## [2026-05-21] · `69ac4f3`


### 🐛 Fixed

- **ci**: Pass changelog through env var to avoid bash syntax errors

---

## [2026-05-21] · `cf363dd`


### 🐛 Fixed

- **ci**: Fix 403 push, bad action versions, and wrong branch triggers

---

## [2026-05-21] · `e488545`


### 🔧 Maintenance

- Removed BOM on the start of file

---

## [2026-05-21] · `2f25103`


### ✨ Added

- **plugin**: Phase 2 NexusLynxReporter — push heartbeat/logs/config to Railway
- **reporter**: REDACT filter + configurable log/alert levels
- **anti-dupe**: Block-break dupe prevention across rng/mmo/traits

### 🐛 Fixed

- **reporter**: Extend REDACT filter to cover JDBC connection URLs
- **discord**: Translate server status messages to Portuguese

### ♻️ Changed

- **config**: Centralize all secrets in key_configs.yml
- **reporter**: Remove per-key filter from pushConfig — key_configs.yml is the only skipped file
- **config**: Key_configs.yml holds secrets only — non-sensitive keys moved to module files

---

## [2026-05-14] · `bab3917`


### ✨ Added

- **i18n**: Wire LanguageManager into security, protections, clans modules
- **i18n**: Wire LanguageManager into MachineManager, SilkSpawners, Twitch; add all new lang keys to 4 locales
- **i18n**: Migrate gui/mmo/web/ae/energy/essentials/protections to LanguageManager

## [2026-05-13] · `3cfce4c`


### ✨ Added

- **i18n**: Wire TagGUI/RtpWorldGUI to LanguageManager + add LanguageSelectGUI

---

## [2026-05-13] · `2201b42`


### 📚 Documentation

- **config**: Annotate key_configs.yml with source env var for each key

---

## [2026-05-13] · `191f461`


### 🔧 Maintenance

- **deps**: Bump actions/upload-artifact from 4 to 7
- Migrate org references from O-Tiger to Tg-TheNexus

## [2026-05-02] · `ba0ebd5`


### 🔧 Maintenance

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### ✨ Added

- **logger**: Colorize module tags by prefix

### 🐛 Fixed

- **deps**: Upgrade ProtocolLib 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)
- **config**: Wire all key_configs.yml fields to module configs
- **machines**: Implement MachineEngine stale TODOs
- **integrations**: Remove unused Plugin field, log LuckPerms errors

### 📚 Documentation

- Update README, CONTRIBUTING, CREDITS, ECOSYSTEM
- Add ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

### 🔧 Maintenance

- Simplify startup log, remove ProGuard, reduce Dependabot noise
- **deps**: Bump actions/upload-artifact from 4 to 7
- Added Staff warning on medium risk Pr's

### 🔧 Maintenance

- **dependabot**: Risk classification + auto-close low-risk PRs

## [2026-05-12] · `13f15da`


### 🔧 Maintenance

- Stripped BOM character

## [2026-05-11] · `bcdd189`


### ✨ Added

- **events**: Add 6 anime bosses, rename isekai→anime, AddonLoader, BOM fix

### 🐛 Fixed

- **tools**: Classify all 2696 items — expand CMD_MODULES, add MAGICAL/SEED/MOB category styles; regenerate all prompt batches

## [2026-04-29] · `bbac1d1`


### 📚 Documentation

- Update CONFIGURATIONS — key_configs.yml section, blacklist section, nexus-lynx/nexus-bot keys

## [2026-04-28] · `40babb7`


### ✨ Added

- **security**: Auth blacklist + KeyConfig central credentials file

### 🐛 Fixed

- **chat**: Extract finalReason for lambda capture in MuteCommand

---

## [2026-05-02] · `ba0ebd5`


### 🔧 Maintenance

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### 🔧 Maintenance

- Added Staff warning on medium risk Pr's

---

## [2026-05-13] · `9479dbc`


### 🔧 Maintenance

- **dependabot**: Risk classification + auto-close low-risk PRs

---

## [2026-05-13] · `f22c9c1`


### 📚 Documentation

- Add ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

---

## [2026-05-13] · `f5aa66a`


### 🐛 Fixed

- **config**: Wire all key_configs.yml fields to module configs
- **machines**: Implement MachineEngine stale TODOs
- **integrations**: Remove unused Plugin field, log LuckPerms errors

### 📚 Documentation

- Update README, CONTRIBUTING, CREDITS, ECOSYSTEM

---

## [2026-05-13] · `552aa62`


### ✨ Added

- **logger**: Colorize module tags by prefix

---

## [2026-05-13] · `c5966c3`


### 🐛 Fixed

- **deps**: Upgrade ProtocolLib 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)

---

## [2026-05-13] · `74b3432`


### 🔧 Maintenance

- Simplify startup log, remove ProGuard, reduce Dependabot noise

---

## [2026-05-12] · `13f15da`


### 🔧 Maintenance

- Stripped BOM character

---

## [2026-05-11] · `bcdd189`


### 🐛 Fixed

- **tools**: Classify all 2696 items — expand CMD_MODULES, add MAGICAL/SEED/MOB category styles; regenerate all prompt batches

---

## [2026-05-11] · `7ac6735`


### ✨ Added

- **events**: Add 6 anime bosses, rename isekai→anime, AddonLoader, BOM fix

---

## [2026-04-29] · `bbac1d1`


### 📚 Documentation

- Update CONFIGURATIONS — key_configs.yml section, blacklist section, nexus-lynx/nexus-bot keys

## [2026-04-28] · `40babb7`


### ✨ Added

- **security**: Auth blacklist + KeyConfig central credentials file

### 🐛 Fixed

- **chat**: Extract finalReason for lambda capture in MuteCommand

---

## [2026-04-26] · `792efb0`


### ✨ Added

- **discord**: Forward moderation events to nexus-bot /api/moderation via HTTP

### 🔧 Maintenance

- Add .rtk/ to gitignore

---

## [2026-04-22] · `3782900`


### ✨ Added

- **web**: Replace inbound HTTP receiver with outbound polling

---

## [2026-04-22] · `762a968`


### 📚 Documentation

- Fix auth config path, add channels.yml section, expand checklist

---

## [2026-04-21] · `984477f`


### 🔧 Maintenance

- Add commented security channel entry to default channels.yml

---

## [2026-04-21] · `ddb3481`


### 🔒 Security

- Wire short-session Discord alert + add ops/ DDoS runbooks

---

## [2026-04-20] · `b322900`


### 🐛 Fixed

- **auth**: Bypass Java auth for Bedrock/Floodgate players

### 🔒 Security

- Bot/scanner hardening — short-session detection, IP auto-trust gate, Postgres session fix

---

## [2026-04-20] · `a998d1f`


### 📚 Documentation

- Add web/web-config.yml reference + security hardening changelog

---

## [2026-04-18] · `7f36abc`


### 🔒 Security

- AES-CBC key persistence, receiver secret auth, player name validation, session columns

---

## [2026-04-12] · `f52f78d`


### ✨ Added

- **twitch**: IRC event handling, sub/cheer/raid rewards, key raffle gate
- **web**: TwitchEventReceiver endpoint for Stream Panel integration
- **essentials**: RTP command with world selector GUI

### 🐛 Fixed

- **security**: FastLogin premium confirmation + auth hardening

### 🔧 Maintenance

- **data**: Item/machine/recipe YAML updates + plugin wiring

## [2026-03-24] · `cc57494`


### ✨ Added

- **fastlogin**: Scaffolda módulo nexusprism-fastlogin com autenticação premium via ProtocolLib

### 🐛 Fixed

- **mmo/segurança/encantamentos**: Corrige mensagens MMO, verificação premium e Auto Smelt
- **lang**: Move mmo para nível raiz do YAML (estava aninhado em economy)
- **plugin**: Qualifica ProtectionHandler como MachineManager.ProtectionHandler
- **fastlogin**: Substitui handshake RSA/AES por lookup assíncrono nome→UUID
- **fastlogin**: Injeta UUID via reflexão de campo (compatível Spigot e Paper)
- **fastlogin**: Injeta UUID via PlayerProfile no Paper, reflexão de campo no Spigot

### 🔧 Maintenance

- Moved nested mmo block message to root

---

## [2026-03-24] · `94b05a7`


### 🐛 Fixed

- **items**: Adiciona _templates.yml com item_template base para data/items/
- **data**: Corrige erros de inicialização do servidor
- **items**: Corrige conflitos de CMD dos itens comprimidos (30000-30002)

### 🔧 Maintenance

- Correção de escape inválido '\$" para "$"

---

## [2026-03-24] · `39476a5`

### ✨ Added

- **research**: Research tree system driven by `researches.yml` — entries have tier (BASIC/ADVANCED/INFINITY), parchment cost, dependencies, and unlocks
- **research**: Research progress persisted in SQLite, MySQL, and YAML
- **guide**: Infinity Table recipes now auto-registered in the in-game guide
- **machines**: VOID_COLLECTOR_BLOCK and VOID_SMELTER_BLOCK added (tier Infinity)
- **items**: SIGNALUM_INGOT and COMPRESSED_DIAMOND added to items.yml
- **discord**: ConsoleLogHandler — forwards server console output to a Discord channel
- **guide**: Category and tier icons for the guide are now YAML-driven via `gui_items.yml`; addon devs can register custom category icons without touching Java

### 🔧 Maintenance

- **config**: All data files restructured under `data/` hierarchy (`data/items/`, `data/machines/<tier>/`, `data/crafting/`, `data/smelting/`, `data/crafting/infinity_table/`)
- **config**: Root-level `items.yml`, `machines.yml`, `recipes.yml` removed — superseded by `data/` structure
- **recipes**: Machine recipes now defined inline inside the machine block under a `recipes:` key
- **recipes**: `nexus:ITEM_ID` prefix now supported in all recipe YAML files for referencing custom items

### 🐛 Fixed

- **storage**: Config keys renamed from `storage.*` to `database.*` to match `config.yml`
- **storage**: MySQL < 8 migration (`ALTER TABLE ADD COLUMN`) no longer uses `IF NOT EXISTS` — catches error code 1060 instead
- **research**: ResearchManager now reloads correctly on `/nexus reload`

### ⚖️ Legal

- License changed from MIT to proprietary All Rights Reserved

---

## [2026-03-22] · `7260628`


### 🔧 Maintenance

- **release**: Adicionar inputs version e changelist ao workflow_dispatch

---

## [2026-03-22] · `1a79a0f`


### ✨ Added

- **tab,protections,essentials**: Animações nomeadas, ordenação por grupo, GUI de flags, homes dinâmico

---

## [2026-03-22] · `5b49358`


### ✨ Added

- **discord,events**: GamePresence TYPE|text, Blood Moon chance, death/achievement embeds

### 🐛 Fixed

- **enchantments**: Add nexusprism-core dep for LanguageManager
- **tab**: Corrigido parâmetro ausente no construtor TabCommand

### 📚 Documentation

- Atualização de changelog, configurações e placeholders (2026-03-22)

### 🔧 Maintenance

- Alteração Geral: LanguageManager integrado em todos os módulos

---

## [2026-03-21] · `83b864b`


### 🔧 Maintenance

- Added server vote option to reset the MC server. Based on gnomomuitoloco ( on discord ) work

## [2026-03-20] · `e6356c5`


### ✨ Added

- **discord,integrations**: Add panel control, server vote, and PAPI providers

---

## [2026-03-19] · `bb5ecb9`


### ✨ Added

- **energy**: Expose energy API via EnergyProvider/EnergyRegistry
- **addon-example**: Add EnergyRegistry usage example

### 🐛 Fixed

- **economy**: Use public field def.id instead of nonexistent getId() in JobProviderImpl
- **protections**: Use correct Region.getFlag(RegionFlag) and DuelManager API in ProtectionsProviderImpl
- **providers**: Correct HologramLine, BloodMoonManager.getWorldName, and EventsProviderImpl world check
- **plugin**: Resolve BackpackProviderImpl and MachineRegistrarImpl compile errors

---

## [2026-03-19] · `1875bb0`


### 🐛 Fixed

- **chat**: Use correct ChannelRegistry and ChatChannel method names in ChatProviderImpl

---

## [2026-03-19] · `55c634e`


### ✨ Added

- **security**: UUID-based premium verification with persistent cache
- **events**: Admin /isekai command with force-start and boss selection
- **mmo**: Dynamic mana cost system and new dual-blade ability
- **mmo**: Ability key binding system with GUI and in-game hotkeys
- **api**: Add 9 provider interfaces, registries, and MachineProcessingRegistry
- **modules**: Wire providers into module constructors and shutdowns
- **machines**: Hook MachineProcessingRegistry into MachineEngine
- **addon-example**: Add public template project with README and publish workflow
- **api**: Add content loader, infinity recipe registry, and machine registrar interfaces

### ♻️ Changed

- Rename nexusslime → nexusprism across all layers

### 🔧 Maintenance

- Refactoring all references from nexusslime to nexusprism
- Fixed notify job on dependabot-discord workflow. root cause: My brain cells forget to  add the dependabot secrets

## [2026-03-18] · `ca5db45`


### ✨ Added

- **security**: Leveled mobs and mob stacker enhancements
- **economy**: Jobs, shop, auction house, and player warps
- **events**: Blood Moon, Sacrifice Arc, and Anime Boss system
- **mmo**: Stats, skill trees, abilities, professions, and mana system

### 🐛 Fixed

- **tab**: Correct TAB config defaults

### 🔧 Maintenance

- Added a fallback to prevent false positives on login / register
- Register Events and MMO modules, rename plugin to NexusPrism

## [2026-03-16] · `cc4853a`


### 🔧 Maintenance

- Added scoreboards and MOTD customizations  to TAB module
- Added forge/neoforge to the watchlist, to prevent exploiters, higher timer for clear world and a check for players. If none was found then skips world clean

## [2026-03-10] · `a92e2ee`


### 🔧 Maintenance

- Added jitpack support to API
- update the jitpack.yml to force use of maven 3.9
- idk
- minor fix: add yaml definition to code block

## [2026-03-09] · `e5a7a7f`


### 🔧 Maintenance

- The authentication flow has been improved, now verifying the account type (premium or cracked) and the IPs associated with it. For first-time access, an administrator will need to grant trust to the IP..

## [2026-03-08] · `6676d8d`


### 🔧 Maintenance

- add holograms module, mod/ore detector, configurable antilag, and spawner upgrades.
- Removed credit references ( not a p2w server btw )

## [2026-03-04] · `b9749a0`


### 🔧 Maintenance

- Improved Auth Flow to also detect IP and blocks unrecognized ones
- Wired new fixes for auth and security flows

## [2026-03-02] · `e5562d2`


### 🔧 Maintenance

- Updated documentation files
- Added SkinsRestorer support to premium accounts, cracked ones must use commands.
- Forgot to add the files to gitignore

## [2026-03-01] · `f5f4ee5`


### 🔧 Maintenance

- Changed auth flow to map-based

## [2026-02-28] · `bfc7f2f`


### 🔧 Maintenance

- Bump actions/upload-artifact from 6 to 7 in the gha-major group
- Improved Auth flow: _ Now it's session based, default time 2 hours

## [2026-02-27] · `4b773aa`


### 🔧 Maintenance

- Added:
- added changelog

## [2026-02-26] · `8d8020d`


### 🔧 Maintenance

- Updated some files
- Updated poms.xml of each module
- Improved Protections Module to be like RedProtection Also added some of my old projects, like Echoes boss, and dreaming experience
- Completly remove old nuvotifier dependency and add a public image as avatar of workflow
- Fixing sed causing the URL to be malformated
- Added support to running actions from discord

## [2026-02-25] · `9b39ccd`


### 🔧 Maintenance

- Fixed nuvotifier maven import download, by adding it locally
- Create SECURITY.md
- Disabled Votifier for now. Planning out on add again, but as a Internal code, not just a API call.
- Forgot about the dependency
- Votifier disabled on Nexus.....

### 🔧 Maintenance

- - Added emoji support to chat module; - Now it will be possible to mention someone between discord <-> minecraft, using their currently names on each. The mentioned user must be verified on the discord server to get notified. - Added lang keys to the new modules.

## [2026-02-24] · `6b1c020`


### 🔧 Maintenance

- Bump org.postgresql:postgresql from 42.7.4 to 42.7.7

## [2026-02-23] · `93ac56c`


### 🔧 Maintenance

- Added chat formatter and channel redirects
- updated dependabot-discord workflow
- Added multicrafting support for infinity items tiers
- Changed to jq payloads for safier use
- Correct indent on README and undo the changes of merge pull from dependabot ( causes incompability)

## [2026-02-21] · `265156e`


### 🔧 Maintenance

- Bump com.sk89q.worldguard:worldguard-bukkit

## [2026-02-11] · `7681a88`


### 🔧 Maintenance

- Linked webstore with nexusslime-web module Improve even more discord module, allowing configurations through yml files.

## [2026-02-07] · `1600a94`


### 🔧 Maintenance

- Bump the maven-major group across 1 directory with 2 updates

## [2026-02-04] · `7dc0811`


### 🔧 Maintenance

- Discord API implementation

## [2026-01-28] · `955cfc5`


### 🔧 Maintenance

- Discord integration testings

## [2026-01-20] · `fe77e92`


### 🔧 Maintenance

- Update issue templates
- ﻿# ItemYamlLoader: support named templates

### 🔧 Maintenance

- Avoid ProtocolLib download during build (optional at runtime)

## [2026-01-19] · `06bbb4b`


### 🔧 Maintenance

- Updated workflows and added CONTRIBUTING.md

## [2026-01-18] · `7d5b8ab`


### 🔧 Maintenance

- Updated .gitignore
- Updated release.yml workflow

## [2026-01-17] · `3fcae81`


### ✨ Added

- Implement tiered processing machines and Core Systems Infrastructure

### 🔧 Maintenance

- Created workflows for builds and release
- Updated release.yml
- Bump the gha-major group with 3 updates
- Idk, I just missed some fields on Send Discord notification

## [2026-01-16] · `5771bc7`


### 🔧 Maintenance

- Initial Commit - Working Items Placeholders

---

## [2.0.0-BETA] — Initial Release

### ✨ Added

- Complete rewrite as a **+25-module Maven multi-module project**
- New `nexusprism-api` module providing a public API for addon developers
- All feature systems are now self-contained modules with their own lifecycle
- Switched from YAML-only persistence to **SQLite / PostgreSQL** via `nexusprism-storage`
- `CustomItemRegistry` with PDC-based item tagging (`nexusprism:id`)
- 500+ data-driven items defined in `items.yml`
- Item tier system: Basic → Advanced → Infinity
- Research tree with XP-gated unlocks
- Multi-language support: English, Brazilian Portuguese, Spanish, Simplified Chinese
- **nexusprism-essentials** — 40+ QoL commands (homes, warps, TPA, AFK, jail, utility)
- **nexusprism-economy** — Dual-currency system, `/sell`, `/baltop`, configurable sell prices
- **nexusprism-clans** — Territory claiming, upgrade tree, clan chest, clan chat
- **nexusprism-security** — BCrypt auth, CAPTCHA anti-bot, VPN detection, anti-lag, anti-dupe
- **nexusprism-discord** — JDA bot, account linking, role sync, webhooks, GitHub Actions monitoring
- **nexusprism-crystaldefense** — Wave-based cooperative minigame
- **nexusprism-votifier** — Standalone Votifier V1/V2 server with streaks and leaderboard
- **nexusprism-dreams** — Sleep cutscene system (dreams and nightmares)
- **nexusprism-protections** — Region claiming, flags, 1v1 duel system
- **nexusprism-custommobs** — YAML-defined bosses with AI forms and loot tables
- **nexusprism-twitch** — Account linking, live alerts, chat relay, viewer giveaways
- **nexusprism-ae** — ME (Applied Energistics-style) network storage
- **nexusprism-energy** — Energy generation and cable networks
- **nexusprism-chat** — 4-channel chat (global, local, staff, trade) with moderation
- **nexusprism-events** — Blood Moon, Sacrifice Arc, and Anime Boss system
- **nexusprism-mmo** — Stats, skill trees, abilities, professions, and mana system
- **nexusprism-tab** — Custom TAB list header/footer with LuckPerms prefix
- **nexusprism-holograms** — YAML-driven floating text holograms
- **nexusprism-traits** — Tarot card trait system with economy integration
- **nexusprism-rng** — Daily spin wheel, lucky blocks, gacha, research levels
- **nexusprism-crates** — Key-based loot crates with animated openings
- **nexusprism-enchantments** — 175 custom enchants (6 rarities, 10 trigger types)
- **nexusprism-structures** — Structure loot injection (11 vanilla structures + addon API)
- **nexusprism-waila** — WAILA/HUD machine tooltips
- **nexusprism-web** — Webstore delivery bridge, VIP kits, payment handling, GDPR
- **PlaceholderAPI** — 14 providers, 30+ placeholders across all modules
- **LuckPerms** — Permissions and group-based placeholders
- `MachineYamlLoader` — machines defined in `machines.yml`, no Java required
- `MachineEngine` — async machine processing
- Multiblock crafting stations with YAML recipe format (`infinity_recipes/`)
- Energy generators: Solar Panels, Coal Generators
- Cable-based energy transport with configurable loss per block
