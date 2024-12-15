# Design Patterns in Pizza Restaurant Application

## Introduction

Design patterns are proven solutions to common software design problems. In the Pizza Restaurant application, several design patterns have been employed to enhance code quality and maintainability. This document explains each design pattern used and explores the concept of overengineering with illustrative examples.

## Applied Design Patterns

### 1. **Factory Pattern**

- **Purpose:** To create objects without specifying the exact class of the object that will be created.
- **Usage in Application:** Used to instantiate different types of pizzas (e.g., Margherita, Pepperoni) based on user input.
- **Example:**

    ```python
    class PizzaFactory:
        def create_pizza(self, pizza_type):
            if pizza_type == 'Margherita':
                return MargheritaPizza()
            elif pizza_type == 'Pepperoni':
                return PepperoniPizza()
            else:
                raise ValueError("Unknown pizza type")
    ```

### 2. **Strategy Pattern**

- **Purpose:** To define a family of algorithms, encapsulate each one, and make them interchangeable.
- **Usage in Application:** Implementing different pricing strategies (e.g., regular pricing, discount pricing).
- **Example:**

    ```python
    class PricingStrategy(ABC):
        @abstractmethod
        def calculate_price(self, base_price):
            pass

    class RegularPricing(PricingStrategy):
        def calculate_price(self, base_price):
            return base_price

    class DiscountPricing(PricingStrategy):
        def calculate_price(self, base_price):
            return base_price * 0.9
    ```

### 3. **Observer Pattern**

- **Purpose:** To define a one-to-many dependency so that when one object changes state, all its dependents are notified.
- **Usage in Application:** Notifying kitchen staff when a new order is placed.
- **Example:**

    ```python
    class Subject:
        def __init__(self):
            self._observers = []

        def attach(self, observer):
            self._observers.append(observer)

        def notify(self, message):
            for observer in self._observers:
                observer.update(message)

    class KitchenStaff:
        def update(self, message):
            print(f"Kitchen received: {message}")
    ```

### 4. **Decorator Pattern**

- **Purpose:** To attach additional responsibilities to an object dynamically.
- **Usage in Application:** Adding extra toppings to a pizza without modifying the original pizza classes.
- **Example:**

    ```python
    class Pizza(ABC):
        @abstractmethod
        def get_description(self):
            pass

        @abstractmethod
        def get_cost(self):
            pass

    class BasicPizza(Pizza):
        def get_description(self):
            return "Basic Pizza"

        def get_cost(self):
            return 5.0

    class ToppingDecorator(Pizza):
        def __init__(self, pizza):
            self._pizza = pizza

        @abstractmethod
        def get_description(self):
            pass

    class Cheese(ToppingDecorator):
        def get_description(self):
            return self._pizza.get_description() + ", Cheese"

        def get_cost(self):
            return self._pizza.get_cost() + 1.0
    ```

## Overengineering: A Cautionary Tale

### **What is Overengineering?**

Overengineering occurs when a solution is more complex than necessary to solve the problem at hand. It can lead to increased development time, higher maintenance costs, and reduced code readability.

### **Example of Overengineering in the Pizza Restaurant Application**

Imagine implementing a full-fledged plugin system to handle pizza toppings, allowing users to add any number of toppings dynamically. While this provides flexibility, it may be unnecessary for the current scope of the application and introduces unnecessary complexity.

#### **Overengineered Code Example:**

```python
class ToppingPlugin(ABC):
    @abstractmethod
    def add_topping(self, pizza):
        pass

class CheesePlugin(ToppingPlugin):
    def add_topping(self, pizza):
        pizza.add_topping("Cheese")
        pizza.cost += 1.0

class PepperoniPlugin(ToppingPlugin):
    def add_topping(self, pizza):
        pizza.add_topping("Pepperoni")
        pizza.cost += 1.5

# Plugin Manager
class PluginManager:
    def __init__(self):
        self._plugins = []

    def register_plugin(self, plugin: ToppingPlugin):
        self._plugins.append(plugin)

    def apply_plugins(self, pizza):
        for plugin in self._plugins:
            plugin.add_topping(pizza)

# Usage
plugin_manager = PluginManager()
plugin_manager.register_plugin(CheesePlugin())
plugin_manager.register_plugin(PepperoniPlugin())

pizza = BasicPizza()
plugin_manager.apply_plugins(pizza)
