from cmath import pi, exp

def discrete_fourier_transform(x, k):
	omega = 2 * pi * k / (N := len(x))
	return sum(x[n] * exp(-1j * omega * n) for n in range(N))
	
import matplotlib.pyplot as plt

def plot_frequency_spectrum(samples,samples_per_second,min_frequency=0,max_frequency=None):
	num_bins = len(samples) // 2
	nyquist_frequency = samples_per_second // 2
	magnitudes = []
	for k in range(num_bins):
		magnitudes.append(abs(discrete_fourier_transform(samples, k)))
				
	# Normalize magnitudes
	magnitudes = [m / max(magnitudes) for m in magnitudes]
	
	# Calculate frequency bins
	bin_resolution = samples_per_second / len(samples)
	frequency_bins = [k * bin_resolution for k in range(num_bins)]
	
	plt.xlim(min_frequency, max_frequency or nyquist_frequency)
	plt.bar(frequency_bins, magnitudes, width=bin_resolution)
