#audio cutter trial 1
from pydub import AudioSegment
from playsound import playsound
sound = AudioSegment.from_mp3("1.mp3")
# AudioSegment.converter = "ffmpeg.exe"
# AudioSegment.ffmpeg = "ffmpeg.exe"
# AudioSegment.ffprobe = "ffprobe.exe"

StartMin=0 
StartSec=0
EndMin=1
EndSec=30
StartMin1=2 
StartSec1=30
EndMin1=3
EndSec1=30


Start= StartMin*60*1000 + StartSec*1000
ENd= (EndMin*60*1000 + EndSec*1000) -1000

Start1= StartMin1*60*1000 + StartSec1*1000
End1= (EndMin1*60*1000 + EndSec1*1000) -1000

extract1 = sound[Start1:End1]
extract = sound[Start:ENd]
ex = (extract) + (extract1)
ex.export("3.mp3", format = "mp3")

playsound("3.mp3")

#click on terminal then ctrl+c to stop playing
