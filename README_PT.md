# SmashBuilder

<div align="center">

<img src="logo.png" alt="SmashBuilder Logo" width="160" height="160" style="border-radius: 24px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);" />

## SmashBuilder — Calculadora de Builds para League of Legends

[![Status](https://img.shields.io/badge/Status-Beta-green?style=for-the-badge)](#)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-667eea.svg?style=for-the-badge&labelColor=1a202c)](https://opensource.org/licenses/MIT)
[![Interface](https://img.shields.io/badge/Interface-CLI_Terminal-5865f2?style=for-the-badge)](#)

<div style="margin: 20px 0; max-width: 85%;">
  <p style="font-size: 1.05em; color: #4a5568; margin: 0;">
    SmashBuilder é uma calculadora avançada de builds para League of Legends com interface terminal cyberpunk. Permita que jogadores calculem atributos finais, DPS estimado e comparem builds de forma eficiente através de uma experiência terminal futurística e imersiva.
  </p>
</div>
</div>

## 🚀 Início Rápido

bash
# Iniciar a interface cyberpunk
python start_cyberpunk.py

# Ou usar o CLI diretamente
python -m cli.app quick


## 📋 Visão Geral do Projeto

O **SmashBuilder** é uma calculadora avançada de builds para League of Legends com uma estética de terminal cyberpunk. Este projeto permite que jogadores calculem rapidamente atributos finais, DPS estimado e comparem builds de forma eficiente, tudo através de uma experiência terminal futurística e imersiva.

## 🎯 Características Principais

### 🎨 Interface Terminal Cyberpunk
- **Banner ASCII animado**: Arte cyberpunk personalizada usando pyfiglet
- **Esquema de cores neon**: Paleta completa (ciano, verde, amarelo, magenta, vermelho)
- **Animações de carregamento**: Sequências de caracteres personalizadas (▓▒░)
- **Menus estilizados**: Elementos de navegação com bordas Unicode
- **Feedback em tempo real**: Respostas visuais para todas as operações
- **Experiência imersiva**: Estética futurística e acolhedora

### 🚀 Motor de Cálculo
- **Cálculo de atributos finais**: AD, AS, HP, Armor, MR, Crit e mais
- **DPS estimado**: Configurável contra vários alvos de teste
- **Comparação de builds**: Análise lado a lado de construções
- **Suporte a campeões**: Múltiplos campeões com stats base e crescimento
- **Itens & Runas**: Sistemas configuráveis com modificadores flat e percentuais
- **Escalonamento por Nível**: Tabelas de stats para níveis 1, 6, 11, 16 e 18

### 🌐 Cobertura de Dados
- **Campeões**: Banco de dados local com stats base e coeficientes de crescimento
- **Itens**: Catálogo completo com modificadores flat e percentuais
- **Runas**: Presets configuráveis para vários arquétipos de build
- **Alvos**: Configurações predefinidas (Squishy, Tank, etc.)

## 📁 Estrutura do Projeto

### 🔧 Módulos Principais

#### **cyberpunk_terminal.py** - Interface Principal
- **Classe `CyberpunkTerminal`**: Implementação completa da interface cyberpunk
- **Banner ASCII**: Arte futurística com pyfiglet
- **Sistema de Cores**: Implementação completa da paleta neon
- **Menus Interativos**: Estrutura de navegação intuitiva
- **Integração Backend**: Conexão com o motor de cálculo

#### **start_cyberpunk.py** - Launch
- **Instalação Automática**: Verificação e instalação de dependências
- **Verificação do Sistema**: Validação de compatibilidade do ambiente
- **Ponto de Entrada Principal**: Inicialização unificada da aplicação

#### **cli/app.py** - Interface de Linha de Comando
- **Acesso Direto via CLI**: Executar cálculos pela linha de comando
- **Subcomandos**: Modo `quick` para cálculos rápidos
- **Opções Configuráveis**: Análise flexível de argumentos

### 🗂️ Módulos de Dados

#### **models/** - Modelos de Dados Essenciais
- **Champion**: Data class para stats e scaling de campeões
- **Item**: Estruturas de modificadores de itens (flat/percentual)
- **Rune**: Configurações de presets de runas
- **Target**: Configuração de inimigo para cálculos de dano

#### **data/** - Bases de Dados
- **champions.json**: Stats base para todos os campeões suportados
- **items.json**: Catálogo completo de itens
- **runes.json**: Definições de presets de runas
- **targets.json**: Configurações de alvos de teste

## 💻 Instalação e Uso

### Pré-requisitos
- Python 3.8 ou superior
- pip (Gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**
   bash
   git clone https://github.com/seu-usuario/smashbuilder.git
   cd smashbuilder
   

2. **Instale as dependências:**
   bash
   pip install -r requirements.txt
   

3. **Execute a aplicação:**
   bash
   python start_cyberpunk.py
   

### Exemplos de Uso

#### **Modo Interativo**
bash
python start_cyberpunk.py
# Navegue pela interface cyberpunk


#### **Cálculo Rápido (CLI)**
bash
python -m cli.app quick --champion Jinx --items "Kraken Slayer,Runaan's Hurricane,Infinity Edge"


#### **Comparação de Builds**
bash
python -m cli.app compare --build1 "item1,item2,item3" --build2 "item4,item5,item6"


## 🛠️ Stack Tecnológica

- **Linguagem**: Python 3.8+
- **UI**: Terminal (CLI) com códigos de escape ANSI
- **Armazenamento**: Arquivos JSON
- **Arte**: pyfiglet (Arte ASCII)
- **Cores**: rich (Estilização terminal)

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Fork o repositório
2. Crie uma branch de feature (`git checkout -b feature/FeatureIncrivel`)
3. Commite suas mudanças (`git commit -m 'Adiciona FeatureIncrivel'`)
4. Push para a branch (`git push origin feature/FeatureIncrivel`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- **League of Legends** - Dados e conceitos do jogo
- **Python Rich** - Estilização e formatação de terminal
- **Pyfiglet** - Geração de arte ASCII
- **Comunidade Open Source** - Inspiração e boas práticas
