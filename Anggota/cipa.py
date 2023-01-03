import playsound
from gtts import gTTS
import speech_recognition as sr
import os
import pyaudio
import wave
import matplotlib.pyplot as mpl
import numpy as npy

FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

pa = pyaudio.PyAudio()

stream = pa.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=FRAMES_PER_BUFFER
)

print("Welcome to Speech-to-Text Converter by SC\n")
print("Select : ")
print("1. Text to Speech converter")
print("2. Speech to Text converter (INPUT MIC)")
pilihan = input("Select [1/2] : ")

if(pilihan == "1"):
    teks = input("enter a sentence: ")
    lang = 'id'
    output = gTTS(text = teks, lang = lang, slow = False)
    output.save("hasilConverter_TexttoSpeech.wav")
    print("file saved")
    open("hasilConverter_Texttospeech.wav")
    playsound.playsound("hasilConverter_TexttoSpeech.wav", True)
    os.remove("hasilConverter_TexttoSpeech.wav")

elif(pilihan == "2"):
    engine = sr.Recognizer()
    mic = sr.Microphone()
    hasil = ""

    with mic as source:
        print("Say something")
        print("Recording ...")
        rekaman = engine.listen(source)
        
        seconds = 8
        frames = []
        second_tracking = 0
        second_count = 0
        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)
            second_tracking += 1
            if second_tracking == RATE/FRAMES_PER_BUFFER:
                second_count += 1
                second_tracking = 0
                print(f'Time Left: {seconds - second_count} seconds')


        stream.stop_stream()
        stream.close()
        pa.terminate()

        obj = wave.open('lemaster_tech.wav', 'wb')
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(pa.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b''.join(frames))
        obj.close()

        file = wave.open('lemaster_tech.wav', 'rb')

        sample_freq = file.getframerate()
        frames = file.getnframes()
        signal_wave = file.readframes(-1)

        file.close()

        time = frames / sample_freq

        audio_array = npy.frombuffer(signal_wave, dtype=npy.int16)

        times = npy.linspace(0, time, num=frames)

        mpl.figure(figsize=(10, 5))
        mpl.plot(times, audio_array)
        mpl.ylabel('Signal Wave')
        mpl.xlabel('Time (s)')
        mpl.xlim(0, time)
        mpl.title('The Thing I Just Recorded!!')
        mpl.show()

        print("Done")

        try:
            hasil = engine.recognize_google(rekaman, language = 'id')
            print(hasil)
        except engine.UnknownValueError:
            print("Sorry, your sound wasn't detected, Please try again.")
        except Exception as e:
            print(e)
        
        file = wave.open('lemaster_tech.wav', 'rb')

        sample_freq = file.getframerate()
        frames = file.getnframes()
        signal_wave = file.readframes(-1)

        file.close()

        time = frames / sample_freq

        audio_array = npy.frombuffer(signal_wave, dtype=npy.int16)

        times = npy.linspace(0, time, num=frames)

        mpl.figure(figsize=(10, 5))
        mpl.plot(times, audio_array)
        mpl.ylabel('Signal Wave')
        mpl.xlabel('Time (s)')
        mpl.xlim(0, time)
        mpl.title('The Thing I Just Recorded!!')
        mpl.show()
        
        text_file = open("hasilConverter_Texttospeech.txt", "w")
        text_file.write(hasil)
        text_file.close()
else:
    print("Please enter only available options.")
    