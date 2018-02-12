import pyaudio
import wave

# FORMAT = pyaudio.paInt16
# CHANNELS = 2
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# WAVE_OUTPUT_FILENAME = "file.wav"

audio = pyaudio.PyAudio()

def set_config():
    config={"record_prgm_path":"/c/example",
            "FORMAT":pyaudio.paInt16,
            "CHANNELS":2,
            "RATE":44100,
            "CHUNK":1024,
            "RECORD_SECONDS":5,
            "WAVE_OUTPUT_FILENAME":"file.wav"
    }
    return config

def main():
    print("record_pc_mic_tool main!")
    print("Set config")
    config = set_config()
    print(config.__str__())

    print("Using example with pyadio")
    stream = audio.open(format=config["FORMAT"], channels=config["CHANNELS"],
                        rate=config["RATE"], input=True,
                        frames_per_buffer=config["CHUNK"])
    print("recording...")
    frames = []

    for i in range(0, int(config["RATE"] / config["CHUNK"] * config["RECORD_SECONDS"])):
        data = stream.read(config["CHUNK"])
        frames.append(data)
    print("finished recording")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(config["WAVE_OUTPUT_FILENAME"], 'wb')
    waveFile.setnchannels(config["CHANNELS"])
    waveFile.setsampwidth(audio.get_sample_size(config["FORMAT"]))
    waveFile.setframerate(config["RATE"])
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

if __name__ == "__main__":
    main()