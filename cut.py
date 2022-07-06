from tkinter import *
import tkinter.ttk as ttk
import time
from mutagen.mp3 import MP3
import pygame
from pydub import AudioSegment
from tkinter import messagebox



pygame.mixer.init()

cut = Tk()
cut.title('Cut')
cut.geometry('900x600')

def play():                                     #play 
    song = playlist1.get(ACTIVE)
    song = f'E:/sem 2/python programming/python ptoject/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    global paused
    paused = False
    my_label.config(text = '')
    horizontal_slider1.config(value = 0)
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
    

def play_time():
    song = playlist1.get(ACTIVE)
    song= f"E:/sem 2/python programming/python ptoject/audio/{song}.mp3"
    mut = MP3(song)
    global l_song
    l_song= mut.info.length

    song_length = time.strftime('%H:%M:%S', time.gmtime(l_song))

    Curr_time = pygame.mixer.music.get_pos()/1000
    mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(Curr_time))

    Curr_time+=1
    if int(horizontal_slider1.get())== int(l_song):
        my_label.config(text = f"{song_length} / {song_length}")

    elif paused:
        pass
    elif horizontal_slider1.get()== Curr_time:
        slider_pos= int(l_song)
        horizontal_slider1.config(to = slider_pos, value = 0) 
    
    else:
        slider_pos= int(l_song)
        horizontal_slider1.config(to = slider_pos, value = horizontal_slider1.get())
        
        mod_curr_time = time.strftime(f'%H:%M:%S', time.gmtime(int(horizontal_slider1.get())))

        my_label.config(text = f"{mod_curr_time} / {song_length}")

        nxt_time= horizontal_slider1.get() +1
        horizontal_slider1.config(value= nxt_time)


    # my_label.config(text = f"{mod_curr_time} / {song_length}")

    # horizontal_slider1.config(value= Curr_time)
    # horizontal_slider1.after(1000,play_time)
    my_label.after(1000, play_time)


def slider(x):
    song = playlist1.get(ACTIVE)
    song = f'E:/sem 2/python programming/python ptoject/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start= int(horizontal_slider1.get()))

def slide():
    global startIndex, startpt, start_pt
    start1 =int(horizontal_slider1.get())
    startIndex = start1*1000

    
    startpt = time.strftime(f'%H:%M:%S', time.gmtime(int(horizontal_slider1.get()-1)))
    # global start_pt
    start_pt =  Label(cut, text=f" Starting Point :{startpt}")
    start_pt.pack(pady=10)
    start_btt1['state']= DISABLED

def slide2():
    global endIndex, endpt, end_pt
    end1 = int(horizontal_slider1.get())
    endIndex =end1*1000
    if endIndex<= startIndex:
        messagebox.showerror("Invalid Value Detected", "End point is lesser than starting point")
        confirm_btt1['state']= DISABLED
        
    elif endIndex-startIndex <1000:
        messagebox.showerror("Length is too short", "Choose a greater length")
        confirm_btt1['state']= DISABLED
    else:
        confirm_btt1['state']= NORMAL

    endpt = time.strftime(f'%H:%M:%S', time.gmtime(int(horizontal_slider1.get()-1)))
    # global end_pt
    end_pt =  Label(cut, text=f" Ending Point :{endpt}")
    end_pt.pack(pady = 10)
    end_btt1['state']= DISABLED

def edit_st():
    start_pt.destroy()
    start_btt1["state"]= NORMAL

def edit_ed():
    end_pt.destroy()
    end_btt1["state"]= NORMAL

def cutting(Start, End, sound):
    slice = sound[Start:End]
    return slice


def confirmwindow():
    confirm_btt1 = Label(cut , text = f" Start Point: {startpt}\nEnd Point: {endpt}").pack()
    song = playlist1.get(ACTIVE)
    song1 = f'E:/sem 2/python programming/python ptoject/audio/{song}.mp3'
    sound= AudioSegment.from_mp3(song1)
    slice = cutting(startIndex, endIndex, sound)
    slice.export(f'1_cut.mp3' , format = "mp3")

def run(music):
    global playlist1, my_label, horizontal_slider1, start_btt1, end_btt1, confirm_btt1
    playlist1= Listbox(cut , bg= "black", fg = "green" , selectbackground= "white", selectforeground= "red" , width =60 )
    playlist1.pack(pady =30)
    music = music.replace("E:/sem 2/python programming/python ptoject/audio/", "")
    music = music.replace(".mp3", "")
    playlist1.insert(END, music)

    horizontal_slider1 = ttk.Scale(cut, from_= 0, to=100, length= 360, value=0, orient=HORIZONTAL, command = slider)              #slideer
    horizontal_slider1.pack()
    # horizontal_slide2r = ttk.Scale(cut, from_= 0, to=100, length= 360, orient=HORIZONTAL)                 
    # horizontal_slide2r.pack()

    my_label = Label(cut, text = '', bd=1, anchor= E)
    my_label.pack(pady =5 )

    ctrls_frame1=Frame(cut)
    ctrls_frame1.pack()

    # play_img= PhotoImage(file= "play1.png")
    # pause_img= PhotoImage(file = "pause1.png")

    play_btt1 = Button(ctrls_frame1, text = 'PLAY', borderwidth = 6, command = play )
    pause_btt1 =Button(ctrls_frame1, text = 'PAUSE' , borderwidth = 6, command = lambda : pause(paused))

    play_btt1.grid(row =1, column =1, padx=5) 
    pause_btt1.grid(row =1, column =3, padx=5) 

    start_btt1 =Button(ctrls_frame1, text = "Lock Start Point", borderwidth = 5, command= slide )
    end_btt1 =Button(ctrls_frame1, text = "Lock End Point", borderwidth = 5, command = slide2 )
    edit_start_btt1 = Button(ctrls_frame1, text = "Edit Starting Point", borderwidth = 5, command= edit_st)
    edit_end_btt1 = Button(ctrls_frame1, text = "Edit Ending Point", borderwidth = 5, command= edit_ed)



    end_btt1.grid(row =2, column =3, padx=10,pady =10) 
    start_btt1.grid(row =2, column =1 ,padx=10,pady =10) 
    edit_start_btt1.grid(row = 4, column=1, padx=10,pady =10)
    edit_end_btt1.grid(row = 4, column= 3, padx = 10,pady =10)

    confirm_btt1 = Button(ctrls_frame1, borderwidth = 5 , text="CONFIRM" , width=10 , command=confirmwindow)
    confirm_btt1.grid(row=5 , column=2)

    # quit_btt = Button(ctrls_frame1, text = "QUIT", bd= 5, command = cut.quit )
    # quit_btt.grid(row= 6, column= 5 , padx=10 )


    cut.mainloop()

