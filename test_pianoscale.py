import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO

sr = 44100

wave_data = waveIO.read_wav_file('c4scale.wav')
wave_data = waveIO.unpack(wave_data)

data, freqs, bins, im = plt.specgram(wave_data, NFFT=1024, Fs=sr, noverlap=900)
plt.ylim(0,2000)
plt.show()

plt.plot(wave_data)
plt.show()