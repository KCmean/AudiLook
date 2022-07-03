from tkinter import *
import tkinter.ttk as ttk
import pygame
from PIL import ImageTk, Image

app = Tk()
app.title(' Audio Cutter and Merger ')
app.geometry('500x400')

img = Image.open('play.png') 
img = img.resize((50,50))

pygame.mixer.init()

def play():                                     #play 
    song = playlist.get(ACTIVE)
    song = f'{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    global paused
    paused = False
    
global paused
paused = False   

def pause(is_paused):                          #pause
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.pause()
        paused=True




def scale(x):                                                   #slider
    slider_label.config(text= int(position_slider.get()))


   
playlist= Listbox(app , bg= "black", fg = "green" , selectbackground= "gray", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
music= "1.mp3"
# music = music.replace("", "")
music = music.replace(".mp3", "")
playlist.insert(END, music)

ctrls_frame=Frame(app)
ctrls_frame.pack()

play_img= PhotoImage(file= "play.png")
pause_img= PhotoImage(file = "pause.png")

play_btt = Button(ctrls_frame, image= play_img, borderwidth = 0, command = play )
pause_btt =Button(ctrls_frame, image = pause_img , borderwidth = 0, command = lambda : pause(paused))
back_btt =Button(ctrls_frame, text = "back", borderwidth = 10  )
next_btt =Button(ctrls_frame, text = "next", borderwidth = 10 )
 
back_btt.grid(row =0, column =1, padx=10) 
play_btt.grid(row =0, column =2, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 
next_btt.grid(row =0, column =4, padx=10) 

position_slider= ttk.Scale(app, from_= 0, to=100, value=0, orient=HORIZONTAL, length = 360, command = scale)
position_slider.pack(pady=20)

start_pt = int(position_slider.get())

slider_label= Label(app, text='0')
slider_label.pack(pady=10)

app.mainloop()