import wave
import numpy

# The following are correct for the file I provided.
# For other files, investigate how to the info using the wave module.
SAMPLE_WIDTH = 2    # 16-bit = 2 bytes
N_CHANNELS = 1      # 1=mono,2=stereo
SAMPLE_RATE = 44100 # Hz, 
    

def read_wav_file(name):
    """
    This function reads a WAV file named 'name' and returns
    the contents as a packed string.
    """

    # Open wave file for reading
    w = wave.open(name, 'rb')

    # Read the entire wave file as a raw string.
    # Caution, this could use a lot of memory!
    # If worried, modify this 
    rawdata = w.readframes(w.getnframes())
    
    return rawdata
    


def unpack(data):
    """
    This function extracts a raw byte string into an array of
    16-bit integers.
    """
    import audioop

    undata = numpy.empty(len(data)/2, dtype=numpy.int16)
    for i in xrange(0, len(data)/SAMPLE_WIDTH):
        undata[i] = audioop.getsample(data,SAMPLE_WIDTH,i)

    return undata

def pack(data):
    """
    Pack a list of wav samples back into a string for audio
    output. This function returns the raw data as a string.
    """
    from io import StringIO
    import cStringIO
    import struct
    
    sio = cStringIO.StringIO() # For storing packed string

    for d in data:
        sio.write(struct.pack('h',d))

    return sio.getvalue()

def write_wav_file(name,data):
    """
    Save the packed string in 'data' as a wave file
    with name given by string 'name'.
    """
    w = wave.open(name, 'wb')
    w.setnchannels(N_CHANNELS)
    w.setsampwidth(SAMPLE_WIDTH)
    w.setframerate(SAMPLE_RATE)
    w.setnframes(len(data)/SAMPLE_WIDTH) 
    w.writeframesraw(data)
    w.close()
 
def play(data):
    """
    Play data (either packed or unpacked) using pyaudio.
    """
    import pyaudio
    p = pyaudio.PyAudio()

    # open stream
    stream = p.open(format = pyaudio.paInt16,   
                    channels = N_CHANNELS,
                    rate = SAMPLE_RATE,
                    output = True)
    stream.write(data)
    stream.close()
    p.terminate()
