#!/usr/bin/env python3
"""
🔥 SmashBuilder - Teste do Sistema 🔥
Script para testar rapidamente o funcionamento do sistema
"""

import sys
from pathlib import Path

def test_imports():
    """Testa se todos os imports estão funcionando"""
    print("🔧 Testando imports...")

    try:
        from calc.models import ChampionStats, Item, ItemModifier, StatType, ModifierType
        print("✅ calc.models importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar calc.models: {e}")
        return False

    try:
        from calc.formulas import FormulaEngine
        print("✅ calc.formulas importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar calc.formulas: {e}")
        return False

    try:
        from data_io.loader import DataLoader
        print("✅ data_io.loader importado com sucesso")
    except ImportError as e:
        print(f"❌ Erro ao importar data_io.loader: {e}")
        return False

    return True

def test_data_loading():
    """Testa o carregamento de dados"""
    print("\n📊 Testando carregamento de dados...")

    try:
        from data_io.loader import data_loader

        # Testar campeões
        champions = data_loader.load_champions()
        print(f"✅ {len(champions)} campeões carregados")

        # Testar itens
        items = data_loader.load_items()
        print(f"✅ {len(items)} itens carregados")

        # Testar presets
        presets = data_loader.load_presets()
        print(f"✅ {len(presets['targets'])} alvos, {len(presets['runes'])} runas carregados")

        return True

    except Exception as e:
        print(f"❌ Erro ao carregar dados: {e}")
        return False

def test_calculation():
    """Testa cálculos básicos"""
    print("\n🧮 Testando cálculos...")

    try:
        from calc.models import ChampionStats, Item, ItemModifier, StatType, ModifierType, Build
        from calc.formulas import formula_engine
        from data_io.loader import data_loader

        # Criar campeão de teste
        champion = ChampionStats(
            name="Test Champion",
            base_ad=60,
            base_as=0.65,
            base_hp=600,
            base_armor=30,
            base_mr=30,
            base_ms=335,
            growth_ad=3,
            growth_as=2,
            growth_hp=100,
            growth_armor=4,
            growth_mr=1.3,
            growth_ms=0,
            champion_class="Test",
            patch="14.1"
        )

        # Criar item de teste
        item = Item(
            name="Test Item",
            modifiers=[
                ItemModifier(stat=StatType.AD, value=40, modifier_type=ModifierType.FLAT)
            ],
            cost=1000
        )

        # Criar build
        build = Build(
            name="Test Build",
            champion=champion,
            level=11,
            items=[item]
        )

        # Calcular
        final_stats = formula_engine.calculate_final_stats(build)

        print(f"✅ Cálculo realizado - AD final: {final_stats.ad}")
        print(f"✅ AS final: {final_stats.as_}")
        print(f"✅ HP final: {final_stats.hp}")

        return True

    except Exception as e:
        print(f"❌ Erro no cálculo: {e}")
        return False

def test_real_data():
    """Testa com dados reais"""
    print("\n🎮 Testando com dados reais...")

    try:
        from calc.models import Build
        from calc.formulas import formula_engine
        from data_io.loader import data_loader

        # Carregar Kai'Sa
        kaisa = data_loader.get_champion("kai'sa")
        if not kaisa:
            print("❌ Kai'Sa não encontrada")
            return False

        # Carregar Infinity Edge
        ie = data_loader.get_item("infinity edge")
        if not ie:
            print("❌ Infinity Edge não encontrado")
            return False

        # Carregar alvo
        presets = data_loader.load_presets()
        target = presets["targets"]["fragile"]

        # Criar build
        build = Build(
            name="Kai'Sa Test",
            champion=kaisa,
            level=11,
            items=[ie],
            target=target
        )

        # Calcular
        final_stats = formula_engine.calculate_final_stats(build)

        print(f"✅ Kai'Sa Level 11 com IE:")
        print(f"   AD: {final_stats.ad}")
        print(f"   AS: {final_stats.as_}")
        print(f"   Crit: {final_stats.crit_chance}%")
        if final_stats.dps:
            print(f"   DPS: {final_stats.dps}")

        return True

    except Exception as e:
        print(f"❌ Erro com dados reais: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🔥" + "="*60 + "🔥")
    print("    SMASHBUILDER - TESTE DO SISTEMA")
    print("🔥" + "="*60 + "🔥")

    tests = [
        test_imports,
        test_data_loading,
        test_calculation,
        test_real_data
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        else:
            print(f"\n❌ Teste falhou: {test.__name__}")

    print(f"\n🔥 RESULTADO: {passed}/{total} testes passaram")

    if passed == total:
        print("✅ Todos os testes passaram! Sistema funcionando corretamente.")
        return True
    else:
        print("❌ Alguns testes falharam. Verifique os erros acima.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
