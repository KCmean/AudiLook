from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame
from tkinter import messagebox
from tkinter import filedialog
from pydub import AudioSegment


merge = Tk()
merge.title("Merge")
merge.geometry('700x600')

def merge1(slice1, slice2):
    sound1= AudioSegment.from_mp3(slice1)
    sound2 = AudioSegment.from_mp3(slice2)

    merge_1 = slice1+ slice2
    # L1=Label(merge, text = "Save As", bd = 2 )
    # ENT = Entry(merge, bd= 5)
    # ENT.pack(side = RIGHT)
    merge_1.export(f"E:/sem 2/python programming/python ptoject/audio/merge.mp3", format= 'mp3')
    
#adding songs
def add_song():                               
    songadd = filedialog.askopenfilename(initialdir="audio/" , title="Choose a somg" , filetypes=(("mp3 files" , "*.mp3"),))
    songadd = songadd.replace("E:/sem 2/python programming/python ptoject/audio/","")
    songadd = songadd.replace(".mp3","")
    playlist.insert(END,songadd)
    slices.append(songadd)

def song1():
    song = playlist.get(ACTIVE)
    global song_1
    song_1 = f'E:/sem 2/python programming/python ptoject/audio/{song}'

def song2():
    song = playlist.get(ACTIVE)
    global song_2
    song_2 = f'E:/sem 2/python programming/python ptoject/audio/{song}'


slices=[]
#musicbox

playlist= Listbox(merge , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
music= "E:/sem 2/python programming/python ptoject/audio/1.mp3"
music = music.replace("E:/sem 2/python programming/python ptoject/audio/", "")
music = music.replace(".mp3", "")
playlist.insert(END, music)

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

song1_btt.grid(row= 0 , column = 1, padx= 10)
song2_btt.grid(row= 0 , column = 3, padx= 10)
merge_btt.grid(row= 1, column =2, padx =10)



merge.mainloop()







