from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame
from tkinter import messagebox
from tkinter import filedialog
from pydub import AudioSegment


merge = Tk()
merge.title("Audio Merger")
merge.geometry('900x600')

def merge1(slice1, slice2):
    sound1= AudioSegment.from_mp3(slice1)
    sound2 = AudioSegment.from_mp3(slice2)

    merge_1 = sound1+ sound2
    # L1=Label(merge, text = "Save As", bd = 2 )
    # ENT = Entry(merge, bd= 5)
    # ENT.pack(side = RIGHT)
    merge_1.export(f"audio/merge.mp3", format= 'mp3')
    L1= Label(merge, text= "[NOTE : Merged audio saved as MERGED.mp3. \nYou can return to MP3 player to play your audio.]")
    L1.pack(pady = 10)

    
#adding songs
def add_song():                               
    songadd = filedialog.askopenfilename(initialdir="audio/" , title="Choose a song" , filetypes=(("mp3 files" , "*.mp3"),))
    songadd = songadd.replace("C:/Users/ryzen/Documents/GitHub/Audio-editor/audio/","")
    songadd = songadd.replace(".mp3","")
    playlist.insert(END,songadd)

def song1():
    song = playlist.get(ACTIVE)
    global song_1, sel_song1
    song_1 = f'audio/{song}.mp3'
    sel_song1 = Label(merge, text = f'SONG 1 : {song}')
    sel_song1.pack(pady =10)
    song1_btt['state']= DISABLED
    song2_btt["state"]= NORMAL

def song2():
    song = playlist.get(ACTIVE)
    global song_2 , sel_song2
    song_2 = f'audio/{song}.mp3'
    sel_song2 = Label(merge, text = f'SONG 2 : {song}')
    sel_song2.pack(pady=10)
    song2_btt['state']= DISABLED
    reset_btt["state"]= NORMAL

def reset():
    playlist.select_clear(ACTIVE)
    sel_song1.destroy()
    sel_song2.destroy()
    song1_btt['state']= NORMAL
    song2_btt['state']= DISABLED


#musicbox

playlist= Listbox(merge , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
# music= "C:/Users/ryzen/Documents/GitHub/Audio-editor/audio/ 1.mp3"
# music = music.replace("C:/Users/ryzen/Documents/GitHub/Audio-editor/audio/", "")
# music = music.replace(".mp3", "")
# playlist.insert(END, music)

# for i in slices:
#     ex = merge(i)
#     ex.export("Merge.mp3", format = 'mp3')

#cretaing list
my_menu = Menu(merge)
merge.config(menu=my_menu)

#add song 
addsong = Menu(my_menu)
my_menu.add_cascade(label="Add Song" , menu=addsong)
addsong.add_command(label="Add one song to playlist" , command=add_song)

ctrls_frame = Frame(merge)
ctrls_frame.pack(pady=10)
song1_btt = Button(ctrls_frame, text = 'SONG 1', bd = 5, command = song1)
song2_btt = Button(ctrls_frame, text = 'SONG 2', bd = 5, command = song2)
merge_btt = Button(ctrls_frame, text = 'MERGE', bd =5, command = lambda : merge1(song_1, song_2))
reset_btt = Button(ctrls_frame, text = 'RESET', bd = 5, command = reset)
song2_btt['state']= DISABLED
reset_btt["state"]= DISABLED


song1_btt.grid(row= 0 , column = 1, padx= 10)
song2_btt.grid(row= 0 , column = 3, padx= 10)
merge_btt.grid(row= 1, column =2, padx =10, pady=10)
reset_btt.grid(row = 2,  column =2, padx = 10, pady= 10)



merge.mainloop()







