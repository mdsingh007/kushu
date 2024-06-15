from importlib.resources import path
from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import os
import pyperclip
import time
import sys

# pyperclip.copy('The text to be copied to the clipboard.')


def get_valid_links(url):
    ''' get all links with href attribute'''
    req = requests.get(url)
    soup = soup = bs(req.text, 'html.parser')

    links = soup.find_all('a')
    href = []
    for l in links:
        try:
            href.append (l['href'])
        except:
            pass
    return href

def download_mp3(u):
    # u = '''https://pagalfree.com/download/128-Chori Chori Jab Nazrein Mili Part 1 - Kareeb 128 Kbps.mp3'''
    
    assert '.mp3' in u
    
    r = requests.get(u)
    fname = u.split('/')[-1]
    fpath = os.path.join(os.getcwd(), 'music', folder, fname)
    print(fp)
    open(fpath, 'wb').write(r.content)



# url = 'https://pagalfree.com/album/anari-1993.html'
url = pyperclip.paste()
print(f'\n\n\n#### Downloading {url}\n\n')
assert 'pagalfree.com' in url


folder = url.split('/')[-1].split('.')[0]
# input(f'create folder - {folder} ? (cmd+c to cancel)')



href = get_valid_links(url)

if len(sys.argv) > 1 and sys.argv[1] == 'song':
    folder = 'mixed'
    mp = ([ x for x in href if '320' in x ][0])
    print (mp)
    download_mp3(mp)
else:    
    os.mkdir( os.path.join( os.getcwd(), 'music', folder ) )
    murls = [ x for x in href if '/music/' in x ]
    # pprint (murls)

    # input(f'download these? (cmd+c to cancel)')


    for u in murls:
        href = get_valid_links(u)
        mp = ([ x for x in href if '320' in x ][0])
        print (mp)
        download_mp3(mp)

    
# download_mp3()
