# 🔥 SmashBuilder - Guia Completo do Usuário 🔥

![SmashBuilder Logo](logo.png)

## 📋 Índice

1. [Primeiros Passos](#-primeiros-passos)
2. [Interface Cyberpunk](#-interface-cyberpunk)
3. [Comandos CLI](#-comandos-cli)
4. [Atualizando Base de Dados](#-atualizando-base-de-dados)
5. [Exemplos Práticos](#-exemplos-práticos)
6. [Solução de Problemas](#-solução-de-problemas)
7. [Dicas Avançadas](#-dicas-avançadas)

---

## 🚀 Primeiros Passos

### Instalação Rápida

```bash
# 1. Navegue até o diretório do SmashBuilder
cd SmashBuilder

# 2. Execute o launcher automático (RECOMENDADO)
python start_cyberpunk.py
```

O launcher irá:
- ✅ Verificar versão do Python (3.8+)
- ✅ Instalar dependências automaticamente
- ✅ Inicializar a interface cyberpunk

### Verificação do Sistema

```bash
# Teste se tudo está funcionando
python test_system.py
```

**Resultado esperado:**
```
🔥 RESULTADO: 4/4 testes passaram
✅ Todos os testes passaram! Sistema funcionando corretamente.
```

---

## 🎨 Interface Cyberpunk

### Iniciando a Interface

```bash
python start_cyberpunk.py
```

### Menu Principal

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                       MENU PRINCIPAL - SMASHBUILDER                       ║
╠═══════════════════════════════════════════════════════════════════════════╣
║ [1] ► CALCULAR BUILD RÁPIDA                                               ║
║ [2] ► COMPARAR DUAS BUILDS                                                ║
║ [3] ► TABELA POR NÍVEIS                                                   ║
║ [4] ► CONFIGURAÇÕES AVANÇADAS                                             ║
║ [5] ► CATÁLOGO DE CAMPEÕES                                                ║
║ [6] ► CATÁLOGO DE ITENS                                                   ║
║ [7] ► EXPORTAR RESULTADOS                                                 ║
║ [8] ► SOBRE O SISTEMA                                                     ║
║ [0] ► SAIR DO SISTEMA                                                     ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

### Opção 1: Calcular Build Rápida

1. **Selecione um campeão:**
   ```
   Campeões disponíveis:
     1. Kai'Sa
     2. Jinx
     3. Vayne
     ... e mais 7 campeões
   
   Digite o nome do campeão: Kai'Sa
   ```

2. **Escolha o nível:**
   ```
   Nível (1-18) [11]: 11
   ```

3. **Digite os itens:**
   ```
   Itens populares:
     • Infinity Edge
     • Phantom Dancer
     • Kraken Slayer
     • Bloodthirster
   
   Digite os itens (separados por vírgula): Infinity Edge, Phantom Dancer
   ```

4. **Selecione um alvo:**
   ```
   Alvos disponíveis:
     • fragile: Frágil (HP: 1800, Armor: 30)
     • adc: ADC (HP: 2000, Armor: 70)
     • bruiser: Bruiser (HP: 2800, Armor: 120)
     • tank: Tank (HP: 3500, Armor: 200)
   
   Selecione um alvo [fragile]: bruiser
   ```

5. **Veja os resultados:**
   ```
   📊 Estatísticas Finais
   ┌─────────────────┬─────────┐
   │ Atributo        │ Valor   │
   ├─────────────────┼─────────┤
   │ Attack Damage   │ 189.0   │
   │ Attack Speed    │ 1.25    │
   │ Critical Chance │ 40.0%   │
   │ Health          │ 2374.0  │
   │ DPS             │ 285.4   │
   └─────────────────┴─────────┘
   ```

---

## 💻 Comandos CLI

### Calculadora Rápida Interativa

```bash
python -m cli.app quick
```

### Calcular Build Específica

```bash
python -m cli.app build \
  --champ "Kai'Sa" \
  --level 11 \
  --items "Infinity Edge,Phantom Dancer,Kraken Slayer" \
  --target "bruiser" \
  --export csv
```

**Parâmetros:**
- `--champ`: Nome do campeão (obrigatório)
- `--level`: Nível 1-18 (padrão: 11)
- `--items`: Itens separados por vírgula
- `--target`: Alvo (fragile, adc, mage, bruiser, tank, dummy)
- `--export`: Formato de export (csv, json, txt)

### Tabela por Níveis

```bash
python -m cli.app table \
  --champ "Jinx" \
  --levels 1,6,11,16,18 \
  --items "Kraken Slayer,Infinity Edge"
```

**Resultado:**
```
📊 Jinx - Stats por Nível
┌───────┬──────┬──────┬──────┬───────┬──────┐
│ Nível │ AD   │ AS   │ HP   │ Armor │ MR   │
├───────┼──────┼──────┼──────┼───────┼──────┤
│ 1     │ 124  │ 0.78 │ 630  │ 26.0  │ 30.0 │
│ 6     │ 141  │ 0.83 │ 1130 │ 49.5  │ 36.5 │
│ 11    │ 158  │ 0.88 │ 1630 │ 73.0  │ 43.0 │
│ 16    │ 175  │ 0.94 │ 2130 │ 96.5  │ 49.5 │
│ 18    │ 182  │ 0.96 │ 2330 │ 106.0 │ 52.0 │
└───────┴──────┴──────┴──────┴───────┴──────┘
```

### Listar Dados Disponíveis

```bash
# Ver todos os campeões
python -m cli.app champions

# Ver todos os itens
python -m cli.app items
```

---

## 📊 Atualizando Base de Dados

### ⚠️ IMPORTANTE: Base de Dados Limitada

A base de dados atual contém apenas **10 campeões** e **20 itens** para demonstração. Para uso completo, você precisa expandir os arquivos JSON.

### Adicionando Novos Campeões

**Arquivo:** `data/champions.json`

```json
{
  "champions": [
    {
      "name": "Novo Campeão",
      "base_ad": 60,
      "base_ap": 0,
      "base_as": 0.65,
      "base_hp": 600,
      "base_mana": 300,
      "base_armor": 30,
      "base_mr": 30,
      "base_ms": 335,
      "growth_ad": 3.0,
      "growth_ap": 0,
      "growth_as": 2.5,
      "growth_hp": 100,
      "growth_mana": 40,
      "growth_armor": 4.0,
      "growth_mr": 1.3,
      "growth_ms": 0,
      "champion_class": "Marksman",
      "patch": "14.1"
    }
  ]
}
```

**Como obter dados reais:**
1. **Site oficial:** [League of Legends Wiki](https://leagueoflegends.fandom.com)
2. **API Riot:** [Riot Developer Portal](https://developer.riotgames.com)
3. **Ferramentas:** LoL Wiki, Champion.gg, U.GG

### Adicionando Novos Itens

**Arquivo:** `data/items.json`

```json
{
  "items": [
    {
      "name": "Novo Item",
      "modifiers": [
        {
          "stat": "attack_damage",
          "value": 50,
          "modifier_type": "flat"
        },
        {
          "stat": "attack_speed",
          "value": 20,
          "modifier_type": "percent"
        }
      ],
      "cost": 2800,
      "unique": false,
      "mythic": false
    }
  ]
}
```

**Tipos de Stats Disponíveis:**
- `attack_damage` (AD)
- `ability_power` (AP)
- `attack_speed` (AS)
- `critical_chance` (Crit)
- `health` (HP)
- `mana` (Mana)
- `armor` (Armor)
- `magic_resistance` (MR)
- `movement_speed` (MS)

**Tipos de Modificadores:**
- `flat`: Valor fixo (+50 AD)
- `percent`: Percentual (+20% AS)

### Validando Dados Adicionados

```bash
# Teste se os novos dados estão válidos
python -c "from data_io.loader import data_loader; data_loader.validate_data_integrity()"
```

### Exemplo: Adicionando Ezreal

```json
{
  "name": "Ezreal",
  "base_ad": 60,
  "base_ap": 0,
  "base_as": 0.625,
  "base_hp": 600,
  "base_mana": 375,
  "base_armor": 24,
  "base_mr": 30,
  "base_ms": 325,
  "growth_ad": 2.5,
  "growth_ap": 0,
  "growth_as": 1.5,
  "growth_hp": 102,
  "growth_mana": 70,
  "growth_armor": 4.5,
  "growth_mr": 1.3,
  "growth_ms": 0,
  "champion_class": "Marksman",
  "patch": "14.1"
}
```

---

## 🎯 Exemplos Práticos

### Exemplo 1: Build Crítica ADC

```bash
python -m cli.app build \
  --champ "Jinx" \
  --level 18 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge,Phantom Dancer,Lord Dominik's Regards,Bloodthirster" \
  --target "tank" \
  --export csv
```

### Exemplo 2: Comparação de Power Spikes

```bash
# Level 6 (primeiro item)
python -m cli.app build --champ "Kai'Sa" --level 6 --items "Kraken Slayer" --target "fragile"

# Level 11 (dois itens)
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "fragile"

# Level 16 (três itens)
python -m cli.app build --champ "Kai'Sa" --level 16 --items "Kraken Slayer,Infinity Edge,Phantom Dancer" --target "fragile"
```

### Exemplo 3: Build de Mago

```bash
python -m cli.app build \
  --champ "Ahri" \
  --level 11 \
  --items "Luden's Tempest,Rabadon's Deathcap,Zhonya's Hourglass" \
  --target "fragile"
```

### Exemplo 4: Análise de Tanque

```bash
python -m cli.app build \
  --champ "Garen" \
  --level 16 \
  --items "Sunfire Aegis,Chain Vest,Negatron Cloak,Ruby Crystal" \
  --target "adc"
```

---

## 🔧 Solução de Problemas

### Erro: "Campeão não encontrado"

**Problema:** `❌ Campeão 'kaisa' não encontrado!`

**Solução:**
```bash
# Verifique a grafia exata
python -m cli.app champions

# Use exatamente como aparece na lista
python -m cli.app build --champ "Kai'Sa"  # Com apóstrofe
```

### Erro: "Item não encontrado"

**Problema:** `⚠️ Item 'IE' não encontrado, ignorando...`

**Solução:**
```bash
# Veja nomes exatos dos itens
python -m cli.app items

# Use o nome completo
--items "Infinity Edge"  # Não "IE"
```

### Erro: "No module named 'colorama'"

**Problema:** Dependências não instaladas

**Solução:**
```bash
# Use o launcher automático
python start_cyberpunk.py

# OU instale manualmente
pip install -r requirements.txt
```

### Interface não aparece corretamente

**Problema:** Cores ou caracteres especiais não funcionam

**Solução:**
- **Windows:** Use PowerShell ou Windows Terminal
- **Linux/Mac:** Terminal padrão deve funcionar
- **Alternativa:** Use a CLI sem interface cyberpunk

```bash
python -m cli.app quick
```

### Erro: "Nível fora do range"

**Problema:** `❌ Nível deve estar entre 1 e 18!`

**Solução:**
```bash
# Use níveis válidos
--level 11  # ✅ Correto
--level 25  # ❌ Inválido
```

---

## 💡 Dicas Avançadas

### 1. Automatização com Scripts

**Criar script de análise:**
```bash
#!/bin/bash
# analise_kaisa.sh

echo "=== Análise Kai'Sa ==="

echo "Build Early Game:"
python -m cli.app build --champ "Kai'Sa" --level 6 --items "Kraken Slayer" --target "fragile"

echo "Build Mid Game:"
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "bruiser"

echo "Build Late Game:"
python -m cli.app build --champ "Kai'Sa" --level 18 --items "Kraken Slayer,Infinity Edge,Phantom Dancer,Bloodthirster" --target "tank"
```

### 2. Export para Análise

```bash
# Exportar múltiplas builds para comparação
python -m cli.app build --champ "Jinx" --level 11 --items "Kraken Slayer,Infinity Edge" --export csv --target "bruiser"
python -m cli.app build --champ "Jinx" --level 11 --items "Galeforce,Infinity Edge" --export csv --target "bruiser"

# Analisar no Excel/Google Sheets
```

### 3. Testando Builds Personalizadas

```bash
# Build experimental
python -m cli.app build \
  --champ "Vayne" \
  --level 11 \
  --items "Kraken Slayer,Berserker's Greaves,Phantom Dancer,Infinity Edge" \
  --target "tank"
```

### 4. Análise de Custo-Benefício

```bash
# Compare itens por custo
python -m cli.app items | grep -E "(cost|name)"
```

### 5. Validação de Dados Customizados

```bash
# Após adicionar novos campeões/itens
python test_system.py

# Verificar integridade
python -c "
from data_io.loader import data_loader
errors = data_loader.validate_data_integrity()
print('Erros encontrados:', errors)
"
```

### 6. Backup da Base de Dados

```bash
# Fazer backup antes de modificar
cp -r data/ data_backup/

# Restaurar se necessário
cp -r data_backup/ data/
```

---

## 🎮 Casos de Uso Comuns

### Para Jogadores Casuais
- Use a **interface cyberpunk** para experiência visual
- Teste builds populares com **calculadora rápida**
- Compare diferentes itens no mesmo campeão

### Para Jogadores Competitivos
- Use **CLI** para análises rápidas
- **Export CSV** para planilhas detalhadas
- **Tabela por níveis** para timing de power spikes

### Para Criadores de Conteúdo
- **Scripts automatizados** para múltiplas análises
- **Export** para gráficos e apresentações
- **Comparações** para guias e tutoriais

### Para Desenvolvedores
- **Adicione novos campeões** conforme patches
- **Customize fórmulas** em `calc/formulas.py`
- **Integre com APIs** externas

---

## 🔥 Conclusão

O SmashBuilder oferece flexibilidade total para análise de builds de League of Legends. Com este guia, você pode:

✅ **Usar todas as funcionalidades** do sistema
✅ **Expandir a base de dados** com novos campeões e itens
✅ **Resolver problemas** comuns rapidamente
✅ **Automatizar análises** para uso avançado

**Lembre-se:** A base de dados atual é limitada. Expanda-a conforme suas necessidades para aproveitar todo o potencial do SmashBuilder!

**🔥 Domine suas builds e conquiste a Fenda do Invocador! 🔥**
