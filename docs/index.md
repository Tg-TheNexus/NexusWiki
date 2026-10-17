# NexusPrism

> **Uma reimplementação abrangente e evolução do Slimefun4** — sistemas de tecnologia, magia e qualidade de vida de próxima geração para servidores Minecraft.

NexusPrism é um plugin Spigot modular construído sobre uma arquitetura Maven de +25 módulos. Ele traz itens personalizados, máquinas, redes de energia, clãs, economia, minijogos e integrações profundas em um único JAR leve.

---

## Funcionalidades Principais

| Categoria | Destaques |
| --- | --- |
| **Itens Personalizados** | +500+ itens definidos em YAML |
| **Máquinas** | Crafting multibloco, redes de energia, armazenamento ME |
| **Economia** | Moeda dupla (dinheiro + créditos), /sell, /baltop |
| **Clãs** | Conquista de território, melhorias, baú de clã, chat de clã |
| **Essenciais** | +40 comandos QoL — homes, warps, TPA, AFK, prisão |
| **Segurança** | Auth BCrypt, anti-bot CAPTCHA, anti-dupe, anti-lag |
| **Discord** | Integração com bot, vinculação de conta, sincronização de cargos |
| **Crystal Defense** | Minijogo de defesa de Cristais Ender por ondas |
| **Mobs Personalizados** | Chefes definidos em YAML com tabelas de loot e formas de IA |
| **Votifier** | Servidor Votifier V1/V2 independente, sequências, placares |
| **Sonhos** | Sistema de cutscene de sono com variantes de pesadelo |
| **Proteções** | Reivindicação de regiões, flags, sistema de duelo |
| **Twitch** | Vinculação de conta, alertas ao vivo, relay de chat, sorteios |
| **PlaceholderAPI** | +30 placeholders em todos os módulos |

---

## Visão Geral dos Módulos

```text
NexusPrism
├── nexusprism-api          API pública para desenvolvedores de addons
├── nexusprism-core         Gerenciadores principais, registro PDC, idioma
├── nexusprism-items        Armazenamento de itens personalizados (+500+ itens)
├── nexusprism-machines     Definições de máquinas, motor de processamento
├── nexusprism-systems      Implementação de redes de energia
├── nexusprism-integrations PlaceholderAPI, LuckPerms, SkinsRestorer
├── nexusprism-storage      Persistência SQLite / PostgreSQL
├── nexusprism-gui          Framework de GUI
├── nexusprism-utils        Utilitários auxiliares
├── nexusprism-web          Bridge da loja web, kits VIP, pagamentos
├── nexusprism-plugin       Ponto de entrada principal (Spigot)
├── nexusprism-discord      Bot JDA, webhooks, vinculação de conta
├── nexusprism-chat         Sistema de chat com 4 canais
├── nexusprism-ae           Armazenamento em rede estilo ME
├── nexusprism-energy       Geração de energia e redes de cabos
├── nexusprism-waila        Integração WAILA/HUD
├── nexusprism-security     Auth, anti-bot, anti-lag, anti-dupe
├── nexusprism-clans        Clãs, território, melhorias
├── nexusprism-economy      Dinheiro, créditos, preços de venda
├── nexusprism-essentials   +40 comandos QoL
├── nexusprism-crystaldefense Minijogo Crystal Defense por ondas
├── nexusprism-custommobs   Chefes definidos em YAML
├── nexusprism-dreams       Sistema de cutscene de sono
├── nexusprism-protections  Proteção de regiões, sistema de duelo
├── nexusprism-ss           Suporte a Silk Spawner
├── nexusprism-votifier     Servidor Votifier V1/V2 independente
└── nexusprism-twitch       Integração Twitch
```

---

## Navegação Rápida

| | |
| --- | --- |
| **[Primeiros Passos](getting-started.md)** | Instalação, requisitos e primeiros passos |
| **[Módulo Core](modules/core.md)** | Itens, sistema PDC, registro de itens |
| **[Todos os Módulos](modules/index.md)** | Navegue pelos 13 módulos de funcionalidades |
| **[Referência de Comandos](reference/commands.md)** | Todos os +40 comandos com uso e permissões |
| **[Referência de Permissões](reference/permissions.md)** | Lista completa de nós de permissão |
| **[PlaceholderAPI](reference/placeholders.md)** | Todos os placeholders `%nexusprism_*%` |

---

## Autor

NexusPrism é desenvolvido por **O-Tiger**

- Versão da API: `1.21`
- Dependências opcionais: `PlaceholderAPI`, `LuckPerms`, `SkinsRestorer`
