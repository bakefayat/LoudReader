import time
from pygame import mixer
from mutagen.mp3 import MP3
from playsound import playsound as play
import pandas as pd

#just play sound.
def play_song(song, next = 0):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if (type(song) == int) and next == 1:
        fpath = path + str(song) + 'o' + '.mp3'
    elif (type(song) == int) and next == 0:
        fpath = path + str(song) + '.mp3'
    else:
        fpath = path + song + '.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))
# play 10-20-30-...
def play_dah(num,next = 0):
    if num == 1:
        play_song(10, next)
    if num == 2:
        play_song(20, next)
    if num == 3:
        play_song(30, next)
    if num == 4:
        play_song(40, next)
    if num == 5:
        play_song(50, next)
    if num == 6:
        play_song(60, next)
    if num == 7:
        play_song(70, next)
    if num == 8:
        play_song(80, next)
    if num == 9:
        play_song(90, next)

#play 100-200-300
def play_sadgan(num, next = 0):
    if num == 1:
        play_song(100, next)
    if num == 2:
        play_song(200, next)
    if num == 3:
        play_song(300, next)

# play 11-19
def play_eleven_to_nineteen(num):
    if num == 1:
        play_song(11)
    if num == 2:
        play_song(12)
    if num == 3:
        play_song(13)
    if num == 4:
        play_song(14)
    if num == 5:
        play_song(15)
    if num == 6:
        play_song(16)
    if num == 7:
        play_song(17)
    if num == 8:
        play_song(18)
    if num == 9:
        play_song(19)

#leave gap between them.
def music_length(path):
    song = MP3(path)
    songl = song.info.length
    return songl

#play first digit.
def yekan(num, next = 0):
    if num == 1:
        play_song(1, next)
    if num == 2:
        play_song(2, next)
    if num == 3:
        play_song(3, next)
    if num == 4:
        play_song(4, next)
    if num == 5:
        play_song(5, next)
    if num == 6:
        play_song(6, next)
    if num == 7:
        play_song(7, next)
    if num == 8:
        play_song(8, next)
    if num == 9:
        play_song(9, next)

#play second digit
def dahgan(num, yekan, mmz = 0, next= 0):
    is_eleven = False
    if num == 1 and yekan != 0:
        play_eleven_to_nineteen(yekan)
        is_eleven = True
    else:
        if yekan != 0:
            play_dah(num, 1)
        else:
            play_dah(num, 0)
    return is_eleven

#DONE. play just 'dar' not anything else.
def play_dar():
        play_song('dar')

#play just 'adad' not anything else.
def play_adad():
        play_song('adad')

#play milimeter after length or width.
def play_mil():
        play_song('mil')

def split_num(number):
    number2 = number
    mmz_index = None
    mmz = 0
    sad = 0
    dah = 0
    yek = 0
    number = str(number)
    for i in range(0,len(number)):
        if number[i] == '.':
            mmz_index = i
            mmz = number[i+1]

    number = number[:mmz_index:]
    number = number[::-1]
    is_wierd = False
    leng = len(number)
    yek = int(number[0])
    if leng > 1:
        dah = int(number[1])
    if leng > 2:
        sad = int(number[2])
    if sad:
        if yek or dah:
            play_sadgan(sad,1)
        else:
            play_sadgan(sad,0)
    if dah:
        if yek or mmz:
            is_wierd = dahgan(dah, yek, mmz, 1)
        else:
            is_wierd = dahgan(dah,yek, mmz, 0)
    if yek and not(is_wierd):
        if int(mmz):
            yekan(yek,1)
        else:
            yekan(yek,0)
    if mmz and mmz != '0':
        mmz = int(mmz)
        if not(yek) and not(dah):
            play_song('santo')
        if mmz == 5:
            play_song('nim')
        else:
            yekan(mmz)
        if not(yek) and not(dah):
            play_song('mil')
i = 0
mixer.init()
mixer.music.set_volume(1)
pan = pd.read_excel(r'C:\Users\RDaneshjoo\Desktop\master.xlsx')
df = pd.DataFrame(pan, columns= [ 'طول','عرض','تعداد'])
width = df['طول'].tolist()
length = df['عرض'].tolist()
many = df['تعداد'].tolist()
for k in range(0,len(width)):
        split_num(width[k])
        play_dar()
        split_num(length[k])
        time.sleep(0.3)
        split_num(many[k])
        play_adad()
