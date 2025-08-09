"""
🔥 SmashBuilder - Modelos de Dados 🔥
Estruturas de dados usando Pydantic para validação
"""

from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, validator
from enum import Enum

class StatType(str, Enum):
    """Tipos de atributos suportados"""
    AD = "attack_damage"
    AP = "ability_power"
    AS = "attack_speed"
    CRIT_CHANCE = "critical_chance"
    CRIT_DAMAGE = "critical_damage"
    HP = "health"
    MANA = "mana"
    ARMOR = "armor"
    MR = "magic_resistance"
    MS = "movement_speed"
    LETHALITY = "lethality"
    MAGIC_PEN = "magic_penetration"

class ModifierType(str, Enum):
    """Tipos de modificadores"""
    FLAT = "flat"
    PERCENT = "percent"
    UNIQUE = "unique"

class ChampionStats(BaseModel):
    """Estatísticas base de um campeão"""
    name: str = Field(..., description="Nome do campeão")
    
    # Stats base (nível 1)
    base_ad: float = Field(..., ge=0, description="Attack Damage base")
    base_ap: float = Field(0, ge=0, description="Ability Power base")
    base_as: float = Field(..., ge=0, le=3.0, description="Attack Speed base")
    base_hp: float = Field(..., ge=0, description="Health base")
    base_mana: float = Field(0, ge=0, description="Mana base")
    base_armor: float = Field(..., ge=0, description="Armor base")
    base_mr: float = Field(..., ge=0, description="Magic Resistance base")
    base_ms: float = Field(..., ge=0, description="Movement Speed base")
    
    # Crescimento por nível
    growth_ad: float = Field(..., ge=0, description="AD por nível")
    growth_ap: float = Field(0, ge=0, description="AP por nível")
    growth_as: float = Field(..., ge=0, description="AS% por nível")
    growth_hp: float = Field(..., ge=0, description="HP por nível")
    growth_mana: float = Field(0, ge=0, description="Mana por nível")
    growth_armor: float = Field(..., ge=0, description="Armor por nível")
    growth_mr: float = Field(..., ge=0, description="MR por nível")
    growth_ms: float = Field(0, ge=0, description="MS por nível")
    
    # Metadados
    champion_class: str = Field("Unknown", description="Classe do campeão")
    patch: str = Field("14.1", description="Patch dos dados")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Nome do campeão não pode estar vazio')
        return v.strip()

class ItemModifier(BaseModel):
    """Modificador de um item"""
    stat: StatType = Field(..., description="Tipo de atributo")
    value: float = Field(..., description="Valor do modificador")
    modifier_type: ModifierType = Field(ModifierType.FLAT, description="Tipo de modificador")
    
    @validator('value')
    def value_must_be_positive_for_most_stats(cls, v, values):
        # Alguns stats podem ter valores negativos (debuffs)
        if 'stat' in values and values['stat'] in [StatType.MS] and v < 0:
            return v  # MS pode ser negativo
        if v < 0:
            raise ValueError('Valor deve ser positivo para a maioria dos stats')
        return v

class Item(BaseModel):
    """Representação de um item"""
    name: str = Field(..., description="Nome do item")
    modifiers: List[ItemModifier] = Field(default_factory=list, description="Modificadores do item")
    cost: int = Field(0, ge=0, description="Custo em gold")
    unique: bool = Field(False, description="Se o item é único")
    mythic: bool = Field(False, description="Se o item é mítico")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Nome do item não pode estar vazio')
        return v.strip()

class RuneModifier(BaseModel):
    """Modificador de uma runa"""
    stat: StatType = Field(..., description="Tipo de atributo")
    value: float = Field(..., description="Valor do modificador")
    modifier_type: ModifierType = Field(ModifierType.FLAT, description="Tipo de modificador")

class RunePreset(BaseModel):
    """Preset de runas"""
    name: str = Field(..., description="Nome do preset")
    modifiers: List[RuneModifier] = Field(default_factory=list, description="Modificadores das runas")
    description: str = Field("", description="Descrição do preset")

class Target(BaseModel):
    """Configuração de alvo para cálculo de DPS"""
    name: str = Field(..., description="Nome do alvo")
    hp: float = Field(..., ge=1, description="HP do alvo")
    armor: float = Field(0, ge=0, description="Armor do alvo")
    mr: float = Field(0, ge=0, description="Magic Resistance do alvo")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Nome do alvo não pode estar vazio')
        return v.strip()

class FinalStats(BaseModel):
    """Estatísticas finais calculadas"""
    level: int = Field(..., ge=1, le=18, description="Nível do campeão")
    
    # Stats finais
    ad: float = Field(..., ge=0, description="Attack Damage final")
    ap: float = Field(..., ge=0, description="Ability Power final")
    as_: float = Field(..., ge=0, description="Attack Speed final")
    crit_chance: float = Field(..., ge=0, le=100, description="Critical Chance final (%)")
    crit_damage: float = Field(200, ge=100, description="Critical Damage final (%)")
    hp: float = Field(..., ge=1, description="Health final")
    mana: float = Field(..., ge=0, description="Mana final")
    armor: float = Field(..., ge=0, description="Armor final")
    mr: float = Field(..., ge=0, description="Magic Resistance final")
    ms: float = Field(..., ge=0, description="Movement Speed final")
    
    # Stats derivados
    dps: Optional[float] = Field(None, ge=0, description="DPS estimado")
    ttk: Optional[float] = Field(None, ge=0, description="Time to Kill (segundos)")
    effective_hp_physical: Optional[float] = Field(None, ge=0, description="HP efetivo contra dano físico")
    effective_hp_magical: Optional[float] = Field(None, ge=0, description="HP efetivo contra dano mágico")

class Build(BaseModel):
    """Configuração completa de uma build"""
    name: str = Field(..., description="Nome da build")
    champion: ChampionStats = Field(..., description="Dados do campeão")
    level: int = Field(..., ge=1, le=18, description="Nível do campeão")
    items: List[Item] = Field(default_factory=list, description="Lista de itens")
    runes: Optional[RunePreset] = Field(None, description="Preset de runas")
    target: Optional[Target] = Field(None, description="Alvo para cálculo de DPS")
    
    # Resultados calculados
    final_stats: Optional[FinalStats] = Field(None, description="Estatísticas finais calculadas")
    
    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('Nome da build não pode estar vazio')
        return v.strip()
    
    @validator('items')
    def validate_mythic_items(cls, v):
        mythic_count = sum(1 for item in v if item.mythic)
        if mythic_count > 1:
            raise ValueError('Apenas um item mítico é permitido por build')
        return v

class BuildComparison(BaseModel):
    """Comparação entre duas builds"""
    build_a: Build = Field(..., description="Primeira build")
    build_b: Build = Field(..., description="Segunda build")
    
    # Diferenças calculadas
    stat_differences: Optional[Dict[str, float]] = Field(None, description="Diferenças entre stats")
    dps_difference: Optional[float] = Field(None, description="Diferença de DPS")
    cost_difference: Optional[int] = Field(None, description="Diferença de custo")

# Presets de alvos comuns
PRESET_TARGETS = {
    "fragile": Target(name="Frágil", hp=1800, armor=30, mr=30),
    "adc": Target(name="ADC", hp=2000, armor=70, mr=30),
    "mage": Target(name="Mago", hp=1900, armor=40, mr=40),
    "bruiser": Target(name="Bruiser", hp=2800, armor=120, mr=60),
    "tank": Target(name="Tank", hp=3500, armor=200, mr=120),
    "dummy": Target(name="Dummy", hp=1000, armor=0, mr=0),
}

# Presets de runas comuns
PRESET_RUNES = {
    "ad_carry": RunePreset(
        name="AD Carry",
        description="Runas focadas em dano físico",
        modifiers=[
            RuneModifier(stat=StatType.AD, value=9, modifier_type=ModifierType.FLAT),
            RuneModifier(stat=StatType.AS, value=10, modifier_type=ModifierType.PERCENT),
            RuneModifier(stat=StatType.ARMOR, value=6, modifier_type=ModifierType.FLAT),
        ]
    ),
    "ap_carry": RunePreset(
        name="AP Carry",
        description="Runas focadas em dano mágico",
        modifiers=[
            RuneModifier(stat=StatType.AP, value=15, modifier_type=ModifierType.FLAT),
            RuneModifier(stat=StatType.MR, value=8, modifier_type=ModifierType.FLAT),
            RuneModifier(stat=StatType.HP, value=65, modifier_type=ModifierType.FLAT),
        ]
    ),
    "tank": RunePreset(
        name="Tank",
        description="Runas focadas em resistência",
        modifiers=[
            RuneModifier(stat=StatType.HP, value=120, modifier_type=ModifierType.FLAT),
            RuneModifier(stat=StatType.ARMOR, value=12, modifier_type=ModifierType.FLAT),
            RuneModifier(stat=StatType.MR, value=8, modifier_type=ModifierType.FLAT),
        ]
    ),
}
