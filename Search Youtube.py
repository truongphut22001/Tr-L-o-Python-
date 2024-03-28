import webbrowser
from youtube_search import YoutubeSearch
import time

def Search_Youtube(text):

    while True:
        result = YoutubeSearch(text, max_results=10).to_dict()
        if result:
            break
    url = "https://www.youtube.com/" + result[0]["url_suffix"]
    webbrowser.open(url)
    time.sleep(1)
    print("Youtube đã được mở cùng nội dung bạn tìm kiếm")

Search_Youtube("Hương tóc mạ non quang bình trang thanh lan")