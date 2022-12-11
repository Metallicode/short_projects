import matplotlib.pyplot as plt
import numpy as np

#plot setup
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_ylim([-100,100])
ax.set_xlim([-100,100])

#basic pythagoras equation
def circle(x,r, h=0, k=0):
	return np.sqrt(-((x-h)**2 - r**2))+k

#chatGPT's fix
def circle(x,r, h=0, k=0):
    y = -((x-h)**2 - r**2)
    if y < 0:
        return None
    else:
        return np.sqrt(y)+k

#chatGPT's version
def calc_circumference(x, y, r):
	t = np.linspace(0, 2 * np.pi, r)
	xs = x + r * np.cos(t)
	ys = y + r * np.sin(t)
	return xs, ys

base_radius = 90


t = np.arange(-base_radius, base_radius, 1/360)

plt.scatter(t, circle(t,base_radius))
plt.scatter(t, -circle(t,base_radius))


'''
xv, yv = calc_circumference(0,0, base_radius)
plt.scatter(xv, yv)
'''
plt.show()


















'''
The area of the inscribed circle is pi*r^2 = pi.
The area of the circumscribed circle is 4*pi*r^2 = 4*pi.
The area of the triangle (height 3*r) = 3*sqrt(3)*r^2 = 3*sqrt(3).

'''

