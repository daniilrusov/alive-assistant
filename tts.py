from gtts import gTTS
from playsound import playsound
import os
from RUTTS import TTS

tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=0.8)

def tts_text(text):
    print(text)
    first = text.split('.')[0]
    #os.system(f"wsay.exe '{first}'")
    tts(first, play=True, lenght_scale=1.5)
