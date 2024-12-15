
class InventoryManager:
    _instance = None
    def __init__(self):
        if InventoryManager._instance is not None:
            raise Exception("This is a singleton class. Use get_instance() instead.")
        self.stock = {
            "cheese": 10,
            "olives": 10,
            "mushrooms": 10
        }

    @staticmethod
    def get_instance():
        if InventoryManager._instance is None:
            InventoryManager._instance = InventoryManager()
        return InventoryManager._instance

    def use_ingredient(self, ingredient: str):
        if ingredient not in self.stock:
            raise ValueError("Ingredient not managed by inventory")
        if self.stock[ingredient] <= 0:
            raise ValueError(f"Out of stock: {ingredient}")
        self.stock[ingredient] -= 1
