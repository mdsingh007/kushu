# converts youtube m4a to mp3

#  .\ffmpeg.exe -i "C:\Users\manis\Desktop\YTMusic\Aaj Kal Tere Mere Pyar Ke Charche  Brahmachari (1968)  Shammi Kapoor  Mumtaz  Hindi Karaoke Song.mp4" -acodec libmp3lame -ab 256k oooo.mp3


# assumes all files at root level
from pathlib import Path
import os
import subprocess

infolder = 'C:\\Users\\manis\\Desktop\\YTMusic\\'
outfolder = 'C:\\Users\\manis\\Desktop\\YTMusic\\YTMusicMP3\\'

for f in Path(infolder).glob('*.mp4'):
    of = str(f)[:-4] + '.mp3'
    of = os.path.join(outfolder,  of.split('\\')[-1])
    if not Path(of).exists():
        cmd = f'C:/Programs/ffmpeg-2022/bin/ffmpeg.exe -i "{f}" -acodec libmp3lame -ab 256k "{of}" '
        print(cmd)
        subprocess.run(cmd)


