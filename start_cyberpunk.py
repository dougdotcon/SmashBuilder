#!/usr/bin/env python3
"""
🔥 SmashBuilder - Launcher Automático 🔥
Launcher principal com verificação e instalação automática de dependências
"""

import subprocess
import sys
import os
from pathlib import Path

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ é necessário!")
        print(f"Versão atual: {sys.version}")
        sys.exit(1)
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor} detectado")

def install_requirements():
    """Instala as dependências necessárias"""
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if not requirements_file.exists():
        print("❌ Arquivo requirements.txt não encontrado!")
        sys.exit(1)
    
    print("📦 Verificando dependências...")
    
    try:
        # Tenta importar as principais dependências
        import colorama
        import pyfiglet
        import rich
        import pydantic
        import typer
        print("✅ Todas as dependências estão instaladas")
        return True
    except ImportError as e:
        print(f"⚠️  Dependência faltante detectada: {e}")
        print("🔧 Instalando dependências automaticamente...")
        
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ])
            print("✅ Dependências instaladas com sucesso!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Falha na instalação das dependências!")
            print("💡 Tente executar manualmente: pip install -r requirements.txt")
            return False

def launch_application():
    """Lança a aplicação principal"""
    try:
        from cyberpunk_terminal import CyberpunkTerminal
        
        print("🚀 Iniciando SmashBuilder...")
        terminal = CyberpunkTerminal()
        terminal.run()
        
    except ImportError:
        print("❌ Erro ao importar a aplicação principal!")
        print("💡 Verifique se o arquivo cyberpunk_terminal.py existe")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n🔥 SmashBuilder encerrado pelo usuário")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        sys.exit(1)

def main():
    """Função principal do launcher"""
    print("🔥" + "="*60 + "🔥")
    print("    SMASHBUILDER - LAUNCHER AUTOMÁTICO")
    print("🔥" + "="*60 + "🔥")
    
    # Verificações iniciais
    check_python_version()
    
    # Instalação de dependências
    if not install_requirements():
        sys.exit(1)
    
    # Lançamento da aplicação
    launch_application()

if __name__ == "__main__":
    main()
