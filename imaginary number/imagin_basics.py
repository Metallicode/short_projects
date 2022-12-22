import numpy as np
import matplotlib.pyplot as plt
import math
import cmath

fig, ax = plt.subplots(figsize=(9,9))

plt.axvline(0, color='black')
plt.axhline(0, color='black')

t = np.arange(-100, 100, 0.1)

def set_plot_limit(x_lim=20, y_lim=10):
	ax.set_ylim([-y_lim,y_lim])
	ax.set_xlim([-x_lim,x_lim])

set_plot_limit()






'''
#Quadratic, Cubic, Quartic functions..

quad =  lambda x: x**2 + x
cube  = lambda x: x**3 + x**2
quart = lambda x: x**4 + x**3 - 8*x**2

#plt.plot(t, quad(t))
#plt.plot(t, cube(t))
#plt.plot(t, quart(t))
'''



#the problem	
'''
x = 1
y = 3.14
z = math.sqrt(-1) #this is the problem
'''

#basic complex arithmetic
'''
jx = 4+7j

print(f"{jx=} is of type {type(jx)}")
print(f"{jx.real=}, {jx.imag=}")

jy = 5+3j
print(f"jx+jy={jx+jy}")
print(f"jx-jy={jx-jy}")
print(f"jx*jy={jx*jy}")
print(f"jx/jy={jx/jy}")
print(f"{jx**2=}")

print(f"{math.pow(jx,2)=}") #math module can't handle it
'''


#cmath
'''
#cmath module

print(cmath.sqrt(-1))
'''


#periodic (repeated cycles)
'''
i = 1j
n = 0
for item in range(100):
	n+=1
	print(i**n)
'''


#Rectangular vs Polar
'''
#Rectangular Coordinates 
ja = -4+3j
set_plot_limit(10,10)

plt.scatter(ja.real, ja.imag)#mark the point



#draw rectangular lines
plt.plot((ja.real,ja.real),(0, ja.imag), linestyle='--', color="gray")
plt.plot((0, ja.real),(ja.imag,ja.imag), linestyle='--', color="gray")


#Polar Coordinates

#drow line from origin to point
plt.plot((0, ja.real),(0,ja.imag), linestyle='--', color="red")

#get polar angle and distance from origin
polar_radial_distance = cmath.polar(ja)[0]
polar_angular_distance = cmath.polar(ja)[1]

angles = np.linspace(0, polar_angular_distance, 100)
arc = 1j**(180/np.pi*angles/90) #calculate convergence of line based on angle given in rad using complex numbers
plt.plot([q.real for q in arc], [q.imag for q in arc])

plt.text(ja.real, ja.imag, f'{polar_radial_distance}')
plt.text(0, 0, f'{polar_angular_distance}')
plt.show()
'''

'''
#use for geometric rotation
set_plot_limit(8, 8)

def rotate(z, degrees):
	return z * 1j**(degrees/90)

#set a basic triangle
irp_01 =  4+0j
irp_02 =  1+3j
irp_03 = -1-2j

tri = plt.Polygon(np.array([[irp_01.real,irp_01.imag],[irp_02.real,irp_02.imag], [irp_03.real,irp_03.imag]] ) , facecolor = 'orange')
ax.add_patch(tri)


#rotate triangle
irp_01 = rotate(irp_01, 180)
irp_02 = rotate(irp_02, 180)
irp_03 = rotate(irp_03, 180)

tri = plt.Polygon(np.array([[irp_01.real,irp_01.imag],[irp_02.real,irp_02.imag], [irp_03.real,irp_03.imag]] ) , facecolor = 'green')
ax.add_patch(tri)


'''



plt.show()

