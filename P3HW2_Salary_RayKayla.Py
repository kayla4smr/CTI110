# Kayla Ray
# 6/27/2026
# P3HW3
# The code will display the number of hours worked, pay rate, and gross pay for an employee.

# Ask the user to enter name of the employee
name = input("Enter the name of the employee: ")

# Ask the user to enter the number of hours worked this week
hours_worked = float(input("Enter the number of hours worked this week: "))


# Ask the user to enter the employee's pay rate 
pay_rate = float(input("Enter the employee's pay rate: "))

# If the employee worked more than 40 hours, calculate the overtime pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    overtime_pay = 0
    overtime_hours = 0

#

#Calculate the regular pay
regular_pay = (hours_worked - overtime_hours) * pay_rate  
# Calculate the gross pay
gross_pay = regular_pay + overtime_pay


# Display the results
print("-----------------------------------------")
print(f"Employee Name: {name}")
print()
print("Hours Worked    Pay Rate    OverTime    Overtime Pay    Regular Pay    Gross Pay")
print("------------------------------------------------------------------------------------------")
print(f"{hours_worked:<16.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}{overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:<15.2f}")
    