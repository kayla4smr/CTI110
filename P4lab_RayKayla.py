#Kayla Ray
#7/1/26
#P4Lab1
# This program will import turtle and use it to draw a house.




import turtle

wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightblue")    # Set the background color
alex = turtle.Turtle()

alex.pensize(3)            # increase pensize (takes integer)
alex.pencolor("purple")     # set pencolor (takes string)   

alex.right(90)             # Tell alex to turn by 90 degreespy
alex.forward(50)

for i in (1,2,3,):         # Tell alex to move forward by 50 units
    alex.left(90)             # Tell alex to turn by 90 degrees
    alex.forward(50)    

i=0
alex.color("purple","yellow")                # Set the fill color to yellow
alex.begin_fill()                 # Begin filling the triangle with color
while i != 3:
    alex.right(120)             # Tell alex to turn by 120 degrees
    alex.forward(50)          # Complete the second side of a triangle 
   
    i += 1                                             

alex.end_fill()                   # End filling the triangle with color




wn.mainloop()             # Wait for user to close window
