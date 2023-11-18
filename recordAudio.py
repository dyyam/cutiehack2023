import pyaudio
import wave
import keyboard


chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 1
fs = 44100  # Record at 44100 samples per second
filename = "sounds/output.wav"


p = pyaudio.PyAudio()  # Create an interface to PortAudio



stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

print("Hold down [SPACE] to record audio!")
keyboard.wait("space")
if keyboard.is_pressed("space"): 
    print('Recording...')
    while keyboard.is_pressed("space"):
        data = stream.read(chunk)                                        
        frames.append(data)

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording!')
print(len(frames))

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()