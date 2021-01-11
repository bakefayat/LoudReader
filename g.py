import time
from pygame import mixer
from mutagen.mp3 import MP3
from playsound import playsound as play
import pandas as pd

#TODO: humanize this.
def play_dah(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if num == 1:
        fpath = path + '10.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + '20.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + '30.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + '40.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + '50.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + '60.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + '70.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + '80.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + '90.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

#play hunderds. 1-2-3.
# TODO: humanize it.
def play_sadgan(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if num == 1:
        fpath = path + '100.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + '200.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + '300.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

#DONE. to play 11-19.
def play_eleven_to_nineteen(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if num == 1:
        fpath = path + '11.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + '12.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + '13.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + '14.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + '15.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + '16.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + '17.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + '18.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + '19.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

#Done. to hold program as long as sound length.
def music_length(path):
    song = MP3(path)
    songl = song.info.length
    return songl

#DONE.play digit
def play_digit(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    if num == 1:
        fpath = path + '1.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + '2.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + '3.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + '4.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + '5.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + '6.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + '7.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + '8.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + '9.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

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
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/'
    fpath = path + 'dar.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))

#play just 'adad' not anything else.
def play_adad():
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/'
    fpath = path + 'adad.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))

#play milimeter after length or width.
def play_mil():
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/voice/' 
    fpath = path + 'mil.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))

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
