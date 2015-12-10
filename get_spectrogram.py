import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO

musicwave = waveIO.read_wav_file("furelise_hanning_4500_895.wav")
musicwave = waveIO.unpack(musicwave)
data, freqs, bins, im = plt.specgram(musicwave, NFFT=2048, Fs=44100, noverlap=900)
plt.ylim(0,800)
plt.title("Spectrogram of furelise_hanning_8939_895.wav with hanning sample")
plt.show()