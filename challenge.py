# FInish defining the constant with menu items and calories below:
MENU = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Big Mac": 540,
    "McChicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150
}


# Implement the poor_calories_counter function below:
def poor_calories_counter(order):
    return MENU.get(order, f"{order} not found")


print(poor_calories_counter("Hamburger"))






# Do not modify the code below:
print("##########################################")
print("##################TESTS###################")
print("##########################################\n")

import os
print("Testing with Hamburger")
if poor_calories_counter("Hamburger") == 250:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Big Mac")
if poor_calories_counter("Big Mac") == 540:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")
    
print("French Fries")
if poor_calories_counter("French Fries") == 230:
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")

print("Testing with Shrimp")
if poor_calories_counter("Shrimp") == 'Shrimp not found':
    os.system("echo '\e[32mCorrect\e[0m'")
else:
	os.system("echo '\e[31mIncorrect\e[0m'")