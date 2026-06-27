# Kayla Ray
# 6/21/2026
# This program takes a money amount and displays the lowest dollars and coins needed.



money = float(input("Enter the amount of money as a float with two decimal places:  $ "))

# convert money to cents
cents = int(money * 100)
# calculate dollars 
dollars = cents // 100
cents = cents - (dollars * 100)
# calculate quarters
quarters = cents // 25
cents = cents - (quarters * 25)
# calculate dimes
dimes = cents // 10
cents = cents - (dimes * 10)
# calculate nickels
nickels = cents // 5
cents = cents - (nickels * 5)
# calculate pennies
pennies = cents
 # Display the results
if dollars == 1:
     print("Dollar: 1")
elif dollars > 1:
     print(f"Dollars: {dollars}")

if quarters == 1:
     print("Quarter: 1")
elif quarters > 1:
     print(f"Quarters: {quarters}")

if dimes == 1:
     print("Dime: 1")
elif dimes > 1:
     print(f"Dimes: {dimes}")

if nickels == 1:
     print("Nickel: 1")
elif nickels > 1:
     print(f"Nickels: {nickels}")

if pennies == 1:
     print("Penny: 1")
elif pennies > 1:
     print(f"Pennies: {pennies}")

if money == 0:
        print("No change needed.")
