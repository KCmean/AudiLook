# Importing Modules
from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame

# Explicitly initializing Tkinter interpreter and creating a root Window
app = Tk()
app.title(' Audio Cutter and Merger ')
app.geometry('700x600')

# Initialize mixer module of pygame
pygame.mixer.init()

def play():                                     #play 
    song = playlist.get(ACTIVE)
    song = f'{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    global paused
    paused = False
    play_time()

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

#Function for showing playtime of the Audi
def play_time():
    song = playlist.get(ACTIVE)
    song= f"{song}.mp3"
    mut = MP3(song)
    l_song= mut.info.length

    song_length = time.strftime('%H:%M:%S', time.gmtime(l_song))

    Curr_time = pygame.mixer.music.get_pos()/1000
    mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(Curr_time))
    my_label.config(text = f"{mod_curr_time} / {song_length}")
    my_label.after(1000, play_time)

# Slider Functions
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

def confirmwindow():
    confirm_btt = Label(app , text = f"your start pt is :{startIndex} and end pt is : {endIndex} thus the lenght of your final output will be : {endIndex-startIndex}").pack()



playlist= Listbox(app , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
music= "1.mp3"
# music = music.replace("", "")
music = music.replace(".mp3", "")
playlist.insert(END, music)

# Creating a sliders in TKinter using Scale()
horizontal_slider = Scale(app, from_= 0, to=100, orient=HORIZONTAL)              #slideer
horizontal_slider.pack()
horizontal_slide2r = Scale(app, from_= 100, to=0, orient=HORIZONTAL)                 
horizontal_slide2r.pack()

my_label = Label(app, text = '', bd=1, anchor= E)
my_label.pack(pady =5 )


ctrls_frame=Frame(app)
ctrls_frame.pack()

# Returns Image object
play_img= PhotoImage(file= "play.png")
pause_img= PhotoImage(file = "pause.png")

# Creating Buttons
play_btt = Button(ctrls_frame, image= play_img, borderwidth = 0, command = play )
pause_btt =Button(ctrls_frame, image = pause_img , borderwidth = 0, command = lambda : pause(paused))

# Placing Buttons
play_btt.grid(row =0, column =1, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 

startIndex = 0
endIndex = 0

start_btt =Button(ctrls_frame, text = "select starting text", borderwidth = 5, command= slide )

end_btn =Button(ctrls_frame, text = "select ending point", borderwidth = 5, command = slide2 )


end_btn.grid(row =1, column =3, padx=10) 
start_btt.grid(row =1, column =1 ,padx=10) 


confirm_btt = Button(ctrls_frame, borderwidth = 5 , text="confirm" , width=10 , command=confirmwindow)
confirm_btt.grid(row=1 , column=2)




app.mainloop()  #Makes an infinite loop to run the application
app.update_idletasks()  #Udates processes which are not running or stable
