from gtts import gTTS
import os 
from Prueba2 import *

text = summary
language = 'es'
speech = gTTS(text = text, lang = language, slow = False)
speech.save("Audio.mp3")
os.system("start Audio.mp3")