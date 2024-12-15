
import pytest
from app.pizza_factory import PizzaFactory
from app.toppings import Cheese, Olives, Mushrooms
from app.inventory import InventoryManager

def test_margherita_pizza_creation():
    pizza = PizzaFactory.create_pizza("Margherita")
    assert pizza.get_description() == "Margherita"
    assert pizza.get_cost() == 5.0

def test_pepperoni_pizza_creation():
    pizza = PizzaFactory.create_pizza("Pepperoni")
    assert pizza.get_description() == "Pepperoni"
    assert pizza.get_cost() == 6.0

def test_adding_toppings():
    inv = InventoryManager.get_instance()
    inv.stock = {"cheese": 10, "olives": 10, "mushrooms": 10}

    pizza = PizzaFactory.create_pizza("Margherita")
    pizza = Cheese(pizza)
    assert "Cheese" in pizza.get_description()
    assert pizza.get_cost() == 6.0

    pizza = Olives(pizza)
    assert "Olives" in pizza.get_description()
    assert pizza.get_cost() == 6.5

def test_inventory_depletion():
    inv = InventoryManager.get_instance()
    inv.stock = {"cheese": 1, "olives": 1, "mushrooms": 1}

    pizza = PizzaFactory.create_pizza("Margherita")
    pizza = Cheese(pizza)  
    assert inv.stock["cheese"] == 0

    with pytest.raises(ValueError):
        pizza = Cheese(pizza)

def test_unknown_pizza_type():
    with pytest.raises(ValueError):
        PizzaFactory.create_pizza("UnknownType")
