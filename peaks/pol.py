import matplotlib.pyplot as plt
import numpy as np

def f():
	t = np.arange(0, np.pi*2, 1/1000)
	return t, t**2*(1+np.sin(t*np.sin(t*3* np.sin(np.sin(t/4)))))
	
if __name__ == "__main__":
	x, y = f()
	plt.plot(x,y)
	plt.show()
