# SmashBuilder

<div align="center">

<img src="logo.png" alt="SmashBuilder Logo" width="160" height="160" style="border-radius: 24px; margin: 30px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);" />

## SmashBuilder — League of Legends Build Calculator

[![Status](https://img.shields.io/badge/Status-Beta-green?style=for-the-badge)](#)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-667eea.svg?style=for-the-badge&labelColor=1a202c)](https://opensource.org/licenses/MIT)
[![Interface](https://img.shields.io/badge/Interface-CLI_Terminal-5865f2?style=for-the-badge)](#)

<div style="margin: 20px 0; max-width: 85%;">
  <p style="font-size: 1.05em; color: #4a5568; margin: 0;">
    SmashBuilder is an advanced League of Legends build calculator featuring an immersive cyberpunk terminal interface. It enables players to calculate final attributes, estimated DPS, and compare builds efficiently, complete with CSV/JSON export capabilities.
  </p>
</div>
</div>

## 🚀 Quick Start

bash
# Launch the cyberpunk interface
python start_cyberpunk.py

# Or use the CLI directly
python -m cli.app quick


## 📋 Project Overview

**SmashBuilder** is an advanced build calculator for League of Legends designed with a cyberpunk terminal aesthetic. This project allows players to rapidly calculate final attributes, estimate DPS, and compare builds efficiently through an immersive, futuristic terminal experience.

## 🎯 Key Features

### 🎨 Cyberpunk Terminal Interface
- **Animated ASCII Banner**: Custom cyberpunk artwork using pyfiglet
- **Neon Color Scheme**: Full palette (cyan, green, yellow, magenta, red)
- **Loading Animations**: Custom character sequences (▓▒░)
- **Styled Menus**: Unicode-bordered navigation elements
- **Real-time Feedback**: Visual responses for all operations
- **Immersive Experience**: Futuristic aesthetic and feel

### 🚀 Calculation Engine
- **Final Attribute Calculation**: AD, AS, HP, Armor, MR, Crit, and more
- **Estimated DPS**: Configurable against various target dummies
- **Build Comparison**: Side-by-side build analysis
- **Champion Support**: Multiple champions with base stats and growth
- **Items & Runes**: Configurable systems with flat and percentage modifiers
- **Level Scaling**: Stats tables for levels 1, 6, 11, 16, and 18

### 🌐 Data Coverage
- **Champions**: Local database with base stats and growth coefficients
- **Items**: Complete catalog with flat and percentage modifiers
- **Runes**: Configurable presets for various build archetypes
- **Targets**: Predefined configurations (Squishy, Tank, etc.)

## 📁 Project Structure

### 🔧 Core Modules

#### **cyberpunk_terminal.py** - Main Interface
- **Class `CyberpunkTerminal`**: Complete cyberpunk interface implementation
- **ASCII Banner**: Futuristic art using pyfiglet
- **Color System**: Comprehensive neon palette implementation
- **Interactive Menus**: Intuitive navigation structure
- **Backend Integration**: Connection to the calculation engine

#### **start_cyberpunk.py** - Launcher
- **Auto-installation**: Dependency verification and installation
- **System Check**: Environment compatibility validation
- **Main Entry Point**: Unified application launch

#### **cli/app.py** - Command Line Interface
- **Direct CLI Access**: Execute calculations via command line
- **Subcommands**: `quick` mode for rapid calculations
- **Configurable Options**: Flexible argument parsing

### 🗂️ Data Modules

#### **models/** - Core Data Models
- **Champion**: Data class for champion stats and scaling
- **Item**: Item modifier structures (flat/percentage)
- **Rune**: Rune preset configurations
- **Target**: Enemy configuration for damage calculations

#### **data/** - Databases
- **champions.json**: Base stats for all supported champions
- **items.json**: Complete item catalog
- **runes.json**: Rune preset definitions
- **targets.json**: Target dummy configurations

## 💻 Installation & Usage

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**
   bash
   git clone https://github.com/your-username/smashbuilder.git
   cd smashbuilder
   

2. **Install dependencies:**
   bash
   pip install -r requirements.txt
   

3. **Run the application:**
   bash
   python start_cyberpunk.py
   

### Usage Examples

#### **Interactive Mode**
bash
python start_cyberpunk.py
# Navigate through the cyberpunk interface


#### **Quick Calculation (CLI)**
bash
python -m cli.app quick --champion Jinx --items "Kraken Slayer,Runaan's Hurricane,Infinity Edge"


#### **Build Comparison**
bash
python -m cli.app compare --build1 "item1,item2,item3" --build2 "item4,item5,item6"


## 🛠️ Technology Stack

- **Language**: Python 3.8+
- **UI**: Terminal (CLI) with ANSI escape codes
- **Data Storage**: JSON files
- **Art**: pyfiglet (ASCII art)
- **Colors**: rich (terminal styling)

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **League of Legends** - Game data and concepts
- **Python Rich** - Terminal styling and formatting
- **Pyfiglet** - ASCII art generation
- **Open Source Community** - Inspiration and best practices
