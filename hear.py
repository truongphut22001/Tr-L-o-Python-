
import speech_recognition as sr 

def hear():
    print("Đang nghe : ...")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit = 4)
        try:
            text = r.recognize_google(audio, language= "vi-VN")
            print(text)
            return str(text).lower()
        except:
            return None
        
