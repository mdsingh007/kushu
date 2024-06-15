import pyaudio
import numpy as np

def read_audio():
    # Create a PyAudio object.
    pa = pyaudio.PyAudio()

    # Open a microphone stream.
    # with pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True) as stream:
    stream = pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)
        # Read the audio input.
    data = stream.read(4096)

    # Close the stream.
    stream.close()

    # Return the audio data.
    return data

def convert_audio_to_frequencies(data):
    # Convert the audio data to a NumPy array.
    data = np.frombuffer(data, dtype=np.int32)
    
    # data = np.array(data)
    # data = data.flatten()
    # print(data)
    # waveform = map(ord,list(data))
    # Calculate the Fast Fourier Transform (FFT) of the audio data.
    fft = np.fft.fft(data)

    # Get the frequencies of the FFT.
    frequencies = np.fft.fftfreq(data.shape[0], d=1.0 / 44100)

    # Return the frequencies.
    return frequencies

def find_closest_frequency(frequencies, frequency):
    # Find the index of the closest frequency to the given frequency.
    index = np.argmin(np.abs(frequencies - frequency))

    # Return the frequency at the index.
    return frequencies[index]

def display_frequency(frequency):
    # Display the frequency of the cello.
    print("The frequency of the cello is {} Hz.".format(frequency))

def main():
    # Read the audio input from the microphone.
    data = read_audio()

    # Convert the audio input to frequencies.
    frequencies = convert_audio_to_frequencies(data)

    # Find the closest frequency to the A4 frequency (440 Hz).
    frequency = find_closest_frequency(frequencies, 440)

    # Display the frequency of the cello.
    display_frequency(frequency)


def sample_microphone():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open microphone stream
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=4096)

    # Read data from microphone stream
    data = np.fromstring(stream.read(4096), dtype=np.int16)

    # Close microphone stream
    stream.stop_stream()
    stream.close()

    # Terminate PyAudio
    p.terminate()

    # Compute FFT of audio data
    fft = np.fft.fft(data)

    # Compute frequencies corresponding to FFT bins
    frequencies = np.fft.fftfreq(len(fft), d=1/44100)
    print (frequencies)

    # Find dominant frequency
    max_index = np.argmax(np.abs(fft))
    dominant_frequency = frequencies[max_index]

    # Print dominant frequency
    print("Dominant frequency: {:.2f} Hz".format(dominant_frequency))


if __name__ == "__main__":
    # main()
    sample_microphone()