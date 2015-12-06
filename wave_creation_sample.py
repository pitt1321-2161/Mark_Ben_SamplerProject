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


##############
# Now build a universal sample, with short sections for each note through a few octaves
t = numpy.arange(0, 0.5, dt)
big_sample = create_wave(440, t)
big_sample = numpy.append(big_sample, create_wave(466.16, t))
big_sample = numpy.append(big_sample, create_wave(493, t))
big_sample = numpy.append(big_sample, create_wave(523, t))
big_sample = numpy.append(big_sample, create_wave(554, t))
big_sample = numpy.append(big_sample, create_wave(587, t))
big_sample = numpy.append(big_sample, create_wave(622, t))
big_sample = numpy.append(big_sample, create_wave(659, t))
big_sample = numpy.append(big_sample, create_wave(698, t))
big_sample = numpy.append(big_sample, create_wave(739, t))
big_sample = numpy.append(big_sample, create_wave(783, t))
big_sample = numpy.append(big_sample, create_wave(830, t))
big_sample = numpy.append(big_sample, create_wave(880, t))
big_sample = numpy.append(big_sample, create_wave(932, t))
big_sample = numpy.append(big_sample, create_wave(987, t))
big_sample = numpy.append(big_sample, create_wave(1046, t))
big_sample = numpy.append(big_sample, create_wave(1108, t))
big_sample = numpy.append(big_sample, create_wave(1174, t))
big_sample = numpy.append(big_sample, create_wave(1244, t))
big_sample = numpy.append(big_sample, create_wave(1318, t))
big_sample = numpy.append(big_sample, create_wave(1396, t))
big_sample = numpy.append(big_sample, create_wave(1479, t))
big_sample = numpy.append(big_sample, create_wave(1567, t))
big_sample = numpy.append(big_sample, create_wave(1661, t))
waveIO.write_wav_file("bigsample.wav", waveIO.pack(big_sample))