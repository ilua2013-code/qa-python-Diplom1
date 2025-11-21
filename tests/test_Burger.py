from data import DataBurger
import pytest
from unittest.mock import Mock


class TestBurger:

    """Добавление булочки к бургеру"""
    def test_set_buns(self, mokk_set_buns, burger):
        burger.set_buns(mokk_set_buns)
        assert burger.bun == mokk_set_buns
    
    """Добавление ингридиента  к бургеру"""
    def test_add_ingredient(self, mokk_ingredient_sauce, burger):
        burger.add_ingredient(mokk_ingredient_sauce)
        assert mokk_ingredient_sauce in burger.ingredients
        assert len(burger.ingredients) == 1
    
    """Удаление ингридиента из списка состоящий из двух элеметов"""
    def test_remove_ingredient(self, ingredient_list, burger):
        burger.ingredients = ingredient_list
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 1
    
    """Поменять местами ингридиенты в списке"""
    def test_move_ingredient(self, ingredient_list, burger):
        burger.ingredients = ingredient_list
        burger.move_ingredient(0,1)
        assert burger.ingredients[1] == DataBurger.CUTLET

        
    
    @pytest.mark.parametrize('bun_price, ingredient_prices, expected_price',[(100, [], 200), (100, [50], 250),(200, [50, 100], 550)])
    def test_get_price_full(self, burger,bun_price, ingredient_prices, expected_price):
        """Посчитать цену бургера только с булками, булками и соусом, булками соусом и начинкой"""
        mokk_price = Mock()
        mokk_price.get_price.return_value = bun_price
        burger.bun = mokk_price
        burger.ingredients = []
        for i in ingredient_prices:
            mokk_price_ingr = Mock()
            mokk_price_ingr.get_price.return_value = i
            burger.ingredients.append(mokk_price_ingr)
        
        assert burger.get_price() == expected_price
        

    
    def test_receipt_formatting(self, burger):
    # Тест на точный формат чека
        mokk_bun = Mock()
        mokk_bun.get_price.return_value =  DataBurger.RED_BUN[1]
        mokk_bun.get_name.return_value =  DataBurger.RED_BUN[0]
        burger.bun = mokk_bun
        mokk_ing = Mock()
        mokk_ing.get_type.return_value = DataBurger.HOT_SAUCE[0]
        mokk_ing.get_name.return_value = DataBurger.HOT_SAUCE[1]
        mokk_ing.get_price.return_value = 100
        burger.bun = mokk_bun
        burger.ingredients = [mokk_ing]
        assert DataBurger.expected_receipt == burger.get_receipt() 

    