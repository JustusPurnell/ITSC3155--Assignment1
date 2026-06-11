from savings_account import SavingsAccount
from checking_account import CheckingAccount

savings1 = SavingsAccount("Justus Purnell", 1000, 100, "S1001", "053000219", 0.05)
savings2 = SavingsAccount("John Smith", 500, 50, "S1002", "053000219", 0.03)

checking1 = CheckingAccount("Charlotte Purnell", 1200, 100, "C2001", "053000219", 500)
checking2 = CheckingAccount("Alcenia Purnell", 800, 50, "C2002", "053000219", 300)

savings1.deposit(200)
savings1.add_interest()
savings1.withdraw(300)

savings2.deposit(100)
savings2.add_interest()

checking1.withdraw(150)
checking1.transfer(400, checking2)

checking2.deposit(250)
checking2.transfer(350, checking1)

savings1.print_customer_information()
savings2.print_customer_information()
checking1.print_customer_information()
checking2.print_customer_information()

predict(model, new_location, interval = "confidence", level = 0.95)

predict(model, new_location, interval = "prediction", level = 0.95)