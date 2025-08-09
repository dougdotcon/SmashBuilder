# 🔥 SmashBuilder - Guia de Instalação e Uso 🔥

## 📋 Visão Geral

O **SmashBuilder** é uma calculadora avançada de builds para League of Legends com interface terminal cyberpunk. Este guia mostra como instalar e usar o sistema.

## 🚀 Instalação Rápida

### Método 1: Launcher Automático (Recomendado)

```bash
# Clone ou baixe o projeto
cd SmashBuilder

# Execute o launcher (instala dependências automaticamente)
python start_cyberpunk.py
```

### Método 2: Instalação Manual

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar interface cyberpunk
python cyberpunk_terminal.py

# OU executar CLI
python -m cli.app
```

### Método 3: Instalação como Pacote

```bash
# Instalar como pacote
pip install -e .

# Executar
smashbuilder
```

## 🎮 Como Usar

### Interface Cyberpunk (Principal)

1. **Iniciar o sistema:**
   ```bash
   python start_cyberpunk.py
   ```

2. **Menu Principal:**
   - `[1]` Calcular Build Rápida
   - `[2]` Comparar Duas Builds
   - `[3]` Tabela por Níveis
   - `[4]` Configurações Avançadas
   - `[5]` Catálogo de Campeões
   - `[6]` Catálogo de Itens
   - `[7]` Exportar Resultados
   - `[8]` Sobre o Sistema
   - `[0]` Sair

3. **Calculadora Rápida:**
   - Selecione um campeão (ex: "Kai'Sa")
   - Escolha o nível (1-18)
   - Digite itens separados por vírgula
   - Selecione um alvo
   - Veja os resultados calculados

### Interface CLI

```bash
# Calculadora rápida interativa
python -m cli.app quick

# Calcular build específica
python -m cli.app build --champ "Kai'Sa" --level 11 --items "Infinity Edge,Phantom Dancer" --target "fragile"

# Comparar builds
python -m cli.app compare --buildA build1.json --buildB build2.json

# Tabela por níveis
python -m cli.app table --champ "Kai'Sa" --levels 1,6,11,16,18 --items "Infinity Edge"

# Listar campeões
python -m cli.app champions

# Listar itens
python -m cli.app items
```

## 📊 Dados Disponíveis

### Campeões (10 disponíveis)
- Kai'Sa, Jinx, Vayne (ADCs)
- Yasuo, Zed (Assassinos)
- Ahri, Lux (Magos)
- Garen, Darius (Lutadores)
- Thresh (Suporte)

### Itens (20+ disponíveis)
- **Míticos:** Kraken Slayer, Galeforce, Luden's Tempest, Sunfire Aegis
- **Lendários:** Infinity Edge, Phantom Dancer, Bloodthirster, Rabadon's Deathcap
- **Componentes:** B.F. Sword, Pickaxe, Dagger, Cloak of Agility

### Alvos Predefinidos
- **Frágil:** 1800 HP, 30 Armor, 30 MR
- **ADC:** 2000 HP, 70 Armor, 30 MR
- **Mago:** 1900 HP, 40 Armor, 40 MR
- **Bruiser:** 2800 HP, 120 Armor, 60 MR
- **Tank:** 3500 HP, 200 Armor, 120 MR
- **Dummy:** 1000 HP, 0 Armor, 0 MR

## 🔧 Funcionalidades

### Cálculos Suportados
- **Atributos Finais:** AD, AS, HP, Armor, MR, Crit Chance
- **DPS Estimado:** Contra alvos configuráveis
- **TTK (Time to Kill):** Tempo para eliminar alvo
- **HP Efetivo:** Considerando resistências
- **Crescimento por Nível:** Fórmulas lineares precisas

### Modificadores
- **Flat:** +AD, +HP, +Armor (valores fixos)
- **Percentuais:** +%AS, +%Crit (multiplicadores)
- **Ordem de Aplicação:** Determinística e documentada

### Export de Dados
- **CSV:** Para análise em planilhas
- **JSON:** Configurações reutilizáveis
- **TXT:** Relatórios legíveis

## 🎯 Exemplos de Uso

### Exemplo 1: Build Crítica de Kai'Sa
```bash
python -m cli.app build \
  --champ "Kai'Sa" \
  --level 11 \
  --items "Kraken Slayer,Berserker's Greaves,Infinity Edge" \
  --target "bruiser" \
  --export csv
```

### Exemplo 2: Comparação de Power Spikes
```bash
python -m cli.app table \
  --champ "Jinx" \
  --levels 1,6,11,16,18 \
  --items "Kraken Slayer,Infinity Edge"
```

### Exemplo 3: Análise de Tanque
```bash
python -m cli.app build \
  --champ "Garen" \
  --level 16 \
  --items "Sunfire Aegis,Chain Vest,Negatron Cloak" \
  --target "adc"
```

## 🧪 Testes

### Executar Testes do Sistema
```bash
python test_system.py
```

### Executar Testes Unitários
```bash
pytest tests/
```

### Validar Integridade dos Dados
```bash
python -c "from data_io.loader import data_loader; data_loader.validate_data_integrity()"
```

## 🔍 Solução de Problemas

### Erro: "No module named 'colorama'"
```bash
pip install colorama pyfiglet rich pydantic typer
```

### Erro: "Campeão não encontrado"
- Verifique a grafia (ex: "Kai'Sa" com apóstrofe)
- Use `python -m cli.app champions` para ver lista completa

### Erro: "Item não encontrado"
- Verifique a grafia exata
- Use `python -m cli.app items` para ver lista completa

### Interface não aparece corretamente
- Certifique-se de usar um terminal que suporte cores
- No Windows, use PowerShell ou Windows Terminal

## 📁 Estrutura de Arquivos

```
SmashBuilder/
├── start_cyberpunk.py          # Launcher principal
├── cyberpunk_terminal.py       # Interface cyberpunk
├── test_system.py             # Testes do sistema
├── calc/                      # Engine de cálculo
│   ├── models.py             # Modelos de dados
│   ├── formulas.py           # Fórmulas matemáticas
│   └── dps.py               # Cálculos de DPS
├── data_io/                  # Sistema de I/O
│   ├── loader.py            # Carregamento de dados
│   └── exporter.py          # Exportação de resultados
├── cli/                     # Interface CLI
│   └── app.py              # Aplicação Typer
├── data/                   # Base de dados
│   ├── champions.json      # Dados de campeões
│   ├── items.json         # Dados de itens
│   └── presets.json       # Configurações predefinidas
└── tests/                 # Testes unitários
    └── test_formulas.py   # Testes das fórmulas
```

## 🎨 Personalização

### Adicionar Novos Campeões
Edite `data/champions.json` seguindo o formato existente.

### Adicionar Novos Itens
Edite `data/items.json` com modificadores apropriados.

### Modificar Cores da Interface
Edite `cyberpunk_terminal.py` na classe `CyberpunkColors`.

## 🔮 Roadmap

### v1.1 (Próxima Versão)
- [ ] Mais campeões (50+)
- [ ] Sistema de runas completo
- [ ] Fórmulas de AS reais do LoL
- [ ] Penetração (flat/percentual)

### v1.2 (Futuro)
- [ ] Passivas de itens básicas
- [ ] Habilidades e escalamento
- [ ] Análise de custo-benefício
- [ ] Recomendações automáticas

### v2.0 (Longo Prazo)
- [ ] Sincronização com patches oficiais
- [ ] Sistema de plugins
- [ ] Dashboard web opcional
- [ ] IA para otimização de builds

## 💡 Dicas de Uso

1. **Use o launcher automático** para instalação sem problemas
2. **Teste com dados conhecidos** para validar resultados
3. **Exporte para CSV** para análises detalhadas
4. **Use a tabela por níveis** para ver power spikes
5. **Compare builds similares** para otimização

## 🔥 Conclusão

O SmashBuilder oferece uma experiência única para cálculo de builds de League of Legends, combinando precisão matemática com uma interface cyberpunk imersiva. Use este guia para explorar todas as funcionalidades e otimizar suas builds!

**Bem-vindo ao futuro dos cálculos de build! 🔥**
