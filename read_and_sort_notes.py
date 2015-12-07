#UPDATED FREQUENCIES


import numpy
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import waveIO
import random

sr = 44100.

bpm = 148
dt=0.5

threshold = 525

# This dict holds the "ideal" values for each note in the Fourth octave.
# A wave will be said to correspond to a given note if its frequency is within 1%
# of the ideal values in this table, multiplied appropriately to give the frequency for the correct octave
note_freqs = {
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

#This will hold all our chopped up notes
# Each note consists of a list containing 5 sublists
# Each of those 5 sublists corresponds to an octave 1-5
# Octave 1 is the first element of the list, Octave 6 the sixth
# For example, notes_db["C"][2] will be a list of all wave chunks whose dominant frequency
# corresponds to a C3 note, that is, a C in the 3rd octave
notes_db = {
"A": [[],[],[],[],[],[]],
"A#": [[],[],[],[],[],[]],
"B": [[],[],[],[],[],[]],
"C": [[],[],[],[],[],[]],
"C#": [[],[],[],[],[],[]],
"D": [[],[],[],[],[],[]],
"D#": [[],[],[],[],[],[]],
"E": [[],[],[],[],[],[]],
"F": [[],[],[],[],[],[]],
"F#": [[],[],[],[],[],[]],
"G": [[],[],[],[],[],[]],
"G#":[[],[],[],[],[],[]]
}


all_notes=[]

# Use a given tempo to determine the correct length of time for each chunk of wave
def compute_dt(bpm):
	#assuming dt is for an eighth note
	bps = bpm/60.
	spb = 1./bps
	dt = spb/2.
	return dt

# Split a long wave into chunks of note_size size
# note size is given in terms of list elements, so it must be computed beforehand
def split_wave(wave, note_size):
	chunks=[]
	for i in range(0, len(wave), note_size):
		chunks.append(wave[i:i+note_size])
	return chunks

#places a wave chunk in the correct bin
def store_note(chunk):
	octave_multiplier = 1

	w = numpy.fft.rfft(chunk) / (len(chunk))

	freqs = numpy.fft.fftfreq(len(w))
	idx = numpy.argmax(numpy.abs(w))
	frequency = freqs[idx] * (sr/2)

	#If the loudest frequency is greater than the threshold, store this chunk's index in the appropriate note bin
	# repeat for the next loudest frequency and so on until the frequencies are no longer louder than the threshold
	while numpy.abs(w[idx]) > threshold and 27.5 <= frequency <= 4187:
		#determine what octave then note is in
		# Doubling a frequency increases the note's octave by 1
		# Thus, if the frequency is outside the default range, simply half or double each bin value to figure out what note it is
		while frequency < (note_freqs["C"] * octave_multiplier)*0.99:
			octave_multiplier = octave_multiplier/2.
		while frequency > (note_freqs["B"] * octave_multiplier)*1.01:
			octave_multiplier = octave_multiplier*2

		# store the note in the list of all stored chunk, and get its index within that list
		all_notes.append(chunk)
		note_index = len(all_notes) - 1

		# iterate over each note in the scale, testing the chunk frequency
		# If the chunk frequency is within 1% of the note's frequency for a given octave,
		# place the chunk's index into that octave's bin within the corresponding note bin
		# By storing indices rather than whole chunks here, we can avoid having to store multiple copies of chunks which
		# represent chords
		for note,note_frequency in note_freqs.iteritems():
			octave_frequency = note_frequency * octave_multiplier
			if octave_frequency * 0.99 <= frequency <= octave_frequency*1.01:
				if octave_multiplier==0.125 and note_index not in notes_db[note][0]:
					notes_db[note][0].append(note_index)
					#return [w, freqs]
				elif octave_multiplier==0.25 and note_index not in notes_db[note][1]:
					notes_db[note][1].append(note_index)
					#return [w, freqs]
				elif octave_multiplier==0.5 and note_index not in notes_db[note][2]:
					notes_db[note][2].append(note_index)
					#return [w,freqs]
				elif octave_multiplier==1 and note_index not in notes_db[note][3]:
					notes_db[note][3].append(note_index)
					#return [w, freqs]
				elif octave_multiplier==2 and note_index not in notes_db[note][4]:
					notes_db[note][4].append(note_index)
					#return [w, freqs]
				elif octave_multiplier==4 and note_index not in notes_db[note][5]:
					notes_db[note][5].append(note_index)
					#return [w, freqs]

		#delete this frequency and its data from w and freqs, then compute a new idx and frequency
		w = numpy.delete(w,idx)
		freqs = numpy.delete(freqs,idx)
		idx = numpy.argmax(numpy.abs(w))
		frequency = freqs[idx] * (sr/2)



	
def print_notes():
	for i in range(6):
		note="C"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="C#"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="D"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="D#"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="E"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="F"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="F#"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="G"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="G#"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="A"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="A#"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		note="B"
		print("{!s}{!s}: {!s}".format(note, i+1, len(notes_db[note][i])))
		


# Tests the sample wave I created in a different function. The first quarter of the file is just a ~440hz sin
# The second quarter is a roughly 554hz sin wave
# The third quarter is a roughly 659hz sin wave
def test_sample_wave(chunks):
	for i in range(len(chunks)/4):
		chunk = chunks[i]

		w = numpy.fft.rfft(chunk)
		freqs = numpy.fft.fftfreq(len(w))
		idx = numpy.argmax(numpy.abs(w))
		frequency = freqs[idx] * (sr/2)

		numpy.testing.assert_allclose(frequency, note_freqs["A"], rtol=0.01)
	for i in range(len(chunks)/4,len(chunks)/2):
		chunk = chunks[i]

		w = numpy.fft.rfft(chunk)
		freqs = numpy.fft.fftfreq(len(w))
		idx = numpy.argmax(numpy.abs(w))
		frequency = freqs[idx] * (sr/2)

		numpy.testing.assert_allclose(frequency, note_freqs["C#"], rtol=0.01)
	for i in range(len(chunks)/2,3*len(chunks)/4):
		chunk = chunks[i]

		w = numpy.fft.rfft(chunk)
		freqs = numpy.fft.fftfreq(len(w))
		idx = numpy.argmax(numpy.abs(w))
		frequency = freqs[idx] * (sr/2)

		numpy.testing.assert_allclose(frequency, note_freqs["E"], rtol=0.01)
	print("Tests passed for sample wave!")

def build_song(musicfile, dt):
	note_time = numpy.arange(0,dt, 1/sr)
	song_wave=numpy.array([])
	with open(musicfile,'r') as music:
		for line in music:
			line = line.strip()
			if line == '#':
				continue
			if line == '%':
				empty_sample = numpy.zeros((dt * sr) - 1)
				song_wave = numpy.append(song_wave, empty_sample)
				continue
			line_notes = line.split(',')
			for note in line_notes:
				note_name = note[:-1]
				note_octave = note[-1]

				note_sample_bin = notes_db[note_name][int(note_octave) - 1]
				note_sample_index = random.choice(note_sample_bin)
				note_sample = all_notes[note_sample_index]

				song_wave = numpy.append(song_wave, note_sample)
				song_wave = numpy.append(song_wave, note_sample[::-1])
				song_wave = numpy.append(song_wave, note_sample)

	return song_wave


if __name__ == '__main__':
	global dt
	# figure out the correct dt length based on the tempo of the output wave you want
	dt = compute_dt(bpm)
	# read and parse each sample wave
	for i in range(1, len(sys.argv) - 2):
		#read in the wave file and unpack its data
		wave_data = waveIO.read_wav_file(sys.argv[i])
		wave_data = waveIO.unpack(wave_data)
		wave_time = len(wave_data)/sr

		note_length = dt * sr

		wave_chunks = split_wave(wave_data, int(note_length))
		print(len(wave_chunks))

		#test_sample_wave(wave_chunks)

		for i in range(len(wave_chunks)):
			chunk = wave_chunks[i]
			if len(chunk) != int(note_length):
				continue

			store_note(chunk)
	print_notes()
	# read and parse the music file
	musicfile = sys.argv[-2]
	song = build_song(musicfile, dt)
	waveIO.write_wav_file(sys.argv[-1], waveIO.pack(song))

	