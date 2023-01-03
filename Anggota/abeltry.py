import wave

obj = wavvv.open("abel.wav", "rb")
#Audio signal parameters
#- number of channels
#- sample width
#- framerate/sample_rate, ex: 77,00 Hz
#- Number of frames
#- values of a frame

print("Number of channels", obj.getnchannels())
print("sample width", obj.getsampwidth())
print("frame rate", obj.getframerate())
print("Number of frames", obj.getnframes())
print("parameter", obj.getparams())



