import os
import pandas as pd
from pydub import AudioSegment

# append array of voices.
def play_song(song, next = 0):
    path = r'C:\Users\RDaneshjoo\Downloads\programming\other projects\goya\voice\wav'
    
    if (type(song) == int) and next == 1:
        second_part_of_path = str(song) + 'o' + '.wav'
    elif (type(song) == int) and next == 0:
        second_part_of_path = str(song) + '.wav'
    else:
        second_part_of_path = song + '.wav'

    fpath = os.path.join(path, second_part_of_path)
    song_array.append(fpath)

# play 10-20-30-...
def play_dah(num,next = 0):
    play_song(num*10, next)

# play 100-200-300
def play_sadgan(num, next = 0):
    play_song(num*100, next)

# play 11-19
def play_eleven_to_nineteen(num):
    num = '1' + str(num)
    play_song(num, next)

# play first digit.
def yekan(num, next = 0):
    play_song(num, next)

# play second digit
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

# play just 'dar' not anything else.
def play_dar():
        play_song('dar')

# play just 'adad' not anything else.
def play_adad():
        play_song('adad')
        pass
# play milimeter after length or width.
def play_mil():
        # play_song('mil')
        pass

# split full number to pieces.
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

pan = pd.read_excel(r'C:\Users\RDaneshjoo\Desktop\master.xlsx')
df = pd.DataFrame(pan, columns= [ 'طول','عرض','تعداد'])
width = df['طول'].tolist()
length = df['عرض'].tolist()
many = df['تعداد'].tolist()
song_array = []
file1 = r'C:\Users\RDaneshjoo\Downloads\programming\other projects\goya\voice\wav\blank.wav'
sound1 = AudioSegment.from_wav(file1)
combined = sound1
for k in range(0,len(width)):
        split_num(width[k])
        play_dar()
        split_num(length[k])
        # time.sleep(0.3)
        split_num(many[k])
        play_adad()
for song in song_array:
    sound = AudioSegment.from_wav(song)
    combined += sound
combined.export("joinedFile.wav", format="wav")
