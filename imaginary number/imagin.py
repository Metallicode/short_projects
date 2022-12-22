import numpy as np
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(9,9))
xy_lim = 2

#clear plot
def init_plot(x):
	ax.clear()
	ax.set_ylim([-xy_lim,xy_lim])
	ax.set_xlim([-xy_lim,xy_lim])
	plt.grid(alpha=.5)
	return x/10


def animate(x , n=5):
	x = init_plot(x)
	z = np.e**(2*np.pi*1j*x/n) #this will calculate the rotation
	plt.plot([0,np.imag(z)],[0,np.real(z)], linewidth=3)
	print(f"{x=}, imag: {np.imag(z)}\t real: {np.real(z)}")
	

#run animation
ani = FuncAnimation(fig, animate, interval=50)
plt.show()
