import random

def get_name():
    return input("What is your name? ")

def get_lucky_number():
    return int(input("Enter a lucky number: "))

def generate_fortune(name, number):
    fortunes = [
        "You will have a great day.",
        "Something exciting is coming soon.",
        "A new opportunity is heading your way.",
        "Good luck is on your side."
    ]
    return f"{name}, your lucky number is {number}. {random.choice(fortunes)}"

name = get_name()
number = get_lucky_number()
print(generate_fortune(name, number))