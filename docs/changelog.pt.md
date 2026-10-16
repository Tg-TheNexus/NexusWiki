# Histórico de Alterações

> Gerado automaticamente a partir dos commits do [NexusPrism](https://github.com/Tg-TheNexus/NexusPrism).
> Traduzido automaticamente — pequenas diferenças de fraseado são esperadas.

---

## [2026-10-16] · `2acbad9`


### 📚 Documentação

- Session summary reflects the follow-up fixes (#62)

---

## [2026-10-16] · `447b0d4`


### 🔧 Manutenção

- **deps**: Keep dependabot away from log4j (provided by the server) (#60)

---

## [2026-10-16] · `04b94fb`


### 🐛 Corrigido

- **auth**: Prune old name and IP records and uncollected notifications in UUIDConflictResolver (#59)

---

## [2026-10-16] · `396a934`


### 🐛 Corrigido

- **auth**: Validate names before the Mojang lookup, shorten demotions, log close errors (#58)

---

## [2026-10-16] · `44787b3`


### 📚 Documentação

- Session summary 2026-10-16 (#57)

---

## [2026-10-16] · `96d8c8c`


### 🐛 Corrigido

- **auth**: Mask passwords in logs, BCrypt off the main thread, pre-auth restrictions, per-address lockouts, IP whitelist actually enforced (#55)

---

## [2026-10-16] · `d066a4d`


### 🐛 Corrigido

- **auth**: Bind persistent sessions to the IP and review the identity settings at startup (#54)

---

## [2026-10-16] · `e1085d5`


### ✨ Adicionado

- **security**: Trusted test accounts skip the CAPTCHA by name and IP (#53)

---

## [2026-10-14] · `fefe853`


### ✨ Adicionado

- **supporters**: Supporter-pass SKU and the nxsupporter command (#52)

---

## [2026-10-14] · `64bc66f`


### ✨ Adicionado

- **store**: Cosmetic-only default sku-map and supporter titles (#51)

---

## [2026-10-14] · `41a480b`


### 📚 Documentação

- How to turn the delivery bridge on in a server (#50)

---

## [2026-10-14] · `abfc6dc`


### 🐛 Corrigido

- **delivery**: Bind timestamptz values when marking an order delivered (#49)

---

## [2026-10-14] · `222e5f3`


### ✨ Adicionado

- **delivery**: Bridge database from key_configs, fix item keys, unmapped skus and mark-delivered path (#48)

---

## [2026-10-14] · `2aa89fa`


### 🐛 Corrigido

- **web**: Unify the lynx address and move the webhook secret to key_configs

### 🔧 Manutenção

- Rename GitHub org to Tg-TheNexus
- Rename org to Tg-TheNexus and unify lynx and webhook config keys (#47)

## [2026-10-03] · `780b8af`


### 🔧 Manutenção

- **config**: Point defaults at the nexusheim.com hosts

---

## [2026-09-28] · `c392ae4`


### 🐛 Corrigido

- **ci**: Drop dev branch trigger, NexusPrism doesn't use one

---

## [2026-09-28] · `3b2579e`


### 🐛 Corrigido

- **ci**: Don't fail the whole build when artifact upload hits storage quota

---

## [2026-09-28] · `60616b0`


### 📚 Documentação

- **changelog**: Note the link/linkstreamer split

---

## [2026-09-28] · `2d9c95d`


### ✨ Adicionado

- **twitch**: Split /twitch link into /twitch link and /twitch linkstreamer

---

## [2026-09-27] · `18cd012`


### 🐛 Corrigido

- **events,quests**: Raise Groq max_tokens for gpt-oss-120b's reasoning overhead

---

## [2026-09-27] · `037e895`


### 🐛 Corrigido

- **events,quests**: Groq/compound-mini was also removed from Groq's catalog

---

## [2026-09-26] · `4b18be4`


### 🐛 Corrigido

- **events,quests**: Replace deprecated Groq model in BossTitle/DailyQuests

---

## [2026-09-23] · `17c3478`


### ✨ Adicionado

- **economy**: Publish vanilla sell-prices to shared DB for nexus-bot's /market

---

## [2026-08-09] · `632d673`


### 🔧Manutenção

- **deps**: Bump driver JDBC postgresql 42.7.11 -> 42.7.12

---

## [2026-08-09] · `9f261ed`


### ✨ Adicionado

- **economy**: Adicionar ponte monetária baseada em pesquisas
- **discord**: Links de conta espelhada para nexus-bot

### 🐛 Corrigido

- **config**: Remover estruturas/entradas de pesquisa pendentes

---

## [2026-08-06] · `ab72213`


### ✨ Adicionado

- **events**: Externaliza o equilíbrio do jogo codificado para configurar

### 🐛 Corrigido

- **security**: Limpe o IP/nome de usuário real do exemplo javadoc, remova o URL substituto do nexus-bot codificado

### ♻️Alterado

- **core**: Remover item/máquina/energia/domínio de pesquisa com morte confirmada

### 📚 Documentação

- Atualizar documentos de referência para corresponder ao módulo/superfície API atual

---

## [2026-07-11] · `36e78ff`


### 🐛 Corrigido

- **waila**: Extraia formatSnakeName para string EntityType, corrija erro de compilação
## [2026-07-10] · `0d08f3e`


### ✨ Adicionado

- **waila**: Detecção de entidade e coloração baseada em raridade

---

## [2026-07-09] · `0283136`


### ✨ Adicionado

- **mmo**: Adicionar superfície de gancho NexusATS (T1 com fio, stubs T2/T3)

### 🐛 Corrigido

- **lang**: Remova chaves YAML duplicadas em en_US e pt_BR
## [2026-07-06] · `32d26d9`


### ✨ Adicionado

- **discord**: Notificações de exclusão em massa de grupo com rejeição de 1s
- **discord**: Resolução de menção bidirecional — @@ MC→Discord, # Discord→MC

### 🐛 Corrigido

- **discord**: Webhook tem prioridade para mensagens de jogadores, JDA para mensagens de sistema — evita postagens duplicadas
- **discord**: Carregar todos os membros da guilda na barra de ação pronta + corrigir menção
- **mmo**: Restaurar MmoListener excluído por engano na extração de slimefun

### ♻️Alterado

- **discord**: Excluir DiscordChatListener morto, remover comentário enganoso de chat.webhookUrl
- **discord**: Remover legado @PlayerName→Discord mencionar resolução

### 📚 Documentação

- **discord**: Esclarecer o canal padrão precisa do ID JDA para Discord→MC relay

### 🔧Manutenção

- **config**: Remover seções mortas, corrigir lista de módulos
- **discord**: Remova a chave morta do chat-webhook de key_configs.yml

---

## [2026-07-03] · `ef78584`


### 🔧Manutenção

- **ci**: Etapa de remoção de activate_items movida para NexusATS

---

## [2026-07-03] · `2786877`


### ♻️Alterado

- **events**: Renomeie Sacrifice Arc para The Convergence em todos os arquivos lang e código

---

## [2026-06-19] · `d04c992`


### ✨ Adicionado

- **integration**: Adicionar superfície de gancho NexusATS para bloco de máquina e fiação Waila

---

## [2026-06-19] · `06bfe20`


### ✨ Adicionado

- **waila**: Adicionar reconhecimento de bloco vanilla

### 🐛 Corrigido

- **startup**: Reduza o detalhamento do log e corrija prefixos duplicados e vazamentos de cores
- **twitch**: Para de reconectar após 3 falhas consecutivas de IRC

### ♻️Alterado

- **slimefun**: Extraia máquinas, energia, itens, ae para o futuro plugin NexusItems
## [2026-06-17] · `ce58736`


### ✨ Adicionado

- **machines**: Adicionar sistema de máquina multibloco acionado por YAML

### 🐛 Corrigido

- **items**: Renomeie itens de liga simples para o sufixo _INGOT e remova os espaços reservados de PAPEL
## [2026-06-16] · `cfd4b44`


### 🐛 Corrigido

- **recipes**: Ingredientes ENHANCED_CRAFTING sem forma analisados como seção e não como lista de strings

### ♻️Alterado

- **machines**: Substitua o bloco de máquina da mesa de artesanato aprimorada por multibloco estilo Slimefun
- **machines**: Reescreva a tabela de artesanato aprimorada para um verdadeiro multibloco estilo Slimefun

### 🔧Manutenção

- **items**: Substitua nexus:COPPER_INGOT por COPPER_INGOT vanilla
- **items**: Corrigir categorização – renomear minérios brutos, remover duplicatas vanilla, corrigir correspondência de liga/placa
- **items**: Renomeie DUST_AMETHYST/DUST_NETHERITE para convenção *_DUST consistente
## [2026-06-15] · `dd8cee0`


### ✨ Adicionado

- **machines**: Adicionar máquina de mesa de artesanato aprimorada e sistema de receitas

### 🐛 Corrigido

- **machines**: Resolve MachineCatalog ENHANCED_CRAFTING_TABLE aviso de entrada de item
- **machines**: Correção do aviso ENHANCED_CRAFTING_TABLE MachineCatalog

### ♻️Alterado

- **recipes**: Migrar todas as receitas de criação de plugins para a Tabela de Criação Aprimorada
## [2026-06-14] · `f52e15d`


### 🐛 Corrigido

- **machines**: Resolver 3 avisos de camada cruzada do MachineCatalog
- **machines**: Remova o stub HOLOGRAM_PROJECTOR duplicado de basic_machines.yml

---

## [2026-06-14] · `a434364`


### ✨ Adicionado

- **crafting**: Adicione receitas para 37 itens anteriormente não fabricados

### 🐛 Corrigido

- **items**: Mova SINGULARITY_CONSTRUCTOR para nexus_machines.yml; adicionar definição de máquina + receitas de singularidade

---

## [2026-06-14] · `76b04ab`


### ✨ Adicionado

- **crafting**: Adicionar cadeia de receitas infinita na Tabela Infinity

### 🐛 Corrigido

- **events**: Registre 6 chefes de desafio ausentes em DEFAULT_BOSS_FILES

### ♻️Alterado

- **crafting**: Migrar equipamentos infinitos para Infinity Table; corrigir INFINITY_APPLE

---

## [2026-06-14] · `8b862fc`


### ✨ Adicionado

- **items/tinkers**: Adicionar categoria TINKERS, migrar 137 itens CAST, corrigir INGOT_FORMER para MACHINE
- **tools,ci**: Adicione activate_items.py (conflitos de CMD + regras de categoria) e conecte-se ao CI

### 🐛 Corrigido

- **mmo**: Guarda null customName() antes de ConcurrentHashMap.putIfAbsent em MobHealthDisplay

### ♻️Alterado

- **lang**: Renomeie as chaves lang security.world-cleaner e sincronize os arquivos lang
- **events/challenge**: Adicionar CMDs de exibição aos YAMLs do chefe, atualizar as classes ChallengeBoss
- **items/cobblestone**: Substitua COMPRESSED_COBBLESTONE de 5 camadas por 8 itens explícitos (x9..x43M), remova COBBLE_1-5 duplicatas e GUIs de máquina obsoletas

### 🔧Manutenção

- **tools**: Remova artefatos rp_prompts obsoletos, permita ferramentas/*.py no gitignore
- **items**: Atribua CMDs ausentes às variantes ITEM_BAND e NETWORK_POWER_DISPLAY em gear.yml
## [2026-06-09] · `ca942b3`


### 🐛 Corrigido

- **events**: Renomeie o diretório de recursos JAR challenge_bosses (era anime_bosses)
- **energy,ae**: Ponte do consumidor + feedback de inserção do terminal ME

### ♻️Alterado

- **lang**: Migrar mensagens codificadas para chaves lang (lote 1)
- **lang**: Migrar strings codificadas do plug-in nexusprism para chaves lang
- **lang**: Substitua todos os § literais por & em arquivos lang
- **lang**: Migrar strings restantes do plugin nexusprism para chaves lang
- **lang**: Migrar strings em events/mmo/rng/security/discord/quests para chaves lang
- **lang**: Migrar § strings restantes em chat/core/crates/mmo/machines/enchants para chaves lang e ChatColor
## [2026-06-08] · `d1b12d2`


### ✨ Adicionado

- **items,ae**: Camadas Hammer, capacidade de bytes AE2, correção de persistência ME
- **vfx,mmo,crates**: VFXUtil, placas de identificação de saúde do mob, habilidade VFX, crate VFX

### 🐛 Corrigido

- **machines**: Infraestrutura de energia isenta da verificação da camada GUI do catálogo
- **ae,gui,energy**: Chaves de idioma de status AE, colorir conhecimento da GUI, buffer de geração criativa
- **ae,gui,commands**: Canais a cabo de vidro, GUIs criativas, fornecem preenchimento de guias
- O controlador **ae**: fornece 8 canais básicos para que redes sem cabo funcionem
- **mmo**: Correção do conflito da barra de ação entre a notificação do HUD e do XP

### ♻️Alterado

- **display**: Centralize a barra de ação através do ActionBarManager
- **events**: Renomeie pacote de anime e classes para desafiar
- **events**: Conclua o anime → renomeie o desafio em documentos, idiomas e recursos

### 🔧Manutenção

- **cleanup**: Exclua cópias arquivadas e remova banners CUT obsoletos
- **cleanup**: Remova banners CUT obsoletos restantes e atualize exemplos/caixas
## [2026-06-07] · `c2888ce`


### 🐛 Corrigido

- **machines**: Ignorar chaves de modelo/campos no carregador; descartar arquivo de itens gerados obsoletos
- **items**: Propagar posicionável por meio de modelos + remover itens de máquina gerados duplicados
- **machines**: Adicionar definição de comportamento CREATIVE_CAPACITOR STORAGE
- **machines**: Adicionar geradores ADVANCED + ELECTRIC_BLAST_FURNACE, alinhar IDs FAL/MOB
## [2026-06-06] · `e7a40f7`


### ✨ Adicionado

- **api**: Reconstruir superfície API de item/máquina/receita
- **core**: MachineManager apoiado por PDC + registro/resolvers de itens
- **machines**: Mecanismo digitado, registro, definições, carregador + validador de catálogo
- **ae**: Reconstrua a rede ME como máquinas controladas por MachineContext
- **storage**: Persistir posicionamentos de máquinas via DataManager (SQLite/MySQL/YAML)
- **machines**: Cola de plug-in, ouvintes divididos, manipulador de GUI, carregadores, fiação
- **recipes**: Migrar rede ME, célula de armazenamento + criação de mochila para YAML
- **machines**: Tornar todas as máquinas acessíveis + fornecer GUIs baseadas em tipo
- **energy**: CREATIVE_CAPACITOR infinito + apenas marca blocos manipulados pelo mecanismo
- **energy**: Geradores de mecanismo de ponte em rede de cabo + alternância de modo de exportação

### 🐛 Corrigido

- **machines**: Renomeie a chave gui CRUSHER para ORE_CRUSHER; desduplicação CREATIVE_CAPACITOR
- **items**: Mesclar CREATIVE_GENERATOR_BLOCK perdido em CREATIVE_GENERATOR

### ♻️Alterado

- **energy,mmo,systems,items**: Reconecte os consumidores à nova API de item/máquina
- **machines**: Mesclar itens gerados em machine_blocks + GUIs com reconhecimento de subtipo

### 📚 Documentação

- **recipes**: Documento RecipeLoader codificado para lacunas de migração YAML
- **recipes**: Marcar receitas ME/célula de armazenamento/mochila como migradas

### 🔧Manutenção

- Gitignore atualizado
## [2026-06-04] · `6256f98`


### 🔧Manutenção

- **machines,items**: Arquivar item/máquina/ME Java (sem exclusão) + consumidores de stub
## [2026-06-03] · `7213cc6`


### ✨ Adicionado

- **waila**: Estatísticas de máquina ao vivo no HUD via mecanismo compartilhado (Bug 5)

### 🐛 Corrigido

- **machines**: Break descarta item de máquina personalizado, não o bloco vanilla
- **machines**: Persistir posicionamentos para que as máquinas sobrevivam à reinicialização (Bug 3)
- **machines**: Motor compartilhado único marca todas as máquinas (Bug 4)

### ♻️Alterado

- **machines**: MachineContext digitado + ouvintes divididos (reescrita da Seção 10)

---

## [2026-06-03] · `6d5654a`


### ✨ Adicionado

- **events**: Título Groq por Desafiador no spawn do chefe
- **vip**: Alinhe kits VIP no jogo com níveis de loja virtual + entrega eletrônica
- As redes **ae**: ME agora realmente requerem energia
- **items**: Adicionar categoria de item TOOLS + atualizações de SubCategoryMatcher

### 🐛 Corrigido

- Sistema **ae**: ME não funcional — IDs de bloco maiúsculos + materiais não funcionais
- **data**: Consolidar ID de QUANTUM_STORAGE_CELL + corrigir TOME_OF_ENLIGHTENMENT + mensagem do chefe

### 🔧Manutenção

- **lang**: Renomear Arco de Sacrifício -> Arco de Desafio, Chefe de Anime -> Desafiador do Além
## [2026-06-02] · `3ac9c37`


### ✨ Adicionado

- **twitch**: Feedback visual no jogo para eventos de sub/cheer/raid
- Registro **machines**: MachineComponent para substituição de comportamento por ID de máquina
- Sistema global de aumento de XP estilo SimpleXPBoosts
- **items**: Comportamento de gatilho/ação no estilo ExecutableItems
- **items**: /itemedit editor de itens ao vivo (inspirado no ItemEdit)
- **mmo**: Atalho de teclas no modo de captura — pressione uma tecla para vincular uma habilidade
- **events**: Conceda bônus MMO na recompensa do Sacrifício

### 🐛 Corrigido

- **items**: Remover definição duplicada de ME_NETWORK_ACCESS_TERMINAL
- **advancements**: 1.21 renomeação da pasta datapack + extração com reconhecimento de versão
- **gui**: Falhas de StatsGUI/KeyBindGUI, questnpc UX, prefixo do guia do centro de comando

### 🔧Manutenção

- Pasta do plugin de referência Gitignore /inspirations

---

## [2026-06-02] · `d2ba3e7`


### ✨ Adicionado

- **discord**: Sistema de combate de bônus de função
- Mesclagem automática do ConfigMigrator + comando de migração do MySQL (Fase 3)
- **mmo**: Redesenho da GUI inspirada no AuraSkills + HUD de resfriamento do ataque
- **essentials**: Equipe desaparece + recompensas por marcos de tempo de jogo

### 🐛 Corrigido

- Conflitos ME CMD, itens NETWORK_CAPACITOR ausentes, IDs de receita, executor de atalho de teclado, circuits.yml

### ♻️Alterado

- **ae**: Reprojetar GUIs do Terminal/Drive ME + corrigir bugs críticos

---

## [2026-06-02] · `19ac7e8`


### 🐛 Corrigido

- Jobs NPE + deixar UX, itens ME, comando keybind, argumentos do centro de comando
## [2026-06-01] · `f0cc6ca`


### ✨ Adicionado

- **mmo**: Sistema de dano de arma por item com rastreamento de projéteis
- **advancements**: Sistema de avanço personalizado via datapack + gatilhos de plugin

---

## [2026-06-01] · `b86702c`


### ✨ Adicionado

- **quests**: Adicionar sistema de missões, doadores de NPC, GUI do centro de comando e expansão de atalhos de teclado
- **discord**: Bot Discord e atualizações de integração
- **energy**: Adicionar componente gerador de criativo

### ♻️Alterado

- **core**: Migrar recursos do plugin para dados/subpasta

### 🔧Manutenção

- GUI, MMO, economia e melhorias diversas em todo o módulo
- Remova arquivos inúteis obsoletos, atualize o gitignore e atualize o CHANGELOG

---

## [2026-05-29] · `1985014`


### 🐛 Corrigido

- **ci**: Força PT-BR no prompt Groq, retira aspas circundantes da resposta

---

## [2026-05-29] · `7fcaa1d`


### 🐛 Corrigido

- Mensagem **ci**: AI em português, vá para o conteúdo acima incorporado com formato de cabeçalho Discord

---

## [2026-05-29] · `3d42824`


### 🐛 Corrigido

- **discord**: Messages.yml salvo no caminho errado, fazendo com que todas as chaves retornem [Mensagem ausente]

---

## [2026-05-29] · `8709b16`


### ✨ Adicionado

- **ci**: Mensagem gerada por IA via notificações de build do Groq on Discord

---

## [2026-05-29] · `8ba64aa`


### 🔧Manutenção

- **ci**: Avatar aleatório do robô por build nas notificações do Discord

---

## [2026-05-29] · `6b528c3`


### 🐛 Corrigido

- **ci**: Execute testes em CI, remova fluxo de trabalho de construção redundante, agrupe changelog por tipo de commit

---

## [2026-05-28] · `b3be732`


### 🐛 Corrigido

- **machines-gui**: Extraia machines-gui.yml para a pasta de dados na inicialização

---

## [2026-05-28] · `329fd92`


### 🐛 Corrigido

- **gui**: Guia de navegação, layout de receita, intervalo de paginação

---

## [2026-05-28] · `ec4b039`


### ✨ Adicionado

- **api**: Expor campos posicionáveis/multibloco, adicionar VariantDefinition, corrigir referência de tipo de máquina
- **machines**: Adicionar expansão automática de camadas e subtipo de processamento ao carregador de máquina
- **plugin**: Fase 7 — ponte multibloco, atualizações do carregador DataDriven, renomeações de ID de receita

### 🐛 Corrigido

- **plugin**: Fornecer comando mostra nomes de exibição, alternância de mensagem de interrupção, registro de implementação de API

### 🔧Manutenção

- **items**: Fase 6 — renomeação _BLOCK em massa, limpeza nativa da máquina, padrões de variantes
- **plugin**: Atualizações de Lang/config — mensagens multibloco, alternância de mensagem de interrupção, padrões de economia
- **modules**: Atualizações em economia, mmo, segurança, eventos, gui, características, discórdia, web, ss, guia
- **ops**: Filtros Fail2ban e regras de firewall para pacotes malformados e bloqueio de invasores
## [2026-05-23] · `5cc6c1c`


### ✨ Adicionado

- **tab**: Adicionar comando /nexus scoreboard toggle por jogador
## [2026-05-22] · `70a3df5`


### ✨ Adicionado

- **guide**: Fase 4 concluída – recategorização em massa de 404 itens + exclusão de 10 IDs corrompidos
- **machines**: Adicionar campo de subtipo de processamento a MachineDefinition

### 🐛 Corrigido

- **gui**: Desordem de layout da receita + código de cores bruto no título
- **guide**: Expanda os slots da categoria para 28 e adicione paginação

### 🔧Manutenção

- **items**: Exclua 31 duplicatas legadas de SV_* e camelCase slime
- **guide**: Exclua 4 itens de stub legados do Slimefun + adicione 15 ícones de categoria ausentes

---

## [2026-05-22] · `3ceeabf`


### ✨ Adicionado

- **gui**: Adicionar GUIs de máquina específicas do tipo e despacho por fio

### 🐛 Corrigido

- **gui**: Impedir o roubo de itens de GUIs de habilidades/características via ordem aberta → registro

### ♻️Alterado

- **items**: Renomeie os IDs de chave inglesa + infinito_crafting_* para letras maiúsculas
- **items**: Propagar nexus_crafting_node → NEXUS_CRAFTING_NODE renomear

### 🔧Manutenção

- **items**: Excluir 85 itens YAML legados/duplicados (Fase 1)
- **items**: Renomear nexus_crafting_node_block → NEXUS_CRAFTING_NODE_BLOCK

---

## [2026-05-22] · `4172dec`


### ✨ Adicionado

- **modules**: Alterna entre ativar/desativar por módulo via config.yml e GUI

---

## [2026-05-21] · `208b215`


### 🐛 Corrigido

- **ci**: Passe GH_PAT como entrada de token para action-gh-release

---

## [2026-05-21] · `a43cc50`


### 🐛 Corrigido

- **ci**: Use GH_PAT para criação de versão (GITHUB_TOKEN não tem acesso de gravação organizacional)

---

## [2026-05-21] · `69ac4f3`


### 🐛 Corrigido

- **ci**: Passe o changelog através do env var para evitar erros de sintaxe do bash

---

## [2026-05-21] · `cf363dd`


### 🐛 Corrigido

- **ci**: Corrigir push 403, versões de ações incorretas e gatilhos de ramificação errados

---

## [2026-05-21] · `e488545`


### 🔧Manutenção

- BOM removido no início do arquivo

---

## [2026-05-21] · `2f25103`


### ✨ Adicionado

- **plugin**: Fase 2 NexusLynxReporter - enviar heartbeat/logs/config para Railway
- Filtro **reporter**: REDACT + níveis de log/alerta configuráveis
- **anti-dupe**: Prevenção de bloqueio de quebra de blocos em rng/mmo/traits

### 🐛 Corrigido

- **reporter**: Estende o filtro REDACT para cobrir URLs de conexão JDBC
- **discord**: Traduzir mensagens de status do servidor para português

### ♻️Alterado

- **config**: Centralize todos os segredos em key_configs.yml
- **reporter**: Remova o filtro por chave do pushConfig — key_configs.yml é o único arquivo ignorado
- **config**: Key_configs.yml contém apenas segredos - chaves não confidenciais movidas para arquivos de módulo

---

## [2026-05-14] · `bab3917`


### ✨ Adicionado

- **i18n**: Wire LanguageManager em módulos de segurança, proteções e clãs
- **i18n**: Conecta LanguageManager em MachineManager, SilkSpawners, Twitch; adicione todas as novas chaves de idioma a 4 localidades
- **i18n**: Migrar gui/mmo/web/ae/energy/essentials/protections para LanguageManager
## [2026-05-13] · `3cfce4c`


### ✨ Adicionado

- **i18n**: Conecte TagGUI/RtpWorldGUI ao LanguageManager + adicione LanguageSelectGUI

---

## [2026-05-13] · `2201b42`


### 📚 Documentação

- **config**: Anote key_configs.yml com source env var para cada chave

---

## [2026-05-13] · `191f461`


### 🔧Manutenção

- **deps**: Ações de colisão/artefato de upload de 4 a 7
- Migrar referências organizacionais do O-Tiger para Tg-TheNexus
## [2026-05-02] · `ba0ebd5`


### 🔧Manutenção

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### ✨ Adicionado

- **logger**: Colorir tags do módulo por prefixo

### 🐛 Corrigido

- **deps**: ProtocolLib de atualização 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)
- **config**: Conecte todos os campos key_configs.yml às configurações do módulo
- **machines**: Implementar TODOs obsoletos do MachineEngine
- **integrations**: Remover campo de plug-in não utilizado, registrar erros do LuckPerms

### 📚 Documentação

- Atualizar README, CONTRIBUINDO, CRÉDITOS, ECOSSISTEMA
- Adicionar ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

### 🔧Manutenção

- Simplifique o log de inicialização, remova o ProGuard, reduza o ruído do Dependabot
- **deps**: Ações de colisão/artefato de upload de 4 a 7
- Adicionado aviso da equipe sobre PRs de risco médio

### 🔧Manutenção

- **dependabot**: Classificação de risco + fechamento automático de PRs de baixo risco
## [2026-05-12] · `13f15da`


### 🔧Manutenção

- Caractere BOM despojado
## [2026-05-11] · `bcdd189`


### ✨ Adicionado

- **events**: Adicionar 6 chefes de anime, renomear isekai → anime, AddonLoader, correção de BOM

### 🐛 Corrigido

- **tools**: Classifique todos os 2.696 itens - expanda CMD_MODULES, adicione estilos de categoria MAGICAL/SEED/MOB; regenerar todos os lotes de prompt
## [2026-04-29] · `bbac1d1`


### 📚 Documentação

- Atualizar CONFIGURAÇÕES - seção key_configs.yml, seção lista negra, chaves nexus-lynx/nexus-bot
## [2026-04-28] · `40babb7`


### ✨ Adicionado

- **security**: Lista negra de autenticação + arquivo de credenciais central KeyConfig

### 🐛 Corrigido

- **chat**: Extrair finalReason para captura lambda em MuteCommand

---

## [2026-05-02] · `ba0ebd5`


### 🔧Manutenção

- **deps**: Bump org.postgresql:postgresql

---

## [2026-05-13] · `820739c`


### 🔧Manutenção

- Adicionado aviso da equipe sobre PRs de risco médio

---

## [2026-05-13] · `9479dbc`


### 🔧Manutenção

- **dependabot**: Classificação de risco + fechamento automático de PRs de baixo risco

---

## [2026-05-13] · `f22c9c1`


### 📚 Documentação

- Adicionar ATTACKS.md, NEXUSPRISM_REFERENCE.md, system-wiring.html

---

## [2026-05-13] · `f5aa66a`


### 🐛 Corrigido

- **config**: Conecte todos os campos key_configs.yml às configurações do módulo
- **machines**: Implementar TODOs obsoletos do MachineEngine
- **integrations**: Remover campo de plug-in não utilizado, registrar erros do LuckPerms

### 📚 Documentação

- Atualizar README, CONTRIBUINDO, CRÉDITOS, ECOSSISTEMA

---

## [2026-05-13] · `552aa62`


### ✨ Adicionado

- **logger**: Colorir tags do módulo por prefixo

---

## [2026-05-13] · `c5966c3`


### 🐛 Corrigido

- **deps**: ProtocolLib de atualização 5.1.0 → 5.4.0 (net.dmulloy2 Maven Central)

---

## [2026-05-13] · `74b3432`


### 🔧Manutenção

- Simplifique o log de inicialização, remova o ProGuard, reduza o ruído do Dependabot

---

## [2026-05-12] · `13f15da`


### 🔧Manutenção

- Caractere BOM despojado

---

## [2026-05-11] · `bcdd189`


### 🐛 Corrigido

- **tools**: Classifique todos os 2.696 itens — expanda CMD_MODULES, adicione estilos de categoria MAGICAL/SEED/MOB; regenerar todos os lotes de prompt

---

## [2026-05-11] · `7ac6735`


### ✨ Adicionado

- **events**: Adicionar 6 chefes de anime, renomear isekai → anime, AddonLoader, correção de BOM

---

## [2026-04-29] · `bbac1d1`


### 📚 Documentação

- Atualizar CONFIGURAÇÕES - seção key_configs.yml, seção lista negra, chaves nexus-lynx/nexus-bot
## [2026-04-28] · `40babb7`


### ✨ Adicionado

- **security**: Lista negra de autenticação + arquivo de credenciais central KeyConfig

### 🐛 Corrigido

- **chat**: Extrair finalReason para captura lambda em MuteCommand

---

## [2026-04-26] · `792efb0`


### ✨ Adicionado

- **discord**: Encaminhar eventos de moderação para nexus-bot /api/moderation via HTTP

### 🔧Manutenção

- Adicione .rtk/ ao gitignore

---

## [2026-04-22] · `3782900`


### ✨ Adicionado

- **web**: Substitua o receptor HTTP de entrada por pesquisa de saída

---

## [2026-04-22] · `762a968`


### 📚 Documentação

- Corrija o caminho de configuração de autenticação, adicione a seção Channels.yml, expanda a lista de verificação

---

## [2026-04-21] · `984477f`


### 🔧 Manutenção

- Adicionar entrada de canal de segurança comentada ao canal padrão.yml

---

## [2026-04-21] · `ddb3481`


### 🔒 Segurança

- Alerta Discord de sessão curta + adição de runbooks de operações/DDoS

---

## [2026-04-20] · `b322900`


### 🐛 Corrigido

- **auth**: Ignorar autenticação Java para jogadores Bedrock/Floodgate

### 🔒 Segurança

- Proteção de bot/scanner — detecção de sessões curtas, porta de confiança automática de IP, correção de sessão Postgres

---

## [2026-04-20] · `a998d1f`


### 📚 Documentação

- Adicionar referência web/web-config.yml + changelog de reforço de segurança

---

## [2026-04-18] · `7f36abc`


### 🔒 Segurança

- Persistência de chave AES-CBC, autenticação secreta do receptor, validação de nome de jogador, colunas de sessão

---

## [2026-04-12] · `f52f78d`


### ✨ Adicionado

- **twitch**: Tratamento de eventos IRC, recompensas de sub/cheer/raid, sorteio de chaves
- Endpoint **web**: TwitchEventReceiver para integração com Stream Panel
- Comando **essentials**: RTP com GUI do seletor mundial

### 🐛 Corrigido

- **security**: Confirmação premium FastLogin + proteção de autenticação

### 🔧Manutenção

- **data**: Atualizações YAML de item/máquina/receita + fiação de plugin
## [2026-03-24] · `cc57494`


### ✨ Adicionado

- **fastlogin**: Scaffolda módulo nexusprism-fastlogin com autenticação premium via ProtocolLib

### 🐛 Corrigido

- **mmo/segurança/encantamentos**: Corrige mensagens MMO, seleção premium e Auto Smelt
- **lang**: Move mmo para nível raiz do YAML (estava aninhado em economia)
- **plugin**: Qualifica ProtectionHandler como MachineManager.ProtectionHandler
- **fastlogin**: Substitui handshake RSA/AES por lookup assíncrono nome→UUID
- **fastlogin**: Injeta UUID via reflexão de campo (compatível com Spigot e Paper)
- **fastlogin**: Insira UUID via PlayerProfile no Paper, reflexão de campo no Spigot

### 🔧Manutenção

- Mensagem de bloco MMO aninhada movida para root

---

## [2026-03-24] · `94b05a7`


### 🐛 Corrigido

- **items**: Adiciona _templates.yml com item_template base para data/items/
- **data**: Corrige erros de inicialização do servidor
- **items**: Corrige conflitos de CMD dos itens comprimidos (30000-30002)

### 🔧Manutenção

- Correção de escape inválido '\$" para "$"

---

## [2026-03-24] · `39476a5`

### ✨ Adicionado

- **research**: Sistema de árvore de pesquisa baseado em `researches.yml` — entradas têm tier (BASIC/ADVANCED/INFINITY), custo em pergaminhos, dependências e desbloqueios
- **research**: Progresso de pesquisa persistido em SQLite, MySQL e YAML
- **guide**: Receitas da Infinity Table agora são registradas automaticamente no guia do jogo
- **machines**: VOID_COLLECTOR_BLOCK e VOID_SMELTER_BLOCK adicionados (tier Infinity)
- **items**: SIGNALUM_INGOT e COMPRESSED_DIAMOND adicionados ao items.yml
- **discord**: ConsoleLogHandler — encaminha a saída do console do servidor para um canal do Discord
- **guide**: Ícones de categoria e tier do guia agora são configuráveis via `gui_items.yml`; desenvolvedores de addons podem registrar ícones de categoria personalizados sem alterar Java

### 🔧 Manutenção

- **config**: Todos os arquivos de dados reestruturados sob a hierarquia `data/` (`data/items/`, `data/machines/<tier>/`, `data/crafting/`, `data/smelting/`, `data/crafting/infinity_table/`)
- **config**: Arquivos `items.yml`, `machines.yml` e `recipes.yml` na raiz removidos — substituídos pela estrutura `data/`
- **recipes**: Receitas de máquinas agora definidas inline dentro do bloco da máquina sob a chave `recipes:`
- **recipes**: Prefixo `nexus:ITEM_ID` agora suportado em todos os arquivos YAML de receitas para referenciar itens personalizados

### 🐛 Corrigido

- **storage**: Chaves de configuração renomeadas de `storage.*` para `database.*` para corresponder ao `config.yml`
- **storage**: Migração do MySQL < 8 (`ALTER TABLE ADD COLUMN`) não usa mais `IF NOT EXISTS` — captura o código de erro 1060
- **research**: ResearchManager agora recarrega corretamente no `/nexus reload`

### ⚖️ Legal

- Licença alterada de MIT para proprietária — Todos os Direitos Reservados

---

## [2026-03-22] · `7260628`


### 🔧Manutenção

- **release**: Adicionar inputs version e changelist ao workflow_dispatch

---

## [2026-03-22] · `1a79a0f`


### ✨ Adicionado

- **tab,protections,essentials**: Animações nomeadas, ordenação por grupo, GUI de bandeiras, casas dinâmicas

---

## [2026-03-22] · `5b49358`


### ✨ Adicionado

- **discord,events**: GamePresence TYPE | texto, chance de Blood Moon, incorporações de morte/conquista

### 🐛 Corrigido

- **enchantments**: Adicionar dependência nexusprism-core para LanguageManager
- **tab**: Corrigido parâmetro ausente no construtor TabCommand

### 📚 Documentação

- Atualização de changelog, configurações e placeholders (22/03/2026)

### 🔧 Manutenção

- Alteração Geral: LanguageManager integrado em todos os módulos

---

## [2026-03-21] · `83b864b`


### 🔧 Manutenção

- Adicionada opção de votação no servidor para redefinir o servidor MC. Baseado no trabalho do gnomomuitoloco (no discord)

## [2026-03-20] · `e6356c5`


### ✨ Adicionado

- **discord,integrations**: Adicionar controle de painel, votação de servidor e provedores PAPI

---

## [2026-03-19] · `bb5ecb9`


### ✨ Adicionado

- **energy**: Expor API de energia via EnergyProvider/EnergyRegistry
- **addon-example**: Adicionar exemplo de uso do EnergyRegistry

### 🐛 Corrigido

- **economy**: Usar campo público def.id em vez de getId() inexistente em JobProviderImpl
- **protections**: Usar Region.getFlag(RegionFlag) correto e API DuelManager em ProtectionsProviderImpl
- **providers**: Corrigir HologramLine, BloodMoonManager.getWorldName e verificação de mundo em EventsProviderImpl
- **plugin**: Resolver erros de compilação em BackpackProviderImpl e MachineRegistrarImpl

---

## [2026-03-19] · `1875bb0`


### 🐛 Corrigido

- **chat**: Usar nomes corretos de métodos ChannelRegistry e ChatChannel em ChatProviderImpl

---

## [2026-03-19] · `55c634e`


### ✨ Adicionado

- **security**: Verificação premium baseada em UUID com cache persistente
- **events**: Comando admin /isekai com início forçado e seleção de boss
- **mmo**: Sistema dinâmico de custo de mana e nova habilidade de lâmina dupla
- **mmo**: Sistema de vinculação de teclas de habilidades com GUI e atalhos no jogo
- **api**: Adicionar 9 interfaces de provedor, registros e MachineProcessingRegistry
- **modules**: Conectar provedores nos construtores de módulos e desligamentos
- **machines**: Conectar MachineProcessingRegistry ao MachineEngine
- **addon-example**: Adicionar projeto de template público com README e fluxo de publicação
- **api**: Adicionar carregador de conteúdo, registro de receita infinita e interfaces de registrador de máquina

### ♻️ Alterado

- Renomear nexusslime → nexusprism em todas as camadas

### 🔧 Manutenção

- Refatorando todas as referências de nexusslime para nexusprism
- Corrigido o job de notificação no workflow do dependabot-discord. Causa raiz: minhas células cerebrais se esquecem de adicionar os segredos do dependabot

## [2026-03-18] · `ca5db45`


### ✨ Adicionado

- **security**: Mobs nivelados e melhorias no empilhador de mobs
- **economy**: Jobs, loja, casa de leilões e warps de jogadores
- **events**: Blood Moon, Arco do Sacrifício e sistema de Boss Isekai
- **mmo**: Estatísticas, árvores de habilidades, habilidades, profissões e sistema de mana

### 🐛 Corrigido

- **tab**: Corrigir padrões de configuração do TAB

### 🔧 Manutenção

- Adicionado um substituto para evitar falsos positivos no login/registro
- Registrar módulos Events e MMO, renomear o plugin para NexusPrism

## [2026-03-16] · `cc4853a`


### 🔧 Manutenção

- Adicionados placares e personalizações de MOTD ao módulo TAB
- Adicionado forge/neoforge à lista de observação para evitar exploradores, maior timer para limpeza de mundo e verificação de jogadores. Se nenhum for encontrado, pula a limpeza

## [2026-03-10] · `a92e2ee`


### 🔧 Manutenção

- Adicionado suporte jitpack à API
- Atualizado o jitpack.yml para forçar o uso do maven 3.9
- não sei
- pequena correção: adicionar definição yaml ao bloco de código

## [2026-03-09] · `e5a7a7f`


### 🔧 Manutenção

- O fluxo de autenticação foi melhorado, verificando agora o tipo de conta (premium ou crackeada) e os IPs associados a ela. Para o primeiro acesso, um administrador precisará conceder confiança ao IP.

## [2026-03-08] · `6676d8d`


### 🔧 Manutenção

- Adicionar módulo de hologramas, detector de mod/minério, antilag configurável e atualizações de spawner.
- Referências de crédito removidas (não é um servidor p2w)

## [2026-03-04] · `b9749a0`


### 🔧 Manutenção

- Fluxo de autenticação aprimorado para também detectar IP e bloquear IPs não reconhecidos
- Novas correções conectadas para fluxos de autenticação e segurança

## [2026-03-02] · `e5562d2`


### 🔧 Manutenção

- Arquivos de documentação atualizados
- Adicionado suporte SkinsRestorer para contas premium; as crackeadas devem usar comandos.
- Esqueci de adicionar os arquivos ao .gitignore

## [2026-03-01] · `f5f4ee5`


### 🔧 Manutenção

- Fluxo de autenticação alterado para baseado em mapa

## [2026-02-28] · `bfc7f2f`


### 🔧 Manutenção

- Bump actions/upload-artifact de 6 para 7 no grupo gha-major
- Fluxo de autenticação aprimorado: agora é baseado em sessão, tempo padrão de 2 horas

## [2026-02-27] · `4b773aa`


### 🔧 Manutenção

- Adicionado:
- adicionado registro de alterações

## [2026-02-26] · `8d8020d`


### 🔧 Manutenção

- Atualizados alguns arquivos
- Atualizado o poms.xml de cada módulo
- Módulo de proteções aprimorado para ser semelhante ao RedProtection. Também adicionei alguns dos meus projetos antigos, como o boss Echoes e a experiência de sonho
- Removida completamente a antiga dependência do nuvotifier e adicionada uma imagem pública como avatar do workflow
- Corrigido sed que causava URL malformada
- Adicionado suporte para executar ações a partir do discord

## [2026-02-25] · `9b39ccd`


### 🔧 Manutenção

- Corrigido o download de importação do nuvotifier maven, adicionando-o localmente
- Criar SECURITY.md
- Votificador desativado por enquanto. Planejando adicionar novamente, mas como código interno, não apenas uma chamada de API.
- Esqueci da dependência
- Votificador desativado no Nexus.....

### 🔧 Manutenção

- Adicionado suporte a emoji ao módulo de chat; agora será possível mencionar alguém entre discord <-> minecraft, usando seus nomes atuais em cada plataforma. O usuário mencionado deve ser verificado no servidor discord para ser notificado. Adicionadas chaves de idioma aos novos módulos.

## [2026-02-24] · `6b1c020`


### 🔧 Manutenção

- Bump org.postgresql:postgresql de 42.7.4 para 42.7.7

## [2026-02-23] · `93ac56c`


### 🔧 Manutenção

- Adicionado formatador de chat e redirecionamentos de canal
- Workflow do dependabot-discord atualizado
- Adicionado suporte de multicrafting para tiers de itens infinitos
- Alterado para payloads jq para uso mais seguro
- Corrigir recuo no README e desfazer as alterações do merge pull do dependabot (causa incompatibilidade)

## [2026-02-21] · `265156e`


### 🔧 Manutenção

- Bump com.sk89q.worldguard:worldguard-bukkit

## [2026-02-11] · `7681a88`


### 🔧 Manutenção

- Loja virtual vinculada ao módulo nexusslime-web. Melhorado ainda mais o módulo discord, permitindo configurações através de arquivos yml.

## [2026-02-07] · `1600a94`


### 🔧 Manutenção

- Bump do grupo maven-major em 1 diretório com 2 atualizações

## [2026-02-04] · `7dc0811`


### 🔧 Manutenção

- Implementação da API do Discord

## [2026-01-28] · `955cfc5`


### 🔧 Manutenção

- Testes de integração do Discord

## [2026-01-20] · `fe77e92`


### 🔧 Manutenção

- Atualizar templates de issues
- ItemYamlLoader: suporte a templates nomeados

### 🔧 Manutenção

- Evitar download do ProtocolLib durante a compilação (opcional em tempo de execução)

## [2026-01-19] · `06bbb4b`


### 🔧 Manutenção

- Workflows atualizados e adicionado CONTRIBUTING.md

## [2026-01-18] · `7d5b8ab`


### 🔧 Manutenção

- .gitignore atualizado
- Workflow release.yml atualizado

## [2026-01-17] · `3fcae81`


### ✨ Adicionado

- Implementar máquinas de processamento em camadas e infraestrutura dos sistemas principais

### 🔧 Manutenção

- Criados workflows para builds e releases
- release.yml atualizado
- Bump do grupo gha-major com 3 atualizações
- Não sei, acabei de perder alguns campos na notificação Enviar Discord

## [2026-01-16] · `5771bc7`


### 🔧 Manutenção

- Commit inicial — Placeholders de itens funcionando

---

## [2.0.0-BETA] — Lançamento Inicial

### ✨ Adicionado

- Reescrita completa como um **projeto Maven multi-módulo com +25 módulos**
- Novo módulo `nexusprism-api` fornecendo uma API pública para desenvolvedores de addons
- Todos os sistemas de recursos agora são módulos independentes com ciclo de vida próprio
- Migração de persistência YAML para **SQLite / PostgreSQL** via `nexusprism-storage`
- `CustomItemRegistry` com marcação de itens via PDC (`nexusprism:id`)
- 500+ itens baseados em dados definidos em `items.yml`
- Sistema de tier de itens: Básico → Avançado → Infinito
- Árvore de pesquisa com desbloqueios por XP
- Suporte a múltiplos idiomas: Inglês, Português Brasileiro, Espanhol, Chinês Simplificado
- **nexusprism-essentials** — 40+ comandos QoL (homes, warps, TPA, AFK, prisão, utilitários)
- **nexusprism-economy** — Sistema de moeda dupla, `/sell`, `/baltop`, preços de venda configuráveis
- **nexusprism-clans** — Reivindicação de território, árvore de upgrades, baú de clã, chat de clã
- **nexusprism-security** — Autenticação BCrypt, anti-bot CAPTCHA, detecção de VPN, anti-lag, anti-dupe
- **nexusprism-discord** — Bot JDA, vinculação de contas, sincronização de cargos, webhooks
- **nexusprism-crystaldefense** — Minijogo cooperativo por ondas
- **nexusprism-votifier** — Servidor Votifier V1/V2 independente com sequências e placar
- **nexusprism-dreams** — Sistema de cutscene ao dormir (sonhos e pesadelos)
- **nexusprism-protections** — Reivindicação de regiões, flags, sistema de duelo 1v1
- **nexusprism-custommobs** — Bosses definidos em YAML com formas de IA e tabelas de loot
- **nexusprism-twitch** — Vinculação de conta, alertas ao vivo, relay de chat, sorteios
- **nexusprism-ae** — Armazenamento em rede ME (estilo Applied Energistics)
- **nexusprism-energy** — Geração de energia e redes de cabos
- **nexusprism-chat** — Chat de 4 canais (global, local, staff, comércio) com moderação
- **nexusprism-events** — Lua de Sangue, Arco do Sacrifício e sistema de Boss Isekai
- **nexusprism-mmo** — Estatísticas, árvores de habilidades, habilidades, profissões e sistema de mana
- **nexusprism-tab** — Cabeçalho/rodapé da lista TAB personalizado com prefixo LuckPerms
- **nexusprism-holograms** — Hologramas de texto flutuante baseados em YAML
- **nexusprism-traits** — Sistema de traits com cartas de Tarot e integração com economia
- **nexusprism-rng** — Roleta diária, blocos da sorte, gacha, níveis de pesquisa
- **nexusprism-crates** — Caixas de loot com abertura animada e chaves
- **nexusprism-enchantments** — 175 encantamentos personalizados (6 raridades, 10 tipos de gatilho)
- **nexusprism-structures** — Injeção de loot em estruturas (11 estruturas vanilla + API de addon)
- **nexusprism-waila** — Tooltips de máquinas WAILA/HUD
- **nexusprism-web** — Bridge de loja web, kits VIP, processamento de pagamentos, LGPD
- **PlaceholderAPI** — 14 provedores, 30+ placeholders em todos os módulos
- **LuckPerms** — Permissões e placeholders baseados em grupo
- `MachineYamlLoader` — máquinas definidas em `machines.yml`, sem necessidade de Java
- `MachineEngine` — processamento assíncrono de máquinas
- Estações de crafting multibloco com formato de receita YAML (`infinity_recipes/`)
- Geradores de energia: Painéis Solares, Geradores de Carvão
- Transporte de energia via cabos com perda configurável por bloco
