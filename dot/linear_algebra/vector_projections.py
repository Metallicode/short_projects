import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches
from random import randint

def rotate(origin, point, angle):
	ox, oy = origin
	px, py = point[0]-ox, point[1]-oy
	s = np.sin(angle)
	c = np.cos(angle)
	qx = ox + c * (px - ox) - s * (py - oy)
	qy = oy + s * (px - ox) + c * (py - oy)
	return qx, qy

def init_plot():
	ax.clear()
	ax.set_ylim([-xy_lim,xy_lim])
	ax.set_xlim([-xy_lim,xy_lim])
	
def plot_vectors(va, vb):
	v_a = np.array([origin, va])# [[0,0], [1,2]]
	v_b = np.array([origin, vb])# [[0,0], [1,2]]
	plt.plot(v_a.T[0], v_a.T[1])
	plt.plot(v_b.T[0], v_b.T[1])
	plt.scatter(*va)
	plt.scatter(*vb)
	
	

#set plot style
xy_lim = 5
fig, ax = plt.subplots(figsize=(9,9))
init_plot()

#add axis lines
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')

#origin point
origin = np.array([0,0])

#arbitrary points
a = np.array([randint(-xy_lim, xy_lim),randint(-xy_lim, xy_lim)])
b = np.array([randint(-xy_lim, xy_lim),randint(-xy_lim, xy_lim)])

x_axis = np.array([1,0])

plot_vectors(a, b)

###########################################################################


#calc vector magnitude
a_mag = np.sqrt(((a[0]-origin[0])**2)+((a[1]-origin[1])**2))
b_mag = np.sqrt(((b[0]-origin[0])**2)+((b[1]-origin[1])**2))

#vector magnitude
print(f"a magnitude {a_mag}")
print(f"b magnitude {b_mag}")

#calc the vectors dot product
ab_dot = np.dot(a, b)
print(f"dot product {np.dot(a, b)}")

#calc angle between vectors
ab_theta_rad = np.arccos(ab_dot/(np.abs(a_mag)*np.abs(b_mag)))

#angle between vectors
print(f"ab theta (in radians) {ab_theta_rad}")
print(f"ab theta (in degrees) {(180/np.pi)*ab_theta_rad}")



###########################################################################


#plot animation 
def animate(i):
	
	init_plot() #clear the plot
	a = np.array([np.sin(0.05 *i),np.cos(0.05 *i)])*1 #calc vector a new direcion 
	plot_vectors(a, b) #plot the vectors
	
	#calu the dot product
	dot = np.dot(a, b) #calculate the dot product
	theta = np.arccos(np.dot(b,x_axis)/b_mag) #calculate the angle between x axis to b
	theta = (np.pi/2)+theta if b[1] > 0 else (np.pi/2)-theta  #set angle perpendicular to b 
	plt.scatter(*rotate(tuple(origin),(dot, 0), theta)) #rotate the dot vector with theta
	
	#calc vector a projection on b (|a|cos θ)	
	a_mag = np.sqrt(((a[0]-origin[0])**2)+((a[1]-origin[1])**2)) #magnitude of a
	ab_theta_rad = np.arccos(dot/(np.abs(a_mag)*np.abs(b_mag))) #angle between vectors
	projection = a_mag*np.cos(ab_theta_rad) #calc vector a projection on b
	theta =  (np.pi/2)+theta #set theta
	plt.scatter(*rotate(tuple(origin),(-projection, 0), theta)) #rotate b direction and plot	
	#print(f"{a} {dot}")

ani = FuncAnimation(fig, animate, interval=50)
plt.show()

