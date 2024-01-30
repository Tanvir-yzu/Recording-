# File: text.py
from microphone import Microphone

def main():
    try:
        # Create an instance of the Microphone class
        microphone_instance = Microphone()

        # Use the microphone_instance for recording (10 seconds in this example)
        audio_data = microphone_instance.start_recording(duration=10)

        if audio_data is not None:
            # Save the recorded audio to a file
            microphone_instance.save_audio(audio_data, filename="recorded_audio.wav")

        # Stop recording
        microphone_instance.stop_recording()

        print("Microphone instance created successfully.")

    except ImportError as e:
        print(f"ImportError: {e}")
        print("Please make sure the required modules are installed.")

    except Exception as ex:
        print(f"An error occurred: {ex}")

if __name__ == "__main__":
    main()
