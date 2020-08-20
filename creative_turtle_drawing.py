import turtle
wn=turtle.Screen()          # Asking for the graphics screen

wn.bgcolor("lightgreen")    # For background Color
# A beautiful thing is that this color written in the bracket is not "case-sensitive"

robort_1=turtle.Turtle()    # Robort 1 is created to apply commands on it, its a turtle object
robort_1.pensize(5)         # pen sie can be varied
robort_1.shape("turtle")    # Shape of the robort changed

obort_1.forward(150)       # Robort 1 taking action
robort_1.left(90)

wn.exitonclick()           # To retain the sreen till we click on it
