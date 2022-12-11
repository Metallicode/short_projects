import matplotlib.pyplot as plt
import numpy as np

#plot setup
fig, ax = plt.subplots()
ax.set_ylim([-1.2,1.2])
ax.set_xlim([-1.2,1.2])

#transform running numbers into a direction
def get_direction(d):
	d*=(np.pi / 180.)
	return np.cos(d), np.sin(d) 

base_radius = 1

'''
x, y = get_direction(190)
t = np.arange(0, 1.0, 1/100)

#show line pointing at direction
xv = x*t
yv = y*t

plt.plot(xv, yv)

plt.show()
'''


t = np.arange(0, 1.0, 1/360)

for i in range(len(t)):
	x, y = get_direction(i*6)
	plt.scatter(x*t[i], y*t[i])

plt.show()


