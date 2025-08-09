# 📊 SmashBuilder - Expandindo a Base de Dados 📊

## ⚠️ AVISO IMPORTANTE

A base de dados atual do SmashBuilder contém apenas:
- **10 campeões** (demonstração)
- **20 itens** (básicos)
- **Dados do Patch 14.1** (exemplo)

Para uso completo, você precisa expandir manualmente os arquivos JSON com dados atualizados.

---

## 📁 Estrutura dos Arquivos de Dados

```
data/
├── champions.json    # Dados de campeões
├── items.json       # Dados de itens
└── presets.json     # Alvos, runas e buffs
```

---

## 🏆 Adicionando Campeões

### Formato do Arquivo `champions.json`

```json
{
  "champions": [
    {
      "name": "Nome do Campeão",
      "base_ad": 0.0,           // Attack Damage base (nível 1)
      "base_ap": 0.0,           // Ability Power base
      "base_as": 0.0,           // Attack Speed base
      "base_hp": 0.0,           // Health base
      "base_mana": 0.0,         // Mana base (0 se não usa mana)
      "base_armor": 0.0,        // Armor base
      "base_mr": 0.0,           // Magic Resistance base
      "base_ms": 0.0,           // Movement Speed base
      "growth_ad": 0.0,         // AD por nível
      "growth_ap": 0.0,         // AP por nível
      "growth_as": 0.0,         // AS% por nível
      "growth_hp": 0.0,         // HP por nível
      "growth_mana": 0.0,       // Mana por nível
      "growth_armor": 0.0,      // Armor por nível
      "growth_mr": 0.0,         // MR por nível
      "growth_ms": 0.0,         // MS por nível (geralmente 0)
      "champion_class": "Classe",
      "patch": "14.1"
    }
  ]
}
```

### Onde Encontrar Dados de Campeões

#### 1. **League of Legends Wiki** (Mais Confiável)
- **URL:** https://leagueoflegends.fandom.com
- **Exemplo:** https://leagueoflegends.fandom.com/wiki/Ezreal/LoL
- **Seção:** "Base Statistics"

#### 2. **Riot Games API** (Oficial)
- **URL:** https://developer.riotgames.com
- **Endpoint:** Data Dragon API
- **Arquivo:** `champion.json`

#### 3. **Sites de Estatísticas**
- **LoLalytics:** https://lolalytics.com
- **U.GG:** https://u.gg
- **Champion.gg:** https://champion.gg

### Exemplo Prático: Adicionando Ezreal

**1. Acesse a Wiki do Ezreal:**
```
https://leagueoflegends.fandom.com/wiki/Ezreal/LoL
```

**2. Encontre "Base Statistics":**
```
Health: 600 (+102)
Mana: 375 (+70)
Attack damage: 60 (+2.5)
Attack speed: 0.625 (+1.5%)
Armor: 24 (+4.5)
Magic resistance: 30 (+1.3)
Movement speed: 325
```

**3. Adicione ao JSON:**
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

### Lista de Campeões Prioritários

**ADCs (Atiradores):**
- Ezreal, Caitlyn, Ashe, Tristana, Lucian, Xayah, Aphelios, Jhin, Miss Fortune, Sivir

**Assassinos:**
- Akali, Katarina, Talon, Fizz, LeBlanc, Qiyana, Rengar, Kha'Zix

**Magos:**
- Syndra, Orianna, Azir, Cassiopeia, Viktor, Ryze, Anivia, Vel'Koz

**Lutadores:**
- Fiora, Camille, Jax, Irelia, Riven, Aatrox, Sett, Viego

**Tanques:**
- Malphite, Ornn, Maokai, Sion, Cho'Gath, Nautilus, Leona

---

## 🛡️ Adicionando Itens

### Formato do Arquivo `items.json`

```json
{
  "items": [
    {
      "name": "Nome do Item",
      "modifiers": [
        {
          "stat": "tipo_do_stat",
          "value": 0.0,
          "modifier_type": "flat_ou_percent"
        }
      ],
      "cost": 0,
      "unique": false,
      "mythic": false
    }
  ]
}
```

### Tipos de Stats Disponíveis

```json
"attack_damage"      // AD
"ability_power"      // AP
"attack_speed"       // AS
"critical_chance"    // Crit Chance
"critical_damage"    // Crit Damage (padrão 200%)
"health"            // HP
"mana"              // Mana
"armor"             // Armor
"magic_resistance"   // MR
"movement_speed"     // MS
"lethality"         // Lethality
"magic_penetration"  // Magic Pen
```

### Tipos de Modificadores

```json
"flat"     // Valor fixo (+50 AD)
"percent"  // Percentual (+25% AS)
"unique"   // Passiva única (futuro)
```

### Exemplo: Adicionando Blade of the Ruined King

```json
{
  "name": "Blade of the Ruined King",
  "modifiers": [
    {
      "stat": "attack_damage",
      "value": 40,
      "modifier_type": "flat"
    },
    {
      "stat": "attack_speed",
      "value": 25,
      "modifier_type": "percent"
    }
  ],
  "cost": 3200,
  "unique": true,
  "mythic": false
}
```

### Lista de Itens Prioritários

**Itens Míticos ADC:**
- Immortal Shieldbow, Eclipse, Crown of the Shattered Queen

**Itens Lendários ADC:**
- Blade of the Ruined King, Runaan's Hurricane, Rapid Firecannon, Mortal Reminder

**Itens Míticos AP:**
- Everfrost, Night Harvester, Riftmaker, Liandry's Anguish

**Itens Lendários AP:**
- Cosmic Drive, Horizon Focus, Banshee's Veil, Morellonomicon

**Itens de Tank:**
- Thornmail, Randuin's Omen, Spirit Visage, Force of Nature

**Botas:**
- Plated Steelcaps, Mercury's Treads, Ionian Boots of Lucidity, Sorcerer's Shoes

---

## 🎯 Atualizando Presets

### Arquivo `presets.json`

Este arquivo contém alvos, runas e buffs predefinidos. Geralmente não precisa ser alterado, mas você pode:

**Adicionar novos alvos:**
```json
"super_tank": {
  "name": "Super Tank",
  "hp": 4000,
  "armor": 300,
  "mr": 200
}
```

**Adicionar novas runas:**
```json
"lethality_assassin": {
  "name": "Lethality Assassin",
  "description": "Runas para assassinos lethality",
  "modifiers": [
    {
      "stat": "attack_damage",
      "value": 12,
      "modifier_type": "flat"
    },
    {
      "stat": "lethality",
      "value": 8,
      "modifier_type": "flat"
    }
  ]
}
```

---

## 🔧 Ferramentas para Coleta de Dados

### Script Python para Riot API

```python
import requests
import json

def get_champion_data(champion_name, patch="14.1"):
    """Busca dados de campeão via Riot API"""
    url = f"https://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/champion/{champion_name}.json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        champion = data['data'][champion_name]
        
        return {
            "name": champion['name'],
            "base_ad": float(champion['stats']['attackdamage']),
            "base_ap": 0,  # AP base é sempre 0
            "base_as": float(champion['stats']['attackspeed']),
            "base_hp": float(champion['stats']['hp']),
            "base_mana": float(champion['stats']['mp']),
            "base_armor": float(champion['stats']['armor']),
            "base_mr": float(champion['stats']['spellblock']),
            "base_ms": float(champion['stats']['movespeed']),
            "growth_ad": float(champion['stats']['attackdamageperlevel']),
            "growth_ap": 0,
            "growth_as": float(champion['stats']['attackspeedperlevel']),
            "growth_hp": float(champion['stats']['hpperlevel']),
            "growth_mana": float(champion['stats']['mpperlevel']),
            "growth_armor": float(champion['stats']['armorperlevel']),
            "growth_mr": float(champion['stats']['spellblockperlevel']),
            "growth_ms": 0,
            "champion_class": champion['tags'][0] if champion['tags'] else "Unknown",
            "patch": patch
        }
    return None

# Exemplo de uso
ezreal_data = get_champion_data("Ezreal")
print(json.dumps(ezreal_data, indent=2))
```

### Script para Itens

```python
def get_item_data(item_id, patch="14.1"):
    """Busca dados de item via Riot API"""
    url = f"https://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/item.json"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if str(item_id) in data['data']:
            item = data['data'][str(item_id)]
            
            # Processar stats do item
            modifiers = []
            if 'stats' in item:
                for stat, value in item['stats'].items():
                    # Mapear stats da API para nosso formato
                    stat_mapping = {
                        'FlatPhysicalDamageMod': 'attack_damage',
                        'FlatMagicDamageMod': 'ability_power',
                        'PercentAttackSpeedMod': 'attack_speed',
                        'FlatCritChanceMod': 'critical_chance',
                        'FlatHPPoolMod': 'health',
                        'FlatMPPoolMod': 'mana',
                        'FlatArmorMod': 'armor',
                        'FlatSpellBlockMod': 'magic_resistance',
                        'FlatMovementSpeedMod': 'movement_speed'
                    }
                    
                    if stat in stat_mapping:
                        modifier_type = "percent" if "Percent" in stat else "flat"
                        modifiers.append({
                            "stat": stat_mapping[stat],
                            "value": value,
                            "modifier_type": modifier_type
                        })
            
            return {
                "name": item['name'],
                "modifiers": modifiers,
                "cost": item.get('gold', {}).get('total', 0),
                "unique": 'unique' in item.get('description', '').lower(),
                "mythic": 'mythic' in item.get('description', '').lower()
            }
    return None
```

---

## ✅ Validação dos Dados

### Após Adicionar Novos Dados

```bash
# 1. Teste a integridade
python -c "from data_io.loader import data_loader; data_loader.validate_data_integrity()"

# 2. Execute os testes do sistema
python test_system.py

# 3. Teste um campeão específico
python -m cli.app build --champ "Novo Campeão" --level 11 --items "Infinity Edge"
```

### Checklist de Validação

- [ ] Todos os campos obrigatórios preenchidos
- [ ] Valores numéricos positivos (exceto growth_ms)
- [ ] Nomes únicos (sem duplicatas)
- [ ] JSON válido (sem erros de sintaxe)
- [ ] Stats realistas (AD base 40-80, AS base 0.6-0.7, etc.)

---

## 🚀 Automatização da Atualização

### Script de Atualização Completa

```bash
#!/bin/bash
# update_database.sh

echo "🔄 Atualizando base de dados do SmashBuilder..."

# Backup atual
cp -r data/ data_backup_$(date +%Y%m%d)/

# Baixar dados mais recentes (implementar conforme necessário)
python scripts/update_champions.py
python scripts/update_items.py

# Validar
python test_system.py

echo "✅ Atualização concluída!"
```

### Agendamento Automático

```bash
# Crontab para atualização semanal
0 0 * * 0 cd /path/to/SmashBuilder && ./update_database.sh
```

---

## 📈 Roadmap de Expansão

### Fase 1: Campeões Populares (50+)
- Todos os ADCs
- Assassinos meta
- Magos populares
- Lutadores top tier

### Fase 2: Itens Completos (100+)
- Todos os itens míticos
- Itens lendários por classe
- Componentes básicos
- Botas especializadas

### Fase 3: Dados Avançados
- Passivas de itens
- Runas detalhadas
- Buffs de dragão/barão
- Fórmulas específicas por campeão

### Fase 4: Automação
- Sincronização com API Riot
- Atualização automática por patch
- Validação de dados em tempo real

---

## 🔥 Conclusão

A expansão da base de dados é essencial para aproveitar todo o potencial do SmashBuilder. Com este guia, você pode:

✅ **Adicionar qualquer campeão** do League of Legends
✅ **Incluir todos os itens** relevantes
✅ **Manter dados atualizados** por patch
✅ **Automatizar o processo** de atualização

**Lembre-se:** Dados precisos = cálculos precisos = builds otimizadas!

**🔥 Expanda sua base de dados e domine a Fenda! 🔥**
