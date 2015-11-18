import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO
#import pyaudio

def create_wave(freq,t):
    return 5000 * numpy.cos(freq * 2 * numpy.pi * t)

sr = 44100.
dt = 1 / sr
NFFT = 1024
fs = 1.0/dt
t = numpy.arange(0,2,dt)
t_sin=create_wave(440, t)
third_sin=create_wave(440 * 2**(4/12.), t)
fifth_sin=create_wave(440 * 2**(7/12.), t)

chord_sin = t_sin + third_sin + fifth_sin

t_sin = numpy.append(t_sin, third_sin)
t_sin = numpy.append(t_sin, fifth_sin)
t_sin = numpy.append(t_sin, chord_sin)

data, freqs, bins, im = plt.specgram(t_sin, NFFT=NFFT, Fs=fs, noverlap=900)
plt.ylim(0,2000)
plt.show()
#print(data)
waveIO.write_wav_file("samplewave.wav", waveIO.pack(t_sin))
