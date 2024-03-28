from hear import *
from speak import *
from datetime import date
from datetime import datetime
from datetime import time

import webbrowser
import time

speak("Xin chào mọi người, tôi là chị Google. Xin đặt câu hỏi cho tôi")

while True:
    you = hear()

    if you == None:
        speak("Mình chưa nghe được bạn nói, bạn nói lại được không ?")

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