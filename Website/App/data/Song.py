import wave
import math

class song(object): #di dalam song itu ada apa aja

    def __init__(self,songName): 
        self.song = wave.open(songName,'r') #ngebaca modul wave
    
    def getChannel(self): #buat nentuin jenis audio
        data = self.song.getnchannels()
        if(data == 1):
            result = "Mono"
        else:
            result = "Stereo"
        return result

    def getFramerate(self): #buat nentuin fps (frekuensi lagu)
        data = self.song.getframerate()
        return data

    def getnFrames(self): 
        data = round(int(self.song.getnframes()/48000))
        return data

    def getSampWidth(self): #buat nentuin bytes
        data = self.song.getsampwidth()
        return data

    def getComptype(self):
        data = self.song.getcomptype()
        if data == "NONE":
            result = "Not supported to compression."
        else:
            result = "Supported to compression."
        return result

    def getTime(self): #durasi lagu
        time = int(self.getnFrames()/self.getFramerate()/60)
        return time