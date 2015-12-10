import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO

musicwave = waveIO.read_wav_file(sys.argv[1])
musicwave = waveIO.unpack(musicwave)
data, freqs, bins, im = plt.specgram(musicwave, NFFT=2048, Fs=44100, noverlap=900)
plt.ylim(0,800)
plt.title("Spectrogram of {!s}".format(sys.argv[1]))
plt.show()