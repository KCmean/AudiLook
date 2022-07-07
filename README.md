# Audio Player and Editor

Desigined a simple Audio editor in python
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.




## pydub 
```bash
pip install pydub
```
```import pydub ```

```from pydub import Audiosegment```

we used pydub module for audio maipulation and to perform actions like merging and cutting audios

## pygame
```bash
pip install pygame
```
```import pygame```

pygame to play sound although playsound can also be used for playing audios 

## Mutagen
```bash
pip install mutagen
```
```from mutagen.mp3 import MP3```

Muta gen to get the favourable format for our audios 

## Time
```bash
pip install time
```
```import time```

to sync the song with its lenght and to precisely cut the song on the basis of time elapsed

## Tkinter
```bash
pip install tk
```
```from tkinter import *```

```import tkinter.ttk as ttk```

```from tkinter import messagebox```

```from tkinter import filedialog```


Used tkinter to design the GUI of the app and to run various functions.


## Usage
Sample code(demonstrating how to pause/unpause the audio)
```python
#pause/unpause
global paused
paused = False   

def pause(is_paused):                          
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused= False
    else:
        pygame.mixer.music.pause()
        paused=True

```
## Owners
[Vedant Chavan](https://github.com/VedantChavan03)

[Kunal Chaturvedi](https://github.com/KCmean)


[Atharv Chandane](https://github.com/Atharv-Chandane)




## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

<hr>
##Thankyou

