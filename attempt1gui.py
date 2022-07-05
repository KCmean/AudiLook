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

 

play_btt.grid(row =0, column =2, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 

# startEntry=Entry(app, width= 25,)
# startEntry.pack()
# endEntry=Entry(app, width= 25)
# endEntry.pack()



# start_pt = position_slider.get()
# end_pt = int(position_slider.get())

horizontal_slider = Scale(app, from_= 0, to=100, orient=HORIZONTAL)                 #slide
horizontal_slider.pack()

def slide():
    start_btt =  Label(app, text=f" Starting point :{horizontal_slider.get()}").pack()
    startIndex = horizontal_slider.get()

# horizontal_slider_button = Button(app, text ="Confirm Audio point for editing",pady=20, command=slide).pack()

start_btt =Button(ctrls_frame, text = "select starting text", borderwidth = 10, command=slide )
end_btn =Button(ctrls_frame, text = "select ending point", borderwidth = 10 )

end_btn.grid(row =1, column =4, padx=10) 
start_btt.grid(row =1, column =1 ,padx=10) 


# slider_label= Label(app, text='0')
# slider_label.pack(pady=10)

app.mainloop()
app.update_idletasks()
