import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# file_path = "./poultry_dataset/chicken_dataset/Healthy/2.wav"
# file_path = "./poultry_dataset/chicken_dataset/Noise/1.wav"
file_path = "./poultry_dataset/chicken_dataset/Unhealthy/2.wav"

def load_audio(file_path, sample_rate=44100):
    audio, sr = librosa.load(file_path, sr=sample_rate, mono=False)
    return audio, sr

def calculate_spectrogram(audio, sample_rate):
    # Convert stereo to mono
    mono_audio = librosa.to_mono(audio)
    # Compute the spectrogram
    stft = librosa.stft(mono_audio)
    spectrogram = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return spectrogram

def visualize_audio(audio, sample_rate):
    spectrogram = calculate_spectrogram(audio, sample_rate)
    # Plot the spectrogram
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)  # Adjusted subplot parameters
    librosa.display.specshow(spectrogram, sr=sample_rate, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    audio, sample_rate = load_audio(file_path)
    visualize_audio(audio, sample_rate)
