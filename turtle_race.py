from turtle import Turtle, Screen
import random
is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Choose your turtle, Enter a colour :  ")
colors=["purple","blue","green","yellow","orange","red"]
all_turtles=[]

for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=-120+turtle_index*50)
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on=True

while(is_race_on):
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_colour=turtle.pencolor()
            if winning_colour==user_bet:
                print(f"You've won. The winner of the race is {winning_colour} turtle")
            else:
                print(f"You've lost. The winner of the race is {winning_colour} turtle")
        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()
    