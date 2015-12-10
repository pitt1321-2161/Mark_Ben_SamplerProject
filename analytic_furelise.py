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

def build_song(musicfile):
	song_wave=numpy.array([])
	with open(musicfile,'r') as music:
		t = numpy.arange(0,0.2027,1/44100.)
		for line in music:
			line = line.strip()
			if line == '#':
				continue
			if line == '%':
				empty_sample = numpy.zeros(8938)
				song_wave = numpy.append(song_wave, empty_sample)
				continue
			line_notes = line.split(',')
			for note in line_notes:
				note_name = note[:-1]
				note_octave = note[-1]
				if note_octave == '4':
					song_wave = numpy.append(song_wave, window_hanning(create_wave(freqs4[note_name],t)))
				elif note_octave == '5':
					song_wave = numpy.append(song_wave, window_hanning(create_wave(freqs5[note_name],t)))
				elif note_octave == '6':
					song_wave = numpy.append(song_wave, window_hanning(create_wave(freqs6[note_name],t)))


	return song_wave

freqs4 = {
"A":440.,
"A#":466.16,
"B":493.88,
"C":261.63,
"C#":277.18,
"D":293.66,
"D#":311.13,
"E":329.63,
"F":349.23,
"F#":369.99,
"G":391.99,
"G#":415.31
}

freqs5 = {}
freqs6 = {}

note_length = 8938

if __name__ == '__main__':
	for note in freqs4:
		freqs5[note] = 2*freqs4[note]
		freqs6[note] = 4*freqs4[note]
	musicfile = sys.argv[1]
	musicwave = build_song(musicfile)
	data, freqs, bins, im = plt.specgram(musicwave, NFFT=2048, Fs=44100, noverlap=900)
	plt.ylim(0,800)
	plt.title("Spectrogram of analytic_furelise_hanning.wav")
	plt.show()
	waveIO.write_wav_file("analytic_furelise.wav", waveIO.pack(musicwave))