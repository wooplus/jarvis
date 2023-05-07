from gtts import gTTS
import os
with open('mails.txt', 'r') as file:
    myText = file.read().replace('\n','')
language = 'en'
tts = gTTS(text=myText, lang=language, slow= False)
tts.save("output.mp3")
os.system("emails.mp3")