# from platform import python_implementation
from pytube import YouTube
from pytube import Playlist
import sys
import time
import pyperclip


def download_audio(url):
    print ('downloading ', url)
    s = YouTube(url).streams
    print (s)
    s.filter(mime_type='audio/mp4').order_by('abr')[-1].download()

def pyper():
    print ('waiting; ctrl+z to exit')
    while True:
        print ('.', end=' ', flush=True)
        time.sleep(2)
        url = pyperclip.paste()
        if url and 'www.youtube.com' in url:
            download_audio(url)
            pyperclip.copy("")
            print()
            print ('waiting; ctrl+z to exit')

def download_playlist():
    print ('downloading yt playlist')
    url = pyperclip.paste()
    p = Playlist(url)
    print(f'Downloading: {p.title}')
    for url in p.video_urls[:3]:
        print(url)
        # download_audio(url)

if __name__ == '__main__':
    print (sys.argv)
    if len(sys.argv) > 1 and sys.argv[1] == 'p':
        download_playlist()
    else:
        pyper()
    
