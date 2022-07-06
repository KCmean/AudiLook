from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame
from tkinter import filedialog

app = Tk()
app.title(' Audio Cutter and Merger ')
app.geometry('700x600')

headingText  =  Label(app , text="MUSIC EDITOR AND PLAYER" ,font="Times 30 bold",pady=50)
headingText.pack()
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

def play_time():                               #time elapse
    song = playlist.get(ACTIVE)
    song= f"{song}.mp3"
    mut = MP3(song)
    l_song= mut.info.length

    song_length = time.strftime('%H:%M:%S', time.gmtime(l_song))

    Curr_time = pygame.mixer.music.get_pos()/1000
    mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(Curr_time))
    my_label.config(text = f"{mod_curr_time} / {song_length}")
    my_label.after(1000, play_time)

def add_song():                               #adding songs
    song = filedialog.askopenfilename(initialdir="audio/" , title="Choose a somg" , filetypes=(("mp3 files" , "*.mp3"),))
    print(song)


playlist= Listbox(app , bg= "grey", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
music= ["1.mp3","2.mp3","3.mp3"]
# music = music.replace("", "")
# music = music.replace(".mp3", "")
playlist.insert(END, music)


#cretaing list
my_menu = Menu(app)
app.config(menu=my_menu)

#add song 
addsong = Menu(my_menu)
my_menu.add_cascade(label="Add Song" , menu=addsong)
addsong.add_command(label="Add one song to playlist" , command=add_song)




my_label = Label(app, text = '', bd=1, anchor= E)
my_label.pack(pady =5 )



ctrls_frame=Frame(app)
ctrls_frame.pack()

play_img= PhotoImage(file= "play.png")
pause_img= PhotoImage(file = "pause.png")

play_btt = Button(ctrls_frame, image= play_img, borderwidth = 0, command = play )
pause_btt =Button(ctrls_frame, image = pause_img , borderwidth = 0, command = lambda : pause(paused))

play_btt.grid(row =0, column =1, padx=10) 
pause_btt.grid(row =0, column =3, padx=10) 




app.mainloop()
app.update_idletasks()
