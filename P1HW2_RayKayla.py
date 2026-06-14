# Kayla Ray
# 6/12/26
# Travel Expense 
# This program calculates the total travel expenses.

# Pseudocode:
# Ask the user to enter their budget for the trip
budget = float(input("Enter your budget for the trip: "))
# Ask the user to enter the destination
destination = input("Enter your destination: ")
# Ask user for amount they will spend on gas
gas = float(input("Enter the amount you will spend on gas: "))
# Ask user for amount they will spend on accommodation
accommodation = float(input("Enter the amount you will spend on accommodation: "))
# Ask user for amount they will spend on food
food = float(input("Enter the amount you will spend on food: "))
# add expenses
total_expenses = gas + accommodation + food
# subtract expenses from budget
remaining_budget = budget - total_expenses


print("----------Travel Expenses----------")
print("Destination: ", destination)
print("Budget: $", format(budget, ".2f"))
print("Gas: $", format(gas, ".2f"))
print("Accommodation: $", format(accommodation, ".2f"))
print("Food: $", format(food, ".2f"))
print("remaining budget: $", format(remaining_budget, ".2f"))
