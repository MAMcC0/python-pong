from turtle import Screen
from paddle import Paddle



screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong with Python")
screen.tracer(0)

rpaddle = Paddle((375, 0))
lpaddle = Paddle((-375, 0))




screen.listen()
screen.onkey(rpaddle.move_up, "Up")
screen.onkey(rpaddle.move_down, "Down")



game_on = True

while game_on:
    screen.update










screen.exitonclick()