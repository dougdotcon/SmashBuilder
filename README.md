<div align="center">

<img src="logo.png" alt="SmashBuilder Logo" width="160" height="160" style="border-radius: 24px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);" />

## SmashBuilder — Calculadora de Builds para League of Legends

[![Status](https://img.shields.io/badge/Status-Beta-green?style=for-the-badge)](#)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-667eea.svg?style=for-the-badge&labelColor=1a202c)](https://opensource.org/licenses/MIT)
[![Interface](https://img.shields.io/badge/Interface-CLI_Terminal-5865f2?style=for-the-badge)](#)

<div style="margin: 20px 0; max-width: 85%;">
  <p style="font-size: 1.05em; color: #4a5568; margin: 0;">
    SmashBuilder é uma calculadora avançada de builds para League of Legends com uma interface de terminal com estética cyberpunk. Calcule atributos finais, DPS estimado e compare builds, com exportação em CSV/JSON. Execute via launcher ou CLI.
  </p>
</div>



---

### Início Rápido

```bash
python start_cyberpunk.py
# ou
python -m cli.app quick
```
## 📋 Visão Geral do Projeto

O **SmashBuilder** é uma calculadora avançada de builds para League of Legends com interface terminal cyberpunk. Este projeto permite que jogadores calculem rapidamente atributos finais, DPS estimado e comparem builds de forma eficiente, tudo através de uma experiência terminal futurística e imersiva.

## 🎯 Características Principais

### 🎨 Interface Terminal Cyberpunk
- **Banner ASCII animado** com arte cyberpunk personalizada
- **Esquema de cores neon** (ciano, verde, amarelo, magenta, vermelho)
- **Animações de carregamento** com caracteres especiais (▓▒░)
- **Menus estilizados** com bordas ASCII Unicode
- **Feedback visual em tempo real** para todas as operações
- **Experiência imersiva** com estética futurística

### 🚀 Funcionalidades de Cálculo
- **Cálculo de atributos finais** (AD, AS, HP, Armor, MR, Crit)
- **DPS estimado** contra alvos configuráveis
- **Comparação de builds** lado a lado
- **Suporte a múltiplos campeões** com dados base/crescimento
- **Sistema de itens e runas** configurável
- **Tabelas por nível** (1, 6, 11, 16, 18)

### 🌐 Cobertura de Dados
- **Campeões**: Base de dados local com stats base e crescimento
- **Itens**: Catálogo completo com modificadores flat e percentuais
- **Runas**: Presets configuráveis para diferentes builds
- **Alvos**: Configurações predefinidas (frágil, tanque, etc.)

## 📁 Estrutura do Projeto

### 🔧 Arquivos Principais

#### **cyberpunk_terminal.py** - Interface Principal
- **Classe CyberpunkTerminal**: Interface completa cyberpunk
- **Banner ASCII**: Arte futurística com pyfiglet
- **Sistema de cores**: Esquema neon completo
- **Menus interativos**: Navegação intuitiva
- **Integração backend**: Conexão com sistema de cálculo

#### **start_cyberpunk.py** - Launcher Automático
- **Auto-instalação**: Verificação e instalação de dependências
- **Tratamento de erros**: Recuperação automática de falhas
- **Inicialização**: Launcher principal do sistema

#### **calc/models.py** - Modelos de Dados
- **Classe ChampionStats**: Estrutura de dados para campeões
- **Classe ItemMod**: Modificadores de itens
- **Classe Build**: Configuração completa de build
- **Classe Target**: Configuração de alvos

#### **calc/formulas.py** - Engine de Fórmulas
- **Sistema de aplicação**: Ordem determinística de modificadores
- **Cálculos base**: Crescimento por nível linear
- **Modificadores**: Flat e percentuais
- **Validação**: Caps e limites

#### **calc/dps.py** - Cálculo de DPS
- **DPS básico**: Ataque básico otimizado
- **TTK**: Time to Kill aproximado
- **Redução de dano**: Sistema de armor/MR
- **Crítico**: Cálculo de dano médio

### 📄 Base de Dados

#### **data/champions.json** - Catálogo de Campeões
- **Stats base**: AD, HP, Armor, MR, AS base
- **Crescimento**: Valores por nível
- **Metadados**: Nome, classe, patch

#### **data/items.json** - Catálogo de Itens
- **Modificadores flat**: +AD, +HP, +Armor
- **Modificadores percentuais**: +%AS, +%Crit
- **Preços**: Para análise de custo-benefício

#### **data/presets.json** - Configurações Predefinidas
- **Alvos**: Frágil, tanque, bruiser
- **Runas**: Presets populares
- **Buffs**: Elixir, barão, dragão

## 🎨 Padrão Visual Cyberpunk

### 🌈 Esquema de Cores
```python
# Cores principais do sistema
Fore.CYAN     # Títulos e elementos principais
Fore.GREEN    # Status positivo e confirmações
Fore.YELLOW   # Avisos e informações importantes
Fore.RED      # Erros e ações críticas
Fore.MAGENTA  # Arte ASCII e elementos decorativos
```

### 🎭 Elementos Visuais

#### Banner Principal
```
███████╗███╗   ███╗ █████╗ ███████╗██╗  ██╗    ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗
██╔════╝████╗ ████║██╔══██╗██╔════╝██║  ██║    ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗
███████╗██╔████╔██║███████║███████╗███████║    ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝
╚════██║██║╚██╔╝██║██╔══██║╚════██║██╔══██║    ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗
███████║██║ ╚═╝ ██║██║  ██║███████║██║  ██║    ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║
╚══════╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝
```

#### Animações de Carregamento
```
[▓▓▓] Calculando atributos finais [▓▓▓]
[▒▒▒] Aplicando modificadores [▒▒▒]
[░░░] Computando DPS [░░░]
[✓] Cálculo concluído! [COMPLETO]
```

#### Feedback de Status
```
[✓ SUCESSO] Build calculada com sucesso!
[✗ ERRO] Campeão não encontrado
[⚠ AVISO] Nível fora do range (1-18)
[ℹ INFO] Sistema de cálculo ativado
```

## 🚀 Sistema de Cálculo Avançado

### 📊 Engine de Fórmulas

#### **Ordem de Aplicação (Determinística)**
1. **Stats base + crescimento por nível**
2. **Modificadores flat** (itens, runas, buffs)
3. **Modificadores percentuais** (+%AS, +%HP, etc.)
4. **Caps e limites** (AS máximo, etc.)
5. **Cálculos derivados** (DPS, TTK)

#### **Fórmulas Suportadas**
- **Crescimento linear**: `base + (growth * (level-1))`
- **Attack Speed**: Tratamento especial para caps
- **Redução de dano**: `damage * 100/(100+armor)`
- **Crítico**: `AD * (1 + CritChance * CritMultiplier)`

### 🎯 Capacidades de Cálculo

- **Atributos suportados**: AD, AP, AS, Crit, Armor, MR, HP, Mana, MS
- **Níveis**: 1-18 com cálculos precisos
- **Comparação**: Até 2 builds simultaneamente
- **Export**: CSV/JSON para análise externa
- **Validação**: Entrada de dados robusta

## 🔧 Dependências e Tecnologias

### 📦 Bibliotecas Python
```python
# Interface e Visual
colorama>=0.4.4      # Cores no terminal
pyfiglet>=0.8.0      # Arte ASCII
rich>=13.0.0         # Tabelas e formatação

# Validação e Dados
pydantic>=2.0.0      # Validação de modelos
typer>=0.9.0         # Interface CLI

# Manipulação de Dados
pandas>=1.5.0        # Processamento de dados
ruamel.yaml>=0.17.0  # Configurações YAML

# Testes
pytest>=7.0.0        # Framework de testes
```

### 💾 Formatos de Export
- **CSV (.csv)**: Formato universal para planilhas
- **JSON (.json)**: Configurações e dados estruturados
- **YAML (.yaml)**: Configurações legíveis

## 🎮 Fluxo de Operação

### 1. **Inicialização do Sistema**
```bash
python start_cyberpunk.py
```
- Verificação automática de dependências
- Instalação de pacotes faltantes
- Inicialização da interface cyberpunk

### 2. **Configuração de Build**
- **Campeão**: Seleção do catálogo ou entrada manual
- **Nível**: 1-18 ou tabela multi-nível
- **Itens**: Seleção por nome ou configuração custom
- **Runas**: Presets ou configuração manual

### 3. **Configuração de Alvo**
- **HP alvo**: Valor específico ou preset
- **Resistências**: Armor e MR do alvo
- **Classe**: Frágil, tanque, bruiser

### 4. **Cálculo e Resultados**
- **Atributos finais**: Todos os stats calculados
- **DPS estimado**: Contra o alvo configurado
- **TTK**: Time to Kill aproximado
- **Comparação**: Side-by-side se múltiplas builds

### 5. **Export e Análise**
- **Tabelas formatadas**: Rich terminal output
- **Export CSV**: Para análise em planilhas
- **Configurações salvas**: Reutilização de builds

## 📊 Comandos CLI

### **Comandos Principais**

#### `calc quick`
Fluxo guiado interativo
```bash
python -m smashbuilder calc quick
```

#### `calc build`
Modo direto com parâmetros
```bash
python -m smashbuilder calc build --champ "Kai'Sa" --level 11 --items "Infinity Edge,Phantom Dancer" --target "fragile"
```

#### `calc compare`
Comparação de builds
```bash
python -m smashbuilder calc compare --buildA kaisa_crit.json --buildB kaisa_onhit.json
```

#### `calc table`
Tabela por níveis
```bash
python -m smashbuilder calc table --champ "Kai'Sa" --levels 1,6,11,16,18 --items "Infinity Edge"
```

#### `calc export`
Export de resultados
```bash
python -m smashbuilder calc export --format csv --output kaisa_analysis.csv
```

## 📈 Vantagens da Interface Terminal

### 🚀 Performance
- **Menor uso de memória**: ~3-5MB vs ~50-100MB (GUI)
- **Inicialização instantânea**: Sem carregamento de componentes gráficos
- **Cálculos otimizados**: Engine matemática eficiente
- **Menor overhead**: Interface nativa do terminal

### 🎯 Usabilidade
- **Interface intuitiva**: Menus numerados e comandos claros
- **Feedback imediato**: Cores e animações em tempo real
- **Experiência imersiva**: Estética cyberpunk única
- **Navegação fluida**: Controle total via teclado

### 🔧 Flexibilidade
- **Execução remota**: Funciona via SSH
- **Automação completa**: Integração fácil com scripts
- **Compatibilidade universal**: Qualquer terminal/SO
- **Portabilidade**: Não depende de sistema gráfico

## 🚀 Comandos de Execução

### **Método 1: Launcher Automático (Recomendado)**
```bash
python start_cyberpunk.py
```

### **Método 2: Módulo Python**
```bash
python -m smashbuilder
```

### **Método 3: Instalação via pip**
```bash
pip install -e .
smashbuilder calc quick
```

## 📚 Documentação Completa

### 📖 **Guias do Usuário**
- **[GUIA_COMPLETO_USUARIO.md](GUIA_COMPLETO_USUARIO.md)** - Tutorial completo de uso
- **[INSTALACAO_E_USO.md](INSTALACAO_E_USO.md)** - Guia de instalação e primeiros passos
- **[EXEMPLOS_PRATICOS.md](EXEMPLOS_PRATICOS.md)** - Exemplos práticos e casos de uso
- **[NOVAS_FUNCIONALIDADES.md](NOVAS_FUNCIONALIDADES.md)** - 🆕 Funcionalidades recém-implementadas

### 🔧 **Documentação Técnica**
- **[EXPANDINDO_BASE_DADOS.md](EXPANDINDO_BASE_DADOS.md)** - Como adicionar campeões e itens
- **[ASIMOVLeadCaptor_DOCUMENTACAO_COMPLETA.md](ASIMOVLeadCaptor_DOCUMENTACAO_COMPLETA.md)** - Documentação de referência

### ⚠️ **IMPORTANTE: Base de Dados Limitada**

A versão atual contém apenas:
- **10 campeões** (Kai'Sa, Jinx, Vayne, Yasuo, Zed, Ahri, Garen, Darius, Lux, Thresh)
- **20 itens** básicos
- **Dados do Patch 14.1** (exemplo)

**Para uso completo, consulte [EXPANDINDO_BASE_DADOS.md](EXPANDINDO_BASE_DADOS.md) para adicionar mais campeões e itens.**

## 🎯 Início Rápido

### 1. **Teste o Sistema**
```bash
python test_system.py
```

### 2. **Interface Cyberpunk**
```bash
python start_cyberpunk.py
```

### 3. **Calculadora Rápida CLI**
```bash
python -m cli.app quick
```

### 4. **Exemplo Prático (Seleção por Número)**
```bash
# Calculadora rápida com seleção numérica
python -m cli.app quick

# Exemplo: Escolher Kai'Sa (1), Itens (1,3,5), Alvo Bruiser (4)
```

### 5. **Gerenciar Dados**
```bash
# Adicionar novo campeão
python -m cli.app add-champion

# Adicionar novo item
python -m cli.app add-item

# Comparação interativa
python -m cli.app compare-interactive
```

## 🔥 Recursos Principais

✅ **Interface cyberpunk imersiva** com animações e cores neon
✅ **Seleção por número** para campeões, itens e alvos (mais rápido!)
✅ **Cálculos matemáticos precisos** com fórmulas validadas
✅ **10 campeões** com stats base e crescimento
✅ **20+ itens** com modificadores flat e percentuais
✅ **6 alvos predefinidos** para análise de DPS
✅ **Gerenciamento de dados** - adicione campeões e itens pelo terminal
✅ **Comparação interativa** de builds em tempo real
✅ **Export CSV/JSON/TXT** para análise externa
✅ **Validação robusta** com regras de negócio (apenas 1 mítico)
✅ **Backup automático** dos dados
✅ **Sistema modular** para fácil expansão

**🔥 Bem-vindo ao futuro dos cálculos de build! 🔥**

---

**Desenvolvido com 💚 para a comunidade de League of Legends!**
