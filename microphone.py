# File: microphone/microphone.py
import sounddevice as sd
import numpy as np
import wavio

class Microphone:
    def __init__(self, sample_rate=44100):
        self.sample_rate = sample_rate
        self.is_active = False

    def start_recording(self, duration=5):
        try:
            self.is_active = True
            print("Recording started. Speak into the microphone...")

            # Calculate the number of frames based on the sample rate and duration
            num_frames = int(duration * self.sample_rate)

            # Record audio
            audio_data = sd.rec(num_frames, samplerate=self.sample_rate, channels=1, dtype='int16')
            sd.wait()

            print("Recording complete.")
            return audio_data

        except Exception as e:
            print(f"An error occurred during recording: {e}")
            return None

    def stop_recording(self):
        self.is_active = False

    def save_audio(self, audio_data, filename="recorded_audio.wav"):
        try:
            print(f"Saving audio to {filename}...")
            wavio.write(filename, audio_data, self.sample_rate, sampwidth=3)  # 24-bit WAV format
            print("Audio saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving audio: {e}")
