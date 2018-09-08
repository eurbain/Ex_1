from turtle import * 
a = 0
forward(120)
left(90)
color('red')
forward(80)
while a <120:
        a = a +1
        if ( a % 3 == 0):
            color('blue')
        elif (a % 7 == 0):
            color("yellow")
        else:
            color("red")

        forward(150)
        left(150)