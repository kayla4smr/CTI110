# Kayla Ray 
# 06/16/2026
# P2LAB2

# This program uses dictionary to store cars and their MPG, then calculates the average MPG and prints the cars with above average MPG.

# Create a dictionary to store car models and their MPG
cars = {
    "Camaro" : 18.21,
    'Prius' : 52.36,
    'Model S' : 110,
    'Silverado' : 26,

}
# Store and print all keys
Keys = cars.keys()
print (list(Keys))

# Ask the user to enter car
car = input("Enter a car model: ")

print()

# Display the MPG of the entered car model
Mpg = cars.get(car)
print(f"The MPG of {car} is {Mpg}.")

print()

# Ask user how many miles they will be driving
miles = float(input(f"How many miles will you be driving? {car}"))  

print()


# caulate the gallons of fuel needed for the trip
gallons_needed = miles / Mpg

# Display the gallons of fuel needed, rounded to 2 decimal places
print(f"You will need {gallons_needed:.2f} gallons of fuel for your trip in the {car}.")

