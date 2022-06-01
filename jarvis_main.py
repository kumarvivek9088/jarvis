import struct
import pyaudio
import pvporcupine
from pydub.playback import play
from pydub import AudioSegment
import speech_recognition as sr
import pyttsx3
from speak import speak
import subprocess


porcupine=None
pyaud=None
audio_stream=None
p=None
def startsound():
    audio=AudioSegment.from_wav("start up sound.wav")
    play(audio)

def endsound():
    audio=AudioSegment.from_wav("end up sound.wav")
    play(audio)
try:
    porcupine=pvporcupine.create(keywords=["jarvis","alexa","ok google"])
    paud=pyaudio.PyAudio()
    audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
    while True:
        keyword=audio_stream.read(porcupine.frame_length)
        keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)
        keyword_index=porcupine.process(keyword)
        if keyword_index>=0:
            if p!=None:
                p.terminate()
            startsound()
            recognize=sr.Recognizer()
            with sr.Microphone() as source:
                audio=recognize.listen(source,4,3)
                endsound()
            try:
                query=recognize.recognize_google(audio,language='en-in')
                file=open("myfile.txt",'w')
                file.write(query)
                file.close()
                print(query)
                p=subprocess.Popen("jarvis_command.exe")
            except sr.UnknownValueError:
                speak("not recognize")
            

finally:
    if porcupine is not None:
        porcupine.delete()
    if audio_stream is not None:
        audio_stream.close()
    if paud is not None:
        paud.terminate()