# Structures Module

NexusPrism owns the **hook**, not the loot content. It listens to Paper's
`LootGenerateEvent` and dispatches to whatever addon has registered a
[`StructureProvider`](#addon-api) — it ships no structure loot table of its own.

> Previously this module had its own YAML-driven custom loot table system
> (`structures/loot-tables.yml`). That was removed 2026-08-06 — the item-resolution part of
> it was confirmed non-functional (always resolved to nothing), and any real loot content
> now belongs to addon plugins via the `StructureProvider` API below. See
> `NexusATS/docs/planning/PLAN-presplit-core-infra.md` for the design notes if you're
> building a replacement loot-table system in NexusATS.

---

## How It Works

1. A structure chest generates loot (any vanilla structure, or a modded one).
2. NexusPrism identifies the loot table key (e.g. `minecraft:chests/simple_dungeon`).
3. Every registered `StructureProvider` is asked for extra items via `generateLoot(...)`.
4. Whatever items the providers return are appended to the chest.

No commands, no config file — loot injection is fully passive and entirely addon-driven.

---

## Addon API

Addon plugins register a custom loot provider via `StructureRegistry`
(`io.github.otiger.nexusprism.api.structures`):

```java
public class MyStructureProvider implements StructureProvider {
    @Override
    public String getProviderId() { return "my_addon"; }

    @Override
    public List<ItemStack> generateLoot(String lootTableKey, Inventory inventory, Random rng) {
        if (!handles(lootTableKey)) return List.of();
        // ... roll your own loot table here ...
        return List.of(myItem);
    }
}

// onEnable():
StructureRegistry.register(new MyStructureProvider());

// onDisable():
StructureRegistry.unregister(provider);
```

`generateLoot` receives the full loot table key, the chest inventory (read-only reference),
and a seeded `Random` — everything needed to implement any custom loot table format
independently, without NexusPrism needing to know about it.
