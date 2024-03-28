from hear import *
from speak import *
from datetime import date, datetime, time
import webbrowser
import time
import os

import wikipedia
wikipedia.set_lang("vi")

from youtube_search import YoutubeSearch

def wiki_search(text):
    try:
        infor = wikipedia.summary(text).split('\n')
        speak(infor[0].split(".")[0])
        for a in infor[1:]:
            speak("Bạn muốn nghe thêm không ?")
            ans = hear()
            if "có" not in ans:
                break
            speak(a)
        
        speak("Cảm ơn bạn đã lắng nghe. Bạn muốn mình giúp gì nữa không")
    
    except:
        speak("Mình không tìm được tài liệu bạn muốn tìm kiếm. Bạn muốn giúp gì khác không ?")



def search_youtube(text):

    while True:
        result = YoutubeSearch(text, max_results=10).to_dict()
        if result:
            break
    url = "https://www.youtube.com/" + result[0]["url_suffix"]
    webbrowser.open(url)
    time.sleep(1)
    speak("Youtube đã được mở cùng nội dung bạn tìm kiếm")


def search_google(text):
    url = "https://www.google.com/search?q=" + text
    webbrowser.open(url)
    print("Bạn cần giúp gì khác nữa không ?")

speak("Xin chào mọi người, tôi là chị Google. Xin đặt câu hỏi cho tôi")

while True:
    you = hear()

    if you == None:
        speak("Mình chưa nghe được bạn nói, bạn nói lại được không ?")

    elif "tìm" in you and "thông tin" in you:
        wiki_search(you)

    elif "mở" in you and "clip" in you:
        search_youtube(you)

    elif "search google" in you:
        search_google(you[14:])
    
    elif ("hôm nay" in you) or ("bây giờ" in you):
        now = datetime.now()
        if "giờ" in you:
            t = now.strftime("%H h, %M phút, %S giây")
            speak(t)
        if "ngày" in you:
            t = now.strftime("Hôm nay là ngày %d, tháng %m, năm %Y")
            speak(t)

    elif "mở" in you:
        if "facebook" in you:
            webbrowser.open("https://www.facebook.com/")
            time.sleep(1)
            speak("Facebook đã được mở")
        if "zalo" in you:
            webbrowser.open("https://chat.zalo.me/")
            time.sleep(1)
            speak("Zalo đã được mở")
        if "youtube" in you:
            webbrowser.open("https://www.youtube.com/")
            time.sleep(1)
            speak("Youtube đã được mở")


    elif "chủ tịch" in you and "việt nam" in you and "đầu tiên" in you:
        speak("Chủ tịch Hồ Chí Minh nha bạn")


    elif "con người" in you:
        speak("Mình chỉ là trợ lý ảo thôi")
    
    elif "tạm biệt" in you:
        speak("Tạm biệt, hẹn gặp lại bạn")
        break