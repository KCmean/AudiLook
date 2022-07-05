from tkinter import *

root = Tk()
root.title("Audio Editor - Slider")
root.geometry("400x400")

#While integrating codes put length of Audio instead of 'to_=400'
horizontal_slider = Scale(root, from_= 0, to=100, orient=HORIZONTAL)
horizontal_slider.pack()

def slide():
    horizontal_slider_label =  Label(root, text=horizontal_slider.get()).pack()

horizontal_slider_button = Button(root, text ="Confirm Audio point for editing", command=slide).pack()

root.mainloop()
root.update_idletasks()
