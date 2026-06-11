class BankAccount:
    bank_title = "Charlotte Community Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self._account_number = account_number      # protected member
        self.__routing_number = routing_number     # private member

    def deposit(self, amount):
        self.current_balance += amount
        print(f"${amount} deposited.")

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Withdrawal denied. Balance would fall below minimum balance.")
        else:
            self.current_balance -= amount
            print(f"${amount} withdrawn.")

    def print_customer_information(self):
        print("\nBank Title:", BankAccount.bank_title)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)
        print("Account Number:", self._account_number)
        print("Routing Number:", self.__routing_number)