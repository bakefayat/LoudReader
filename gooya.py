from pygame import mixer 
from mutagen.mp3 import MP3
import time
mixer.init() 
mixer.music.set_volume(0.7) 
while(True):
        path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/'
        #mixer.music.play()
        mixer.Channel(0).play(mixer.Sound(path + "d1.mp3"))
        song = MP3(path + 'd1.mp3')
        songl = song.info.length
        print(songl)
        time.sleep(songl)
        mixer.Channel(1).play(mixer.Sound(path + "d2.mp3"))
        time.sleep(0.1)
        mixer.Channel(2).play(mixer.Sound(path + "d3.mp3"))
        time.sleep(0.1)
        input()              
