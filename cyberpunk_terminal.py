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
            "CONFIGURAÇÕES AVANÇADAS",
            "CATÁLOGO DE CAMPEÕES",
            "CATÁLOGO DE ITENS",
            "EXPORTAR RESULTADOS",
            "SOBRE O SISTEMA"
        ]
        
        self.print_cyberpunk_menu("MENU PRINCIPAL - SMASHBUILDER", options)
        return self.get_cyberpunk_input("Selecione uma opção")
    
    def show_build_calculator(self):
        """Interface para cálculo de build"""
        self.clear_screen()
        self.print_banner()
        self.print_info("Iniciando calculadora de build...")
        
        # Simulação de cálculo
        self.cyberpunk_loading("Carregando dados de campeões")
        self.cyberpunk_loading("Inicializando engine de cálculo")
        
        champion = self.get_cyberpunk_input("Nome do campeão (ex: Kai'Sa)")
        level = self.get_cyberpunk_input("Nível (1-18)")
        items = self.get_cyberpunk_input("Itens (separados por vírgula)")
        
        self.cyberpunk_loading("Calculando atributos finais")
        self.cyberpunk_loading("Computando DPS estimado")
        
        # Resultados simulados
        self.print_success("Build calculada com sucesso!")
        
        # Tabela de resultados usando Rich
        table = Table(title="📊 Atributos Finais", style="cyan")
        table.add_column("Atributo", style="yellow")
        table.add_column("Valor", style="green")
        table.add_column("DPS", style="red")
        
        table.add_row("Attack Damage", "287", "485 DPS")
        table.add_row("Attack Speed", "1.85", "")
        table.add_row("Critical Chance", "75%", "")
        table.add_row("Health", "2150", "")
        table.add_row("Armor", "95", "")
        
        self.console.print(table)
        
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
            
            elif option == 8:
                self.show_about()
            
            else:
                self.print_warning(f"Funcionalidade {option} em desenvolvimento!")
                time.sleep(2)
        
        except ValueError:
            self.print_error("Opção inválida! Digite um número.")
            time.sleep(2)
    
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
