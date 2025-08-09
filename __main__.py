#!/usr/bin/env python3
"""
🔥 SmashBuilder - Ponto de Entrada Principal 🔥
Permite execução como módulo: python -m smashbuilder
"""

import sys
from pathlib import Path

# Adicionar o diretório atual ao path para imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def main():
    """Função principal de entrada"""
    try:
        # Tentar importar e executar a interface cyberpunk
        from cyberpunk_terminal import CyberpunkTerminal
        
        terminal = CyberpunkTerminal()
        terminal.run()
        
    except ImportError:
        # Fallback para CLI se a interface cyberpunk não estiver disponível
        print("Interface cyberpunk não disponível, usando CLI...")
        
        try:
            from cli.app import app
            app()
        except ImportError:
            print("❌ Erro: Dependências não encontradas!")
            print("💡 Execute: python start_cyberpunk.py")
            sys.exit(1)
    
    except KeyboardInterrupt:
        print("\n🔥 SmashBuilder encerrado pelo usuário")
        sys.exit(0)
    
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
