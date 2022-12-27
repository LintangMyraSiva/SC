import speech_recognition as sr

engine = sr.Recognizer()
mic = sr.Microphone()
hasil = ""
angine.pause_treshold = 3

with mic as source:
    print("Silahkan mulai bicara")
    rekaman = engine.listen(source)
    print("Waktu habis")
    
    try:
        hasil = engine.recognize_google(rekaman, language = "id-ID")
        print(hasil)
    except engine.UnknownValueError:
        print("Maff tidak bisa di deteksi, mohon  coba lagi")
    except Excepion as e:
        print(e)
        
text_file = open("hasil.txt, w")
text_file.write(hasil)
text_file.closet()
