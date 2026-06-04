recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = large_dollars * 1.00
        total += half_dollars * 0.50
        total += quarters * 0.25
        total += nickels * 0.05

        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


sandwich_machine = SandwichMachine(resources)

machine_on = True

while machine_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_machine.machine_resources['cheese']} pound(s)")
    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if sandwich_machine.check_resources(ingredients):
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich(choice, ingredients)
    else:
        print("Invalid choice.")
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


class SandwichMachine:

    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = large_dollars * 1.00
        total += half_dollars * 0.50
        total += quarters * 0.25
        total += nickels * 0.05

        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")


sandwich_machine = SandwichMachine(resources)

machine_on = True

while machine_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_machine.machine_resources['cheese']} pound(s)")
    elif choice in recipes:
        sandwich = recipes[choice]
        ingredients = sandwich["ingredients"]
        cost = sandwich["cost"]

        if sandwich_machine.check_resources(ingredients):
            coins = sandwich_machine.process_coins()
            if sandwich_machine.transaction_result(coins, cost):
                sandwich_machine.make_sandwich(choice, ingredients)
    else:
        print("Invalid choice.")
