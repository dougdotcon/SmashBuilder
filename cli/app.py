"""
🔥 SmashBuilder - Aplicação CLI Principal 🔥
Interface de linha de comando usando Typer
"""

import typer
from typing import List, Optional
from pathlib import Path
import json
import sys

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

try:
    from calc.models import Build, Target, PRESET_TARGETS
    from calc.formulas import formula_engine
    from data_io.loader import data_loader
    from data_io.exporter import data_exporter
except ImportError:
    # Fallback para execução direta
    sys.path.append(str(Path(__file__).parent.parent))
    from calc.models import Build, Target, PRESET_TARGETS
    from calc.formulas import formula_engine
    from data_io.loader import data_loader
    from data_io.exporter import data_exporter

app = typer.Typer(
    name="smashbuilder",
    help="🔥 SmashBuilder - Calculadora de Builds para League of Legends 🔥"
)
console = Console()

@app.command()
def quick():
    """Calculadora rápida interativa com seleção por número"""
    console.print("🔥 [bold cyan]SmashBuilder - Calculadora Rápida[/bold cyan] 🔥")
    console.print()

    # Carregar dados
    try:
        champions = data_loader.load_champions()
        items = data_loader.load_items()
        presets = data_loader.load_presets()
    except Exception as e:
        console.print(f"[red]Erro ao carregar dados: {e}[/red]")
        raise typer.Exit(1)

    # Seleção de campeão por número
    console.print("[yellow]📋 Campeões disponíveis:[/yellow]")
    champion_list = list(champions.values())

    champion_table = Table(title="Selecionar Campeão")
    champion_table.add_column("#", style="cyan")
    champion_table.add_column("Nome", style="yellow")
    champion_table.add_column("Classe", style="green")
    champion_table.add_column("AD Base", style="red")

    for i, champion in enumerate(champion_list, 1):
        champion_table.add_row(
            str(i),
            champion.name,
            champion.champion_class,
            f"{champion.base_ad:.0f}"
        )

    console.print(champion_table)

    champion_choice = typer.prompt("\nEscolha o campeão (número ou nome)")

    # Tentar interpretar como número primeiro
    try:
        champion_num = int(champion_choice)
        if 1 <= champion_num <= len(champion_list):
            champion = champion_list[champion_num - 1]
        else:
            console.print(f"[red]Número inválido! Use 1-{len(champion_list)}[/red]")
            raise typer.Exit(1)
    except ValueError:
        # Se não for número, tentar como nome
        champion = data_loader.get_champion(champion_choice)
        if not champion:
            console.print(f"[red]Campeão '{champion_choice}' não encontrado![/red]")
            raise typer.Exit(1)

    # Nível
    level = typer.prompt("Nível (1-18)", type=int, default=11)
    if not (1 <= level <= 18):
        console.print("[red]Nível deve estar entre 1 e 18![/red]")
        raise typer.Exit(1)

    # Seleção de itens por número
    console.print(f"\n[green]✅ Campeão selecionado: {champion.name}[/green]")

    console.print("\n[yellow]🛡️ Itens disponíveis:[/yellow]")
    item_list = list(items.values())
    # Mostrar itens ordenados por custo
    sorted_items = sorted(item_list, key=lambda x: x.cost, reverse=True)[:15]  # Top 15

    item_table = Table(title="Selecionar Itens")
    item_table.add_column("#", style="cyan")
    item_table.add_column("Nome", style="yellow")
    item_table.add_column("Custo", style="green")
    item_table.add_column("Tipo", style="magenta")

    for i, item in enumerate(sorted_items, 1):
        item_type = "🔥 Mítico" if item.mythic else "⭐ Único" if item.unique else "Normal"
        item_table.add_row(
            str(i),
            item.name,
            f"{item.cost}g",
            item_type
        )

    console.print(item_table)

    items_input = typer.prompt("\nEscolha os itens (números separados por vírgula, ex: 1,3,5)", default="")
    selected_items = []

    if items_input.strip():
        for item_choice in items_input.split(","):
            item_choice = item_choice.strip()

            try:
                # Tentar interpretar como número
                item_num = int(item_choice)
                if 1 <= item_num <= len(sorted_items):
                    item = sorted_items[item_num - 1]

                    # Verificar regra de mítico
                    if item.mythic:
                        mythic_count = sum(1 for selected_item in selected_items if selected_item.mythic)
                        if mythic_count > 0:
                            console.print(f"[red]⚠️ Apenas um item mítico permitido! Ignorando {item.name}[/red]")
                            continue

                    selected_items.append(item)
                    console.print(f"[green]✅ Adicionado: {item.name}[/green]")
                else:
                    console.print(f"[yellow]Número {item_num} inválido, ignorando...[/yellow]")
            except ValueError:
                # Se não for número, tentar como nome
                item = data_loader.get_item(item_choice)
                if item:
                    selected_items.append(item)
                    console.print(f"[green]✅ Adicionado: {item.name}[/green]")
                else:
                    console.print(f"[yellow]Item '{item_choice}' não encontrado, ignorando...[/yellow]")

    # Seleção de alvo por número
    console.print(f"\n[green]✅ Itens selecionados: {len(selected_items)}[/green]")

    console.print("\n[yellow]🎯 Alvos disponíveis:[/yellow]")
    target_list = list(presets["targets"].values())

    target_table = Table(title="Selecionar Alvo")
    target_table.add_column("#", style="cyan")
    target_table.add_column("Nome", style="yellow")
    target_table.add_column("HP", style="red")
    target_table.add_column("Armor", style="blue")
    target_table.add_column("MR", style="magenta")

    for i, target_obj in enumerate(target_list, 1):
        target_table.add_row(
            str(i),
            target_obj.name,
            f"{target_obj.hp:.0f}",
            f"{target_obj.armor:.0f}",
            f"{target_obj.mr:.0f}"
        )

    console.print(target_table)

    target_input = typer.prompt("Escolha o alvo (número ou nome)", default="1")

    try:
        # Tentar interpretar como número
        target_num = int(target_input)
        if 1 <= target_num <= len(target_list):
            target = target_list[target_num - 1]
        else:
            console.print(f"[yellow]Número inválido, usando alvo padrão[/yellow]")
            target = target_list[0]  # Primeiro alvo como padrão
    except ValueError:
        # Se não for número, tentar como nome/chave
        target = presets["targets"].get(target_input.lower())
        if not target:
            # Tentar buscar por nome
            target = next((t for t in target_list if t.name.lower() == target_input.lower()), None)
            if not target:
                console.print(f"[yellow]Alvo '{target_input}' não encontrado, usando 'Frágil'[/yellow]")
                target = target_list[0]

    # Criar e calcular build
    build = Build(
        name=f"{champion.name} Level {level}",
        champion=champion,
        level=level,
        items=selected_items,
        target=target
    )

    console.print("\n[green]Calculando build...[/green]")

    try:
        final_stats = formula_engine.calculate_final_stats(build)
        build.final_stats = final_stats

        # Exibir resultados
        display_build_results(build)

        # Opção de exportar
        export = typer.confirm("\nDeseja exportar os resultados?", default=False)
        if export:
            export_format = typer.prompt("Formato (json/csv/txt)", default="csv")

            if export_format.lower() == "json":
                filepath = data_exporter.export_build_to_json(build)
            elif export_format.lower() == "txt":
                filepath = data_exporter.create_build_report(build)
            else:
                filepath = data_exporter.export_build_to_csv(build)

            console.print(f"[green]Resultados exportados para: {filepath}[/green]")

    except Exception as e:
        console.print(f"[red]Erro ao calcular build: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def build(
    champ: str = typer.Option(..., "--champ", "-c", help="Nome do campeão"),
    level: int = typer.Option(11, "--level", "-l", help="Nível do campeão (1-18)"),
    items: str = typer.Option("", "--items", "-i", help="Itens separados por vírgula"),
    target: str = typer.Option("fragile", "--target", "-t", help="Alvo para cálculo de DPS"),
    export_format: Optional[str] = typer.Option(None, "--export", "-e", help="Formato de export (json/csv/txt)")
):
    """Calcula uma build específica"""

    try:
        # Carregar dados
        champion = data_loader.get_champion(champ)
        if not champion:
            console.print(f"[red]Campeão '{champ}' não encontrado![/red]")
            raise typer.Exit(1)

        # Validar nível
        if not (1 <= level <= 18):
            console.print("[red]Nível deve estar entre 1 e 18![/red]")
            raise typer.Exit(1)

        # Carregar itens
        selected_items = []
        if items.strip():
            for item_name in items.split(","):
                item_name = item_name.strip()
                item = data_loader.get_item(item_name)
                if item:
                    selected_items.append(item)
                else:
                    console.print(f"[yellow]Item '{item_name}' não encontrado, ignorando...[/yellow]")

        # Carregar alvo
        presets = data_loader.load_presets()
        target_obj = presets["targets"].get(target.lower())
        if not target_obj:
            console.print(f"[yellow]Alvo '{target}' não encontrado, usando 'fragile'[/yellow]")
            target_obj = presets["targets"]["fragile"]

        # Criar e calcular build
        build_obj = Build(
            name=f"{champion.name} Level {level}",
            champion=champion,
            level=level,
            items=selected_items,
            target=target_obj
        )

        final_stats = formula_engine.calculate_final_stats(build_obj)
        build_obj.final_stats = final_stats

        # Exibir resultados
        display_build_results(build_obj)

        # Exportar se solicitado
        if export_format:
            if export_format.lower() == "json":
                filepath = data_exporter.export_build_to_json(build_obj)
            elif export_format.lower() == "txt":
                filepath = data_exporter.create_build_report(build_obj)
            else:
                filepath = data_exporter.export_build_to_csv(build_obj)

            console.print(f"[green]Resultados exportados para: {filepath}[/green]")

    except Exception as e:
        console.print(f"[red]Erro: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def compare(
    build_a: str = typer.Option(..., "--buildA", "-a", help="Arquivo JSON da primeira build"),
    build_b: str = typer.Option(..., "--buildB", "-b", help="Arquivo JSON da segunda build"),
    export_format: Optional[str] = typer.Option(None, "--export", "-e", help="Formato de export (csv/json)")
):
    """Compara duas builds"""
    console.print("🔥 [bold cyan]Comparação de Builds[/bold cyan] 🔥")

    try:
        # Carregar builds dos arquivos JSON
        import json
        from pathlib import Path

        build_a_path = Path(build_a)
        build_b_path = Path(build_b)

        if not build_a_path.exists():
            console.print(f"[red]Arquivo não encontrado: {build_a}[/red]")
            raise typer.Exit(1)

        if not build_b_path.exists():
            console.print(f"[red]Arquivo não encontrado: {build_b}[/red]")
            raise typer.Exit(1)

        # Carregar dados das builds
        with open(build_a_path, 'r', encoding='utf-8') as f:
            build_a_data = json.load(f)

        with open(build_b_path, 'r', encoding='utf-8') as f:
            build_b_data = json.load(f)

        # Reconstruir builds a partir dos dados
        build_obj_a = reconstruct_build_from_json(build_a_data)
        build_obj_b = reconstruct_build_from_json(build_b_data)

        # Calcular stats finais
        final_stats_a = formula_engine.calculate_final_stats(build_obj_a)
        final_stats_b = formula_engine.calculate_final_stats(build_obj_b)

        build_obj_a.final_stats = final_stats_a
        build_obj_b.final_stats = final_stats_b

        # Criar comparação
        from calc.models import BuildComparison
        comparison = BuildComparison(build_a=build_obj_a, build_b=build_obj_b)

        # Calcular diferenças
        stat_differences = formula_engine.compare_stats(final_stats_a, final_stats_b)
        comparison.stat_differences = stat_differences
        comparison.dps_difference = stat_differences.get('dps', 0)
        comparison.cost_difference = sum(item.cost for item in build_obj_b.items) - sum(item.cost for item in build_obj_a.items)

        # Exibir comparação
        display_build_comparison(comparison)

        # Exportar se solicitado
        if export_format:
            if export_format.lower() == "csv":
                filepath = data_exporter.export_comparison_to_csv(comparison)
                console.print(f"[green]Comparação exportada para: {filepath}[/green]")
            else:
                console.print(f"[yellow]Formato {export_format} não suportado para comparação[/yellow]")

    except Exception as e:
        console.print(f"[red]Erro ao comparar builds: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def table(
    champ: str = typer.Option(..., "--champ", "-c", help="Nome do campeão"),
    levels: str = typer.Option("1,6,11,16,18", "--levels", "-l", help="Níveis separados por vírgula"),
    items: str = typer.Option("", "--items", "-i", help="Itens separados por vírgula")
):
    """Exibe tabela de stats por nível"""
    console.print("🔥 [bold cyan]Tabela por Níveis[/bold cyan] 🔥")

    try:
        # Carregar campeão
        champion = data_loader.get_champion(champ)
        if not champion:
            console.print(f"[red]Campeão '{champ}' não encontrado![/red]")
            raise typer.Exit(1)

        # Processar níveis
        level_list = [int(l.strip()) for l in levels.split(",")]
        level_list = [l for l in level_list if 1 <= l <= 18]

        if not level_list:
            console.print("[red]Nenhum nível válido fornecido![/red]")
            raise typer.Exit(1)

        # Carregar itens
        selected_items = []
        if items.strip():
            for item_name in items.split(","):
                item_name = item_name.strip()
                item = data_loader.get_item(item_name)
                if item:
                    selected_items.append(item)

        # Criar tabela
        table = Table(title=f"📊 {champion.name} - Stats por Nível")
        table.add_column("Nível", style="cyan")
        table.add_column("AD", style="red")
        table.add_column("AS", style="yellow")
        table.add_column("HP", style="green")
        table.add_column("Armor", style="blue")
        table.add_column("MR", style="magenta")

        for level in sorted(level_list):
            # Calcular stats para este nível
            build_obj = Build(
                name=f"{champion.name} Level {level}",
                champion=champion,
                level=level,
                items=selected_items
            )

            final_stats = formula_engine.calculate_final_stats(build_obj)

            table.add_row(
                str(level),
                f"{final_stats.ad:.1f}",
                f"{final_stats.as_:.2f}",
                f"{final_stats.hp:.0f}",
                f"{final_stats.armor:.1f}",
                f"{final_stats.mr:.1f}"
            )

        console.print(table)

    except Exception as e:
        console.print(f"[red]Erro: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def champions():
    """Lista todos os campeões disponíveis"""
    try:
        champions = data_loader.load_champions()

        table = Table(title="📋 Campeões Disponíveis")
        table.add_column("Nome", style="cyan")
        table.add_column("Classe", style="yellow")
        table.add_column("AD Base", style="red")
        table.add_column("AS Base", style="green")
        table.add_column("HP Base", style="blue")

        for champion in sorted(champions.values(), key=lambda c: c.name):
            table.add_row(
                champion.name,
                champion.champion_class,
                f"{champion.base_ad:.0f}",
                f"{champion.base_as:.3f}",
                f"{champion.base_hp:.0f}"
            )

        console.print(table)
        console.print(f"\n[green]Total: {len(champions)} campeões[/green]")

    except Exception as e:
        console.print(f"[red]Erro ao carregar campeões: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def items():
    """Lista todos os itens disponíveis"""
    try:
        items = data_loader.load_items()

        table = Table(title="🛡️ Itens Disponíveis")
        table.add_column("#", style="dim")
        table.add_column("Nome", style="cyan")
        table.add_column("Custo", style="yellow")
        table.add_column("Mítico", style="red")
        table.add_column("Único", style="green")

        for i, item in enumerate(sorted(items.values(), key=lambda i: i.cost, reverse=True), 1):
            table.add_row(
                str(i),
                item.name,
                f"{item.cost}g",
                "✓" if item.mythic else "✗",
                "✓" if item.unique else "✗"
            )

        console.print(table)
        console.print(f"\n[green]Total: {len(items)} itens[/green]")

    except Exception as e:
        console.print(f"[red]Erro ao carregar itens: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def add_champion():
    """Adiciona um novo campeão interativamente"""
    console.print("🔥 [bold cyan]Adicionar Novo Campeão[/bold cyan] 🔥")

    try:
        from calc.models import ChampionStats
        import json

        # Coletar dados do campeão
        name = typer.prompt("Nome do campeão")
        champion_class = typer.prompt("Classe do campeão", default="Unknown")
        patch = typer.prompt("Patch", default="14.1")

        console.print("\n[yellow]📊 Stats Base (Nível 1):[/yellow]")
        base_ad = typer.prompt("Attack Damage base", type=float)
        base_as = typer.prompt("Attack Speed base", type=float)
        base_hp = typer.prompt("Health base", type=float)
        base_mana = typer.prompt("Mana base (0 se não usa mana)", type=float, default=0)
        base_armor = typer.prompt("Armor base", type=float)
        base_mr = typer.prompt("Magic Resistance base", type=float)
        base_ms = typer.prompt("Movement Speed base", type=float)

        console.print("\n[yellow]📈 Crescimento por Nível:[/yellow]")
        growth_ad = typer.prompt("AD por nível", type=float)
        growth_as = typer.prompt("AS% por nível", type=float)
        growth_hp = typer.prompt("HP por nível", type=float)
        growth_mana = typer.prompt("Mana por nível", type=float, default=0)
        growth_armor = typer.prompt("Armor por nível", type=float)
        growth_mr = typer.prompt("MR por nível", type=float)
        growth_ms = typer.prompt("MS por nível (geralmente 0)", type=float, default=0)

        # Criar objeto campeão para validação
        champion = ChampionStats(
            name=name,
            base_ad=base_ad,
            base_ap=0,  # AP base é sempre 0
            base_as=base_as,
            base_hp=base_hp,
            base_mana=base_mana,
            base_armor=base_armor,
            base_mr=base_mr,
            base_ms=base_ms,
            growth_ad=growth_ad,
            growth_ap=0,  # AP growth é sempre 0
            growth_as=growth_as,
            growth_hp=growth_hp,
            growth_mana=growth_mana,
            growth_armor=growth_armor,
            growth_mr=growth_mr,
            growth_ms=growth_ms,
            champion_class=champion_class,
            patch=patch
        )

        # Mostrar preview
        console.print("\n[green]✅ Preview do Campeão:[/green]")
        preview_table = Table(title=f"📋 {champion.name}")
        preview_table.add_column("Atributo", style="yellow")
        preview_table.add_column("Base", style="cyan")
        preview_table.add_column("Crescimento", style="green")
        preview_table.add_column("Nível 18", style="magenta")

        level_18_stats = [
            ("AD", base_ad, growth_ad, base_ad + (growth_ad * 17)),
            ("AS", base_as, f"{growth_as}%", base_as * (1 + (growth_as * 17 / 100))),
            ("HP", base_hp, growth_hp, base_hp + (growth_hp * 17)),
            ("Armor", base_armor, growth_armor, base_armor + (growth_armor * 17)),
            ("MR", base_mr, growth_mr, base_mr + (growth_mr * 17)),
        ]

        for stat_name, base_val, growth_val, level_18_val in level_18_stats:
            preview_table.add_row(
                stat_name,
                f"{base_val:.1f}",
                f"{growth_val}",
                f"{level_18_val:.1f}"
            )

        console.print(preview_table)

        # Confirmar adição
        if typer.confirm("\nDeseja adicionar este campeão?"):
            # Carregar dados existentes
            champions_file = Path("data/champions.json")
            with open(champions_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Adicionar novo campeão
            champion_dict = {
                "name": champion.name,
                "base_ad": champion.base_ad,
                "base_ap": champion.base_ap,
                "base_as": champion.base_as,
                "base_hp": champion.base_hp,
                "base_mana": champion.base_mana,
                "base_armor": champion.base_armor,
                "base_mr": champion.base_mr,
                "base_ms": champion.base_ms,
                "growth_ad": champion.growth_ad,
                "growth_ap": champion.growth_ap,
                "growth_as": champion.growth_as,
                "growth_hp": champion.growth_hp,
                "growth_mana": champion.growth_mana,
                "growth_armor": champion.growth_armor,
                "growth_mr": champion.growth_mr,
                "growth_ms": champion.growth_ms,
                "champion_class": champion.champion_class,
                "patch": champion.patch
            }

            data["champions"].append(champion_dict)

            # Salvar arquivo
            with open(champions_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            console.print(f"[green]✅ Campeão '{champion.name}' adicionado com sucesso![/green]")

            # Recarregar dados
            data_loader.load_champions(force_reload=True)
        else:
            console.print("[yellow]❌ Operação cancelada[/yellow]")

    except Exception as e:
        console.print(f"[red]Erro ao adicionar campeão: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def add_item():
    """Adiciona um novo item interativamente"""
    console.print("🔥 [bold cyan]Adicionar Novo Item[/bold cyan] 🔥")

    try:
        from calc.models import Item, ItemModifier, StatType, ModifierType
        import json

        # Coletar dados básicos do item
        name = typer.prompt("Nome do item")
        cost = typer.prompt("Custo em gold", type=int, default=0)
        unique = typer.confirm("É um item único?", default=False)
        mythic = typer.confirm("É um item mítico?", default=False)

        # Coletar modificadores
        modifiers = []
        console.print("\n[yellow]📊 Modificadores do Item:[/yellow]")
        console.print("Stats disponíveis:")

        stat_options = {
            1: ("attack_damage", "Attack Damage"),
            2: ("ability_power", "Ability Power"),
            3: ("attack_speed", "Attack Speed"),
            4: ("critical_chance", "Critical Chance"),
            5: ("health", "Health"),
            6: ("mana", "Mana"),
            7: ("armor", "Armor"),
            8: ("magic_resistance", "Magic Resistance"),
            9: ("movement_speed", "Movement Speed"),
        }

        for num, (stat_key, stat_name) in stat_options.items():
            console.print(f"  {num}. {stat_name}")

        while True:
            console.print("\n[cyan]Adicionar modificador (ou 0 para finalizar):[/cyan]")
            choice = typer.prompt("Escolha o stat (número)", type=int)

            if choice == 0:
                break

            if choice not in stat_options:
                console.print("[red]Opção inválida![/red]")
                continue

            stat_key, stat_name = stat_options[choice]
            value = typer.prompt(f"Valor para {stat_name}", type=float)

            # Determinar tipo de modificador
            if stat_key in ["attack_speed", "critical_chance"]:
                mod_type = typer.prompt("Tipo (flat/percent)", default="percent")
            else:
                mod_type = typer.prompt("Tipo (flat/percent)", default="flat")

            try:
                modifier = ItemModifier(
                    stat=StatType(stat_key),
                    value=value,
                    modifier_type=ModifierType(mod_type)
                )
                modifiers.append(modifier)
                console.print(f"[green]✅ Adicionado: +{value} {stat_name} ({mod_type})[/green]")
            except ValueError as e:
                console.print(f"[red]Erro: {e}[/red]")

        # Criar objeto item para validação
        item = Item(
            name=name,
            modifiers=modifiers,
            cost=cost,
            unique=unique,
            mythic=mythic
        )

        # Mostrar preview
        console.print("\n[green]✅ Preview do Item:[/green]")
        preview_table = Table(title=f"🛡️ {item.name}")
        preview_table.add_column("Propriedade", style="yellow")
        preview_table.add_column("Valor", style="cyan")

        preview_table.add_row("Custo", f"{item.cost}g")
        preview_table.add_row("Único", "✓" if item.unique else "✗")
        preview_table.add_row("Mítico", "✓" if item.mythic else "✗")
        preview_table.add_row("Modificadores", str(len(item.modifiers)))

        console.print(preview_table)

        if modifiers:
            mod_table = Table(title="📊 Modificadores")
            mod_table.add_column("Stat", style="yellow")
            mod_table.add_column("Valor", style="green")
            mod_table.add_column("Tipo", style="cyan")

            for mod in modifiers:
                stat_name = mod.stat.value.replace("_", " ").title()
                mod_table.add_row(stat_name, str(mod.value), mod.modifier_type.value)

            console.print(mod_table)

        # Confirmar adição
        if typer.confirm("\nDeseja adicionar este item?"):
            # Carregar dados existentes
            items_file = Path("data/items.json")
            with open(items_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # Adicionar novo item
            item_dict = {
                "name": item.name,
                "modifiers": [
                    {
                        "stat": mod.stat.value,
                        "value": mod.value,
                        "modifier_type": mod.modifier_type.value
                    }
                    for mod in item.modifiers
                ],
                "cost": item.cost,
                "unique": item.unique,
                "mythic": item.mythic
            }

            data["items"].append(item_dict)

            # Salvar arquivo
            with open(items_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

            console.print(f"[green]✅ Item '{item.name}' adicionado com sucesso![/green]")

            # Recarregar dados
            data_loader.load_items(force_reload=True)
        else:
            console.print("[yellow]❌ Operação cancelada[/yellow]")

    except Exception as e:
        console.print(f"[red]Erro ao adicionar item: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def compare_interactive():
    """Compara duas builds interativamente"""
    console.print("🔥 [bold cyan]Comparação Interativa de Builds[/bold cyan] 🔥")

    try:
        # Carregar dados
        champions = data_loader.load_champions()
        items = data_loader.load_items()
        presets = data_loader.load_presets()

        builds = []

        for build_num in [1, 2]:
            console.print(f"\n[yellow]📋 Configurando Build {build_num}:[/yellow]")

            # Seleção de campeão
            champion_list = list(champions.values())
            champion_table = Table(title=f"Campeão para Build {build_num}")
            champion_table.add_column("#", style="cyan")
            champion_table.add_column("Nome", style="yellow")
            champion_table.add_column("Classe", style="green")

            for i, champion in enumerate(champion_list, 1):
                champion_table.add_row(str(i), champion.name, champion.champion_class)

            console.print(champion_table)
            champion_choice = typer.prompt(f"Campeão para Build {build_num} (número)")

            try:
                champion_num = int(champion_choice)
                if 1 <= champion_num <= len(champion_list):
                    champion = champion_list[champion_num - 1]
                else:
                    console.print("[red]Número inválido![/red]")
                    continue
            except ValueError:
                console.print("[red]Digite um número válido![/red]")
                continue

            # Nível
            level = typer.prompt(f"Nível para Build {build_num}", type=int, default=11)
            if not (1 <= level <= 18):
                console.print("[red]Nível inválido, usando 11[/red]")
                level = 11

            # Itens
            item_list = sorted(items.values(), key=lambda x: x.cost, reverse=True)[:15]
            item_table = Table(title=f"Itens para Build {build_num}")
            item_table.add_column("#", style="cyan")
            item_table.add_column("Nome", style="yellow")
            item_table.add_column("Custo", style="green")

            for i, item in enumerate(item_list, 1):
                item_table.add_row(str(i), item.name, f"{item.cost}g")

            console.print(item_table)
            items_input = typer.prompt(f"Itens para Build {build_num} (números separados por vírgula)", default="")

            selected_items = []
            if items_input.strip():
                for item_choice in items_input.split(","):
                    try:
                        item_num = int(item_choice.strip())
                        if 1 <= item_num <= len(item_list):
                            selected_items.append(item_list[item_num - 1])
                    except ValueError:
                        continue

            # Alvo (mesmo para ambas as builds)
            if build_num == 1:
                target_list = list(presets["targets"].values())
                target_table = Table(title="Selecionar Alvo")
                target_table.add_column("#", style="cyan")
                target_table.add_column("Nome", style="yellow")
                target_table.add_column("HP", style="red")

                for i, target_obj in enumerate(target_list, 1):
                    target_table.add_row(str(i), target_obj.name, f"{target_obj.hp:.0f}")

                console.print(target_table)
                target_choice = typer.prompt("Alvo (número)", default="1")

                try:
                    target_num = int(target_choice)
                    if 1 <= target_num <= len(target_list):
                        target = target_list[target_num - 1]
                    else:
                        target = target_list[0]
                except ValueError:
                    target = target_list[0]

            # Criar build
            build = Build(
                name=f"Build {build_num}: {champion.name} Lv{level}",
                champion=champion,
                level=level,
                items=selected_items,
                target=target
            )

            # Calcular stats
            final_stats = formula_engine.calculate_final_stats(build)
            build.final_stats = final_stats
            builds.append(build)

            console.print(f"[green]✅ Build {build_num} configurada: {champion.name} com {len(selected_items)} itens[/green]")

        # Comparar builds
        if len(builds) == 2:
            from calc.models import BuildComparison
            comparison = BuildComparison(build_a=builds[0], build_b=builds[1])

            # Calcular diferenças
            stat_differences = formula_engine.compare_stats(builds[0].final_stats, builds[1].final_stats)
            comparison.stat_differences = stat_differences
            comparison.dps_difference = stat_differences.get('dps', 0)
            comparison.cost_difference = sum(item.cost for item in builds[1].items) - sum(item.cost for item in builds[0].items)

            # Exibir comparação
            display_build_comparison(comparison)

            # Opção de exportar
            if typer.confirm("Exportar comparação para CSV?", default=False):
                filepath = data_exporter.export_comparison_to_csv(comparison)
                console.print(f"[green]Comparação exportada para: {filepath}[/green]")

    except Exception as e:
        console.print(f"[red]Erro na comparação: {e}[/red]")
        raise typer.Exit(1)

def reconstruct_build_from_json(build_data: dict):
    """Reconstrói uma build a partir de dados JSON"""
    from calc.models import ChampionStats, Item, ItemModifier, Build, Target, StatType, ModifierType

    # Reconstruir campeão
    champion_data = build_data["champion"]
    champion = ChampionStats(**champion_data)

    # Reconstruir itens
    items = []
    for item_data in build_data["items"]:
        modifiers = []
        for mod_data in item_data["modifiers"]:
            modifier = ItemModifier(
                stat=StatType(mod_data["stat"]),
                value=mod_data["value"],
                modifier_type=ModifierType(mod_data["modifier_type"])
            )
            modifiers.append(modifier)

        item = Item(
            name=item_data["name"],
            modifiers=modifiers,
            cost=item_data["cost"]
        )
        items.append(item)

    # Reconstruir alvo
    target = None
    if build_data.get("target"):
        target_data = build_data["target"]
        target = Target(**target_data)

    # Criar build
    build = Build(
        name=build_data["name"],
        champion=champion,
        level=build_data["level"],
        items=items,
        target=target
    )

    return build

def display_build_comparison(comparison):
    """Exibe comparação entre duas builds"""
    from calc.models import BuildComparison

    console.print("\n🔥 [bold cyan]COMPARAÇÃO DE BUILDS[/bold cyan] 🔥\n")

    # Informações das builds
    info_table = Table(title="📋 Informações das Builds")
    info_table.add_column("Aspecto", style="yellow")
    info_table.add_column("Build A", style="cyan")
    info_table.add_column("Build B", style="magenta")

    build_a = comparison.build_a
    build_b = comparison.build_b

    info_table.add_row("Nome", build_a.name, build_b.name)
    info_table.add_row("Campeão", build_a.champion.name, build_b.champion.name)
    info_table.add_row("Nível", str(build_a.level), str(build_b.level))
    info_table.add_row("Qtd Itens", str(len(build_a.items)), str(len(build_b.items)))
    info_table.add_row("Custo Total", f"{sum(item.cost for item in build_a.items)}g", f"{sum(item.cost for item in build_b.items)}g")

    console.print(info_table)

    # Comparação de stats
    stats_table = Table(title="📊 Comparação de Estatísticas")
    stats_table.add_column("Atributo", style="yellow")
    stats_table.add_column("Build A", style="cyan")
    stats_table.add_column("Build B", style="magenta")
    stats_table.add_column("Diferença", style="green")
    stats_table.add_column("% Diferença", style="red")

    stats_a = build_a.final_stats
    stats_b = build_b.final_stats

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

        # Formatação baseada no tipo de stat
        if stat_name in ["Attack Speed", "Time to Kill"]:
            value_a_str = f"{value_a:.2f}"
            value_b_str = f"{value_b:.2f}"
            diff_str = f"{diff:+.2f}"
        elif stat_name in ["Critical Chance"]:
            value_a_str = f"{value_a:.1f}%"
            value_b_str = f"{value_b:.1f}%"
            diff_str = f"{diff:+.1f}%"
        else:
            value_a_str = f"{value_a:.0f}"
            value_b_str = f"{value_b:.0f}"
            diff_str = f"{diff:+.0f}"

        percent_str = f"{percent_diff:+.1f}%"

        # Colorir diferença
        if diff > 0:
            diff_str = f"[green]{diff_str}[/green]"
            percent_str = f"[green]{percent_str}[/green]"
        elif diff < 0:
            diff_str = f"[red]{diff_str}[/red]"
            percent_str = f"[red]{percent_str}[/red]"
        else:
            diff_str = f"[yellow]{diff_str}[/yellow]"
            percent_str = f"[yellow]{percent_str}[/yellow]"

        stats_table.add_row(stat_name, value_a_str, value_b_str, diff_str, percent_str)

    console.print(stats_table)

    # Resumo da comparação
    if comparison.dps_difference:
        if comparison.dps_difference > 0:
            console.print(f"\n[green]✅ Build B tem {comparison.dps_difference:.1f} DPS a mais (+{comparison.dps_difference/stats_a.dps*100:.1f}%)[/green]")
        else:
            console.print(f"\n[red]❌ Build B tem {abs(comparison.dps_difference):.1f} DPS a menos ({comparison.dps_difference/stats_a.dps*100:.1f}%)[/red]")

    if comparison.cost_difference:
        if comparison.cost_difference > 0:
            console.print(f"[yellow]💰 Build B custa {comparison.cost_difference}g a mais[/yellow]")
        else:
            console.print(f"[green]💰 Build B custa {abs(comparison.cost_difference)}g a menos[/green]")

def display_build_results(build: Build):
    """Exibe os resultados de uma build"""
    if not build.final_stats:
        console.print("[red]Nenhum resultado calculado![/red]")
        return

    # Informações da build
    panel_content = f"""
[bold cyan]Campeão:[/bold cyan] {build.champion.name}
[bold cyan]Nível:[/bold cyan] {build.level}
[bold cyan]Itens:[/bold cyan] {len(build.items)} itens
[bold cyan]Custo Total:[/bold cyan] {sum(item.cost for item in build.items)}g
    """

    console.print(Panel(panel_content, title="📋 Informações da Build", border_style="cyan"))

    # Tabela de stats
    stats_table = Table(title="📊 Estatísticas Finais")
    stats_table.add_column("Atributo", style="yellow")
    stats_table.add_column("Valor", style="green")

    stats = build.final_stats
    stats_table.add_row("Attack Damage", f"{stats.ad:.1f}")
    stats_table.add_row("Ability Power", f"{stats.ap:.1f}")
    stats_table.add_row("Attack Speed", f"{stats.as_:.2f}")
    stats_table.add_row("Critical Chance", f"{stats.crit_chance:.1f}%")
    stats_table.add_row("Health", f"{stats.hp:.0f}")
    stats_table.add_row("Armor", f"{stats.armor:.1f}")
    stats_table.add_row("Magic Resistance", f"{stats.mr:.1f}")
    stats_table.add_row("Movement Speed", f"{stats.ms:.0f}")

    console.print(stats_table)

    # Análise de combate
    if stats.dps and build.target:
        combat_table = Table(title="⚔️ Análise de Combate")
        combat_table.add_column("Métrica", style="yellow")
        combat_table.add_column("Valor", style="red")

        combat_table.add_row("Alvo", build.target.name)
        combat_table.add_row("DPS", f"{stats.dps:.1f}")
        if stats.ttk:
            combat_table.add_row("Time to Kill", f"{stats.ttk:.1f}s")
        if stats.effective_hp_physical:
            combat_table.add_row("HP Efetivo (Físico)", f"{stats.effective_hp_physical:.0f}")

        console.print(combat_table)

if __name__ == "__main__":
    app()
