# API para Desenvolvedores NexusPrism

*Última atualização: 2026-03-22*

> ⚠️ **Parcialmente desatualizado (sinalizado em 2026-08-06, ainda não reescrito por completo).**
> As seções `Mochilas`, `Redes de Energia`, `Registro de itens` e `ResearchManager` abaixo
> descrevem uma API (`NexusPrismAPI.get().getService(...)`, `BackpackRegistry`,
> `EnergyRegistry`, `ItemRegistry`) que foi **confirmada como nunca ter existido de fato no
> código** — nenhum serviço desses é registrado via `ServicesManager` do Bukkit em lugar
> nenhum, e os sistemas subjacentes (`BackpackManager`, energia, pesquisa) eram código morto,
> já removido (veja `NexusATS/docs/planning/PLAN-presplit-core-infra.md`). Todo esse domínio
> agora pertence ao NexusATS — não construa integrações contra as seções abaixo. Os hooks
> genéricos que **de fato existem** hoje são `NexusPrism.registerBlockClassifier()`,
> `registerAddonCommand()`/`registerAddonTabCompleter()` e
> `DataManager.setPlayerField()`/`getPlayerField()` — veja o `ECOSYSTEM.md` na raiz do
> repositório do ecossistema para exemplos reais e atualizados.

Este guia mostra como integrar com o NexusPrism a partir de um plugin Bukkit/Paper externo ou de um addon nativo. Você compila apenas contra `nexusprism-api` — nunca contra os JARs concretos dos módulos.

---

## Passo 1 — Adicionar a dependência

O NexusPrism é publicado via **JitPack**. Adicione o repositório e o artefato da API ao seu `pom.xml`:

```xml
<repositories>
    <repository>
        <id>jitpack.io</id>
        <url>https://jitpack.io</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>com.github.Tg-TheNexus.NexusPrismModularizado</groupId>
        <artifactId>nexusprism-api</artifactId>
        <version>master-SNAPSHOT</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
```

> **O escopo `provided` é obrigatório.** O NexusPrism inclui a API em tempo de execução — não a inclua (shade) no seu JAR.

Para Gradle (Kotlin DSL):

```kotlin
repositories {
    maven("https://jitpack.io")
}

dependencies {
    compileOnly("com.github.Tg-TheNexus.NexusPrismModularizado:nexusprism-api:master-SNAPSHOT")
}
```

---

## Passo 2 — Declarar a dependência no `plugin.yml`

Como o NexusPrism é opcional para a maioria das integrações, use `softdepend`. Use `depend` somente se o seu plugin não funcionar de forma alguma sem ele.

```yaml
name: MeuPlugin
version: 1.0.0
main: com.exemplo.MeuPlugin
api-version: "1.21"

softdepend:
  - NexusPrism
```

---

## Passo 3 — Obter a instância da API

Sempre obtenha a API dentro do `onEnable()`, **após** o servidor estar completamente iniciado. Nunca a chame de um inicializador estático ou construtor.

```java
import io.github.otiger.nexusprism.api.NexusPrismAPI;

public class MeuPlugin extends JavaPlugin {

    private NexusPrismAPI nexus;

    @Override
    public void onEnable() {
        nexus = NexusPrismAPI.get();

        if (nexus == null) {
            getLogger().warning("NexusPrism não encontrado — integração desativada.");
            return;
        }

        if (!nexus.isReady()) {
            getLogger().warning("NexusPrism ainda está inicializando.");
            return;
        }

        getLogger().info("Conectado ao NexusPrism " + nexus.getVersion());
    }
}
```

---

## Passo 4 — Provedores de módulos

Cada módulo opcional do NexusPrism expõe um provedor tipado através de um registro estático. Todos os provedores retornam `Optional` — se o módulo estiver desativado ou não instalado, o Optional estará vazio. Sempre use `ifPresent` ou `orElse` para lidar com isso com segurança.

### Economia

```java
UUID uuid = player.getUniqueId();

// Ler saldo
double saldo = NexusPrismAPI.economy()
        .map(eco -> eco.getBalance(uuid))
        .orElse(0.0);

// Adicionar dinheiro
NexusPrismAPI.economy().ifPresent(eco -> eco.addMoney(uuid, 500.0));

// Cobrar jogador (retorna false se saldo insuficiente)
boolean sucesso = NexusPrismAPI.economy()
        .map(eco -> eco.withdrawMoney(uuid, 100.0))
        .orElse(false);

// Top saldos
NexusPrismAPI.economy().ifPresent(eco ->
    eco.getTopBalances(10).forEach(entry ->
        System.out.println(entry.uuid() + " → " + entry.balance())));
```

### Autenticação / Segurança

```java
// Verificar se o jogador está logado (padrão true quando módulo ausente)
boolean logado = NexusPrismAPI.auth()
        .map(auth -> auth.isAuthenticated(uuid))
        .orElse(true);
```

### Clãs

```java
// Obter tag do clã do jogador
String tag = NexusPrismAPI.clans()
        .flatMap(c -> c.getClanTag(uuid))
        .orElse("");

// Verificar se está em um clã
boolean temCla = NexusPrismAPI.clans()
        .map(c -> c.isInClan(uuid))
        .orElse(false);
```

### Essentials

```java
// Teleportar jogador para a home "base"
NexusPrismAPI.essentials().ifPresent(ess ->
        ess.teleportHome(player, "base"));

// Verificar status AFK
boolean estaAfk = NexusPrismAPI.essentials()
        .map(ess -> ess.isAfk(uuid))
        .orElse(false);
```

### Votos

```java
// Total de votos do jogador
int votos = NexusPrismAPI.votes()
        .map(v -> v.getTotalVotes(uuid))
        .orElse(0);

// Sequência atual de votos
int sequencia = NexusPrismAPI.votes()
        .map(v -> v.getStreak(uuid))
        .orElse(0);
```

### Encantamentos Personalizados

```java
// Verificar se um item tem um encantamento personalizado
boolean temEnchant = NexusPrismAPI.enchants()
        .map(e -> e.hasEnchant(item, "SOUL_MENDER"))
        .orElse(false);

// Obter o nível de um encantamento
int nivel = NexusPrismAPI.enchants()
        .map(e -> e.getLevel(item, "SOUL_MENDER"))
        .orElse(0);
```

### Caixas (Crates)

```java
// Dar uma chave de caixa ao jogador
NexusPrismAPI.crates().ifPresent(c ->
        c.giveKey(player, "VOTE_CRATE", 1));
```

### MMO

```java
import io.github.otiger.nexusprism.api.mmo.MmoRegistry;

UUID uuid = player.getUniqueId();

MmoRegistry.get().ifPresent(mmo -> {
    int nivel  = mmo.getLevel(uuid);
    int mana   = mmo.getCurrentMana(uuid);
    int maxMana = mmo.getMaxMana(uuid);

    // Consome mana (retorna false se insuficiente)
    if (mmo.hasMana(uuid, 20) && mmo.consumeMana(uuid, 20)) {
        // habilidade ativada
    }

    // Adiciona XP a uma árvore de habilidades
    mmo.addSkillXp(player, "warrior", 100L);

    // Adiciona XP a uma profissão
    mmo.addProfessionXp(player, "mining", 50L);

    int forca = mmo.getStat(uuid, "STRENGTH");
    List<String> habilidades = mmo.getUnlockedAbilityIds(uuid);
});
```

### Chat

```java
import io.github.otiger.nexusprism.api.chat.ChatRegistry;

ChatRegistry.get().ifPresent(chat -> {
    boolean silenciado = chat.isMuted(uuid);
    chat.mute(uuid, 10 * 60 * 1000L, "Spam", "Console");
    chat.broadcastToChannel("global", "[MeuAddon] Anúncio do servidor!");
    String canalAtivo = chat.getActiveChannel(uuid);
});
```

### Proteções

```java
import io.github.otiger.nexusprism.api.protections.ProtectionsRegistry;

ProtectionsRegistry.get().ifPresent(prot -> {
    boolean pvp = prot.isPvpAllowed(location);
    boolean emDuelo = prot.isInDuel(uuid);
    prot.getDuelOpponent(uuid).ifPresent(oponente -> { /* ... */ });
    List<String> regioes = prot.getRegionNamesAt(location);
    int reivindicadas = prot.getRegionCount(uuid);
});
```

### Eventos (Lua de Sangue, Arco do Sacrifício, Chefe Isekai)

```java
import io.github.otiger.nexusprism.api.events.EventsRegistry;

EventsRegistry.get().ifPresent(events -> {
    boolean luaAtiva   = events.isBloodMoonActive();
    int sequencia      = events.getSacrificeStreak(uuid);
    boolean emSacrificio = events.isInSacrifice(uuid);
    boolean temChefe   = events.hasActiveBossFight(uuid);
});
```

### Hologramas

```java
import io.github.otiger.nexusprism.api.holograms.HologramRegistry;

HologramRegistry.get().ifPresent(holo -> {
    holo.create("meu_holo", location);
    holo.addLine("meu_holo", "§aOlá do meu addon!");
    holo.setLine("meu_holo", 0, "§eLinha atualizada");
    holo.showToPlayer("meu_holo", player);
    holo.delete("meu_holo");
});
```

### Mochilas

```java
import io.github.otiger.nexusprism.api.backpack.BackpackRegistry;

BackpackRegistry.get().ifPresent(bp -> {
    int quantidade = bp.getBackpackCount(uuid);
    bp.openFirstBackpack(player);
    bp.openBackpack(player, ids.get(0));
});
```

### Traits (Cartas de Tarô)

```java
import io.github.otiger.nexusprism.api.traits.TraitsRegistry;

TraitsRegistry.get().ifPresent(traits -> {
    List<String> cartas = traits.getCards(uuid);
    boolean temCarta    = traits.hasCard(uuid, "The Tower");
    int nivelPesquisa   = traits.getResearchLevel(uuid);
});
```

### Discord

```java
import io.github.otiger.nexusprism.api.discord.DiscordRegistry;

DiscordRegistry.get().ifPresent(discord -> {
    boolean vinculado = discord.isLinked(uuid);
    discord.sendMessage("server-log", "[MeuAddon] Algo aconteceu!");
    discord.sendWebhook("server-log", "Bot MeuAddon", null, "Jogador fez algo.");
});
```

### Empregos

```java
import io.github.otiger.nexusprism.api.economy.JobRegistry;

JobRegistry.get().ifPresent(empregos -> {
    Optional<String> empregoId = empregos.getActiveJob(uuid);
    boolean temEmprego = empregos.hasJob(uuid);
    if (temEmprego) {
        int nivel = empregos.getLevel(uuid, empregoId.get());
    }
    empregos.joinJob(uuid, "miner");
    empregos.leaveJob(uuid);
});
```

### Redes de Energia

```java
import io.github.otiger.nexusprism.api.energy.EnergyRegistry;

EnergyRegistry.get().ifPresent(energia -> {
    energia.getNetworkAt(location).ifPresent(rede -> {
        long armazenado = rede.getTotalStoredEnergy();
        long cap        = rede.getTotalCapacity();
        int  fluxo      = rede.getNetFlow();
    });
    energia.registerComponent(meuComponente);
    energia.unregisterComponent(meuComponente);
});
```

---

## Passo 10 — Carregamento de Conteúdo de Addons

Addons nativos podem registrar **itens**, **máquinas**, **receitas de crafting** e **receitas de infinity** diretamente de arquivos YAML empacotados no JAR.

```java
ContentLoadResult result = content()
        .items("items.yml")
        .machines("machines.yml")
        .recipes("recipes.yml")
        .infinityRecipes("infinity_recipes")
        .register();

result.logTo(getLogger());
```

### Receitas de Processamento de Máquinas (programático)

```java
import io.github.otiger.nexusprism.api.machines.recipe.MachineProcessingRecipe;
import io.github.otiger.nexusprism.api.machines.recipe.MachineProcessingRegistry;

MachineProcessingRegistry.register(
    MachineProcessingRecipe.builder("minha_receita", "EXAMPLE_FURNACE")
            .input("DIAMOND", 1)
            .output("EXAMPLE_INGOT", 3)
            .time(120)
            .source(getId())
            .build()
);

// Em onDisable — sempre limpe:
MachineProcessingRegistry.unregisterBySource(getId());
```

---

## Passo 5 — Itens personalizados

Use `NexusItemBuilder` para inspecionar qualquer `ItemStack` e verificar se é um item personalizado do NexusPrism.

```java
import io.github.otiger.nexusprism.api.items.builder.NexusItemBuilder;

ItemStack item = player.getInventory().getItemInMainHand();

// Obter o ID interno do item (ex: "COPPER_DUST", "CELESTIAL_SWORD")
String id = NexusItemBuilder.getItemId(item); // null se não for item NexusPrism

if ("CELESTIAL_SWORD".equals(id)) {
    player.sendMessage("Você está segurando a Espada Celestial!");
}
```

Para criar um item do registro:

```java
import io.github.otiger.nexusprism.api.registry.ItemRegistry;

ItemRegistry registro = nexus.getService(ItemRegistry.class);
if (registro != null) {
    registro.getItem("COPPER_DUST").ifPresent(nexusItem -> {
        ItemStack stack = nexusItem.buildStack(1);
        player.getInventory().addItem(stack);
    });
}
```

---

## Passo 6 — API de Território

Se você estiver construindo um sistema de reivindicação de terrenos e quiser que ele se integre às verificações de proteção do NexusPrism, implemente `TerritoryProvider` e registre-o.

```java
import io.github.otiger.nexusprism.api.territory.TerritoryProvider;
import io.github.otiger.nexusprism.api.territory.TerritoryRegistry;

public class MeuProvedorRegiao implements TerritoryProvider {

    @Override
    public boolean isClaimed(Location location) {
        return MeuGerenciadorRegiao.isClaimed(location);
    }

    @Override
    public boolean canBuild(Player player, Location location) {
        return MeuGerenciadorRegiao.canBuild(player, location);
    }

    @Override
    public boolean canInteract(Player player, Location location) {
        return MeuGerenciadorRegiao.canInteract(player, location);
    }

    @Override
    public Optional<String> getClaimName(Location location) {
        return MeuGerenciadorRegiao.getRegionName(location);
    }
}
```

```java
private final MeuProvedorRegiao provedor = new MeuProvedorRegiao();

@Override
public void onEnable() {
    TerritoryRegistry.register(provedor);
}

@Override
public void onDisable() {
    TerritoryRegistry.unregister(provedor);
}
```

> O NexusPrism usa agregação **deny-wins**: se qualquer provedor negar `canBuild`, a ação é bloqueada.

---

## Passo 7 — Flags de eventos

`EventFlags` expõe flags de estado em tempo real do módulo de eventos.

```java
import io.github.otiger.nexusprism.api.events.EventFlags;

// A Lua de Sangue está ativa?
if (EventFlags.bloodMoonActive) {
    // Aplique efeitos especiais...
}

// Multiplicador de recompensa por kill (1.0 = normal, 1.5 = +50% na Lua de Sangue)
double multiplicador = EventFlags.killPayMultiplier;
double recompensa = baseRecompensa * multiplicador;
```

---

## Passo 8 — Injeção de loot em estruturas

Registre um `StructureProvider` para injetar loot personalizado em estruturas vanilla durante a geração.

```java
import io.github.otiger.nexusprism.api.structures.StructureProvider;
import io.github.otiger.nexusprism.api.structures.StructureRegistry;

public class MeuLootProvider implements StructureProvider {

    @Override
    public NamespacedKey structure() {
        return NamespacedKey.minecraft("village/plains/houses/plains_small_house_1");
    }

    @Override
    public List<ItemStack> loot() {
        return List.of(new ItemStack(Material.DIAMOND, 1));
    }
}

// Registrar no onEnable:
StructureRegistry.register(new MeuLootProvider());
```

---

## Passo 9 — Escrevendo um addon nativo

Addons nativos são JARs colocados em `plugins/NexusPrism/addons/`. Eles são carregados diretamente pelo NexusPrism e não precisam de `plugin.yml` próprio.

### 1. Criar a classe do addon

```java
import io.github.otiger.nexusprism.api.addon.AbstractNexusAddon;

public class MeuAddon extends AbstractNexusAddon {

    @Override
    public void onEnable() {
        saveDefaultConfig();
        String msg = getConfig().getString("mensagem-boas-vindas", "Olá!");
        getLogger().info(msg);
        getLogger().info("Conectado — NexusPrism " + getAPI().getVersion());
    }

    @Override
    public void onDisable() {
        getLogger().info(getName() + " desativado.");
    }
}
```

### 2. Criar `addon.yml` dentro do JAR

```yaml
id: meu-addon
name: Meu Addon
version: 1.0.0
description: Demonstra a API de addon do NexusPrism.
authors:
  - SeuNome
main: com.exemplo.MeuAddon
min-nexus-version: 1.0.0
dependencies: []
soft-dependencies: []
```

### 3. Compilar e instalar

```
mvn package
cp target/meu-addon-1.0.0.jar plugins/NexusPrism/addons/
```

---

## Passo 11 — Provedores de integração (permissões, placeholders, idioma)

Estas três interfaces ficam em `nexusprism-api` e são usadas pelo NexusPrism internamente. Addons podem lê-las via `getService()` ou implementá-las para substituir/estender o comportamento padrão.

### PermissionProvider

Abstrai o sistema de permissões subjacente (LuckPerms, Vault, etc.). Obtenha o provedor ativo para consultar grupos, prefix/suffix e metadados sem dependência em tempo de compilação do LuckPerms.

```java
import io.github.otiger.nexusprism.api.integration.PermissionProvider;

PermissionProvider perms = NexusPrismAPI.get().getService(PermissionProvider.class);
if (perms == null || !perms.isAvailable()) return;

boolean isAdmin = perms.hasPermission(player, "nexusprism.admin");
String grupo    = perms.getPrimaryGroup(player).orElse("default");
String prefix   = perms.getPrefix(player).orElse("");
int tier        = perms.getNexusTierLevel(player); // 1–5, 0 se nenhum
```

### PlaceholderProvider

SPI que o NexusPrism expõe para a ponte PAPI. Implemente e registre para adicionar novos identificadores `%nexusprism_*%` a partir do seu addon.

```java
import io.github.otiger.nexusprism.api.integration.PlaceholderProvider;

public class MeusPlaceholders implements PlaceholderProvider {
    @Override public String getIdentifier() { return "meuaddon"; }

    @Override
    public String onPlaceholderRequest(Player player, String params) {
        if ("pontos".equals(params)) return String.valueOf(MeuAddon.getPontos(player));
        return null;
    }
}
```

### LangProvider

Implementado pelo `LanguageManager` do core. Obtenha-o para buscar mensagens traduzidas e coloridas para um jogador específico (respeitando o idioma escolhido).

```java
import io.github.otiger.nexusprism.api.lang.LangProvider;

LangProvider lang = NexusPrismAPI.get().getService(LangProvider.class);
if (lang == null) return;

String msg = lang.getMsg(player.getUniqueId(), "chat.channel-switched", "channel", "Global");
player.sendMessage(msg);

lang.setPlayerLanguage(player.getUniqueId(), "pt_BR");
List<String> disponiveis = lang.getAvailableLanguages(); // ["en_US", "pt_BR", ...]
```

---

## Exemplo completo de integração

Plugin que recompensa jogadores com dinheiro ao matar, respeitando o multiplicador da Lua de Sangue:

```java
package com.exemplo;

import io.github.otiger.nexusprism.api.NexusPrismAPI;
import io.github.otiger.nexusprism.api.events.EventFlags;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.PlayerDeathEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class RecompensaKillPlugin extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        if (NexusPrismAPI.get() == null) {
            getLogger().warning("NexusPrism não encontrado — recompensas desativadas.");
            return;
        }
        getServer().getPluginManager().registerEvents(this, this);
    }

    @EventHandler
    public void onMorteJogador(PlayerDeathEvent event) {
        if (!(event.getEntity().getKiller() instanceof Player killer)) return;

        double base = 25.0;
        double recompensa = base * EventFlags.killPayMultiplier;

        NexusPrismAPI.economy().ifPresent(eco -> {
            eco.addMoney(killer.getUniqueId(), recompensa);
            killer.sendMessage("§a+$" + String.format("%.0f", recompensa) + " §7pela kill!");
        });
    }
}
```

---

## Referência Rápida

| Superfície da API | Classe / método |
|---|---|
| Obter instância da API | `NexusPrismAPI.get()` |
| **Provedores principais** | |
| Economia | `NexusPrismAPI.economy()` → `EconomyProvider` |
| Auth | `NexusPrismAPI.auth()` → `AuthProvider` |
| Clãs | `NexusPrismAPI.clans()` → `ClanProvider` |
| Essentials | `NexusPrismAPI.essentials()` → `EssentialsProvider` |
| Votos | `NexusPrismAPI.votes()` → `VoteProvider` |
| Encantamentos | `NexusPrismAPI.enchants()` → `CustomEnchantProvider` |
| Caixas | `NexusPrismAPI.crates()` → `CrateProvider` |
| **Provedores de módulos** | |
| MMO (nível, stats, mana, skills, profissões) | `MmoRegistry.get()` → `MmoProvider` |
| Chat (silêncio, canais, broadcast) | `ChatRegistry.get()` → `ChatProvider` |
| Proteções (PvP, regiões, duelos) | `ProtectionsRegistry.get()` → `ProtectionsProvider` |
| Eventos (Lua de Sangue, Sacrifício, Isekai) | `EventsRegistry.get()` → `EventsProvider` |
| Hologramas (criar, atualizar, mostrar/ocultar) | `HologramRegistry.get()` → `HologramProvider` |
| Mochilas (quantidade, abrir GUI) | `BackpackRegistry.get()` → `BackpackProvider` |
| Traits / Cartas de Tarô | `TraitsRegistry.get()` → `TraitsProvider` |
| Discord (vincular, enviar mensagem/webhook) | `DiscordRegistry.get()` → `DiscordProvider` |
| Empregos (emprego ativo, nível, XP) | `JobRegistry.get()` → `JobProvider` |
| Redes de energia | `EnergyRegistry.get()` → `EnergyProvider` |
| **Provedores de integração** | |
| Backend de permissões (grupos, prefix, meta) | `nexus.getService(PermissionProvider.class)` |
| Expansão de placeholders (ponte PAPI) | `nexus.getService(PlaceholderProvider.class)` |
| Idioma / tradução | `nexus.getService(LangProvider.class)` |
| **Conteúdo e extensibilidade** | |
| Carregamento de conteúdo de addon | `content().items().machines().recipes().register()` |
| Receitas de processamento de máquinas | `MachineProcessingRegistry.register(MachineProcessingRecipe)` |
| ID de item | `NexusItemBuilder.getItemId(ItemStack)` |
| Registro de itens | `nexus.getService(ItemRegistry.class)` |
| Território | `TerritoryRegistry.register(TerritoryProvider)` |
| Estado de eventos | `EventFlags.bloodMoonActive`, `EventFlags.killPayMultiplier` |
| Estruturas | `StructureRegistry.register(StructureProvider)` |
| Base de addon nativo | `AbstractNexusAddon` + `addon.yml` |
| Template inicial | [O-Tiger/NexusPrism-Addon-Example](https://github.com/Tg-TheNexus/NexusPrism-Addon-Example) |

---

## ResearchManager

Acesse a árvore de pesquisa e o progresso do jogador de forma programática.

```java
ResearchManager research = NexusPrismAPI.get().getService(ResearchManager.class);
```

> `ResearchManager` é um sistema central, não um provider de módulo. Não é acessível via o padrão provider/registry — use `getService()`.

```java
```

### Verificando o status de pesquisa

```java
// Via PlayerData (disponível em qualquer evento de entrada de jogador ou em seu próprio listener)
boolean hasUnlocked = playerData.hasCompletedResearch("copper_wire_research");
Set<String> done = playerData.getCompletedResearches();
```

### Formato de entrada do researches.yml

```yaml
copper_wire_research:
  name: "Copper Wire"
  description: "Desbloqueia a receita de crafting para Copper Wire."
  tier: BASIC                    # BASIC | ADVANCED | INFINITY
  parchment-cost: 1              # número de pergaminhos consumidos
  dependencies: []               # lista de IDs de entradas que devem ser concluídas antes
  unlocks:
    - COPPER_WIRE                # IDs de itens adicionados aos itens desbloqueados do jogador
```

### Tiers e pergaminhos

| Tier | Item de pergaminho |
|---|---|
| BASIC | `RESEARCH_PARCHMENT_BASIC` |
| ADVANCED | `RESEARCH_PARCHMENT_ADVANCED` |
| INFINITY | `RESEARCH_PARCHMENT_INFINITY` |

---

## Ícones de Categoria do Guia (`gui_items.yml`)

Desde a v2.3.0, o ícone de material para cada categoria e tier do guia é definido em `gui_items.yml` em vez de estar codificado diretamente no Java.

```yaml
# gui_items.yml
categories:
  MY_CATEGORY:
    material: ENCHANTING_TABLE
tiers:
  MY_TIER:
    material: DRAGON_EGG
```

O guia reconhece as entradas automaticamente no reload. Substituições em `guide.yml` têm prioridade maior do que `gui_items.yml`. Entradas em `gui_items.yml` não presentes em `guide.yml` utilizam o valor definido aqui.

---

## Boas práticas

- **Sempre verifique null** em `NexusPrismAPI.get()` antes de usar qualquer provedor.
- **Use `softdepend`** a menos que seu plugin seja literalmente um JAR de addon.
- **Nunca faça shade** de `nexusprism-api` — use escopo `provided`/`compileOnly`.
- **Cancele o registro de provedores** no `onDisable()` para evitar listeners fantasma após reload.
- **Use cadeias de `Optional`** (`ifPresent`, `orElse`) — nunca chame `.get()` em um Optional vazio.
- **Verifique `isReady()`** se você chamar a API imediatamente no enable.
