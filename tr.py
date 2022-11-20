import turtle as t
t.speed(7)
t.pensize(2)

R=200

st = 3
segments=5

'''
for i in range(segments//st):
	t.circle(R, steps=st)
	t.pu()
	t.circle(R, 360/segments)
	t.pd()
'''

for i in range(segments):
	t.circle(R, 360/segments)
	t.circle(5)

#t.circle(R, 360/segments)
#t.circle(R, steps=3)
input()
