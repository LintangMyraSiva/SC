import tkinter as tk
from playsound import playsound
from gtts import gTTS
import pyaudio
import wave
import matplotlib.pyplot as mpl
import numpy as npy

# Membuat Setting fps
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

# Class dengan nama App 
class App:
    # Untuk menampilkan GUI
    def __init__(self, root):
        self.root = root
        self.root.title("Ubah Teks Menjadi Suara")
        self.root.geometry("200x200")
        
        #  Membuat inputan teks
        self.text = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.text)
        self.entry.grid(row=0,column=0)
        
        # Membuat button yang ketika di klik masuk ke convert_to_speech
        self.button = tk.Button(self.root, text="Ubah menjadi suara", command=self.convert_to_speech)
        self.button.grid(row=1,column=0)


    def convert_to_speech(self):
        # Mengambil text inputan
        text = self.text.get()
        # Mengubah bahasa menjadi indonesia
        lang = 'id'
        # Membuat sound
        tts = gTTS(text=text,lang=lang)
        tts.save("sound.wav")
        playsound("sound.wav")
    
# Menjalankan Program
root = tk.Tk()
app = App(root)
root.mainloop()
