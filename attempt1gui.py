from cProfile import label
from tkinter import *
import tkinter.ttk as ttk
import pygame
from PIL import ImageTk, Image

app = Tk()
app.title(' Audio Cutter and Merger ')
app.geometry('700x600')

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





playlist= Listbox(app , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
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

 

play_btt.grid(row =0, column =1, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 




horizontal_slider = Scale(app, from_= 0, to=100, orient=HORIZONTAL)              #slideer
horizontal_slider.pack()
horizontal_slide2r = Scale(app, from_= 100, to=0, orient=HORIZONTAL)                 
horizontal_slide2r.pack()

startIndex = 0
endIndex = 0
def slide():
    start_btt =  Label(app, text=f" Starting point :{horizontal_slider.get()}").pack()
    global startIndex
    startIndex = horizontal_slider.get()
    horizontal_slider['state'] = DISABLED
def slide2():
    end_btt =  Label(app, text=f" Ending point :{horizontal_slide2r.get()}").pack()
    global endIndex
    endIndex = horizontal_slide2r.get()
    horizontal_slide2r['state'] = DISABLED

start_btt =Button(ctrls_frame, text = "select starting text", borderwidth = 10, command=slide )

end_btn =Button(ctrls_frame, text = "select ending point", borderwidth = 10, command = slide2 )


end_btn.grid(row =1, column =3, padx=10) 
start_btt.grid(row =1, column =1 ,padx=10) 

def confirmwindow():
    confirm_btt = Label(app , text = f"your start pt is :{startIndex} and end pt is : {endIndex} thus the lenght of your final output will be : {startIndex-endIndex}").pack()

confirm_btt = Button(ctrls_frame, borderwidth = 10 , text="confirm" , width=10 , command=confirmwindow)
confirm_btt.grid(row=1 , column=2)




app.mainloop()
app.update_idletasks()
