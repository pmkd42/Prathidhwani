import speech_recognition as sr
from os import path
from pydub import AudioSegment
import moviepy.editor
import os

#aud = vid.audio
#aud.write_audiofile('l1.mp3')
# convert mp3 file to wav                                                       
#soundu = AudioSegment.from_mp3("l1.mp3")
#soundu.export("transcript.wav", format="wav")


# transcribe audio file                                                         
AUDIO_FILE = "transcript.wav"

# use the audio file as the audio source                                        


# offset = 29
# duration = 5


captions = ""
captions2 = ""
f = open("phrases.txt", "w")
f2 = open("phrases2.txt", "w")
if(os.path.isfile(AUDIO_FILE)):
    print("idhe")
    with sr.AudioFile(AUDIO_FILE) as source:                                         
        r = sr.Recognizer()                                                 
        r.adjust_for_ambient_noise(source)                                           
        audio1 = r.record(source,offset = 29,duration = 10)
        captions += r.recognize_google(audio1) + ' '
        captions2 += r.recognize_google(audio1) + '\n'
        for i in range(28):                                                          
            audio2 = r.record(source,offset = 0,duration = 10)
            captions += r.recognize_google(audio2) + ' '
            captions2 += r.recognize_google(audio2) + '\n'
else:
    print("illa")
    vid = moviepy.editor.VideoFileClip('l1.mp4')
    vid.audio.write_audiofile("transcript.wav",codec='pcm_s16le')
    with sr.AudioFile(AUDIO_FILE) as source:                                         
        r = sr.Recognizer()                                                 
        r.adjust_for_ambient_noise(source)                                           
        audio1 = r.record(source,offset = 29,duration = 10)
        captions += r.recognize_google(audio1) + ' '
        captions2 += r.recognize_google(audio1) + '\n'
        for i in range(28):                                                          
            audio2 = r.record(source,offset = 0,duration = 10)
            captions += r.recognize_google(audio2) + ' '
            captions2 += r.recognize_google(audio2) + '\n'
f.write(captions)
f2.write(captions2)
f.close()
f2.close()
print(captions)
