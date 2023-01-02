import playsound
from gtts import gTTS
import speech_recognition as sr
import os

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
    engine.pause_threshold = 3

    with mic as source:
        print("Say something")
        print("Recording ...")
        rekaman = engine.listen(source)
        print("Done")

        try:
            hasil = engine.recognize_google(rekaman, language = 'id')
            print(hasil)
        except engine.UnknownValueError:
            print("Sorry, your sound wasn't detected, Please try again.")
        except Exception as e:
            print(e)
        
        text_file = open("hasilConverter_Texttospeech.txt", "w")
        text_file.write(hasil)
        text_file.close()
else:
    print("Please enter only available options.")
    