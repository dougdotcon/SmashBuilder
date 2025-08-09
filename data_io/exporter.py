"""
🔥 SmashBuilder - Exportador de Dados 🔥
Sistema para exportar resultados em diferentes formatos
"""

import json
import csv
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Union, Any
from datetime import datetime

try:
    from calc.models import Build, FinalStats, BuildComparison
except ImportError:
    # Fallback para execução direta
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    from calc.models import Build, FinalStats, BuildComparison

class DataExporter:
    """Exportador principal de dados"""

    def __init__(self, output_dir: Union[str, Path] = None):
        if output_dir is None:
            self.output_dir = Path.cwd() / "exports"
        else:
            self.output_dir = Path(output_dir)

        # Criar diretório se não existir
        self.output_dir.mkdir(exist_ok=True)

    def export_build_to_json(self, build: Build, filename: str = None) -> Path:
        """Exporta uma build para JSON"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"build_{build.name.replace(' ', '_')}_{timestamp}.json"

        filepath = self.output_dir / filename

        # Converter build para dict
        build_dict = {
            "name": build.name,
            "champion": {
                "name": build.champion.name,
                "base_ad": build.champion.base_ad,
                "base_as": build.champion.base_as,
                "base_hp": build.champion.base_hp,
                "base_armor": build.champion.base_armor,
                "base_mr": build.champion.base_mr,
                "growth_ad": build.champion.growth_ad,
                "growth_as": build.champion.growth_as,
                "growth_hp": build.champion.growth_hp,
                "growth_armor": build.champion.growth_armor,
                "growth_mr": build.champion.growth_mr,
                "champion_class": build.champion.champion_class,
                "patch": build.champion.patch
            },
            "level": build.level,
            "items": [
                {
                    "name": item.name,
                    "cost": item.cost,
                    "modifiers": [
                        {
                            "stat": mod.stat.value,
                            "value": mod.value,
                            "modifier_type": mod.modifier_type.value
                        }
                        for mod in item.modifiers
                    ]
                }
                for item in build.items
            ],
            "runes": {
                "name": build.runes.name,
                "description": build.runes.description,
                "modifiers": [
                    {
                        "stat": mod.stat.value,
                        "value": mod.value,
                        "modifier_type": mod.modifier_type.value
                    }
                    for mod in build.runes.modifiers
                ]
            } if build.runes else None,
            "target": {
                "name": build.target.name,
                "hp": build.target.hp,
                "armor": build.target.armor,
                "mr": build.target.mr
            } if build.target else None,
            "final_stats": {
                "level": build.final_stats.level,
                "ad": build.final_stats.ad,
                "ap": build.final_stats.ap,
                "as": build.final_stats.as_,
                "crit_chance": build.final_stats.crit_chance,
                "crit_damage": build.final_stats.crit_damage,
                "hp": build.final_stats.hp,
                "mana": build.final_stats.mana,
                "armor": build.final_stats.armor,
                "mr": build.final_stats.mr,
                "ms": build.final_stats.ms,
                "dps": build.final_stats.dps,
                "ttk": build.final_stats.ttk,
                "effective_hp_physical": build.final_stats.effective_hp_physical,
                "effective_hp_magical": build.final_stats.effective_hp_magical
            } if build.final_stats else None,
            "export_timestamp": datetime.now().isoformat(),
            "total_cost": sum(item.cost for item in build.items)
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(build_dict, f, indent=2, ensure_ascii=False)

        return filepath

    def export_build_to_csv(self, build: Build, filename: str = None) -> Path:
        """Exporta uma build para CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"build_{build.name.replace(' ', '_')}_{timestamp}.csv"

        filepath = self.output_dir / filename

        # Preparar dados para CSV
        rows = []

        # Informações básicas
        rows.append(["Categoria", "Atributo", "Valor"])
        rows.append(["Build", "Nome", build.name])
        rows.append(["Build", "Campeão", build.champion.name])
        rows.append(["Build", "Nível", build.level])
        rows.append(["Build", "Custo Total", sum(item.cost for item in build.items)])
        rows.append([])

        # Stats finais
        if build.final_stats:
            rows.append(["Stats Finais", "Attack Damage", build.final_stats.ad])
            rows.append(["Stats Finais", "Ability Power", build.final_stats.ap])
            rows.append(["Stats Finais", "Attack Speed", build.final_stats.as_])
            rows.append(["Stats Finais", "Critical Chance (%)", build.final_stats.crit_chance])
            rows.append(["Stats Finais", "Critical Damage (%)", build.final_stats.crit_damage])
            rows.append(["Stats Finais", "Health", build.final_stats.hp])
            rows.append(["Stats Finais", "Mana", build.final_stats.mana])
            rows.append(["Stats Finais", "Armor", build.final_stats.armor])
            rows.append(["Stats Finais", "Magic Resistance", build.final_stats.mr])
            rows.append(["Stats Finais", "Movement Speed", build.final_stats.ms])
            rows.append([])

            # DPS e combate
            if build.final_stats.dps:
                rows.append(["Combate", "DPS", build.final_stats.dps])
            if build.final_stats.ttk:
                rows.append(["Combate", "Time to Kill (s)", build.final_stats.ttk])
            if build.final_stats.effective_hp_physical:
                rows.append(["Combate", "HP Efetivo (Físico)", build.final_stats.effective_hp_physical])
            if build.final_stats.effective_hp_magical:
                rows.append(["Combate", "HP Efetivo (Mágico)", build.final_stats.effective_hp_magical])
            rows.append([])

        # Itens
        rows.append(["Itens", "Nome", "Custo"])
        for item in build.items:
            rows.append(["Itens", item.name, item.cost])

        # Escrever CSV
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        return filepath

    def export_comparison_to_csv(self, comparison: BuildComparison, filename: str = None) -> Path:
        """Exporta comparação de builds para CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"comparison_{timestamp}.csv"

        filepath = self.output_dir / filename

        rows = []
        rows.append(["Atributo", "Build A", "Build B", "Diferença", "% Diferença"])

        # Stats básicos
        stats_a = comparison.build_a.final_stats
        stats_b = comparison.build_b.final_stats

        if stats_a and stats_b:
            comparisons = [
                ("Attack Damage", stats_a.ad, stats_b.ad),
                ("Ability Power", stats_a.ap, stats_b.ap),
                ("Attack Speed", stats_a.as_, stats_b.as_),
                ("Critical Chance", stats_a.crit_chance, stats_b.crit_chance),
                ("Health", stats_a.hp, stats_b.hp),
                ("Armor", stats_a.armor, stats_b.armor),
                ("Magic Resistance", stats_a.mr, stats_b.mr),
                ("Movement Speed", stats_a.ms, stats_b.ms),
            ]

            if stats_a.dps and stats_b.dps:
                comparisons.append(("DPS", stats_a.dps, stats_b.dps))

            if stats_a.ttk and stats_b.ttk:
                comparisons.append(("Time to Kill", stats_a.ttk, stats_b.ttk))

            for stat_name, value_a, value_b in comparisons:
                diff = value_b - value_a
                percent_diff = (diff / value_a * 100) if value_a != 0 else 0

                rows.append([
                    stat_name,
                    round(value_a, 2),
                    round(value_b, 2),
                    round(diff, 2),
                    f"{round(percent_diff, 2)}%"
                ])

        # Custo
        cost_a = sum(item.cost for item in comparison.build_a.items)
        cost_b = sum(item.cost for item in comparison.build_b.items)
        cost_diff = cost_b - cost_a
        cost_percent = (cost_diff / cost_a * 100) if cost_a != 0 else 0

        rows.append([
            "Custo Total",
            cost_a,
            cost_b,
            cost_diff,
            f"{round(cost_percent, 2)}%"
        ])

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        return filepath

    def export_level_table_to_csv(self, champion_name: str, items: List[str], levels: List[int], stats_by_level: Dict[int, Dict], filename: str = None) -> Path:
        """Exporta tabela por níveis para CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"level_table_{champion_name.replace(' ', '_')}_{timestamp}.csv"

        filepath = self.output_dir / filename

        # Cabeçalho
        headers = ["Nível", "AD", "AS", "HP", "Armor", "MR", "DPS", "TTK"]

        rows = [headers]

        for level in sorted(levels):
            if level in stats_by_level:
                stats = stats_by_level[level]
                row = [
                    level,
                    round(stats.get("ad", 0), 2),
                    round(stats.get("as", 0), 2),
                    round(stats.get("hp", 0), 2),
                    round(stats.get("armor", 0), 2),
                    round(stats.get("mr", 0), 2),
                    round(stats.get("dps", 0), 2),
                    round(stats.get("ttk", 0), 2)
                ]
                rows.append(row)

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        return filepath

    def export_to_yaml(self, data: Dict, filename: str) -> Path:
        """Exporta dados para YAML"""
        filepath = self.output_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, allow_unicode=True)

        return filepath

    def create_build_report(self, build: Build, filename: str = None) -> Path:
        """Cria um relatório completo da build em texto"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"report_{build.name.replace(' ', '_')}_{timestamp}.txt"

        filepath = self.output_dir / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("🔥 SMASHBUILDER - RELATÓRIO DE BUILD 🔥\n")
            f.write("=" * 50 + "\n\n")

            f.write(f"Build: {build.name}\n")
            f.write(f"Campeão: {build.champion.name}\n")
            f.write(f"Nível: {build.level}\n")
            f.write(f"Classe: {build.champion.champion_class}\n")
            f.write(f"Patch: {build.champion.patch}\n\n")

            # Itens
            f.write("ITENS:\n")
            f.write("-" * 20 + "\n")
            total_cost = 0
            for item in build.items:
                f.write(f"• {item.name} ({item.cost}g)\n")
                total_cost += item.cost
            f.write(f"\nCusto Total: {total_cost}g\n\n")

            # Stats finais
            if build.final_stats:
                f.write("ESTATÍSTICAS FINAIS:\n")
                f.write("-" * 25 + "\n")
                f.write(f"Attack Damage: {build.final_stats.ad}\n")
                f.write(f"Ability Power: {build.final_stats.ap}\n")
                f.write(f"Attack Speed: {build.final_stats.as_}\n")
                f.write(f"Critical Chance: {build.final_stats.crit_chance}%\n")
                f.write(f"Health: {build.final_stats.hp}\n")
                f.write(f"Armor: {build.final_stats.armor}\n")
                f.write(f"Magic Resistance: {build.final_stats.mr}\n")
                f.write(f"Movement Speed: {build.final_stats.ms}\n\n")

                # Combate
                if build.final_stats.dps:
                    f.write("ANÁLISE DE COMBATE:\n")
                    f.write("-" * 20 + "\n")
                    f.write(f"DPS: {build.final_stats.dps}\n")
                    if build.final_stats.ttk:
                        f.write(f"Time to Kill: {build.final_stats.ttk}s\n")
                    if build.final_stats.effective_hp_physical:
                        f.write(f"HP Efetivo (Físico): {build.final_stats.effective_hp_physical}\n")
                    if build.final_stats.effective_hp_magical:
                        f.write(f"HP Efetivo (Mágico): {build.final_stats.effective_hp_magical}\n")

            f.write(f"\nRelatório gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")

        return filepath

# Instância global do exportador
data_exporter = DataExporter()
