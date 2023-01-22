import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

########### Challenge 4 - Random Walk ########
def ran_color():
	
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	colours = (r,g,b)
	return colours

	


for _ in range(200):
	tim.pensize(15)

	ran_angle=random.randint(0,90)
	ran_move=random.randint(0,20)
	tim.forward(ran_move)
	tim.right(ran_angle)
	tim.color(ran_color())
	
	

	