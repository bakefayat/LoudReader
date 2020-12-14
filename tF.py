from pygame import mixer
from mutagen.mp3 import MP3
import time
mixer.init()
mixer.music.set_volume(0.8)
i = 0
def play_eleven_to_nineteen(num,i):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    if num == 1:
        mixer.Channel(i).play(mixer.Sound(path + 'd1.mp3'))
    if num == 2:
        mixer.Channel(i).play(mixer.Sound(path + 'd12.mp3'))
    if num == 3:
        mixer.Channel(i).play(mixer.Sound(path + 'd13.mp3'))
    if num == 4:
        mixer.Channel(i).play(mixer.Sound(path + 'd14.mp3'))
    if num == 5:
        mixer.Channel(i).play(mixer.Sound(path + 'd15.mp3'))
    if num == 6:
        mixer.Channel(i).play(mixer.Sound(path + 'd16.mp3'))
    if num == 7:
        mixer.Channel(i).play(mixer.Sound(path + 'd17.mp3'))
    if num == 8:
        mixer.Channel(i).play(mixer.Sound(path + 'd18.mp3'))
    if num == 9:
        mixer.Channel(i).play(mixer.Sound(path + 'd19.mp3'))
    return i+1


path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
i = play_eleven_to_nineteen(4,i)
i += 1
song = MP3(path + 'd1.mp3')
songl = song.info.length
time.sleep(songl-0.5)
i = play_eleven_to_nineteen(5,i)
print(i)

#mixer.Channel(0).play(mixer.Sound(path + "d1.mp3"))
#mixer.Channel(1).play(mixer.Sound(path + "d2.mp3"))
#mixer.Channel(2).play(mixer.Sound(path + "d3.mp3"))
#mixer.Channel(3).play(mixer.Sound(path + "d4.mp3"))
#mixer.Channel(4).play(mixer.Sound(path + "d5.mp3"))




    #song = MP3(path + 'd1.mp3')
    #songl = song.info.length
    #print(songl)
input()