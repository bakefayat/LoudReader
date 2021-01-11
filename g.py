import time
from pygame import mixer
from mutagen.mp3 import MP3
from playsound import playsound as play
import pandas as pd

def play_song(song):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if (type(song) == int):
        fpath = path + str(song) + '.mp3'
    else:
        fpath = path + song + '.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))

def play_dah(num):
    if num == 1:
        play_song(10)
    if num == 2:
        play_song(20)
    if num == 3:
        play_song(30)
    if num == 4:
        play_song(40)
    if num == 5:
        play_song(50)
    if num == 6:
        play_song(60)
    if num == 7:
        play_song(70)
    if num == 8:
        play_song(80)
    if num == 9:
        play_song(90)


# TODO: humanize it.
def play_sadgan(num):
    if num == 1:
        play_song(100)
    if num == 2:
        play_song(200)
    if num == 3:
        play_song(300)

#DONE. to play 11-19.
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

#Done. to hold program as long as sound length.
def music_length(path):
    song = MP3(path)
    songl = song.info.length
    return songl

# TODO: should be humanized.
def play_digit(num):
    if num == 1:
        play_song(1)
    if num == 2:
        play_song(2)
    if num == 3:
        play_song(3)
    if num == 4:
        play_song(4)
    if num == 5:
        play_song(5)
    if num == 6:
        play_song(6)
    if num == 7:
        play_song(7)
    if num == 8:
        play_song(8)
    if num == 9:
        play_song(9)

#DONE. play first digit.
def yekan(num):
    play_digit(num)

#DONE.
def dahgan(num,yekan):
    is_eleven = False
    if num == 1 and yekan != 0:
        play_eleven_to_nineteen(yekan)
        is_eleven = True
    else:
        play_dah(num)
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
        play_sadgan(sad)
    if dah:
        is_wierd = dahgan(dah,yek)
    if yek and not(is_wierd):
        yekan(yek)
    if mmz and mmz != '0':
        mmz = int(mmz)
        yekan(mmz)
        play_mil()
 
#read from excel file then play that.
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
        split_num(many[k])
        play_adad()
