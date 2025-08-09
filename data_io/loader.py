"""
🔥 SmashBuilder - Carregador de Dados 🔥
Sistema para carregar dados de campeões, itens e presets
"""

import json
import yaml
from pathlib import Path
from typing import Dict, List, Optional, Union

try:
    from calc.models import (
        ChampionStats, Item, ItemModifier, RunePreset, RuneModifier,
        Target, StatType, ModifierType
    )
except ImportError:
    # Fallback para execução direta
    import sys
    sys.path.append(str(Path(__file__).parent.parent))
    from calc.models import (
        ChampionStats, Item, ItemModifier, RunePreset, RuneModifier,
        Target, StatType, ModifierType
    )

class DataLoader:
    """Carregador principal de dados"""

    def __init__(self, data_dir: Union[str, Path] = None):
        if data_dir is None:
            # Diretório padrão relativo ao arquivo atual
            self.data_dir = Path(__file__).parent.parent / "data"
        else:
            self.data_dir = Path(data_dir)

        self._champions_cache = None
        self._items_cache = None
        self._presets_cache = None

    def load_json(self, filename: str) -> Dict:
        """Carrega arquivo JSON"""
        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao decodificar JSON em {filename}: {e}")

    def load_yaml(self, filename: str) -> Dict:
        """Carrega arquivo YAML"""
        file_path = self.data_dir / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise ValueError(f"Erro ao decodificar YAML em {filename}: {e}")

    def load_champions(self, force_reload: bool = False) -> Dict[str, ChampionStats]:
        """Carrega dados de campeões"""
        if self._champions_cache is None or force_reload:
            data = self.load_json("champions.json")
            champions = {}

            for champion_data in data.get("champions", []):
                try:
                    champion = ChampionStats(**champion_data)
                    champions[champion.name.lower()] = champion
                except Exception as e:
                    print(f"Erro ao carregar campeão {champion_data.get('name', 'Unknown')}: {e}")

            self._champions_cache = champions

        return self._champions_cache

    def load_items(self, force_reload: bool = False) -> Dict[str, Item]:
        """Carrega dados de itens"""
        if self._items_cache is None or force_reload:
            data = self.load_json("items.json")
            items = {}

            for item_data in data.get("items", []):
                try:
                    # Converter modificadores
                    modifiers = []
                    for mod_data in item_data.get("modifiers", []):
                        modifier = ItemModifier(
                            stat=StatType(mod_data["stat"]),
                            value=mod_data["value"],
                            modifier_type=ModifierType(mod_data["modifier_type"])
                        )
                        modifiers.append(modifier)

                    # Criar item
                    item = Item(
                        name=item_data["name"],
                        modifiers=modifiers,
                        cost=item_data.get("cost", 0),
                        unique=item_data.get("unique", False),
                        mythic=item_data.get("mythic", False)
                    )

                    items[item.name.lower()] = item

                except Exception as e:
                    print(f"Erro ao carregar item {item_data.get('name', 'Unknown')}: {e}")

            self._items_cache = items

        return self._items_cache

    def load_presets(self, force_reload: bool = False) -> Dict:
        """Carrega presets de alvos, runas e buffs"""
        if self._presets_cache is None or force_reload:
            data = self.load_json("presets.json")

            # Carregar alvos
            targets = {}
            for target_key, target_data in data.get("targets", {}).items():
                try:
                    target = Target(**target_data)
                    targets[target_key] = target
                except Exception as e:
                    print(f"Erro ao carregar alvo {target_key}: {e}")

            # Carregar runas
            runes = {}
            for rune_key, rune_data in data.get("runes", {}).items():
                try:
                    # Converter modificadores
                    modifiers = []
                    for mod_data in rune_data.get("modifiers", []):
                        modifier = RuneModifier(
                            stat=StatType(mod_data["stat"]),
                            value=mod_data["value"],
                            modifier_type=ModifierType(mod_data["modifier_type"])
                        )
                        modifiers.append(modifier)

                    rune_preset = RunePreset(
                        name=rune_data["name"],
                        description=rune_data.get("description", ""),
                        modifiers=modifiers
                    )

                    runes[rune_key] = rune_preset

                except Exception as e:
                    print(f"Erro ao carregar runa {rune_key}: {e}")

            # Carregar buffs (similar às runas)
            buffs = {}
            for buff_key, buff_data in data.get("buffs", {}).items():
                try:
                    modifiers = []
                    for mod_data in buff_data.get("modifiers", []):
                        modifier = RuneModifier(
                            stat=StatType(mod_data["stat"]),
                            value=mod_data["value"],
                            modifier_type=ModifierType(mod_data["modifier_type"])
                        )
                        modifiers.append(modifier)

                    buff_preset = RunePreset(
                        name=buff_data["name"],
                        description=buff_data.get("description", ""),
                        modifiers=modifiers
                    )

                    buffs[buff_key] = buff_preset

                except Exception as e:
                    print(f"Erro ao carregar buff {buff_key}: {e}")

            self._presets_cache = {
                "targets": targets,
                "runes": runes,
                "buffs": buffs,
                "build_templates": data.get("build_templates", {})
            }

        return self._presets_cache

    def get_champion(self, name: str) -> Optional[ChampionStats]:
        """Busca um campeão por nome"""
        champions = self.load_champions()
        return champions.get(name.lower())

    def get_item(self, name: str) -> Optional[Item]:
        """Busca um item por nome"""
        items = self.load_items()
        return items.get(name.lower())

    def get_target(self, name: str) -> Optional[Target]:
        """Busca um alvo por nome"""
        presets = self.load_presets()
        return presets["targets"].get(name.lower())

    def get_rune_preset(self, name: str) -> Optional[RunePreset]:
        """Busca um preset de runas por nome"""
        presets = self.load_presets()
        return presets["runes"].get(name.lower())

    def search_champions(self, query: str) -> List[ChampionStats]:
        """Busca campeões por nome parcial"""
        champions = self.load_champions()
        query_lower = query.lower()

        results = []
        for name, champion in champions.items():
            if query_lower in name or query_lower in champion.name.lower():
                results.append(champion)

        return results

    def search_items(self, query: str) -> List[Item]:
        """Busca itens por nome parcial"""
        items = self.load_items()
        query_lower = query.lower()

        results = []
        for name, item in items.items():
            if query_lower in name or query_lower in item.name.lower():
                results.append(item)

        return results

    def get_items_by_stat(self, stat: StatType) -> List[Item]:
        """Busca itens que modificam um stat específico"""
        items = self.load_items()
        results = []

        for item in items.values():
            for modifier in item.modifiers:
                if modifier.stat == stat:
                    results.append(item)
                    break

        return results

    def validate_data_integrity(self) -> Dict[str, List[str]]:
        """Valida a integridade dos dados carregados"""
        errors = {
            "champions": [],
            "items": [],
            "presets": []
        }

        try:
            champions = self.load_champions()
            print(f"✅ {len(champions)} campeões carregados com sucesso")
        except Exception as e:
            errors["champions"].append(str(e))

        try:
            items = self.load_items()
            print(f"✅ {len(items)} itens carregados com sucesso")
        except Exception as e:
            errors["items"].append(str(e))

        try:
            presets = self.load_presets()
            print(f"✅ {len(presets['targets'])} alvos, {len(presets['runes'])} runas, {len(presets['buffs'])} buffs carregados")
        except Exception as e:
            errors["presets"].append(str(e))

        return errors

# Instância global do carregador
data_loader = DataLoader()
