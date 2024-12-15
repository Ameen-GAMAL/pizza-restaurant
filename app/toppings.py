
from abc import ABC, abstractmethod
from .pizzas import Pizza
from .inventory import InventoryManager

class ToppingDecorator(Pizza, ABC):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Cheese(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)

        InventoryManager.get_instance().use_ingredient("cheese")

    def get_description(self) -> str:
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 1.0


class Olives(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        InventoryManager.get_instance().use_ingredient("olives")

    def get_description(self) -> str:
        return self.pizza.get_description() + ", Olives"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.5


class Mushrooms(ToppingDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        InventoryManager.get_instance().use_ingredient("mushrooms")

    def get_description(self) -> str:
        return self.pizza.get_description() + ", Mushrooms"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.7
