# Importing Modules
from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame
from tkinter import messagebox
from tkinter import filedialog
from pydub import AudioSegment



#setting up
app = Tk()
app.title(' Audio Player ')
app.geometry('900x600')
app['bg']= 'black'

background = PhotoImage(file = "playerBg.png")
labelBG = Label(app , image = background)
labelBG.place(x = 0,y = 0)

#Heading text
headingText  =  Label(app , text="MUSIC EDITOR AND PLAYER" ,fg = "White" , font="  Times 30 bold", bg = "#09021E" ,pady=20)
headingText.pack(pady = 30)
pygame.mixer.init()

#play 
def play():     
    global stopped
    stopped = False                              
    song = playlist.get(ACTIVE)
    song = f'E:/sem 2/python programming/python ptoject/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    global paused
    paused = False
    my_label.config(text = '')
    horizontal_slider.config(value = 0)
    play_time()

global paused
paused = False   

#pause/unpause
def pause(is_paused):                          
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.pause()
        paused=True
    
    
global stopped
stopped = False
def stop():
    pygame.mixer.music.stop()
    playlist.select_clear(ACTIVE)
    my_label.config(text = '')
    horizontal_slider.config(value = 0)
    global stopped
    stopped = True

def slider(x):
    song = playlist.get(ACTIVE)
    song = f'E:/sem 2/python programming/python ptoject/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start= int(horizontal_slider.get()))


#time elapse
def play_time():
    if stopped:
        return
    song = playlist.get(ACTIVE)
    song= f"E:/sem 2/python programming/python ptoject/audio/{song}.mp3"
    mut = MP3(song)
    global l_song
    l_song= mut.info.length

    song_length = time.strftime('%H:%M:%S', time.gmtime(l_song))

    Curr_time = pygame.mixer.music.get_pos()/1000
    mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(Curr_time))

    Curr_time+=1
    if int(horizontal_slider.get())== int(l_song):
        my_label.config(text = f"{song_length} / {song_length}")

    elif paused:
        pass
    elif horizontal_slider.get()== Curr_time:
        slider_pos= int(l_song)
        horizontal_slider.config(to = slider_pos, value = 0) 
    
    else:
        slider_pos= int(l_song)
        horizontal_slider.config(to = slider_pos, value = horizontal_slider.get())
        
        mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(int(horizontal_slider.get())))

        my_label.config(text = f"{mod_curr_time} / {song_length}")

        nxt_time= horizontal_slider.get() +1
        horizontal_slider.config(value= nxt_time)

    my_label.after(1000, play_time)

def cutWindowOpen():    
        
        import cut
        music = playlist.get(ACTIVE)
        cut.run(music)

def mergeWindowOpen():
    import merge


#adding songs
def add_song():                               
    songadd = filedialog.askopenfilename(initialdir="audio/" , title="Choose a song" , filetypes=(("mp3 files" , "*.mp3"),))
    songadd = songadd.replace("E:/sem 2/python programming/python ptoject/audio/","")
    songadd = songadd.replace(".mp3","")
    playlist.insert(END,songadd)



#musicbox

playlist= Listbox(app , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
playlist.pack(pady =30)
music= "E:/sem 2/python programming/python ptoject/audio/1.mp3"
music = music.replace("E:/sem 2/python programming/python ptoject/audio/", "")
music = music.replace(".mp3", "")
playlist.insert(END, music)


#cretaing list
my_menu = Menu(app)
app.config(menu=my_menu)

#add song 
addsong = Menu(my_menu)
my_menu.add_cascade(label="Add Song" , menu=addsong)
addsong.add_command(label="Add one song to playlist" , command=add_song)



my_label = Label(app, text = '',fg = "White" , bg = "#09021E", bd=1, anchor= E)
my_label.pack(pady =1 )

#slider
horizontal_slider = ttk.Scale(app, from_= 0, to=100, length= 360, value=0, orient=HORIZONTAL, command = slider)             
horizontal_slider.pack(pady = 10)


ctrls_frame=Frame(app)
ctrls_frame.pack(pady = 20)

# play and pause buttonn
play_img= PhotoImage(file= "play.png")
pause_img= PhotoImage(file = "pause.png")
stop_img = PhotoImage(file='stop.png')

# Creating Buttons
play_btt = Button(ctrls_frame, image= play_img, borderwidth = 0, command = play )
pause_btt =Button(ctrls_frame, image = pause_img , borderwidth = 0, command = lambda : pause(paused))
stop_btt = Button(ctrls_frame, image= stop_img ,borderwidth=0, command=stop)
cutt_btt = Button(ctrls_frame , text="CUT/TRIM AUDIO",fg = "White" , bg = "#09021E",  borderwidth=5 , command= cutWindowOpen)
merge_btt = Button(ctrls_frame , text="MERGE AUDIO",fg = "White" , bg = "#09021E", borderwidth=5 , command= mergeWindowOpen)


# Placing Buttons
play_btt.grid(row =0, column =1, padx=10) 
pause_btt.grid(row =0, column =2, padx=10) 
stop_btt.grid(row =0, column=3, padx= 10)
cutt_btt.grid(row =1, column = 2, padx= 10,pady=10)
merge_btt.grid( row =2, column =2 , padx = 10, pady =10)

app.mainloop()
app.update_idletasks()