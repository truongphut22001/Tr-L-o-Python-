import webbrowser

def search_google(text):
    url = "https://www.google.com/search?q=" + text
    webbrowser.open(url)
    print("Bạn cần giúp gì khác nữa không ?")

