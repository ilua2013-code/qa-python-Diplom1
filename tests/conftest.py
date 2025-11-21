import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from prakticum.bun import Bun
import pytest
from prakticum.bun import Bun
from unittest.mock import Mock, MagicMock, patch, create_autospec
from data import DataBurger
from prakticum.ingredient import Ingredient
from prakticum.burger import Burger


@pytest.fixture
def burger():
    """Создает чистый объект Burger без ингредиентов"""
    return Burger()

@pytest.fixture
def mokk_set_buns():
    """Мок булочки black bun с ценой 100"""
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = DataBurger.BLACK_BUN[0]
    mock_bun.get_price.return_value = DataBurger.BLACK_BUN[1]
    return mock_bun

@pytest.fixture
def mokk_ingredient_sauce():
    """Мок соуса hot sauce с ценой 100"""
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_type.return_value = DataBurger.HOT_SAUCE[0]
    mock_ingredient.get_name.return_value = DataBurger.HOT_SAUCE[1]
    mock_ingredient.get_price.return_value = DataBurger.HOT_SAUCE[2]
    return mock_ingredient

@pytest.fixture
def mokk_ingredient_filling():
    """Мок начинки cutlet с ценой 100"""
    mock_ingredient = Mock(spec=Ingredient)
    mock_ingredient.get_type.return_value = DataBurger.CUTLET[0]
    mock_ingredient.get_name.return_value = DataBurger.CUTLET[1]
    mock_ingredient.get_price.return_value = DataBurger.CUTLET[2]
    return mock_ingredient

@pytest.fixture
def ingredient_list():
    """Список из двух ингредиентов для тестов удаления и перемещения"""
    return [DataBurger.CUTLET, DataBurger.HOT_SAUCE]