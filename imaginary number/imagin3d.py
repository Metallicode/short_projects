import numpy as np
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')
ax.set_proj_type('ortho')

#basic 3d wave
f=50
t = np.arange(0, 1, 1/1000) 	#time
r = np.arange(1, 0, -1/1000)**2 #amplitude 

z = np.e**(2*np.pi*(1j*t*f))*r #calc the function

ax.plot(t,np.real(z),np.imag(z))
plt.show()
