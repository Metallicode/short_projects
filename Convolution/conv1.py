import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_stonks():
	df = pd.read_csv('data.csv')
	df = df["Close"]
	return np.array(df)


a=20

#y = [3,7,12,2,13,1,17,5]
y = get_stonks()
flt = np.ones(a)/a

c = np.convolve(y,flt, "same")
print(c)

t=range(0, len(y))

plt.plot(t,y, "black")
plt.plot(t,c, "red")
plt.show()



















