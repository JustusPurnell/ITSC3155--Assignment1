from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, other_account):
        if amount > self.transfer_limit:
            print("Transfer denied. Amount is over the transfer limit.")
        elif self.current_balance - amount < self.minimum_balance:
            print("Transfer denied. Balance would fall below minimum balance.")
        else:
            self.current_balance -= amount
            other_account.current_balance += amount
            print(f"${amount} transferred to {other_account.customer_name}.")
            