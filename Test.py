import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

directory = "./poultry_dataset/chicken_dataset/Noise/"
save_directory = "C:/Users/user/Desktop/Spectrogram_Data/Noise/"

# C:\Users\user\Desktop\Spectrogram_Data\Healthy
def load_audio(file_path, sample_rate=44100):
    audio, sr = librosa.load(file_path, sr=sample_rate, mono=False)
    return audio, sr

def calculate_spectrogram(audio, sample_rate):
    mono_audio = librosa.to_mono(audio)
    stft = librosa.stft(mono_audio)
    spectrogram = librosa.amplitude_to_db(np.abs(stft), ref=np.max)
    return spectrogram

def visualize_and_save(audio, sample_rate, file_name):
    spectrogram = calculate_spectrogram(audio, sample_rate)
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 1, 1)
    librosa.display.specshow(spectrogram, sr=sample_rate, x_axis="time", y_axis="log")
    plt.colorbar(format="%+2.0f dB")
    plt.title("Spectrogram")
    plt.tight_layout()
    save_path = os.path.join(save_directory, f"{file_name}.png")
    plt.savefig(save_path)
    plt.close()

if __name__ == "__main__":
    start_index = 1
    end_index = 86
    for i in range(start_index, end_index + 1):
        file_path = f"{directory}{i}.wav"
        audio, sample_rate = load_audio(file_path)
        print(f"Processing audio file: {file_path}")
        visualize_and_save(audio, sample_rate, i)
