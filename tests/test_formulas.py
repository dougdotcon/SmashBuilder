"""
🔥 SmashBuilder - Testes de Fórmulas 🔥
Testes unitários para o engine de fórmulas
"""

import pytest
from calc.models import ChampionStats, Item, ItemModifier, StatType, ModifierType, Build, Target
from calc.formulas import FormulaEngine

class TestFormulaEngine:
    """Testes para o engine de fórmulas"""
    
    def setup_method(self):
        """Setup para cada teste"""
        self.engine = FormulaEngine()
        
        # Campeão de teste (baseado em Kai'Sa)
        self.test_champion = ChampionStats(
            name="Test Champion",
            base_ad=59,
            base_as=0.644,
            base_hp=640,
            base_armor=28,
            base_mr=30,
            base_ms=335,
            growth_ad=2,
            growth_as=1.8,
            growth_hp=102,
            growth_armor=4.2,
            growth_mr=1.3,
            growth_ms=0,
            champion_class="Test",
            patch="14.1"
        )
        
        # Item de teste
        self.test_item = Item(
            name="Test Item",
            modifiers=[
                ItemModifier(stat=StatType.AD, value=40, modifier_type=ModifierType.FLAT),
                ItemModifier(stat=StatType.AS, value=25, modifier_type=ModifierType.PERCENT)
            ],
            cost=1000
        )
        
        # Alvo de teste
        self.test_target = Target(name="Test Target", hp=1000, armor=50, mr=30)
    
    def test_base_stats_level_1(self):
        """Testa cálculo de stats base no nível 1"""
        stats = self.engine.calculate_base_stats_at_level(self.test_champion, 1)
        
        # No nível 1, stats devem ser iguais aos base
        assert stats[StatType.AD] == 59
        assert stats[StatType.AS] == 0.644
        assert stats[StatType.HP] == 640
        assert stats[StatType.ARMOR] == 28
        assert stats[StatType.MR] == 30
    
    def test_base_stats_level_18(self):
        """Testa cálculo de stats base no nível 18"""
        stats = self.engine.calculate_base_stats_at_level(self.test_champion, 18)
        
        # No nível 18, deve aplicar crescimento máximo (17 níveis de crescimento)
        expected_ad = 59 + (2 * 17)  # 93
        expected_as = 0.644 * (1 + (1.8 * 17 / 100))  # ~0.84
        expected_hp = 640 + (102 * 17)  # 2374
        
        assert abs(stats[StatType.AD] - expected_ad) < 0.01
        assert abs(stats[StatType.AS] - expected_as) < 0.01
        assert abs(stats[StatType.HP] - expected_hp) < 0.01
    
    def test_invalid_level(self):
        """Testa validação de nível inválido"""
        with pytest.raises(ValueError):
            self.engine.calculate_base_stats_at_level(self.test_champion, 0)
        
        with pytest.raises(ValueError):
            self.engine.calculate_base_stats_at_level(self.test_champion, 19)
    
    def test_item_modifiers_flat(self):
        """Testa aplicação de modificadores flat"""
        base_stats = {StatType.AD: 100, StatType.AS: 1.0}
        
        # Item que adiciona +40 AD
        item = Item(
            name="Flat AD Item",
            modifiers=[ItemModifier(stat=StatType.AD, value=40, modifier_type=ModifierType.FLAT)],
            cost=1000
        )
        
        result = self.engine.apply_item_modifiers(base_stats, [item])
        
        assert result[StatType.AD] == 140  # 100 + 40
        assert result[StatType.AS] == 1.0  # Inalterado
    
    def test_item_modifiers_percent(self):
        """Testa aplicação de modificadores percentuais"""
        base_stats = {StatType.AS: 1.0}
        
        # Item que adiciona +25% AS
        item = Item(
            name="Percent AS Item",
            modifiers=[ItemModifier(stat=StatType.AS, value=25, modifier_type=ModifierType.PERCENT)],
            cost=1000
        )
        
        result = self.engine.apply_item_modifiers(base_stats, [item])
        
        assert abs(result[StatType.AS] - 1.25) < 0.01  # 1.0 * 1.25
    
    def test_attack_speed_cap(self):
        """Testa cap de attack speed"""
        stats = {StatType.AS: 3.0}  # Acima do cap
        
        result = self.engine.apply_caps_and_limits(stats)
        
        assert result[StatType.AS] == 2.5  # Cap máximo
    
    def test_critical_chance_cap(self):
        """Testa cap de critical chance"""
        stats = {StatType.CRIT_CHANCE: 150}  # Acima do cap
        
        result = self.engine.apply_caps_and_limits(stats)
        
        assert result[StatType.CRIT_CHANCE] == 100  # Cap máximo
    
    def test_damage_reduction_calculation(self):
        """Testa cálculo de redução de dano"""
        # 50 armor = ~33.3% redução
        reduction = self.engine.calculate_damage_reduction(50)
        expected = 50 / (100 + 50)  # 0.333...
        
        assert abs(reduction - expected) < 0.01
    
    def test_effective_hp_calculation(self):
        """Testa cálculo de HP efetivo"""
        hp = 1000
        armor = 100  # 50% redução de dano
        
        effective_hp = self.engine.calculate_effective_hp(hp, armor)
        expected = hp / (1 - 0.5)  # 2000
        
        assert abs(effective_hp - expected) < 1
    
    def test_dps_calculation(self):
        """Testa cálculo de DPS básico"""
        # Stats simulados
        from calc.models import FinalStats
        
        stats = FinalStats(
            level=11,
            ad=200,
            ap=0,
            as_=1.5,
            crit_chance=50,
            crit_damage=200,
            hp=2000,
            mana=500,
            armor=80,
            mr=50,
            ms=350
        )
        
        dps = self.engine.calculate_dps(stats, self.test_target)
        
        # DPS deve ser > 0 e razoável
        assert dps > 0
        assert dps < 1000  # Sanity check
    
    def test_full_build_calculation(self):
        """Testa cálculo completo de uma build"""
        build = Build(
            name="Test Build",
            champion=self.test_champion,
            level=11,
            items=[self.test_item],
            target=self.test_target
        )
        
        final_stats = self.engine.calculate_final_stats(build)
        
        # Verificar se stats foram calculados
        assert final_stats.level == 11
        assert final_stats.ad > self.test_champion.base_ad  # Deve ter aumentado com item
        assert final_stats.as_ > self.test_champion.base_as  # Deve ter aumentado com item
        assert final_stats.dps is not None
        assert final_stats.dps > 0

if __name__ == "__main__":
    pytest.main([__file__])
