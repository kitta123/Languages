from gtts import gTTS
import os

f = open('kitta.txt')
x = f.read()

language = 'en'

audio = gTTS(text=x,Lang=language,slow=False)
audio.save('kitta.wav')
os.system('kitta.wav')
