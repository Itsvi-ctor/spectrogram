# Converting audios to spectrograms

- Install the following packages 
```py
pip install librosa --user
pip install matplotlib --user
pip install setuptool
pip install --upgrade --force-reinstall librosa
```
- Mak sure to add python to your path

```py
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
```

- Explanation: This block imports the necessary Python libraries for audio processing and visualization.
  - librosa: A library for audio analysis.
  - librosa.display: A submodule for displaying audio data.
  - matplotlib.pyplot as plt: A library for creating plots and visualizations.
  - numpy as np: A library for numerical operations in Python.

## setting the Audio File Path

```py
file_path = "./poultry_dataset/chicken_dataset/Unhealthy/2.wav"
```

- Explanation: This line defines the file path to the audio file you want to analyze. You can uncomment one of the other paths for different audio files.

## Loading Audio

```py
def load_audio(file_path, sample_rate=44100):
    audio, sr = librosa.load(file_path, sr=sample_rate, mono=False)
    return audio, sr
```

- Explanation: This block defines a function load_audio that takes a file path and an optional sample rate as input and returns the loaded audio data and its sample rate. It uses librosa.load() to load the audio.

## Calculating Spectrogram

```py
def calculate_spectrogram(audio, sample_rate):
    mono_audio = librosa.to_mono(audio)
    stft = librosa.stft(mono_audio)
    spectrogram = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return spectrogram
```

- Explanation: This block defines a function calculate_spectrogram that takes audio data and sample rate as input, converts stereo to mono, computes the Short-Time Fourier Transform (STFT), and converts it to a spectrogram using librosa.amplitude_to_db().

## Visualizing Audio

```py
def visualize_audio(audio, sample_rate):
    spectrogram = calculate_spectrogram(audio, sample_rate)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)
    librosa.display.specshow(spectrogram, sr=sample_rate, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    plt.show()
```

- Explanation: This block defines a function visualize_audio that takes audio data and sample rate, calculates the spectrogram using the previous function, and then plots it using librosa.display.specshow().

## Main Execution

```py
if __name__ == "__main__":
    audio, sample_rate = load_audio(file_path)
    visualize_audio(audio, sample_rate)
```

- Explanation: This block checks if the script is being run as the main program. If so, it loads the audio and visualizes it using the defined functions.
  This script essentially loads an audio file, calculates its spectrogram, and visualizes the spectrogram in a logarithmic scale over time.
