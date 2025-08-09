"""
🔥 SmashBuilder - Cálculo de DPS 🔥
Módulo especializado em cálculos de DPS e análise de combate
"""

from typing import Dict, List, Optional, Tuple
import math

try:
    from .models import FinalStats, Target, ChampionStats
    from .formulas import FormulaEngine
except ImportError:
    # Fallback para execução direta
    from models import FinalStats, Target, ChampionStats
    from formulas import FormulaEngine

class DPSCalculator:
    """Calculadora especializada em DPS e análise de combate"""

    def __init__(self):
        self.formula_engine = FormulaEngine()

    def calculate_basic_attack_dps(self, stats: FinalStats, target: Target) -> Dict[str, float]:
        """
        Calcula DPS detalhado de ataques básicos
        """
        # Dano base por ataque
        base_damage = stats.ad

        # Cálculo de crítico
        crit_chance = stats.crit_chance / 100
        crit_multiplier = stats.crit_damage / 100

        # Dano médio por ataque (considerando crítico)
        avg_damage_per_attack = base_damage * (1 + crit_chance * (crit_multiplier - 1))

        # Redução de dano por armor
        armor_reduction = self.formula_engine.calculate_damage_reduction(target.armor)
        effective_damage = avg_damage_per_attack * (1 - armor_reduction)

        # DPS final
        dps = effective_damage * stats.as_

        # TTK
        ttk = target.hp / dps if dps > 0 else float('inf')

        return {
            'base_damage': round(base_damage, 2),
            'avg_damage_per_attack': round(avg_damage_per_attack, 2),
            'effective_damage': round(effective_damage, 2),
            'armor_reduction': round(armor_reduction * 100, 2),  # Em percentual
            'dps': round(dps, 2),
            'ttk': round(ttk, 2),
            'attacks_to_kill': math.ceil(target.hp / effective_damage) if effective_damage > 0 else float('inf')
        }

    def calculate_burst_damage(self, stats: FinalStats, target: Target, num_attacks: int = 3) -> Dict[str, float]:
        """
        Calcula dano de burst (primeiros X ataques)
        """
        # Dano por ataque
        base_damage = stats.ad
        crit_chance = stats.crit_chance / 100
        crit_multiplier = stats.crit_damage / 100

        # Redução de armor
        armor_reduction = self.formula_engine.calculate_damage_reduction(target.armor)

        # Simular ataques individuais
        total_damage = 0
        crit_attacks = 0

        for i in range(num_attacks):
            # Determinar se é crítico (probabilidade)
            is_crit = (i / num_attacks) < crit_chance  # Simplificação para demonstração

            if is_crit:
                damage = base_damage * crit_multiplier
                crit_attacks += 1
            else:
                damage = base_damage

            # Aplicar redução de armor
            effective_damage = damage * (1 - armor_reduction)
            total_damage += effective_damage

        return {
            'total_burst_damage': round(total_damage, 2),
            'average_damage_per_attack': round(total_damage / num_attacks, 2),
            'critical_attacks': crit_attacks,
            'time_for_burst': round(num_attacks / stats.as_, 2),
            'remaining_target_hp': max(0, target.hp - total_damage)
        }

    def calculate_dps_vs_multiple_targets(self, stats: FinalStats, targets: List[Target]) -> Dict[str, Dict[str, float]]:
        """
        Calcula DPS contra múltiplos alvos
        """
        results = {}

        for target in targets:
            dps_data = self.calculate_basic_attack_dps(stats, target)
            results[target.name] = dps_data

        return results

    def calculate_power_curve(self, champion: ChampionStats, items: List, levels: List[int] = None) -> Dict[int, Dict[str, float]]:
        """
        Calcula curva de poder por nível
        """
        if levels is None:
            levels = [1, 6, 11, 16, 18]

        try:
            from .models import Build, PRESET_TARGETS
        except ImportError:
            from models import Build, PRESET_TARGETS

        power_curve = {}
        dummy_target = PRESET_TARGETS["dummy"]

        for level in levels:
            # Criar build temporária
            build = Build(
                name=f"Power Curve Level {level}",
                champion=champion,
                level=level,
                items=items,
                target=dummy_target
            )

            # Calcular stats
            final_stats = self.formula_engine.calculate_final_stats(build)
            dps_data = self.calculate_basic_attack_dps(final_stats, dummy_target)

            power_curve[level] = {
                'ad': final_stats.ad,
                'as': final_stats.as_,
                'hp': final_stats.hp,
                'dps': dps_data['dps'],
                'effective_damage': dps_data['effective_damage']
            }

        return power_curve

    def calculate_gold_efficiency(self, stats_before: FinalStats, stats_after: FinalStats, item_cost: int) -> Dict[str, float]:
        """
        Calcula eficiência de gold de um item
        """
        # Valores base de gold por stat (aproximados do LoL)
        gold_values = {
            'ad': 35,      # ~35 gold por AD
            'ap': 21.75,   # ~21.75 gold por AP
            'as': 25,      # ~25 gold por 1% AS
            'hp': 2.67,    # ~2.67 gold por HP
            'armor': 20,   # ~20 gold por Armor
            'mr': 18,      # ~18 gold por MR
            'crit_chance': 40,  # ~40 gold por 1% crit
        }

        # Calcular diferenças
        stat_gains = {
            'ad': stats_after.ad - stats_before.ad,
            'ap': stats_after.ap - stats_before.ap,
            'as': (stats_after.as_ - stats_before.as_) * 100,  # Converter para %
            'hp': stats_after.hp - stats_before.hp,
            'armor': stats_after.armor - stats_before.armor,
            'mr': stats_after.mr - stats_before.mr,
            'crit_chance': stats_after.crit_chance - stats_before.crit_chance,
        }

        # Calcular valor em gold
        total_gold_value = 0
        for stat, gain in stat_gains.items():
            if gain > 0 and stat in gold_values:
                total_gold_value += gain * gold_values[stat]

        # Eficiência
        efficiency = (total_gold_value / item_cost * 100) if item_cost > 0 else 0

        return {
            'total_gold_value': round(total_gold_value, 2),
            'item_cost': item_cost,
            'efficiency_percent': round(efficiency, 2),
            'gold_per_stat': {stat: round(gain * gold_values.get(stat, 0), 2)
                             for stat, gain in stat_gains.items() if gain > 0}
        }

    def analyze_build_optimization(self, base_build, alternative_items: List) -> Dict[str, any]:
        """
        Analisa otimizações possíveis para uma build
        """
        try:
            from .models import Build
        except ImportError:
            from models import Build

        base_stats = self.formula_engine.calculate_final_stats(base_build)
        base_dps = self.calculate_basic_attack_dps(base_stats, base_build.target)

        recommendations = []

        for item in alternative_items:
            # Criar build com item alternativo
            new_items = base_build.items.copy()
            new_items.append(item)

            new_build = Build(
                name=f"With {item.name}",
                champion=base_build.champion,
                level=base_build.level,
                items=new_items,
                runes=base_build.runes,
                target=base_build.target
            )

            new_stats = self.formula_engine.calculate_final_stats(new_build)
            new_dps = self.calculate_basic_attack_dps(new_stats, base_build.target)

            # Calcular melhoria
            dps_improvement = new_dps['dps'] - base_dps['dps']
            dps_improvement_percent = (dps_improvement / base_dps['dps'] * 100) if base_dps['dps'] > 0 else 0

            # Eficiência de gold
            efficiency = self.calculate_gold_efficiency(base_stats, new_stats, item.cost)

            recommendations.append({
                'item_name': item.name,
                'dps_improvement': round(dps_improvement, 2),
                'dps_improvement_percent': round(dps_improvement_percent, 2),
                'gold_efficiency': efficiency['efficiency_percent'],
                'cost': item.cost,
                'dps_per_gold': round(dps_improvement / item.cost, 4) if item.cost > 0 else 0
            })

        # Ordenar por DPS por gold
        recommendations.sort(key=lambda x: x['dps_per_gold'], reverse=True)

        return {
            'base_dps': base_dps['dps'],
            'recommendations': recommendations[:5],  # Top 5
            'total_cost': sum(item.cost for item in base_build.items)
        }

    def calculate_survivability_metrics(self, stats: FinalStats) -> Dict[str, float]:
        """
        Calcula métricas de sobrevivência
        """
        # HP efetivo contra diferentes tipos de dano
        effective_hp_physical = self.formula_engine.calculate_effective_hp(stats.hp, stats.armor)
        effective_hp_magical = self.formula_engine.calculate_effective_hp(stats.hp, stats.mr)

        # Redução de dano
        physical_reduction = self.formula_engine.calculate_damage_reduction(stats.armor)
        magical_reduction = self.formula_engine.calculate_damage_reduction(stats.mr)

        return {
            'raw_hp': stats.hp,
            'effective_hp_physical': round(effective_hp_physical, 2),
            'effective_hp_magical': round(effective_hp_magical, 2),
            'physical_damage_reduction': round(physical_reduction * 100, 2),
            'magical_damage_reduction': round(magical_reduction * 100, 2),
            'armor': stats.armor,
            'mr': stats.mr,
            'survivability_score': round((effective_hp_physical + effective_hp_magical) / 2, 2)
        }

# Instância global do calculador
dps_calculator = DPSCalculator()
