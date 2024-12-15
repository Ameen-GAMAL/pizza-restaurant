
from app.pizza_factory import PizzaFactory
from app.toppings import Cheese, Olives
from app.inventory import InventoryManager
from app.payment import PayPalPayment, CreditCardPayment

if __name__ == "__main__":

    inv = InventoryManager.get_instance()
    print("Initial Stock:", inv.stock)


    pizza = PizzaFactory.create_pizza("Margherita")

  
    pizza = Cheese(pizza)
    pizza = Olives(pizza)


    print("Order Description:", pizza.get_description())
    print("Total Cost:", pizza.get_cost())

   
    payment_method = PayPalPayment()  
    # payment_method = CreditCardPayment()
    
    payment_method.pay(pizza.get_cost())
