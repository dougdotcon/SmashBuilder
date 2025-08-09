# 🔥 SmashBuilder - Calculadora de Builds para League of Legends 🔥

![SmashBuilder Logo](logo.png)

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

**🔥 Bem-vindo ao futuro dos cálculos de build! 🔥**

---

**Desenvolvido com 💚 para a comunidade de League of Legends!**
