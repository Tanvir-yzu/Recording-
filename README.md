 # Microphone: A Python Module for Audio Recording

## Introduction

The `microphone` module provides a simple and easy-to-use interface for recording audio from a microphone. It is built on top of the `sounddevice` library, which provides a cross-platform API for audio I/O.

## Installation

To install the `microphone` module, simply run the following command in your terminal:

```
pip install microphone
```

## Usage

To use the `microphone` module, first create a `Microphone` object. You can specify the sample rate (in Hz) as an optional argument to the constructor. The default sample rate is 44100 Hz.

```python
import microphone

# Create a Microphone object with a sample rate of 44100 Hz
mic = microphone.Microphone()
```

Once you have created a `Microphone` object, you can start recording audio by calling the `start_recording()` method. You can specify the duration of the recording (in seconds) as an optional argument to this method. The default duration is 5 seconds.

```python
# Start recording audio for 5 seconds
audio_data = mic.start_recording()
```

The `start_recording()` method returns a NumPy array containing the recorded audio data. This array is a one-dimensional array of 16-bit signed integers, representing the audio samples.

After you have finished recording audio, you can stop the recording by calling the `stop_recording()` method.

```python
# Stop recording audio
mic.stop_recording()
```

You can save the recorded audio data to a WAV file by calling the `save_audio()` method. You can specify the filename as an optional argument to this method. The default filename is "recorded_audio.wav".

```python
# Save the recorded audio to a WAV file
mic.save_audio(audio_data)
```

## Example

The following code snippet shows how to use the `microphone` module to record and save a 5-second audio clip:

```python
import microphone

# Create a Microphone object
mic = microphone.Microphone()

# Start recording audio for 5 seconds
audio_data = mic.start_recording()

# Stop recording audio
mic.stop_recording()

# Save the recorded audio to a WAV file
mic.save_audio(audio_data)
```
