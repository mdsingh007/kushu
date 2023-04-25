import pyaudio
import numpy as np

def read_audio():
    # Create a PyAudio object.
    pa = pyaudio.PyAudio()

    # Open a microphone stream.
    with pa.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True) as stream:
        # Read the audio input.
        data = stream.read(4096)

    # Close the stream.
    stream.close()

    # Return the audio data.
    return data

def convert_audio_to_frequencies(data):
    # Convert the audio data to a NumPy array.
    data = np.array(data)

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

if __name__ == "__main__":
    main()