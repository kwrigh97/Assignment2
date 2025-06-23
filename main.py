import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ")

        if choice == "off":
            is_on = False
        elif choice == "report":
            for item, amount in resources.items():
                unit = "slice(s)" if item != "cheese" else "pound(s)"
                print(f"{item.title()}: {amount} {unit}")
        elif choice in recipes:
            sandwich = recipes[choice]
            ingredients = sandwich["ingredients"]
            cost = sandwich["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
                    print(f"{choice} sandwich is ready. Bon appetit!")
        else:
            print("Invalid selection.")

if __name__=="__main__":
    main()
