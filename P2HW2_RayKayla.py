# Kayla Ray
# 6/19/2026
# P2HW2
# This program will ask the user to enter grades for six modules, stores them in a list,
# and displays the lowest grade, highest grade, sum of the grades, and the average grade.

from inspect import _empty


...
#pseudocode
#start
#create an empty list named module_grades
#add module 1 grade to list
#ask user to enter grade for module 2
#add module 2 grade to list
#ask user to enter grade for module 3
#add module 3 grade to list
#ask user to enter grade for module 4
#add module 4 grade to list
#ask user to enter grade for module 5
#add module 5 grade to list
#ask user to enter grade for module 6
#add module 6 grade to list
#find the lowest grade in the list
#find the highest grade in the list
#find the sum of the grades in the list
#find the average grade of the grades
#display the results to the user
#end 
print()

Module_grades = []
Grade1 = float(input("Enter grade for module 1: "))
Module_grades.append(Grade1)


Grade2 = float(input("Enter grade for module 2: "))
Module_grades.append(Grade2)

Grade3 = float(input("Enter grade for module 3: "))
Module_grades.append(Grade3)

Grade4 = float(input("Enter grade for module 4: "))
Module_grades.append(Grade4)

Grade5 = float(input("Enter grade for module 5: "))
Module_grades.append(Grade5)

Grade6 = float(input("Enter grade for module 6: "))
Module_grades.append(Grade6)
print()
lowest_grade = min(Module_grades)
highest_grade = max(Module_grades)
sum_of_grades = sum(Module_grades)
average_grade = sum_of_grades / len(Module_grades)
print()
print("------------RESULTS------------")
print(f"Lowest grade:   {lowest_grade}")
print(f"Highest grade:  {highest_grade}")
print(f"Sum of grades:  {sum_of_grades}")
print(f"Average grade:  {average_grade:.2f}")
print("-------------------------------")