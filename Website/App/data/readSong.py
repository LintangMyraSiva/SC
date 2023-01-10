from .Song import song
import os

cwd = os.getcwd()

song = song(f'{cwd}/App/data/iu.wav')

def getChannel():
    data = song.getChannel()
    return data
def getFramerate():
    data = song.getFramerate()
    return data
def getnFrames():
    data = song.getnFrames()
    return data
def getSampWidth():
    data = song.getSampWidth()
    return data
def getComptype():
    data = song.getComptype()
    return data
def getTime():
    data = song.getTime()
    return data





