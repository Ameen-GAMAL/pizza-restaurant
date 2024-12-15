
from .pizzas import Margherita, Pepperoni, Pizza

class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type.lower() == "margherita":
            return Margherita()
        elif pizza_type.lower() == "pepperoni":
            return Pepperoni()
        else:
            raise ValueError("Unknown pizza type")
