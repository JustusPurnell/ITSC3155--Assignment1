import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes

sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    machine_on = True

    while machine_on:
        choice = input("What would you like? (small/medium/large/off/report): ").lower()

        if choice == "off":
            machine_on = False

        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slices")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slices")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces")

        elif choice in recipes:
            sandwich = recipes[choice]

            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                coins = cashier_instance.process_coins()

                if cashier_instance.transaction_result(coins, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()