"""
🔥 SmashBuilder - Engine de Fórmulas 🔥
Sistema de aplicação de modificadores e cálculos de stats
"""

from typing import Dict, List, Tuple
import math

try:
    from .models import (
        ChampionStats, Item, RunePreset, FinalStats, Build,
        StatType, ModifierType, ItemModifier, RuneModifier
    )
except ImportError:
    # Fallback para execução direta
    from models import (
        ChampionStats, Item, RunePreset, FinalStats, Build,
        StatType, ModifierType, ItemModifier, RuneModifier
    )

class FormulaEngine:
    """Engine principal para cálculos de fórmulas"""

    # Caps e limites do jogo
    MAX_ATTACK_SPEED = 2.5
    MAX_CRITICAL_CHANCE = 100.0
    MIN_DAMAGE_REDUCTION = 0.0
    MAX_DAMAGE_REDUCTION = 0.99

    def __init__(self):
        self.precision = 2  # Casas decimais para arredondamento

    def calculate_base_stats_at_level(self, champion: ChampionStats, level: int) -> Dict[str, float]:
        """
        Calcula os stats base do campeão em um nível específico
        Fórmula: base + (growth * (level - 1))
        """
        if not (1 <= level <= 18):
            raise ValueError(f"Nível deve estar entre 1 e 18, recebido: {level}")

        level_multiplier = level - 1

        base_stats = {
            StatType.AD: champion.base_ad + (champion.growth_ad * level_multiplier),
            StatType.AP: champion.base_ap + (champion.growth_ap * level_multiplier),
            StatType.AS: champion.base_as * (1 + (champion.growth_as * level_multiplier / 100)),
            StatType.HP: champion.base_hp + (champion.growth_hp * level_multiplier),
            StatType.MANA: champion.base_mana + (champion.growth_mana * level_multiplier),
            StatType.ARMOR: champion.base_armor + (champion.growth_armor * level_multiplier),
            StatType.MR: champion.base_mr + (champion.growth_mr * level_multiplier),
            StatType.MS: champion.base_ms + (champion.growth_ms * level_multiplier),
            StatType.CRIT_CHANCE: 0.0,
            StatType.CRIT_DAMAGE: 200.0,  # 200% é o padrão
        }

        return base_stats

    def apply_item_modifiers(self, base_stats: Dict[str, float], items: List[Item]) -> Dict[str, float]:
        """
        Aplica modificadores de itens aos stats base
        Ordem: flat primeiro, depois percentuais
        """
        stats = base_stats.copy()

        # Primeira passada: modificadores flat
        for item in items:
            for modifier in item.modifiers:
                if modifier.modifier_type == ModifierType.FLAT:
                    current_value = stats.get(modifier.stat, 0.0)
                    stats[modifier.stat] = current_value + modifier.value

        # Segunda passada: modificadores percentuais
        for item in items:
            for modifier in item.modifiers:
                if modifier.modifier_type == ModifierType.PERCENT:
                    current_value = stats.get(modifier.stat, 0.0)
                    # Percentual é aplicado sobre o valor atual
                    stats[modifier.stat] = current_value * (1 + modifier.value / 100)

        return stats

    def apply_rune_modifiers(self, stats: Dict[str, float], runes: RunePreset) -> Dict[str, float]:
        """
        Aplica modificadores de runas
        """
        if not runes:
            return stats

        modified_stats = stats.copy()

        # Primeira passada: modificadores flat
        for modifier in runes.modifiers:
            if modifier.modifier_type == ModifierType.FLAT:
                current_value = modified_stats.get(modifier.stat, 0.0)
                modified_stats[modifier.stat] = current_value + modifier.value

        # Segunda passada: modificadores percentuais
        for modifier in runes.modifiers:
            if modifier.modifier_type == ModifierType.PERCENT:
                current_value = modified_stats.get(modifier.stat, 0.0)
                modified_stats[modifier.stat] = current_value * (1 + modifier.value / 100)

        return modified_stats

    def apply_caps_and_limits(self, stats: Dict[str, float]) -> Dict[str, float]:
        """
        Aplica caps e limites do jogo
        """
        capped_stats = stats.copy()

        # Cap de Attack Speed
        if StatType.AS in capped_stats:
            capped_stats[StatType.AS] = min(capped_stats[StatType.AS], self.MAX_ATTACK_SPEED)

        # Cap de Critical Chance
        if StatType.CRIT_CHANCE in capped_stats:
            capped_stats[StatType.CRIT_CHANCE] = min(capped_stats[StatType.CRIT_CHANCE], self.MAX_CRITICAL_CHANCE)

        # Garantir valores mínimos
        for stat_type in [StatType.HP, StatType.AD, StatType.AS]:
            if stat_type in capped_stats:
                capped_stats[stat_type] = max(capped_stats[stat_type], 1.0)

        return capped_stats

    def calculate_final_stats(self, build: Build) -> FinalStats:
        """
        Calcula todas as estatísticas finais de uma build
        """
        # 1. Stats base no nível especificado
        base_stats = self.calculate_base_stats_at_level(build.champion, build.level)

        # 2. Aplicar modificadores de itens
        stats_with_items = self.apply_item_modifiers(base_stats, build.items)

        # 3. Aplicar modificadores de runas
        stats_with_runes = self.apply_rune_modifiers(stats_with_items, build.runes)

        # 4. Aplicar caps e limites
        final_stats_dict = self.apply_caps_and_limits(stats_with_runes)

        # 5. Arredondar valores
        for stat_type, value in final_stats_dict.items():
            final_stats_dict[stat_type] = round(value, self.precision)

        # 6. Criar objeto FinalStats
        final_stats = FinalStats(
            level=build.level,
            ad=final_stats_dict.get(StatType.AD, 0),
            ap=final_stats_dict.get(StatType.AP, 0),
            as_=final_stats_dict.get(StatType.AS, 0),
            crit_chance=final_stats_dict.get(StatType.CRIT_CHANCE, 0),
            crit_damage=final_stats_dict.get(StatType.CRIT_DAMAGE, 200),
            hp=final_stats_dict.get(StatType.HP, 1),
            mana=final_stats_dict.get(StatType.MANA, 0),
            armor=final_stats_dict.get(StatType.ARMOR, 0),
            mr=final_stats_dict.get(StatType.MR, 0),
            ms=final_stats_dict.get(StatType.MS, 0),
        )

        # 7. Calcular stats derivados
        if build.target:
            final_stats.dps = self.calculate_dps(final_stats, build.target)
            final_stats.ttk = self.calculate_ttk(final_stats, build.target)

        final_stats.effective_hp_physical = self.calculate_effective_hp(final_stats.hp, final_stats.armor)
        final_stats.effective_hp_magical = self.calculate_effective_hp(final_stats.hp, final_stats.mr)

        return final_stats

    def calculate_damage_reduction(self, resistance: float) -> float:
        """
        Calcula a redução de dano baseada na resistência
        Fórmula: damage_reduction = resistance / (100 + resistance)
        """
        if resistance < 0:
            # Resistência negativa aumenta o dano
            return -abs(resistance) / (100 - abs(resistance))

        reduction = resistance / (100 + resistance)
        return min(reduction, self.MAX_DAMAGE_REDUCTION)

    def calculate_effective_hp(self, hp: float, resistance: float) -> float:
        """
        Calcula o HP efetivo considerando resistência
        """
        damage_reduction = self.calculate_damage_reduction(resistance)
        effective_multiplier = 1 / (1 - damage_reduction)
        return hp * effective_multiplier

    def calculate_average_damage_per_attack(self, final_stats: FinalStats) -> float:
        """
        Calcula o dano médio por ataque considerando crítico
        """
        base_damage = final_stats.ad
        crit_chance = final_stats.crit_chance / 100  # Converter para decimal
        crit_multiplier = final_stats.crit_damage / 100  # Converter para decimal

        # Dano médio = AD * (1 + crit_chance * (crit_multiplier - 1))
        average_damage = base_damage * (1 + crit_chance * (crit_multiplier - 1))

        return average_damage

    def calculate_dps(self, final_stats: FinalStats, target) -> float:
        """
        Calcula o DPS contra um alvo específico
        """
        # Dano médio por ataque
        avg_damage = self.calculate_average_damage_per_attack(final_stats)

        # Redução de dano por armor
        damage_reduction = self.calculate_damage_reduction(target.armor)
        effective_damage = avg_damage * (1 - damage_reduction)

        # DPS = dano efetivo * attack speed
        dps = effective_damage * final_stats.as_

        return round(dps, self.precision)

    def calculate_ttk(self, final_stats: FinalStats, target) -> float:
        """
        Calcula o Time to Kill (TTK) em segundos
        """
        dps = self.calculate_dps(final_stats, target)

        if dps <= 0:
            return float('inf')  # Impossível matar

        ttk = target.hp / dps
        return round(ttk, self.precision)

    def calculate_build_cost(self, build: Build) -> int:
        """
        Calcula o custo total de uma build
        """
        total_cost = sum(item.cost for item in build.items)
        return total_cost

    def compare_stats(self, stats_a: FinalStats, stats_b: FinalStats) -> Dict[str, float]:
        """
        Compara duas estatísticas finais e retorna as diferenças
        """
        differences = {
            'ad': stats_b.ad - stats_a.ad,
            'ap': stats_b.ap - stats_a.ap,
            'as': stats_b.as_ - stats_a.as_,
            'crit_chance': stats_b.crit_chance - stats_a.crit_chance,
            'hp': stats_b.hp - stats_a.hp,
            'armor': stats_b.armor - stats_a.armor,
            'mr': stats_b.mr - stats_a.mr,
            'ms': stats_b.ms - stats_a.ms,
        }

        if stats_a.dps and stats_b.dps:
            differences['dps'] = stats_b.dps - stats_a.dps

        if stats_a.ttk and stats_b.ttk:
            differences['ttk'] = stats_b.ttk - stats_a.ttk

        return differences

# Instância global do engine
formula_engine = FormulaEngine()
