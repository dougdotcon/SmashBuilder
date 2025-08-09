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
    """Calculadora rápida interativa"""
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

    # Seleção de campeão
    console.print("[yellow]Campeões disponíveis:[/yellow]")
    champion_list = list(champions.keys())
    for i, champ_name in enumerate(champion_list[:10], 1):  # Mostrar apenas os primeiros 10
        console.print(f"  {i}. {champions[champ_name].name}")

    if len(champion_list) > 10:
        console.print(f"  ... e mais {len(champion_list) - 10} campeões")

    champion_input = typer.prompt("\nDigite o nome do campeão")
    champion = data_loader.get_champion(champion_input)

    if not champion:
        console.print(f"[red]Campeão '{champion_input}' não encontrado![/red]")
        raise typer.Exit(1)

    # Nível
    level = typer.prompt("Nível (1-18)", type=int, default=11)
    if not (1 <= level <= 18):
        console.print("[red]Nível deve estar entre 1 e 18![/red]")
        raise typer.Exit(1)

    # Itens
    console.print("\n[yellow]Itens populares:[/yellow]")
    popular_items = ["infinity edge", "phantom dancer", "kraken slayer", "bloodthirster"]
    for item_name in popular_items:
        if item_name in items:
            console.print(f"  • {items[item_name].name}")

    items_input = typer.prompt("\nDigite os itens (separados por vírgula)", default="")
    selected_items = []

    if items_input.strip():
        for item_name in items_input.split(","):
            item_name = item_name.strip()
            item = data_loader.get_item(item_name)
            if item:
                selected_items.append(item)
            else:
                console.print(f"[yellow]Item '{item_name}' não encontrado, ignorando...[/yellow]")

    # Alvo
    console.print("\n[yellow]Alvos disponíveis:[/yellow]")
    for target_key, target in presets["targets"].items():
        console.print(f"  • {target_key}: {target.name} (HP: {target.hp}, Armor: {target.armor})")

    target_input = typer.prompt("Selecione um alvo", default="fragile")
    target = presets["targets"].get(target_input.lower())

    if not target:
        console.print(f"[yellow]Alvo '{target_input}' não encontrado, usando 'fragile'[/yellow]")
        target = presets["targets"]["fragile"]

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
    build_b: str = typer.Option(..., "--buildB", "-b", help="Arquivo JSON da segunda build")
):
    """Compara duas builds"""
    console.print("🔥 [bold cyan]Comparação de Builds[/bold cyan] 🔥")
    console.print(f"[yellow]Funcionalidade em desenvolvimento![/yellow]")
    console.print(f"Build A: {build_a}")
    console.print(f"Build B: {build_b}")

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
        table.add_column("Nome", style="cyan")
        table.add_column("Custo", style="yellow")
        table.add_column("Mítico", style="red")
        table.add_column("Único", style="green")

        for item in sorted(items.values(), key=lambda i: i.cost, reverse=True):
            table.add_row(
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
