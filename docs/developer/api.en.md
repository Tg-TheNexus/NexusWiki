# NexusPrism Developer API

*Last updated: 2026-03-22*

> ⚠️ **Partially outdated (flagged 2026-08-06, not yet rewritten).** The `Backpacks`,
> `Energy networks`, `Item registry`, and `ResearchManager` sections below describe an API
> (`NexusPrismAPI.get().getService(...)`, `BackpackRegistry`, `EnergyRegistry`, `ItemRegistry`)
> that was **confirmed to never actually exist in the codebase** — no such service is
> registered via Bukkit's `ServicesManager` anywhere, and the underlying systems
> (`BackpackManager`, energy, research) were dead code, since removed (see
> `NexusATS/docs/planning/PLAN-presplit-core-infra.md`). That whole domain now belongs to
> NexusATS — do not build against the sections below. The generic hooks that **do** exist
> today are `NexusPrism.registerBlockClassifier()`, `registerAddonCommand()`/
> `registerAddonTabCompleter()`, and `DataManager.setPlayerField()`/`getPlayerField()` — see
> `ECOSYSTEM.md` at the root of the ecosystem repo for current, verified examples.

This guide walks through integrating with NexusPrism from an external Bukkit/Paper plugin or a native addon JAR. You only ever compile against `nexusprism-api` — never against concrete module JARs.

---

## Step 1 — Add the dependency

NexusPrism is published through **JitPack**. Add the repository and the API artifact to your `pom.xml`:

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
        <version>master-SNAPSHOT</version> <!-- or a specific commit hash -->
        <scope>provided</scope>
    </dependency>
</dependencies>
```

> **`provided` scope is required.** NexusPrism ships the API at runtime — do not shade it into your JAR.

For Gradle (Kotlin DSL):

```kotlin
repositories {
    maven("https://jitpack.io")
}

dependencies {
    compileOnly("com.github.Tg-TheNexus.NexusPrismModularizado:nexusprism-api:master-SNAPSHOT")
}
```

---

## Step 2 — Declare the dependency in `plugin.yml`

Because NexusPrism is optional for most integrations, use `softdepend`. Use `depend` only if your plugin cannot function at all without it.

```yaml
name: MyPlugin
version: 1.0.0
main: com.example.MyPlugin
api-version: "1.21"

softdepend:
  - NexusPrism
```

---

## Step 3 — Get the API instance

Always obtain the API inside `onEnable()`, **after** the server is fully started (or listen for `ServerLoadEvent`). Never call it from a static initializer or constructor.

```java
import io.github.otiger.nexusprism.api.NexusPrismAPI;

public class MyPlugin extends JavaPlugin {

    private NexusPrismAPI nexus;

    @Override
    public void onEnable() {
        nexus = NexusPrismAPI.get();

        if (nexus == null) {
            getLogger().warning("NexusPrism not found — integration disabled.");
            return;
        }

        if (!nexus.isReady()) {
            // NexusPrism loaded but hasn't finished startup yet
            // Listen to ServerLoadEvent or use Bukkit.getScheduler().runTaskLater(...)
            getLogger().warning("NexusPrism is still starting up.");
            return;
        }

        getLogger().info("Hooked into NexusPrism " + nexus.getVersion());
    }
}
```

---

## Step 4 — Module providers

Each optional NexusPrism module exposes a typed provider through a static registry. All providers return `Optional` — if the module is disabled or not installed, the Optional is empty. Always use `ifPresent` or `orElse` to handle this safely.

### Economy

```java
import io.github.otiger.nexusprism.api.NexusPrismAPI;

UUID uuid = player.getUniqueId();

// Read balance
double balance = NexusPrismAPI.economy()
        .map(eco -> eco.getBalance(uuid))
        .orElse(0.0);

// Add money
NexusPrismAPI.economy().ifPresent(eco -> eco.addMoney(uuid, 500.0));

// Charge player (returns false if insufficient funds)
boolean success = NexusPrismAPI.economy()
        .map(eco -> eco.withdrawMoney(uuid, 100.0))
        .orElse(false);

// Top balances
NexusPrismAPI.economy().ifPresent(eco -> {
    eco.getTopBalances(10).forEach(entry ->
        System.out.println(entry.uuid() + " → " + entry.balance()));
});
```

### Authentication / Security

```java
// Check if a player is logged in (defaults to true when auth module absent)
boolean loggedIn = NexusPrismAPI.auth()
        .map(auth -> auth.isAuthenticated(uuid))
        .orElse(true);
```

### Clans

```java
// Get a player's clan tag
String tag = NexusPrismAPI.clans()
        .flatMap(c -> c.getClanTag(uuid))
        .orElse("");

// Check clan membership
boolean hasClan = NexusPrismAPI.clans()
        .map(c -> c.isInClan(uuid))
        .orElse(false);
```

### Essentials

```java
// Teleport a player to their home named "base"
NexusPrismAPI.essentials().ifPresent(ess ->
        ess.teleportHome(player, "base"));

// Check AFK status
boolean isAfk = NexusPrismAPI.essentials()
        .map(ess -> ess.isAfk(uuid))
        .orElse(false);
```

### Votes

```java
// Get a player's total vote count
int votes = NexusPrismAPI.votes()
        .map(v -> v.getTotalVotes(uuid))
        .orElse(0);

// Get current vote streak
int streak = NexusPrismAPI.votes()
        .map(v -> v.getStreak(uuid))
        .orElse(0);
```

### Custom Enchantments

```java
// Check if a tool has a specific custom enchant applied
boolean hasEnchant = NexusPrismAPI.enchants()
        .map(e -> e.hasEnchant(item, "SOUL_MENDER"))
        .orElse(false);

// Get the level of a custom enchant on an item
int level = NexusPrismAPI.enchants()
        .map(e -> e.getLevel(item, "SOUL_MENDER"))
        .orElse(0);
```

### Crates

```java
// Give a player a crate key
NexusPrismAPI.crates().ifPresent(c ->
        c.giveKey(player, "VOTE_CRATE", 1));
```

### MMO

```java
import io.github.otiger.nexusprism.api.mmo.MmoRegistry;

UUID uuid = player.getUniqueId();

MmoRegistry.get().ifPresent(mmo -> {
    int level  = mmo.getLevel(uuid);
    int mana   = mmo.getCurrentMana(uuid);
    int maxMana = mmo.getMaxMana(uuid);

    // Consume mana (returns false if not enough)
    if (mmo.hasMana(uuid, 20) && mmo.consumeMana(uuid, 20)) {
        // ability triggered
    }

    // Add XP to a skill tree
    mmo.addSkillXp(player, "warrior", 100L);

    // Add XP to a profession
    mmo.addProfessionXp(player, "mining", 50L);

    // Stat access
    int strength = mmo.getStat(uuid, "STRENGTH");
    List<String> abilities = mmo.getUnlockedAbilityIds(uuid);
});
```

### Chat

```java
import io.github.otiger.nexusprism.api.chat.ChatRegistry;

ChatRegistry.get().ifPresent(chat -> {
    // Mute checks
    boolean muted = chat.isMuted(uuid);

    // Mute for 10 minutes
    chat.mute(uuid, 10 * 60 * 1000L, "Spam", "Console");

    // Broadcast to a channel
    chat.broadcastToChannel("global", "[MyAddon] Server announcement!");

    // Get which channel a player is currently active in
    String activeChannel = chat.getActiveChannel(uuid);
});
```

### Protections

```java
import io.github.otiger.nexusprism.api.protections.ProtectionsRegistry;

ProtectionsRegistry.get().ifPresent(prot -> {
    // PvP check at a location
    boolean pvp = prot.isPvpAllowed(location);

    // Duel state
    boolean inDuel = prot.isInDuel(uuid);
    prot.getDuelOpponent(uuid).ifPresent(opponentUuid -> { /* ... */ });

    // Region info
    List<String> regions = prot.getRegionNamesAt(location);
    prot.getRegionOwnerAt(location).ifPresent(ownerUuid -> { /* ... */ });
    int claimed = prot.getRegionCount(uuid);
});
```

### Events (Blood Moon, Sacrifice Arc, Anime Boss)

```java
import io.github.otiger.nexusprism.api.events.EventsRegistry;

EventsRegistry.get().ifPresent(events -> {
    boolean moonActive = events.isBloodMoonActive();
    boolean inWorld    = events.isBloodMoonActive(player.getWorld());

    int streak         = events.getSacrificeStreak(uuid);
    boolean inSacrifice = events.isInSacrifice(uuid);
    boolean hasBoss    = events.hasActiveBossFight(uuid);

    // Check if player needs to sacrifice (streak milestone reached)
    boolean mustSacrifice = events.needsSacrifice(uuid);
});
```

### Holograms

```java
import io.github.otiger.nexusprism.api.holograms.HologramRegistry;

HologramRegistry.get().ifPresent(holo -> {
    holo.create("my_holo", location);
    holo.addLine("my_holo", "§aHello from my addon!");
    holo.setLine("my_holo", 0, "§eUpdated line");
    holo.removeLine("my_holo", 0);
    holo.moveTo("my_holo", newLocation);

    // Per-player visibility
    holo.showToPlayer("my_holo", player);
    holo.hideFromPlayer("my_holo", player);

    // Cleanup
    holo.delete("my_holo");
});
```

### Backpacks

```java
import io.github.otiger.nexusprism.api.backpack.BackpackRegistry;

BackpackRegistry.get().ifPresent(bp -> {
    int count   = bp.getBackpackCount(uuid);
    int maxCount = bp.getMaxBackpacks(uuid);
    boolean can = bp.canCreateBackpack(player);

    List<UUID> ids = bp.getBackpackIds(uuid);

    // Open GUIs
    bp.openFirstBackpack(player);              // opens first backpack
    bp.openBackpack(player, ids.get(0));       // opens specific one
});
```

### Traits (Tarot cards)

```java
import io.github.otiger.nexusprism.api.traits.TraitsRegistry;

TraitsRegistry.get().ifPresent(traits -> {
    List<String> cards = traits.getCards(uuid);     // card names the player holds
    boolean hasCard    = traits.hasCard(uuid, "The Tower");
    int researchLevel  = traits.getResearchLevel(uuid);
    traits.setResearchLevel(uuid, 5);

    // All available card names
    List<String> allCards = traits.getCardNames();

    // Cooldown info (ms remaining)
    long rerollMs = traits.fullRerollCooldownRemainingMs(uuid);
});
```

### Discord

```java
import io.github.otiger.nexusprism.api.discord.DiscordRegistry;

DiscordRegistry.get().ifPresent(discord -> {
    // Link status
    boolean linked = discord.isLinked(uuid);
    discord.getDiscordId(uuid).ifPresent(discordId -> { /* ... */ });
    discord.getMinecraftUuid("123456789").ifPresent(mcUuid -> { /* ... */ });

    // Send a plain message to a configured channel
    discord.sendMessage("server-log", "[MyAddon] Something happened!");

    // Send a webhook-style message with custom display name and avatar
    discord.sendWebhook("server-log", "MyAddon Bot", null, "Player did a thing.");

    // Generate a link code for a player
    String code = discord.generateLinkCode(uuid);
    player.sendMessage("Your link code: " + code);
});
```

### Jobs

```java
import io.github.otiger.nexusprism.api.economy.JobRegistry;

JobRegistry.get().ifPresent(jobs -> {
    Optional<String> jobId = jobs.getActiveJob(uuid);
    boolean hasJob = jobs.hasJob(uuid);

    if (hasJob) {
        int level = jobs.getLevel(uuid, jobId.get());
        long xp   = jobs.getXp(uuid, jobId.get());
    }

    List<String> allJobs = jobs.getAllJobIds(); // e.g. ["miner", "farmer", "hunter"]

    // Force-join a job
    jobs.joinJob(uuid, "miner");

    // Leave current job
    jobs.leaveJob(uuid);
});
```

### Energy networks

```java
import io.github.otiger.nexusprism.api.energy.EnergyRegistry;

EnergyRegistry.get().ifPresent(energy -> {
    energy.getNetworkAt(location).ifPresent(net -> {
        long stored = net.getTotalStoredEnergy();
        long cap    = net.getTotalCapacity();
        int  netFlow = net.getNetFlow(); // positive = surplus
    });

    // Register / unregister a custom EnergyComponent
    energy.registerComponent(myComponent);    // call in onEnable / block-place listener
    energy.unregisterComponent(myComponent);  // call in onDisable / block-break listener
});
```

---

## Step 5 — Custom items

Use `NexusItemBuilder` to inspect any `ItemStack` and check whether it is a NexusPrism custom item.

```java
import io.github.otiger.nexusprism.api.items.builder.NexusItemBuilder;

ItemStack item = player.getInventory().getItemInMainHand();

// Get the internal item ID (e.g. "COPPER_DUST", "CELESTIAL_SWORD")
String id = NexusItemBuilder.getItemId(item); // null if not a NexusPrism item

if ("CELESTIAL_SWORD".equals(id)) {
    player.sendMessage("You are holding the Celestial Sword!");
}
```

You can also resolve a custom item from the registry via `getService`:

```java
import io.github.otiger.nexusprism.api.registry.ItemRegistry;

ItemRegistry registry = nexus.getService(ItemRegistry.class);
if (registry != null) {
    registry.getItem("COPPER_DUST").ifPresent(nexusItem -> {
        ItemStack stack = nexusItem.buildStack(1);
        player.getInventory().addItem(stack);
    });
}
```

---

## Step 6 — Territory API

If you are building a land-claiming or region system and want it to integrate with NexusPrism's protection checks (machine placement, clan building rules, etc.), implement `TerritoryProvider` and register it.

```java
import io.github.otiger.nexusprism.api.territory.TerritoryProvider;
import io.github.otiger.nexusprism.api.territory.TerritoryRegistry;
import org.bukkit.Location;
import org.bukkit.entity.Player;

public class MyRegionProvider implements TerritoryProvider {

    @Override
    public boolean isClaimed(Location location) {
        return MyRegionManager.isClaimed(location);
    }

    @Override
    public boolean canBuild(Player player, Location location) {
        return MyRegionManager.canBuild(player, location);
    }

    @Override
    public boolean canInteract(Player player, Location location) {
        return MyRegionManager.canInteract(player, location);
    }

    @Override
    public java.util.Optional<String> getClaimName(Location location) {
        return MyRegionManager.getRegionName(location);
    }
}
```

Register and unregister in your plugin's lifecycle:

```java
private final MyRegionProvider provider = new MyRegionProvider();

@Override
public void onEnable() {
    TerritoryRegistry.register(provider);
}

@Override
public void onDisable() {
    TerritoryRegistry.unregister(provider);
}
```

> NexusPrism uses **deny-wins** aggregation: if any registered provider denies `canBuild`, the action is blocked.

---

## Step 7 — Event flags

`EventFlags` exposes live server-state flags from the Events module. Read these to react to Blood Moon and economy multipliers.

```java
import io.github.otiger.nexusprism.api.events.EventFlags;

// Is the Blood Moon currently active?
if (EventFlags.bloodMoonActive) {
    // Double your boss spawn rates, apply particle effects, etc.
}

// Current economy kill-pay multiplier (1.0 = normal, 1.5 = +50% during Blood Moon)
double multiplier = EventFlags.killPayMultiplier;
double reward = baseReward * multiplier;
```

---

## Step 8 — Structure loot injection

Register a `StructureProvider` to inject custom loot into vanilla structures when they are generated.

```java
import io.github.otiger.nexusprism.api.structures.StructureProvider;
import io.github.otiger.nexusprism.api.structures.StructureRegistry;
import org.bukkit.NamespacedKey;
import org.bukkit.inventory.ItemStack;
import java.util.List;

public class MyLootProvider implements StructureProvider {

    @Override
    public NamespacedKey structure() {
        return NamespacedKey.minecraft("village/plains/houses/plains_small_house_1");
    }

    @Override
    public List<ItemStack> loot() {
        // Return items to inject into chests inside this structure
        return List.of(new ItemStack(Material.DIAMOND, 1));
    }
}
```

```java
// Register on enable, unregister on disable
StructureRegistry.register(new MyLootProvider());
```

---

## Step 9 — Writing a native addon

Native addons are JAR files dropped into `plugins/NexusPrism/addons/`. They are loaded by NexusPrism directly and do not need their own `plugin.yml`.

### 1. Create the addon class

```java
import io.github.otiger.nexusprism.api.addon.AbstractNexusAddon;
import io.github.otiger.nexusprism.api.NexusPrismAPI;

public class MyAddon extends AbstractNexusAddon {

    @Override
    public void onEnable() {
        // Load config (reads config.yml from JAR if not yet extracted)
        saveDefaultConfig();
        String welcomeMsg = getConfig().getString("welcome-message", "Hello!");
        getLogger().info(welcomeMsg);

        // Use the API
        NexusPrismAPI api = getAPI();
        getLogger().info("Hooked — NexusPrism " + api.getVersion());

        // Register a territory provider
        TerritoryRegistry.register(new MyRegionProvider());
    }

    @Override
    public void onDisable() {
        TerritoryRegistry.unregister(myProvider);
        getLogger().info(getName() + " disabled.");
    }
}
```

### 2. Create `addon.yml` inside the JAR

```yaml
id: my-addon
name: My Addon
version: 1.0.0
description: Demonstrates the NexusPrism addon API.
authors:
  - YourName
main: com.example.MyAddon
min-nexus-version: 1.0.0

# Hard dependencies (must be present):
dependencies: []

# Optional dependencies (loaded first if present):
soft-dependencies: []
```

### 3. Build and install

```
mvn package
cp target/my-addon-1.0.0.jar plugins/NexusPrism/addons/
```

Restart the server. You should see:

```
[NexusPrism] [MyAddon] Hello!
[NexusPrism] [MyAddon] Hooked — NexusPrism 1.0.0-DEV
```

!!! tip "Starter template"
    A ready-to-clone Maven project is available at **[O-Tiger/NexusPrism-Addon-Example](https://github.com/Tg-TheNexus/NexusPrism-Addon-Example)**. It includes working examples of every API surface described in this guide.

---

## Step 10 — Content loading from addons

Native addons can register custom **items**, **machines**, **crafting recipes**, and **infinity recipes** directly from YAML files bundled in their JAR. NexusPrism merges this content into the server registry at load time.

```java
import io.github.otiger.nexusprism.api.content.ContentLoadResult;

@Override
public void onEnable() {
    // content() returns a fluent builder scoped to this addon.
    // Files are read from the addon's data folder first,
    // then extracted from the JAR if not found on disk.
    ContentLoadResult result = content()
            .items("items.yml")               // custom item definitions
            .machines("machines.yml")         // custom machine type definitions
            .recipes("recipes.yml")           // standard crafting recipes
            .infinityRecipes("infinity_recipes") // all *.yml in this directory
            .register();

    result.logTo(getLogger()); // prints counts & errors
}
```

### Machine processing recipes (programmatic)

If you want to add input→output rules to an **existing machine type** from code (rather than YAML), use `MachineProcessingRegistry`. The engine checks these alongside YAML-defined recipes.

```java
import io.github.otiger.nexusprism.api.machines.recipe.MachineProcessingRecipe;
import io.github.otiger.nexusprism.api.machines.recipe.MachineProcessingRegistry;

@Override
public void onEnable() {
    MachineProcessingRegistry.register(
        MachineProcessingRecipe.builder("my_addon_recipe", "EXAMPLE_FURNACE")
                .input("DIAMOND", 1)
                .input("EXAMPLE_DUST", 4)
                .output("EXAMPLE_INGOT", 3)
                .time(120)          // ticks; 0 = machine default
                .source(getId())    // used for cleanup on disable
                .build()
    );
}

@Override
public void onDisable() {
    // Always clean up — avoids stale entries after reload
    MachineProcessingRegistry.unregisterBySource(getId());
}
```

---

## Step 11 — Integration providers (permissions, placeholders, language)

These three interfaces live in `nexusprism-api` and are used by NexusPrism internally. Addons can read from them via `getService()` or implement them to override / extend the default behaviour.

### PermissionProvider

NexusPrism uses `PermissionProvider` to abstract away the underlying permission plugin (LuckPerms, Vault, etc.). Obtain the active provider to query groups, prefix/suffix and meta values without a hard compile-time dependency on LuckPerms.

```java
import io.github.otiger.nexusprism.api.integration.PermissionProvider;

NexusPrismAPI nexus = NexusPrismAPI.get();
if (nexus == null) return;

PermissionProvider perms = nexus.getService(PermissionProvider.class);
if (perms == null || !perms.isAvailable()) return;

// Check a permission node
boolean isAdmin = perms.hasPermission(player, "nexusprism.admin");

// Get the LuckPerms group (or equivalent)
String group = perms.getPrimaryGroup(player).orElse("default");

// Get all groups
List<String> groups = perms.getPlayerGroups(player);

// Prefix and suffix (colorised, ready to prepend to chat)
String prefix = perms.getPrefix(player).orElse("");
String suffix = perms.getSuffix(player).orElse("");

// Custom meta key
String tier = perms.getMeta(player, "nexus-tier").orElse("0");

// NexusPrism tier level derived from nexusprism.tier.* permissions (1–5, 0 = none)
int tierLevel = perms.getNexusTierLevel(player);
```

### PlaceholderProvider

`PlaceholderProvider` is the SPI NexusPrism exposes to its PAPI bridge. Implement and register it to add new `%nexusprism_*%` placeholder identifiers from your addon.

```java
import io.github.otiger.nexusprism.api.integration.PlaceholderProvider;

public class MyAddonPlaceholders implements PlaceholderProvider {

    @Override
    public String getIdentifier() {
        return "myaddon"; // resolves %myaddon_<params>%
    }

    @Override
    public String onPlaceholderRequest(Player player, String params) {
        if ("score".equals(params)) {
            return String.valueOf(MyAddon.getScore(player));
        }
        return null; // return null to indicate the placeholder wasn't handled
    }
}
```

Register in `onEnable()`:

```java
NexusPrismAPI nexus = NexusPrismAPI.get();
if (nexus != null) {
    PlaceholderProvider existing = nexus.getService(PlaceholderProvider.class);
    // Registration is done through the PAPI expansion — addons that depend
    // on the NexusPrism PAPI expansion will have their providers bridged
    // automatically when PlaceholderAPI is present on the server.
}
```

### LangProvider

`LangProvider` is implemented by NexusPrism's core `LanguageManager`. Obtain it to fetch translated, colourised messages for a specific player (respecting their chosen language).

```java
import io.github.otiger.nexusprism.api.lang.LangProvider;

NexusPrismAPI nexus = NexusPrismAPI.get();
if (nexus == null) return;

LangProvider lang = nexus.getService(LangProvider.class);
if (lang == null) return;

// Fetch a message (returns the key itself if not found)
String msg = lang.getMsg(player.getUniqueId(), "chat.channel-switched", "channel", "Global");
player.sendMessage(msg);

// Check and change a player's language preference
String current = lang.getPlayerLanguage(player.getUniqueId()); // e.g. "en_US"
lang.setPlayerLanguage(player.getUniqueId(), "pt_BR");         // returns false if file not found

// List all available language files
List<String> available = lang.getAvailableLanguages(); // ["en_US", "pt_BR", "es_ES"]
```

---

## Complete integration example

Below is a full minimal plugin that hooks into NexusPrism, rewards players with money on kill, and respects Blood Moon multipliers.

```java
package com.example;

import io.github.otiger.nexusprism.api.NexusPrismAPI;
import io.github.otiger.nexusprism.api.events.EventFlags;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.PlayerDeathEvent;
import org.bukkit.plugin.java.JavaPlugin;

public class KillRewardPlugin extends JavaPlugin implements Listener {

    @Override
    public void onEnable() {
        if (NexusPrismAPI.get() == null) {
            getLogger().warning("NexusPrism not found — disabling kill rewards.");
            return;
        }
        getServer().getPluginManager().registerEvents(this, this);
        getLogger().info("Kill rewards enabled.");
    }

    @EventHandler
    public void onPlayerKill(PlayerDeathEvent event) {
        if (!(event.getEntity().getKiller() instanceof Player killer)) return;

        double base = 25.0;
        double reward = base * EventFlags.killPayMultiplier; // scales with Blood Moon

        NexusPrismAPI.economy().ifPresent(eco -> {
            eco.addMoney(killer.getUniqueId(), reward);
            killer.sendMessage("§a+$" + String.format("%.0f", reward) + " §7for the kill!");
        });
    }
}
```

---

## Quick-reference

| API surface | Class / method |
|---|---|
| Get API instance | `NexusPrismAPI.get()` |
| **Core providers** | |
| Economy | `NexusPrismAPI.economy()` → `EconomyProvider` |
| Auth | `NexusPrismAPI.auth()` → `AuthProvider` |
| Clans | `NexusPrismAPI.clans()` → `ClanProvider` |
| Essentials | `NexusPrismAPI.essentials()` → `EssentialsProvider` |
| Votes | `NexusPrismAPI.votes()` → `VoteProvider` |
| Enchantments | `NexusPrismAPI.enchants()` → `CustomEnchantProvider` |
| Crates | `NexusPrismAPI.crates()` → `CrateProvider` |
| **Module providers** | |
| MMO (level, stats, mana, skills, professions) | `MmoRegistry.get()` → `MmoProvider` |
| Chat (mute, channels, broadcast) | `ChatRegistry.get()` → `ChatProvider` |
| Protections (PvP, regions, duels) | `ProtectionsRegistry.get()` → `ProtectionsProvider` |
| Events (Blood Moon, Sacrifice, Isekai) | `EventsRegistry.get()` → `EventsProvider` |
| Holograms (create, update, show/hide) | `HologramRegistry.get()` → `HologramProvider` |
| Backpacks (count, open GUI) | `BackpackRegistry.get()` → `BackpackProvider` |
| Traits / Tarot cards | `TraitsRegistry.get()` → `TraitsProvider` |
| Discord (link, send message/webhook) | `DiscordRegistry.get()` → `DiscordProvider` |
| Jobs (active job, level, XP) | `JobRegistry.get()` → `JobProvider` |
| Energy networks | `EnergyRegistry.get()` → `EnergyProvider` |
| **Integration providers** | |
| Permission backend (groups, prefix, meta) | `nexus.getService(PermissionProvider.class)` |
| Placeholder expansion (PAPI bridge) | `nexus.getService(PlaceholderProvider.class)` |
| Language / translation | `nexus.getService(LangProvider.class)` |
| **Content & extensibility** | |
| Addon content loading | `content().items().machines().recipes().register()` |
| Machine processing recipes | `MachineProcessingRegistry.register(MachineProcessingRecipe)` |
| Item ID lookup | `NexusItemBuilder.getItemId(ItemStack)` |
| Item registry | `nexus.getService(ItemRegistry.class)` |
| Territory | `TerritoryRegistry.register(TerritoryProvider)` |
| Event state flags | `EventFlags.bloodMoonActive`, `EventFlags.killPayMultiplier` |
| Structure loot | `StructureRegistry.register(StructureProvider)` |
| Native addon base | `AbstractNexusAddon` + `addon.yml` |
| Starter template | [O-Tiger/NexusPrism-Addon-Example](https://github.com/Tg-TheNexus/NexusPrism-Addon-Example) |

---

## ResearchManager

Access the research tree and player progress programmatically.

```java
ResearchManager research = NexusPrismAPI.get().getService(ResearchManager.class);
```

> `ResearchManager` is a core system, not a module provider. It is not accessible via the provider/registry pattern — use `getService()` instead.

### Checking research status

```java
// Via PlayerData (available through any player join event or your own listener)
boolean hasUnlocked = playerData.hasCompletedResearch("copper_wire_research");
Set<String> done = playerData.getCompletedResearches();
```

### researches.yml entry format

```yaml
copper_wire_research:
  name: "Copper Wire"
  description: "Unlocks the crafting recipe for Copper Wire."
  tier: BASIC                    # BASIC | ADVANCED | INFINITY
  parchment-cost: 1              # number of parchments consumed
  dependencies: []               # list of entry IDs that must be completed first
  unlocks:
    - COPPER_WIRE                # item IDs added to the player's unlockedItems
```

### Tiers and parchments

| Tier | Parchment item |
|---|---|
| BASIC | `RESEARCH_PARCHMENT_BASIC` |
| ADVANCED | `RESEARCH_PARCHMENT_ADVANCED` |
| INFINITY | `RESEARCH_PARCHMENT_INFINITY` |

---

## Guide Category Icons (`gui_items.yml`)

Since v2.3.0, the material icon for each guide category and tier is defined in `gui_items.yml` instead of being hardcoded.

```yaml
# gui_items.yml
categories:
  MY_CATEGORY:
    material: ENCHANTING_TABLE
tiers:
  MY_TIER:
    material: DRAGON_EGG
```

The guide picks up entries automatically on reload. `guide.yml` overrides take higher priority than `gui_items.yml`. Entries in `gui_items.yml` not present in `guide.yml` use the value defined here.

---

## Best practices

- **Always null-check** `NexusPrismAPI.get()` before using any provider.
- **Use `softdepend`** unless your plugin is literally an addon JAR — this lets your plugin load even if NexusPrism is absent.
- **Never shade** `nexusprism-api` — use `provided`/`compileOnly` scope.
- **Unregister providers** in `onDisable()` to avoid ghost listeners after reload.
- **Use `Optional` chains** (`ifPresent`, `orElse`) — never call `.get()` on an empty Optional.
- **Check `isReady()`** if you call the API immediately on enable; NexusPrism loads modules asynchronously.
