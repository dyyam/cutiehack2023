import pyaudio
import wave
import keyboard


testing = False
                       

def record():
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

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


def playAudio(soundFile):
        # Open sound file  in read binary form.
    file = wave.open(soundFile, 'rb')
    
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Creates a Stream to which the wav file is written to.
    # Setting output to "True" makes the sound be "played" rather than recorded
    stream = p.open(format = p.get_format_from_width(file.getsampwidth()),
                    channels = file.getnchannels(),
                    rate = file.getframerate(),
                    output = True)
    
    # Read data in chunks
    data = file.readframes(1024)
    
    # Play the sound by writing the audio data to the stream
    while data != b'':
        stream.write(data)
        data = file.readframes(1024)


    # Stop, Close and terminate the stream
    stream.stop_stream()
    stream.close()         
    p.terminate()

if __name__ == "__main__":
    if testing:
        print("Press [SPACE] to record audio!")
        record()
        if (input("Play sound?(y/n): ").strip() == "y"):
            print("playing audio...")
            playAudio("sounds/output.wav")
            print("done!")