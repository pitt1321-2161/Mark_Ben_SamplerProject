import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO

def create_wave(freq,t):
    return 5000 * numpy.cos(freq * 2 * numpy.pi * t)

def window_hanning(wave_window):
	#get the values of a hanning curve. The wave window will be multiplied by these values
	hanning_multipliers = numpy.hanning(len(wave_window))
	result=[]
	for i in range(len(wave_window)):
		result.append(wave_window[i]*hanning_multipliers[i])
	return result

def fft(x):
	X = numpy.zeros(len(x))
	for k in range(len(x)):
		sum_=0
		for n in range(len(x)):
			x_n = x[n]
			i = numpy.array([0+1j])[0]
			sum_ += x_n * numpy.exp(-1 * i * 2 * numpy.pi * k * (n/len(x)))
		X[k] = sum_
	return X

t = numpy.arange(0,1,1/44100.)
sample_wave = create_wave(440,t)

sample_chunk = sample_wave[0:3938]
sample_chunk_hanning = window_hanning(sample_chunk)
sample_chunk_fft = numpy.fft.fft(sample_chunk_hanning)

sample_chunk_experimental_fft = fft(sample_chunk_hanning)

#print(sample_chunk_experimental_fft)
plt.plot(sample_chunk_experimental_fft, 'r', label='using my fft function')
plt.title("fft using my fft function")
plt.show()

plt.plot(sample_chunk_fft, 'b')
plt.title("fft using numpy.fft.fft")
plt.show()