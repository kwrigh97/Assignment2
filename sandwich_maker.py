
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount_needed in ingredients.items():
            if amount_needed > self.machine_resources.get(item, 0):
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, amount_needed in order_ingredients.items():
            if item in self.machine_resources:
                self.machine_resources[item] -= amount_needed