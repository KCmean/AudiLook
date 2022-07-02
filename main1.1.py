from pydub import Audiosegment
from playsound import playsound 

def cut(Start, End, sound):
    slice = sound[Start:End]
    return slice

def merge(*slices):
    merge =0
    for i in slices:
        merge += i
    return merge
slices = []
n=1
while n!=0:
    n = int(input())
    if n==0:
        break
    start_min, start_sec=  map(int , input("\n Enter the starting point as (1(mins) 30(secs)) : "))
    end_min, end_sec = map(int, input("\n Enter the ending point as (1(mins) 30(secs)) : ") )
    start = start_min*60000 + start_sec*1000
    end = end_min*60000 + end_sec*1000
    sound= Audiosegment.from_mp3("1.mp3")
    slice = cut(start, end , sound)
    slices.append(slice)
