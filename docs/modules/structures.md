# Módulo Structures

O NexusPrism possui apenas o **hook**, não o conteúdo de loot. Ele escuta o
`LootGenerateEvent` do Paper e repassa para qualquer addon que tenha registrado um
[`StructureProvider`](#api-de-addon) — ele não fornece nenhuma tabela de loot de estruturas
própria.

> Anteriormente este módulo tinha seu próprio sistema de tabelas de loot personalizadas em
> YAML (`structures/loot-tables.yml`). Isso foi removido em 2026-08-06 — a parte de resolução
> de itens foi confirmada como não-funcional (sempre resolvia para nada), e qualquer conteúdo
> real de loot agora pertence aos plugins addon via a API `StructureProvider` abaixo. Veja
> `NexusATS/docs/planning/PLAN-presplit-core-infra.md` para as notas de design se você
> estiver construindo um sistema substituto de tabelas de loot no NexusATS.

---

## Como Funciona

1. Um baú de estrutura gera loot (qualquer estrutura vanilla, ou uma modificada).
2. O NexusPrism identifica a chave da tabela de loot (ex: `minecraft:chests/simple_dungeon`).
3. Cada `StructureProvider` registrado é consultado por itens extras via `generateLoot(...)`.
4. Os itens retornados pelos provedores são adicionados ao baú.

Nenhum comando, nenhum arquivo de configuração — a injeção de loot é totalmente passiva e
inteiramente controlada por addons.

---

## API de Addon

Plugins addon registram um provedor de loot personalizado via `StructureRegistry`
(`io.github.otiger.nexusprism.api.structures`):

```java
public class MeuStructureProvider implements StructureProvider {
    @Override
    public String getProviderId() { return "meu_addon"; }

    @Override
    public List<ItemStack> generateLoot(String lootTableKey, Inventory inventory, Random rng) {
        if (!handles(lootTableKey)) return List.of();
        // ... calcule sua própria tabela de loot aqui ...
        return List.of(meuItem);
    }
}

// onEnable():
StructureRegistry.register(new MeuStructureProvider());

// onDisable():
StructureRegistry.unregister(provider);
```

`generateLoot` recebe a chave completa da tabela de loot, o inventário do baú (referência
somente-leitura), e um `Random` com seed — tudo o que é necessário para implementar qualquer
formato de tabela de loot personalizado de forma independente, sem que o NexusPrism precise
saber sobre isso.
