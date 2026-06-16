# Kayla Ray
# 6/16/2026
# P2HW1
# This program caluculates and displays travel expenses

# Get users budget
budget = float(input("Enter your budget: "))

print()

# Get users destination
destination = input("Enter your travel destination: ")  

print()

# Get users estimated cost of gas
gas_cost = float(input("Enter your estimated cost of gas: "))

print()

# Get users estimated cost of accomodations/hotel
accomodations_cost = float(input("Enter your estimated cost of accomodations/hotel: ")) 

print()

# Get users estimated cost of food
food_cost = float(input("Enter your estimated cost of food: "))

print()
location = "Location:"
Budget = "Initial Budget:"
Gas = "Gas:"
Accommodations = "Accomodations:"
Food = "Food:"

print("------Travel expenses------")
print(f"{location:20} {destination}")
print(f"{Budget:20} ${budget:.2f}")
print(f"{Gas:20} ${gas_cost:.2f}")
print(f"{Accommodations:20} ${accomodations_cost:.2f}")
print(f"{Food:20} ${food_cost:.2f}")
print("----------------------------")
print()

# remaining Balance
remaining_balance = budget - (gas_cost + accomodations_cost + food_cost)
print(f"Remaining balance: ${remaining_balance:.2f}")

