from turtle import Turtle, Screen, colormode
import random

color_list = [(238, 238, 237), (228, 234, 231), (229, 233, 237), (237, 230, 233), (212, 154, 102), (38, 99, 132), (14, 49, 80), (155, 76, 57), (148, 57, 73), (115, 37, 51), (122, 165, 184), (131, 172, 148), (211, 90, 65), (39, 127, 97), (12, 97, 57), (220, 198, 130), (73, 35, 45), (173, 155, 60), (192, 88, 104), (194, 130, 147), (16, 62, 48), (41, 56, 104), (6, 94, 109), (50, 152, 188), (34, 171, 129), (53, 49, 47), (170, 204, 195), (78, 79, 26), (116, 115, 160), (102, 41, 39)] # list of RGB colors extracted from an image (Hirst painting style)

tim = Turtle()
tim.speed(0) # fastest drawing speed
colormode(255) # allow RGB colors (0–255)
tim.penup() # no draw while move
tim.hideturtle() # hide turtle icon for cleaner drawing

# move turtle to starting position (bottom-left corner)
tim.setheading(220)  # rotate 220 degrees
tim.forward(300)  # move 300 steps
tim.setheading(0)  # face east (0 degrees)

number_dots = 100 # total number of dots to draw
for i in range(1, number_dots + 1):
    tim.dot(20, random.choice(color_list))  # draw a dot (size 20)
    tim.forward(50)  # move forward to next dot position

    if i % 10 == 0: # every 10 dots, move up and start a new row
        tim.setheading(90)  # face north
        tim.forward(50)  # move up one row
        tim.setheading(180)  # face west
        tim.forward(500)  # go back to the start of the row (50 * 10)
        tim.setheading(0)  # face east again

screen = Screen()
screen.exitonclick() # screen close only if you click him