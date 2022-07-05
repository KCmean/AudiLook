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

def pause(is_paused):                          #pause/unpause
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.pause()
        paused=True

horizontal_slider = Scale(app, from_= 0, to=100, orient=HORIZONTAL)                 #slide
horizontal_slider.pack()

def slide():
    horizontal_slider_label =  Label(app, text=horizontal_slider.get()).pack()

horizontal_slider_button = Button(app, text ="Confirm Audio point for editing", command=slide).pack()




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
back_btt =Button(ctrls_frame, text = "start", borderwidth = 10 )
next_btt =Button(ctrls_frame, text = "end", borderwidth = 10)
 
back_btt.grid(row =0, column =1, padx=10) 
play_btt.grid(row =0, column =2, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 
next_btt.grid(row =0, column =4, padx=10) 

startEntry=Entry(app, width= 25,)
startEntry.pack()
endEntry=Entry(app, width= 25)
endEntry.pack()



# start_pt = position_slider.get()
# end_pt = int(position_slider.get())


slider_label= Label(app, text='0')
slider_label.pack(pady=10)

app.mainloop()