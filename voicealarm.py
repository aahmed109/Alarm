# next target: GUI
import pyaudio
import wave
import datetime

chunk = 1024


def split_and_join(time):
    strtime = time.split(":")
    print(strtime)

    for i in range(5):
        strtime[2] = strtime[2][:-1]

    print(strtime[2])
    return strtime[0]+":"+strtime[1]+":"+strtime[2]


def play_alarm():
    wf = wave.open('recording1.wav', 'rb')

    p = pyaudio.PyAudio()

    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
        channels = wf.getnchannels(),
        rate = wf.getframerate(),
        output = True)

    data = wf.readframes(chunk)

    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)

    stream.close()
    p.terminate()


print(datetime.datetime.time(datetime.datetime.now()))
print(str(datetime.datetime.now().time()))

count = 0

while split_and_join(str(datetime.datetime.now().time())) != "09:53:20.0":
    # do nothing
    count += 1

play_alarm()