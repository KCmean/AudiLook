from pydub import AudioSegment
from pydub.playback import play

# import required module
# from playsound import playsound
  
# for playing note.wav file
# playsound('music1.mp3')
# print('playing sound using  playsound')


sound = AudioSegment.from_mp3("E:\\sem 2\python programming\python ptoject\music1.mp3")
play(sound)
