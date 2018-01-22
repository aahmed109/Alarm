# next target: GUI
import pyaudio
import wave

chunk = 1024
formats = pyaudio.paInt16
channel = 2
rates = 44100
record_seconds = 10

wave_output_file = "recording" + "1" + ".wav"

p = pyaudio.PyAudio()

stream = p.open(format=formats,
                channels=channel,
                rate=rates,
                input=True,
                frames_per_buffer=chunk)

print("* recording")

frames = []

for i in range(int(rates/chunk*record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(wave_output_file, 'wb')
wf.setnchannels(channel)
wf.setsampwidth(p.get_sample_size(formats))
wf.setframerate(rates)
wf.writeframes(b''.join(frames))
wf.close()