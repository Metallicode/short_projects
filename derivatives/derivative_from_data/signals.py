import pandas as pd
import numpy as np

def get_sin(frq=5, resolution=1000):
	t = np.linspace(0, 1.0, resolution)
	return t, np.sin(t * np.pi * 2 * frq)

def get_saw(frq=5, resolution=100):
	t = np.arange(0,1.0,1.0/resolution)
	x = t * np.pi * 2 * frq
	return t, -((x/np.pi)%2)+1
	
def get_lin(s=3, resolution=100):
	t = np.linspace(0, 1.0, resolution)
	return t, t*s 

def get_stonks():
	df = pd.read_csv('data.csv')
	df = df["Close"]
	return np.array(df.index), np.array(df)
