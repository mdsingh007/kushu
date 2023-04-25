# from platform import python_implementation
from pytube import YouTube
import sys
import time
import pyperclip


def download_audio(url):
    s = YouTube(url).streams
    s.filter(mime_type='audio/mp4').order_by('abr')[-1].download()

while True:
    
    print ('waiting; ctrl+z to exit')
    time.sleep(2)
    url = pyperclip.paste()
    if url and 'www.youtube.com' in url:
        download_audio(url)
        pyperclip.copy("")


if __name__ == '__main__':
    download_audio('https://www.youtube.com/watch?v=Y4o_8zbelwY')
    
