#!/usr/bin/env python3
"""
🔥 SmashBuilder - Interface Terminal Cyberpunk 🔥
Interface principal com estética cyberpunk para cálculo de builds LoL
"""

import os
import sys
import time
from typing import Optional, List, Dict, Any

try:
    import colorama
    from colorama import Fore, Back, Style
    import pyfiglet
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text
except ImportError as e:
    print(f"❌ Dependência faltante: {e}")
    print("💡 Execute: python start_cyberpunk.py")
    sys.exit(1)

# Inicializar colorama
colorama.init(autoreset=True)

class CyberpunkColors:
    """Esquema de cores cyberpunk padronizado"""
    PRIMARY = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    ACCENT = Fore.MAGENTA
    RESET = Style.RESET_ALL
    BRIGHT = Style.BRIGHT
    DIM = Style.DIM

class CyberpunkTerminal:
    """Interface terminal cyberpunk principal"""

    def __init__(self):
        self.console = Console()
        self.colors = CyberpunkColors()
        self.running = True
        self.clear_screen()

    def clear_screen(self):
        """Limpa a tela do terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_banner(self):
        """Exibe o banner principal do SmashBuilder"""
        banner_text = "SMASH BUILDER"
        banner = pyfiglet.figlet_format(banner_text, font="slant")

        print(f"{self.colors.PRIMARY}{self.colors.BRIGHT}{banner}{self.colors.RESET}")
        print(f"{self.colors.SUCCESS}{'═' * 80}{self.colors.RESET}")
        print(f"{self.colors.WARNING}    ▓▓▓ LEAGUE OF LEGENDS BUILD CALCULATOR CYBERPUNK TERMINAL v1.0 ▓▓▓{self.colors.RESET}")
        print(f"{self.colors.SUCCESS}{'═' * 80}{self.colors.RESET}")
        print()

    def cyberpunk_loading(self, message: str, duration: float = 2.0):
        """Animação de carregamento cyberpunk"""
        chars = "▓▒░"
        steps = int(duration * 10)

        for i in range(steps):
            char = chars[i % len(chars)]
            print(f"\r{self.colors.SUCCESS}[{char * 3}]{self.colors.RESET} {self.colors.PRIMARY}{message}{self.colors.RESET} {self.colors.SUCCESS}[{char * 3}]{self.colors.RESET}", end="")
            time.sleep(0.1)

        print(f"\r{self.colors.SUCCESS}[✓]{self.colors.RESET} {self.colors.PRIMARY}{message}{self.colors.RESET} {self.colors.SUCCESS}[COMPLETO]{self.colors.RESET}")
        time.sleep(0.5)

    def print_success(self, message: str):
        """Mensagem de sucesso"""
        print(f"{self.colors.SUCCESS}[✓ SUCESSO]{self.colors.RESET} {message}")

    def print_error(self, message: str):
        """Mensagem de erro"""
        print(f"{self.colors.ERROR}[✗ ERRO]{self.colors.RESET} {message}")

    def print_warning(self, message: str):
        """Mensagem de aviso"""
        print(f"{self.colors.WARNING}[⚠ AVISO]{self.colors.RESET} {message}")

    def print_info(self, message: str):
        """Mensagem informativa"""
        print(f"{self.colors.PRIMARY}[ℹ INFO]{self.colors.RESET} {message}")

    def print_cyberpunk_menu(self, title: str, options: List[str]):
        """Menu estilizado cyberpunk"""
        print(f"\n{self.colors.PRIMARY}╔{'═' * 75}╗{self.colors.RESET}")
        print(f"{self.colors.PRIMARY}║{title:^75}║{self.colors.RESET}")
        print(f"{self.colors.PRIMARY}╠{'═' * 75}╣{self.colors.RESET}")

        for i, option in enumerate(options, 1):
            print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[{i}]{self.colors.RESET} {self.colors.WARNING}► {option:<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")

        print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[0]{self.colors.RESET} {self.colors.ERROR}► {'SAIR DO SISTEMA':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
        print(f"{self.colors.PRIMARY}╚{'═' * 75}╝{self.colors.RESET}")

    def get_cyberpunk_input(self, prompt: str) -> str:
        """Entrada de dados estilizada"""
        print(f"\n{self.colors.SUCCESS}┌─[{self.colors.PRIMARY}SMASHBUILDER{self.colors.SUCCESS}]─[{self.colors.WARNING}INPUT{self.colors.SUCCESS}]{self.colors.RESET}")
        return input(f"{self.colors.SUCCESS}└──╼ {self.colors.PRIMARY}{prompt}{self.colors.RESET} {self.colors.SUCCESS}►{self.colors.RESET} ")

    def show_main_menu(self):
        """Exibe o menu principal"""
        options = [
            "CALCULAR BUILD RÁPIDA",
            "COMPARAR DUAS BUILDS",
            "TABELA POR NÍVEIS",
            "GERENCIAR DADOS",
            "CATÁLOGO DE CAMPEÕES",
            "CATÁLOGO DE ITENS",
            "EXPORTAR RESULTADOS",
            "SOBRE O SISTEMA"
        ]

        self.print_cyberpunk_menu("MENU PRINCIPAL - SMASHBUILDER", options)
        return self.get_cyberpunk_input("Selecione uma opção")

    def show_champion_selector(self):
        """Mostra seletor de campeões com números"""
        try:
            from data_io.loader import data_loader
            champions = data_loader.load_champions()

            self.print_info("Carregando lista de campeões...")

            print(f"\n{self.colors.PRIMARY}╔{'═' * 75}╗{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}║{'SELECIONAR CAMPEÃO':^75}║{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}╠{'═' * 75}╣{self.colors.RESET}")

            champion_list = list(champions.values())
            for i, champion in enumerate(champion_list, 1):
                class_color = self.colors.SUCCESS if champion.champion_class == "Marksman" else self.colors.WARNING
                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[{i:2}]{self.colors.RESET} {self.colors.ACCENT}►{self.colors.RESET} {champion.name:<25} {class_color}({champion.champion_class}){self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")

            print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[0 ]{self.colors.RESET} {self.colors.ERROR}► {'VOLTAR':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}╚{'═' * 75}╝{self.colors.RESET}")

            choice = self.get_cyberpunk_input("Selecione o campeão (número)")

            try:
                choice_num = int(choice)
                if choice_num == 0:
                    return None
                elif 1 <= choice_num <= len(champion_list):
                    return champion_list[choice_num - 1]
                else:
                    self.print_error("Número inválido!")
                    return None
            except ValueError:
                self.print_error("Digite um número válido!")
                return None

        except Exception as e:
            self.print_error(f"Erro ao carregar campeões: {e}")
            return None

    def show_item_selector(self, max_items=6):
        """Mostra seletor de itens com números"""
        try:
            from data_io.loader import data_loader
            items = data_loader.load_items()

            selected_items = []

            while len(selected_items) < max_items:
                self.clear_screen()
                self.print_banner()
                self.print_info(f"Selecionando itens ({len(selected_items)}/{max_items})")

                if selected_items:
                    print(f"\n{self.colors.SUCCESS}Itens selecionados:{self.colors.RESET}")
                    for i, item in enumerate(selected_items, 1):
                        print(f"  {i}. {item.name} ({item.cost}g)")

                print(f"\n{self.colors.PRIMARY}╔{'═' * 75}╗{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}║{'SELECIONAR ITEM':^75}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}╠{'═' * 75}╣{self.colors.RESET}")

                item_list = list(items.values())
                # Mostrar apenas os primeiros 15 itens para não poluir a tela
                display_items = sorted(item_list, key=lambda x: x.cost, reverse=True)[:15]

                for i, item in enumerate(display_items, 1):
                    mythic_indicator = "🔥" if item.mythic else "  "
                    unique_indicator = "⭐" if item.unique else "  "
                    print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[{i:2}]{self.colors.RESET} {mythic_indicator}{unique_indicator} {item.name:<35} {self.colors.WARNING}{item.cost:>4}g{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")

                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[98]{self.colors.RESET} {self.colors.ACCENT}► {'FINALIZAR SELEÇÃO':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[99]{self.colors.RESET} {self.colors.ERROR}► {'LIMPAR SELEÇÃO':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[0 ]{self.colors.RESET} {self.colors.ERROR}► {'VOLTAR':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}╚{'═' * 75}╝{self.colors.RESET}")

                choice = self.get_cyberpunk_input("Selecione o item (número)")

                try:
                    choice_num = int(choice)
                    if choice_num == 0:
                        return []
                    elif choice_num == 98:
                        return selected_items
                    elif choice_num == 99:
                        selected_items = []
                        self.print_info("Seleção limpa!")
                        time.sleep(1)
                    elif 1 <= choice_num <= len(display_items):
                        selected_item = display_items[choice_num - 1]

                        # Verificar se já foi selecionado
                        if any(item.name == selected_item.name for item in selected_items):
                            self.print_warning("Item já selecionado!")
                            time.sleep(1)
                            continue

                        # Verificar regra de mítico
                        if selected_item.mythic:
                            mythic_count = sum(1 for item in selected_items if item.mythic)
                            if mythic_count > 0:
                                self.print_error("Apenas um item mítico é permitido!")
                                time.sleep(2)
                                continue

                        selected_items.append(selected_item)
                        self.print_success(f"Item '{selected_item.name}' adicionado!")
                        time.sleep(1)
                    else:
                        self.print_error("Número inválido!")
                        time.sleep(1)
                except ValueError:
                    self.print_error("Digite um número válido!")
                    time.sleep(1)

            return selected_items

        except Exception as e:
            self.print_error(f"Erro ao carregar itens: {e}")
            return []

    def show_target_selector(self):
        """Mostra seletor de alvos"""
        try:
            from data_io.loader import data_loader
            presets = data_loader.load_presets()
            targets = presets["targets"]

            print(f"\n{self.colors.PRIMARY}╔{'═' * 75}╗{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}║{'SELECIONAR ALVO':^75}║{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}╠{'═' * 75}╣{self.colors.RESET}")

            target_list = list(targets.values())
            for i, target in enumerate(target_list, 1):
                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[{i}]{self.colors.RESET} {self.colors.ACCENT}►{self.colors.RESET} {target.name:<15} {self.colors.WARNING}HP:{target.hp:<4} Armor:{target.armor:<3} MR:{target.mr:<3}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")

            print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[0]{self.colors.RESET} {self.colors.ERROR}► {'VOLTAR':<65}{self.colors.RESET} {self.colors.PRIMARY}║{self.colors.RESET}")
            print(f"{self.colors.PRIMARY}╚{'═' * 75}╝{self.colors.RESET}")

            choice = self.get_cyberpunk_input("Selecione o alvo (número)")

            try:
                choice_num = int(choice)
                if choice_num == 0:
                    return None
                elif 1 <= choice_num <= len(target_list):
                    return target_list[choice_num - 1]
                else:
                    self.print_error("Número inválido!")
                    return None
            except ValueError:
                self.print_error("Digite um número válido!")
                return None

        except Exception as e:
            self.print_error(f"Erro ao carregar alvos: {e}")
            return None

    def show_build_calculator(self):
        """Interface para cálculo de build"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Iniciando calculadora de build...")

        try:
            from calc.models import Build
            from calc.formulas import formula_engine

            # Seleção de campeão
            self.cyberpunk_loading("Carregando dados de campeões")
            champion = self.show_champion_selector()
            if not champion:
                return

            # Seleção de nível
            level_input = self.get_cyberpunk_input("Nível (1-18) [11]")
            try:
                level = int(level_input) if level_input else 11
                if not (1 <= level <= 18):
                    self.print_error("Nível deve estar entre 1 e 18!")
                    time.sleep(2)
                    return
            except ValueError:
                self.print_error("Nível inválido!")
                time.sleep(2)
                return

            # Seleção de itens
            self.cyberpunk_loading("Carregando catálogo de itens")
            items = self.show_item_selector()
            if not items:
                self.print_warning("Nenhum item selecionado!")

            # Seleção de alvo
            target = self.show_target_selector()
            if not target:
                self.print_warning("Nenhum alvo selecionado!")

            # Criar build
            build = Build(
                name=f"{champion.name} Level {level}",
                champion=champion,
                level=level,
                items=items,
                target=target
            )

            # Calcular
            self.cyberpunk_loading("Calculando atributos finais")
            self.cyberpunk_loading("Computando DPS estimado")

            final_stats = formula_engine.calculate_final_stats(build)
            build.final_stats = final_stats

            self.print_success("Build calculada com sucesso!")

            # Mostrar resultados
            self.show_build_results(build)

        except Exception as e:
            self.print_error(f"Erro no cálculo: {e}")
            time.sleep(3)

    def show_build_results(self, build):
        """Mostra os resultados da build"""
        self.clear_screen()
        self.print_banner()

        # Informações da build
        print(f"\n{self.colors.SUCCESS}{'='*75}{self.colors.RESET}")
        print(f"{self.colors.PRIMARY}🔥 RESULTADOS DA BUILD: {build.name} 🔥{self.colors.RESET}")
        print(f"{self.colors.SUCCESS}{'='*75}{self.colors.RESET}")

        # Tabela de resultados usando Rich
        table = Table(title="📊 Atributos Finais", style="cyan")
        table.add_column("Atributo", style="yellow")
        table.add_column("Valor", style="green")

        stats = build.final_stats
        table.add_row("Attack Damage", f"{stats.ad:.1f}")
        table.add_row("Ability Power", f"{stats.ap:.1f}")
        table.add_row("Attack Speed", f"{stats.as_:.2f}")
        table.add_row("Critical Chance", f"{stats.crit_chance:.1f}%")
        table.add_row("Health", f"{stats.hp:.0f}")
        table.add_row("Armor", f"{stats.armor:.1f}")
        table.add_row("Magic Resistance", f"{stats.mr:.1f}")
        table.add_row("Movement Speed", f"{stats.ms:.0f}")

        self.console.print(table)

        # Análise de combate
        if stats.dps and build.target:
            combat_table = Table(title="⚔️ Análise de Combate", style="red")
            combat_table.add_column("Métrica", style="yellow")
            combat_table.add_column("Valor", style="red")

            combat_table.add_row("Alvo", build.target.name)
            combat_table.add_row("DPS", f"{stats.dps:.1f}")
            if stats.ttk:
                combat_table.add_row("Time to Kill", f"{stats.ttk:.1f}s")
            if stats.effective_hp_physical:
                combat_table.add_row("HP Efetivo (Físico)", f"{stats.effective_hp_physical:.0f}")

            self.console.print(combat_table)

        # Custo total
        total_cost = sum(item.cost for item in build.items)
        print(f"\n{self.colors.WARNING}💰 Custo Total: {total_cost}g{self.colors.RESET}")

        # Opções
        print(f"\n{self.colors.SUCCESS}Opções:{self.colors.RESET}")
        print(f"  {self.colors.SUCCESS}[1]{self.colors.RESET} Exportar para CSV")
        print(f"  {self.colors.SUCCESS}[2]{self.colors.RESET} Exportar para JSON")
        print(f"  {self.colors.SUCCESS}[0]{self.colors.RESET} Voltar ao menu")

        choice = self.get_cyberpunk_input("Escolha uma opção")

        if choice == "1":
            self.export_build(build, "csv")
        elif choice == "2":
            self.export_build(build, "json")

    def export_build(self, build, format_type):
        """Exporta a build"""
        try:
            from data_io.exporter import data_exporter

            self.cyberpunk_loading(f"Exportando para {format_type.upper()}")

            if format_type == "csv":
                filepath = data_exporter.export_build_to_csv(build)
            else:
                filepath = data_exporter.export_build_to_json(build)

            self.print_success(f"Build exportada para: {filepath}")

        except Exception as e:
            self.print_error(f"Erro ao exportar: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def show_data_management_menu(self):
        """Menu de gerenciamento de dados"""
        self.clear_screen()
        self.print_banner()

        options = [
            "ADICIONAR NOVO CAMPEÃO",
            "ADICIONAR NOVO ITEM",
            "LISTAR CAMPEÕES",
            "LISTAR ITENS",
            "VALIDAR BASE DE DADOS",
            "BACKUP DOS DADOS"
        ]

        self.print_cyberpunk_menu("GERENCIAMENTO DE DADOS", options)
        choice = self.get_cyberpunk_input("Selecione uma opção")

        try:
            option = int(choice)

            if option == 0:
                return
            elif option == 1:
                self.add_champion_interactive()
            elif option == 2:
                self.add_item_interactive()
            elif option == 3:
                self.list_champions()
            elif option == 4:
                self.list_items()
            elif option == 5:
                self.validate_database()
            elif option == 6:
                self.backup_data()
            else:
                self.print_warning("Opção inválida!")
                time.sleep(2)

        except ValueError:
            self.print_error("Digite um número válido!")
            time.sleep(2)

    def add_champion_interactive(self):
        """Adiciona campeão interativamente"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Adicionando novo campeão...")

        try:
            from calc.models import ChampionStats
            import json
            from pathlib import Path

            # Coletar dados básicos
            name = self.get_cyberpunk_input("Nome do campeão")
            champion_class = self.get_cyberpunk_input("Classe do campeão [Unknown]") or "Unknown"
            patch = self.get_cyberpunk_input("Patch [14.1]") or "14.1"

            self.print_info("Coletando stats base (nível 1)...")

            # Stats base
            base_ad = float(self.get_cyberpunk_input("Attack Damage base"))
            base_as = float(self.get_cyberpunk_input("Attack Speed base"))
            base_hp = float(self.get_cyberpunk_input("Health base"))
            base_mana = float(self.get_cyberpunk_input("Mana base [0]") or "0")
            base_armor = float(self.get_cyberpunk_input("Armor base"))
            base_mr = float(self.get_cyberpunk_input("Magic Resistance base"))
            base_ms = float(self.get_cyberpunk_input("Movement Speed base"))

            self.print_info("Coletando crescimento por nível...")

            # Crescimento
            growth_ad = float(self.get_cyberpunk_input("AD por nível"))
            growth_as = float(self.get_cyberpunk_input("AS% por nível"))
            growth_hp = float(self.get_cyberpunk_input("HP por nível"))
            growth_mana = float(self.get_cyberpunk_input("Mana por nível [0]") or "0")
            growth_armor = float(self.get_cyberpunk_input("Armor por nível"))
            growth_mr = float(self.get_cyberpunk_input("MR por nível"))
            growth_ms = float(self.get_cyberpunk_input("MS por nível [0]") or "0")

            # Criar campeão para validação
            champion = ChampionStats(
                name=name,
                base_ad=base_ad,
                base_ap=0,
                base_as=base_as,
                base_hp=base_hp,
                base_mana=base_mana,
                base_armor=base_armor,
                base_mr=base_mr,
                base_ms=base_ms,
                growth_ad=growth_ad,
                growth_ap=0,
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
            self.cyberpunk_loading("Validando dados do campeão")

            print(f"\n{self.colors.SUCCESS}✅ Preview do Campeão:{self.colors.RESET}")

            # Tabela de preview usando Rich
            preview_table = Table(title=f"📋 {champion.name}", style="cyan")
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

            self.console.print(preview_table)

            # Confirmar
            confirm = self.get_cyberpunk_input("Adicionar este campeão? (s/n)")

            if confirm.lower() in ['s', 'sim', 'y', 'yes']:
                # Salvar no arquivo
                champions_file = Path("data/champions.json")
                with open(champions_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

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

                with open(champions_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                self.print_success(f"Campeão '{champion.name}' adicionado com sucesso!")

                # Recarregar dados
                from data_io.loader import data_loader
                data_loader.load_champions(force_reload=True)
            else:
                self.print_warning("Operação cancelada!")

        except Exception as e:
            self.print_error(f"Erro ao adicionar campeão: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def add_item_interactive(self):
        """Adiciona item interativamente"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Adicionando novo item...")

        try:
            from calc.models import Item, ItemModifier, StatType, ModifierType
            import json
            from pathlib import Path

            # Dados básicos
            name = self.get_cyberpunk_input("Nome do item")
            cost = int(self.get_cyberpunk_input("Custo em gold [0]") or "0")

            unique_input = self.get_cyberpunk_input("É um item único? (s/n) [n]") or "n"
            unique = unique_input.lower() in ['s', 'sim', 'y', 'yes']

            mythic_input = self.get_cyberpunk_input("É um item mítico? (s/n) [n]") or "n"
            mythic = mythic_input.lower() in ['s', 'sim', 'y', 'yes']

            # Modificadores
            modifiers = []
            self.print_info("Adicionando modificadores...")

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

            while True:
                print(f"\n{self.colors.PRIMARY}╔{'═' * 50}╗{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}║{'ADICIONAR MODIFICADOR':^50}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}╠{'═' * 50}╣{self.colors.RESET}")

                for num, (stat_key, stat_name) in stat_options.items():
                    print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[{num}]{self.colors.RESET} {stat_name:<40} {self.colors.PRIMARY}║{self.colors.RESET}")

                print(f"{self.colors.PRIMARY}║{self.colors.RESET} {self.colors.SUCCESS}[0]{self.colors.RESET} {'FINALIZAR':<40} {self.colors.PRIMARY}║{self.colors.RESET}")
                print(f"{self.colors.PRIMARY}╚{'═' * 50}╝{self.colors.RESET}")

                choice = self.get_cyberpunk_input("Escolha o stat (número)")

                try:
                    choice_num = int(choice)
                    if choice_num == 0:
                        break

                    if choice_num not in stat_options:
                        self.print_error("Opção inválida!")
                        continue

                    stat_key, stat_name = stat_options[choice_num]
                    value = float(self.get_cyberpunk_input(f"Valor para {stat_name}"))

                    # Tipo de modificador
                    if stat_key in ["attack_speed", "critical_chance"]:
                        mod_type_input = self.get_cyberpunk_input("Tipo (flat/percent) [percent]") or "percent"
                    else:
                        mod_type_input = self.get_cyberpunk_input("Tipo (flat/percent) [flat]") or "flat"

                    modifier = ItemModifier(
                        stat=StatType(stat_key),
                        value=value,
                        modifier_type=ModifierType(mod_type_input)
                    )

                    modifiers.append(modifier)
                    self.print_success(f"Adicionado: +{value} {stat_name} ({mod_type_input})")
                    time.sleep(1)

                except ValueError as e:
                    self.print_error(f"Erro: {e}")
                    time.sleep(2)

            # Criar item
            item = Item(
                name=name,
                modifiers=modifiers,
                cost=cost,
                unique=unique,
                mythic=mythic
            )

            # Preview
            self.cyberpunk_loading("Validando item")

            print(f"\n{self.colors.SUCCESS}✅ Preview do Item:{self.colors.RESET}")

            preview_table = Table(title=f"🛡️ {item.name}", style="cyan")
            preview_table.add_column("Propriedade", style="yellow")
            preview_table.add_column("Valor", style="cyan")

            preview_table.add_row("Custo", f"{item.cost}g")
            preview_table.add_row("Único", "✓" if item.unique else "✗")
            preview_table.add_row("Mítico", "✓" if item.mythic else "✗")
            preview_table.add_row("Modificadores", str(len(item.modifiers)))

            self.console.print(preview_table)

            if modifiers:
                mod_table = Table(title="📊 Modificadores", style="green")
                mod_table.add_column("Stat", style="yellow")
                mod_table.add_column("Valor", style="green")
                mod_table.add_column("Tipo", style="cyan")

                for mod in modifiers:
                    stat_name = mod.stat.value.replace("_", " ").title()
                    mod_table.add_row(stat_name, str(mod.value), mod.modifier_type.value)

                self.console.print(mod_table)

            # Confirmar
            confirm = self.get_cyberpunk_input("Adicionar este item? (s/n)")

            if confirm.lower() in ['s', 'sim', 'y', 'yes']:
                # Salvar
                items_file = Path("data/items.json")
                with open(items_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)

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

                with open(items_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)

                self.print_success(f"Item '{item.name}' adicionado com sucesso!")

                # Recarregar
                from data_io.loader import data_loader
                data_loader.load_items(force_reload=True)
            else:
                self.print_warning("Operação cancelada!")

        except Exception as e:
            self.print_error(f"Erro ao adicionar item: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def list_champions(self):
        """Lista campeões disponíveis"""
        self.clear_screen()
        self.print_banner()

        try:
            from data_io.loader import data_loader
            champions = data_loader.load_champions()

            table = Table(title="📋 Campeões Disponíveis", style="cyan")
            table.add_column("#", style="dim")
            table.add_column("Nome", style="cyan")
            table.add_column("Classe", style="yellow")
            table.add_column("AD Base", style="red")
            table.add_column("AS Base", style="green")
            table.add_column("HP Base", style="blue")

            for i, champion in enumerate(sorted(champions.values(), key=lambda c: c.name), 1):
                table.add_row(
                    str(i),
                    champion.name,
                    champion.champion_class,
                    f"{champion.base_ad:.0f}",
                    f"{champion.base_as:.3f}",
                    f"{champion.base_hp:.0f}"
                )

            self.console.print(table)
            self.print_success(f"Total: {len(champions)} campeões")

        except Exception as e:
            self.print_error(f"Erro ao carregar campeões: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def list_items(self):
        """Lista itens disponíveis"""
        self.clear_screen()
        self.print_banner()

        try:
            from data_io.loader import data_loader
            items = data_loader.load_items()

            table = Table(title="🛡️ Itens Disponíveis", style="cyan")
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

            self.console.print(table)
            self.print_success(f"Total: {len(items)} itens")

        except Exception as e:
            self.print_error(f"Erro ao carregar itens: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def validate_database(self):
        """Valida a integridade da base de dados"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Validando integridade da base de dados...")

        try:
            from data_io.loader import data_loader

            self.cyberpunk_loading("Verificando campeões")
            champions = data_loader.load_champions()

            self.cyberpunk_loading("Verificando itens")
            items = data_loader.load_items()

            self.cyberpunk_loading("Verificando presets")
            presets = data_loader.load_presets()

            self.cyberpunk_loading("Executando testes de validação")

            # Executar teste do sistema
            import subprocess
            result = subprocess.run([sys.executable, "test_system.py"],
                                  capture_output=True, text=True)

            if result.returncode == 0:
                self.print_success("✅ Todos os testes passaram!")
                self.print_success(f"✅ {len(champions)} campeões carregados")
                self.print_success(f"✅ {len(items)} itens carregados")
                self.print_success(f"✅ {len(presets['targets'])} alvos carregados")
            else:
                self.print_error("❌ Alguns testes falharam!")
                print(result.stdout)
                print(result.stderr)

        except Exception as e:
            self.print_error(f"Erro na validação: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def backup_data(self):
        """Cria backup dos dados"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Criando backup dos dados...")

        try:
            import shutil
            from datetime import datetime
            from pathlib import Path

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_dir = Path(f"data_backup_{timestamp}")

            self.cyberpunk_loading("Copiando arquivos de dados")
            shutil.copytree("data", backup_dir)

            self.print_success(f"✅ Backup criado em: {backup_dir}")

        except Exception as e:
            self.print_error(f"Erro ao criar backup: {e}")

        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def show_about(self):
        """Informações sobre o sistema"""
        self.clear_screen()
        self.print_banner()

        about_text = """
🔥 SMASHBUILDER v1.0 🔥

Uma calculadora avançada de builds para League of Legends
com interface terminal cyberpunk.

CARACTERÍSTICAS:
• Cálculo preciso de atributos finais
• DPS estimado contra alvos configuráveis
• Comparação de builds lado a lado
• Interface cyberpunk imersiva
• Export para CSV/JSON

DESENVOLVIDO COM:
• Python 3.8+
• Rich para tabelas
• Pydantic para validação
• Colorama para cores

CRIADO PARA A COMUNIDADE DE LEAGUE OF LEGENDS
        """

        panel = Panel(about_text, title="[cyan]SOBRE O SISTEMA[/cyan]", border_style="green")
        self.console.print(panel)

        input(f"\n{self.colors.WARNING}Pressione ENTER para voltar...{self.colors.RESET}")

    def handle_menu_choice(self, choice: str):
        """Processa a escolha do menu"""
        try:
            option = int(choice)

            if option == 0:
                self.running = False
                self.print_info("Encerrando SmashBuilder...")
                self.cyberpunk_loading("Desconectando do sistema")
                return

            elif option == 1:
                self.show_build_calculator()

            elif option == 2:
                self.show_build_comparison()

            elif option == 3:
                self.show_level_table()

            elif option == 4:
                self.show_data_management_menu()

            elif option == 5:
                self.list_champions()

            elif option == 6:
                self.list_items()

            elif option == 7:
                self.show_export_menu()

            elif option == 8:
                self.show_about()

            else:
                self.print_warning(f"Opção {option} inválida!")
                time.sleep(2)

        except ValueError:
            self.print_error("Opção inválida! Digite um número.")
            time.sleep(2)

    def show_build_comparison(self):
        """Interface para comparação de builds"""
        self.clear_screen()
        self.print_banner()
        self.print_warning("Funcionalidade de comparação em desenvolvimento!")
        self.print_info("Use a CLI para comparar builds exportadas:")
        print(f"{self.colors.SUCCESS}python -m cli.app compare --buildA build1.json --buildB build2.json{self.colors.RESET}")
        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def show_level_table(self):
        """Interface para tabela por níveis"""
        self.clear_screen()
        self.print_banner()
        self.print_warning("Funcionalidade de tabela por níveis em desenvolvimento!")
        self.print_info("Use a CLI para gerar tabelas:")
        print(f"{self.colors.SUCCESS}python -m cli.app table --champ \"Kai'Sa\" --levels 1,6,11,16,18{self.colors.RESET}")
        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def show_export_menu(self):
        """Menu de exportação"""
        self.clear_screen()
        self.print_banner()
        self.print_info("As builds são exportadas automaticamente após o cálculo.")
        self.print_info("Arquivos exportados ficam na pasta 'exports/'")
        input(f"\n{self.colors.WARNING}Pressione ENTER para continuar...{self.colors.RESET}")

    def run(self):
        """Loop principal da aplicação"""
        self.print_banner()
        self.cyberpunk_loading("Inicializando sistema neural")
        self.cyberpunk_loading("Carregando base de dados")
        self.cyberpunk_loading("Ativando interface cyberpunk")

        self.print_success("SmashBuilder iniciado com sucesso!")
        time.sleep(1)

        while self.running:
            try:
                self.clear_screen()
                self.print_banner()

                choice = self.show_main_menu()
                self.handle_menu_choice(choice)

            except KeyboardInterrupt:
                print(f"\n{self.colors.ERROR}Sistema interrompido pelo usuário{self.colors.RESET}")
                break
            except Exception as e:
                self.print_error(f"Erro inesperado: {e}")
                time.sleep(3)

        print(f"\n{self.colors.ACCENT}🔥 Obrigado por usar o SmashBuilder! 🔥{self.colors.RESET}")

def main():
    """Função principal"""
    terminal = CyberpunkTerminal()
    terminal.run()

if __name__ == "__main__":
    main()
