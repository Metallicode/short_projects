import turtle as t
t.speed(9)
t.pensize(2)
R=200
points = {}
s = 9

#move starting point
t.pu()
t.right(90) 
t.forward(40) 
t.left(90)
t.pd()

#draw base circle
t.circle(R)
#go to circle top
t.pu()
t.circle(R,extent = 180)
t.pd()
#draw base polygon
#t.circle(R, steps=s)

#save points
t.pu()

pos = {1:"left", 2:"left", 3:"left", 8:"right", 7:"right", 6:"right", 9:"center", 4:"center", 5:"center"}

for i in range(s, 0, -1):
	t.write(i,font=("Arial", 15), align=pos[i])
	points[i] = t.pos()
	t.circle(R, 360/s)
s
t.goto(points[1])
t.pd()

#draw vortex
t.pencolor("red")
t.pensize(5)

#vg = [1, 2, 4, 8, 7, 5, 1]

'''
from vortex_generator import VortexGenerator

vg = VortexGenerator(length=100, base=s+1, n=2)

for i in vg:
	t.goto(points[int(i)])
'''


#primes

from prime_generator import PrimeGenerator
pg = PrimeGenerator(length=200)
for i in pg:
	t.goto(points[int(i)])
	

print(len(points))
print(points)

input()
