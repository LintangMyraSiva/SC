from django.shortcuts import render
from App.data.readSong import *

def index (request):
    return render(request,'Pages/Home.html') 
def aboutwe (request):
    return render(request,'Pages/AboutUs.html') 
def project (request):
    context = {
        'channel' : getChannel(),
        'framerate' : getFramerate(),
        'frames' : getnFrames(),
        'sampwidth' : getSampWidth(),
        'comptype' : getComptype(),
        'time' : getTime()
    }
    return render(request,'Pages/Project.html',context) 

