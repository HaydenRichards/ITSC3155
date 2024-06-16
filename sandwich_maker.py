
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources
        self.size = input("What would you like? (small/ medium/ large/ off/ report): ")

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for x in ingredients:
            if ingredients[x] > self.machine_resources[x]:
                print("Sorry there is not enough " + x + ".")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for x in order_ingredients:
            self.machine_resources[x] -= order_ingredients[x]
        print(sandwich_size + " is ready. Bon appetit!")
