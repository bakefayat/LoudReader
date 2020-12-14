import time
from pygame import mixer
from mutagen.mp3 import MP3
from playsound import playsound as play
import pandas as pd
i = 0
mixer.init()
mixer.music.set_volume(0.7)
start = time.time()
def music_length(path):
    song = MP3(path)
    songl = song.info.length
    return songl

def play_eleven_to_nineteen(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    if num == 1:
        fpath = path + 'd11.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + 'd12.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + 'd13.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + 'd14.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + 'd15.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + 'd16.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + 'd17.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + 'd18.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + 'd19.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

def play_dah(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    if num == 1:
        fpath = path + 'd10.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + 'd20.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + 'd30.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + 'd40.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + 'd50.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + 'd60.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + 'd70.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + 'd80.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + 'd90.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

#start from here
def play_num(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    if num == 1:
        fpath = path + 'd1.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + 'd2.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + 'd3.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 4:
        fpath = path + 'd4.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 5:
        fpath = path + 'd5.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 6:
        fpath = path + 'd6.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 7:
        fpath = path + 'd7.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 8:
        fpath = path + 'd8.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 9:
        fpath = path + 'd9.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

def yekan(num):
    play_num(num)

def dahgan(num,yekan):
    is_eleven = False
    if num == 1 and yekan != 0:
        play_eleven_to_nineteen(yekan)
        is_eleven = True
    else:
        play_dah(num)
    return is_eleven
def sadgan(num):
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    if num == 1:
        fpath = path + 'd100.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 2:
        fpath = path + 'd200.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))
    if num == 3:
        fpath = path + 'd300.mp3'
        mixer.Channel(i).play(mixer.Sound(fpath))
        time.sleep(music_length(fpath))

def play_dar():
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/'
    fpath = path + 'dDar.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))


def play_adad():
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/'
    fpath = path + 'dAdad.mp3'
    mixer.Channel(i).play(mixer.Sound(fpath))
    time.sleep(music_length(fpath))


def play_mil():
    path = 'C:/Users/RDaneshjoo/Downloads/programming/py/goya/' 
    fpath = path + 'dMil.mp3'
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
        sadgan(sad)
    if dah:
        is_wierd = dahgan(dah,yek)
    if yek and not(is_wierd):
        yekan(yek)
    if mmz:
        mmz = int(mmz)
        yekan(mmz)
        play_mil()
 
#split_num(123.1,0)
pan = pd.read_excel(r'C:\Users\RDaneshjoo\Desktop\master.xlsx')
df = pd.DataFrame(pan, columns= [ 'طول','عرض','تعداد'])
w = df['طول'].tolist()
h = df['عرض'].tolist()
c = df['تعداد'].tolist()
for k in range(0,len(h)):
        split_num(w[k])
        play_dar()
        split_num(h[k])
        split_num(c[k])
        play_adad()
