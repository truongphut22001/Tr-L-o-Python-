from gtts import gTTS
import playsound
import os

def speak(text):
    print("Anna: " + text)
    tts = gTTS(text = text, lang= "vi", slow=False)
    tts.save("sound.mp3") 
    playsound.playsound("sound.mp3", True)
    os.remove("sound.mp3")

