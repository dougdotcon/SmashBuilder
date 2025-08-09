# 🎯 SmashBuilder - Exemplos Práticos de Uso 🎯

## 📋 Índice de Exemplos

1. [Builds Clássicas de ADC](#-builds-clássicas-de-adc)
2. [Análise de Power Spikes](#-análise-de-power-spikes)
3. [Comparação de Itens](#-comparação-de-itens)
4. [Builds de Mago](#-builds-de-mago)
5. [Análise de Tanques](#-análise-de-tanques)
6. [Otimização por Custo](#-otimização-por-custo)
7. [Casos Especiais](#-casos-especiais)

---

## 🏹 Builds Clássicas de ADC

### Exemplo 1: Kai'Sa Crítico Full Build

```bash
python -m cli.app build \
  --champ "Kai'Sa" \
  --level 18 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge,Phantom Dancer,Lord Dominik's Regards,Bloodthirster" \
  --target "tank" \
  --export csv
```

**Resultado Esperado:**
```
📊 Estatísticas Finais
┌─────────────────┬─────────┐
│ Attack Damage   │ 289.0   │
│ Attack Speed    │ 2.15    │
│ Critical Chance │ 80.0%   │
│ Health          │ 2374.0  │
│ DPS vs Tank     │ 485.2   │
│ TTK vs Tank     │ 7.2s    │
└─────────────────┴─────────┘
```

### Exemplo 2: Jinx Early Game vs Late Game

**Early Game (Level 6, 1 item):**
```bash
python -m cli.app build \
  --champ "Jinx" \
  --level 6 \
  --items "Kraken Slayer" \
  --target "fragile"
```

**Late Game (Level 18, 6 itens):**
```bash
python -m cli.app build \
  --champ "Jinx" \
  --level 18 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge,Phantom Dancer,Lord Dominik's Regards,Bloodthirster" \
  --target "fragile"
```

**Comparação:**
- **Early:** ~180 DPS
- **Late:** ~650+ DPS
- **Crescimento:** 3.6x mais dano!

---

## 📈 Análise de Power Spikes

### Exemplo 3: Power Spikes de Vayne

```bash
# Tabela completa de power spikes
python -m cli.app table \
  --champ "Vayne" \
  --levels 1,3,6,9,11,13,16,18 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge"
```

**Resultado:**
```
📊 Vayne - Stats por Nível
┌───────┬──────┬──────┬──────┬───────┬──────┐
│ Nível │ AD   │ AS   │ HP   │ Armor │ DPS  │
├───────┼──────┼──────┼──────┼───────┼──────┤
│ 1     │ 125  │ 1.05 │ 550  │ 23.0  │ 131  │
│ 3     │ 130  │ 1.11 │ 756  │ 32.2  │ 144  │
│ 6     │ 137  │ 1.20 │ 1065 │ 46.0  │ 164  │ ← Primeiro item
│ 9     │ 144  │ 1.29 │ 1374 │ 59.8  │ 186  │
│ 11    │ 149  │ 1.35 │ 1580 │ 69.2  │ 201  │ ← Segundo item
│ 13    │ 154  │ 1.42 │ 1786 │ 78.6  │ 219  │
│ 16    │ 161  │ 1.52 │ 2095 │ 92.4  │ 245  │ ← Terceiro item
│ 18    │ 166  │ 1.58 │ 2301 │ 101.8 │ 262  │
└───────┴──────┴──────┴──────┴───────┴──────┘
```

**Insights:**
- **Level 6:** Primeiro power spike significativo (+25% DPS)
- **Level 11:** Segundo item completo (+22% DPS)
- **Level 16:** Build de 3 itens (+22% DPS)

---

## ⚔️ Comparação de Itens

### Exemplo 4: Kraken Slayer vs Galeforce

**Build com Kraken Slayer:**
```bash
python -m cli.app build \
  --champ "Kai'Sa" \
  --level 11 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge" \
  --target "bruiser"
```

**Build com Galeforce:**
```bash
python -m cli.app build \
  --champ "Kai'Sa" \
  --level 11 \
  --items "Galeforce,Berserker's Greaves,Infinity Edge" \
  --target "bruiser"
```

**Comparação Esperada:**
```
┌─────────────────┬─────────────┬─────────────┬─────────────┐
│ Métrica         │ Kraken      │ Galeforce   │ Diferença   │
├─────────────────┼─────────────┼─────────────┼─────────────┤
│ Attack Damage   │ 149.0       │ 144.0       │ -5.0        │
│ Attack Speed    │ 1.25        │ 1.20        │ -0.05       │
│ DPS             │ 285.4       │ 268.1       │ -17.3       │
│ Mobilidade      │ Baixa       │ Alta        │ +Dash       │
└─────────────────┴─────────────┴─────────────┴─────────────┘
```

**Conclusão:** Kraken = +6% DPS, Galeforce = +Mobilidade

---

## 🔮 Builds de Mago

### Exemplo 5: Ahri Burst Build

```bash
python -m cli.app build \
  --champ "Ahri" \
  --level 11 \
  --items "Luden's Tempest,Rabadon's Deathcap,Zhonya's Hourglass" \
  --target "fragile"
```

**Análise de Burst:**
```
📊 Estatísticas Finais
┌─────────────────┬─────────┐
│ Ability Power   │ 385.0   │
│ Health          │ 1632.0  │
│ Armor           │ 63.7    │
│ Magic Resist    │ 43.0    │
│ Survivability   │ Alta    │
└─────────────────┴─────────┘
```

### Exemplo 6: Lux Poke Build

```bash
python -m cli.app build \
  --champ "Lux" \
  --level 11 \
  --items "Luden's Tempest,Void Staff,Rabadon's Deathcap" \
  --target "mage"
```

---

## 🛡️ Análise de Tanques

### Exemplo 7: Garen Tank Build

```bash
python -m cli.app build \
  --champ "Garen" \
  --level 16 \
  --items "Sunfire Aegis,Chain Vest,Negatron Cloak,Ruby Crystal" \
  --target "adc"
```

**Análise de Survivabilidade:**
```
📊 Estatísticas Finais
┌─────────────────────┬─────────┐
│ Health              │ 2814.0  │
│ Armor               │ 140.2   │
│ Magic Resistance    │ 72.0    │
│ HP Efetivo (Físico) │ 6756.0  │
│ HP Efetivo (Mágico) │ 4840.0  │
│ Redução Física      │ 58.3%   │
│ Redução Mágica      │ 41.9%   │
└─────────────────────┴─────────┘
```

### Exemplo 8: Darius Bruiser Build

```bash
python -m cli.app build \
  --champ "Darius" \
  --level 16 \
  --items "Sunfire Aegis,Ruby Crystal,Chain Vest" \
  --target "adc"
```

---

## 💰 Otimização por Custo

### Exemplo 9: Análise Custo-Benefício

**Build Cara (6800g):**
```bash
python -m cli.app build \
  --champ "Jinx" \
  --level 11 \
  --items "Kraken Slayer,Infinity Edge" \
  --target "fragile"
```

**Build Barata (4000g):**
```bash
python -m cli.app build \
  --champ "Jinx" \
  --level 11 \
  --items "Kraken Slayer,B.F. Sword,Cloak of Agility" \
  --target "fragile"
```

**Comparação de Eficiência:**
```
┌─────────────┬─────────┬─────────┬─────────────┐
│ Build       │ Custo   │ DPS     │ DPS/1000g   │
├─────────────┼─────────┼─────────┼─────────────┤
│ Cara        │ 6800g   │ 285.4   │ 42.0        │
│ Barata      │ 4000g   │ 245.1   │ 61.3        │
└─────────────┴─────────┴─────────┴─────────────┘
```

**Insight:** Build barata tem 46% mais eficiência por gold!

---

## 🎯 Casos Especiais

### Exemplo 10: Yasuo (Crítico Único)

```bash
python -m cli.app build \
  --champ "Yasuo" \
  --level 11 \
  --items "Infinity Edge,Phantom Dancer,Berserker's Greaves" \
  --target "fragile"
```

**Nota:** Yasuo tem mecânicas especiais de crítico (dobra chance, reduz dano)

### Exemplo 11: Thresh (Sem Crescimento de Resistência)

```bash
python -m cli.app build \
  --champ "Thresh" \
  --level 18 \
  --items "Sunfire Aegis,Chain Vest,Negatron Cloak" \
  --target "adc"
```

**Peculiaridade:** Thresh não ganha Armor/MR por nível (growth = 0)

### Exemplo 12: Comparação Multi-Alvo

```bash
# Mesmo build contra diferentes alvos
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "fragile"
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "bruiser"
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "tank"
```

**Resultado:**
```
┌─────────────┬─────────┬─────────┬─────────┐
│ Alvo        │ DPS     │ TTK     │ Eficácia│
├─────────────┼─────────┼─────────┼─────────┤
│ Frágil      │ 312.5   │ 5.8s    │ Alta    │
│ Bruiser     │ 285.4   │ 9.8s    │ Média   │
│ Tank        │ 201.2   │ 17.4s   │ Baixa   │
└─────────────┴─────────┴─────────┴─────────┘
```

---

## 🔬 Análises Avançadas

### Exemplo 13: Script de Análise Completa

```bash
#!/bin/bash
# analise_completa.sh

CHAMPION="Kai'Sa"
ITEMS="Kraken Slayer,Infinity Edge,Phantom Dancer"

echo "=== ANÁLISE COMPLETA: $CHAMPION ==="

echo "1. Power Spikes por Nível:"
python -m cli.app table --champ "$CHAMPION" --levels 6,11,16,18 --items "$ITEMS"

echo "2. Eficácia contra diferentes alvos:"
for target in fragile adc bruiser tank; do
    echo "Contra $target:"
    python -m cli.app build --champ "$CHAMPION" --level 11 --items "$ITEMS" --target "$target" | grep -E "(DPS|TTK)"
done

echo "3. Exportando para análise detalhada:"
python -m cli.app build --champ "$CHAMPION" --level 11 --items "$ITEMS" --target "bruiser" --export csv
```

### Exemplo 14: Comparação de Classes

```bash
# ADC vs Assassino vs Mago
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Kraken Slayer,Infinity Edge" --target "fragile"
python -m cli.app build --champ "Zed" --level 11 --items "Eclipse,Youmuu's Ghostblade" --target "fragile"
python -m cli.app build --champ "Ahri" --level 11 --items "Luden's Tempest,Rabadon's Deathcap" --target "fragile"
```

---

## 📊 Interpretando Resultados

### Métricas Importantes

**Para ADCs:**
- **DPS:** >300 = Excelente, 200-300 = Bom, <200 = Fraco
- **Crit Chance:** 60%+ para late game
- **Attack Speed:** 1.5-2.5 (cap = 2.5)

**Para Magos:**
- **AP:** 300+ para burst efetivo
- **Survivabilidade:** HP Efetivo >2500
- **Penetração:** Essencial contra tanks

**Para Tanks:**
- **HP Efetivo:** >5000 contra dano físico
- **Redução de Dano:** >50% em ambos os tipos
- **Custo-Benefício:** Priorizar resistências baratas

### Quando Usar Cada Análise

**Tabela por Níveis:** Power spikes, timing de itens
**Comparação de Builds:** Otimização de itens
**Multi-Alvo:** Versatilidade da build
**Export CSV:** Análise detalhada em planilhas

---

## 🔥 Dicas Finais

### Otimização de Workflow

1. **Use aliases para comandos frequentes:**
```bash
alias sb-build="python -m cli.app build"
alias sb-table="python -m cli.app table"
alias sb-champs="python -m cli.app champions"
```

2. **Crie templates de builds:**
```bash
# Template ADC
sb-build --champ "CHAMPION" --level 11 --items "Kraken Slayer,Infinity Edge,Phantom Dancer" --target "bruiser"
```

3. **Automatize comparações:**
```bash
for item in "Kraken Slayer" "Galeforce" "Immortal Shieldbow"; do
    echo "=== $item ==="
    sb-build --champ "Kai'Sa" --level 11 --items "$item,Infinity Edge" --target "bruiser"
done
```

### Interpretação Estratégica

- **Early Game:** Foque em custo-benefício
- **Mid Game:** Balance entre dano e survivabilidade
- **Late Game:** Maximize DPS total
- **Contra Tanks:** Priorize penetração
- **Contra Squishies:** Maximize burst

**🔥 Use estes exemplos como base para suas próprias análises e domine a Fenda do Invocador! 🔥**
