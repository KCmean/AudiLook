from pydub import AudioSegment
from playsound import playsound


class Music:
    def __init__(self,listofmusicsamples):
        self.availablemusic=[]
        for i in listofmusicsamples:
           self.availablemusic.append(i)
        print(self.availablemusic)
    def displaymMsicSamples(self):
        print("\nSAMPLE AUDIOS WE HAVE ARE:")
        print("\n=========================")
        i=1
        for a in self.availablemusic:
            print(f"{i}) {a}")
            i+=1
    
    def playMusicSample(self):
        print("Enter which music sample you want to play from -->")
        self.sample = input()
        if self.sample in self.availablemusic:
            print("playing your sample:")
            playsound(self.sample)
        else:
            print("!!!PLEASE ENTER A CORRECT SAMPLE NAME!!!")
    

class musicEdit:
    def __init__(self, start, end, sound ,slices):
        self.start= start
        self.end  = end
        self.slices = slices
        self.sound =sound
    def cut(self):
        slice = self.sound[self.start:self.end]
        return slice

    def merge(self):
        merge =0
        for i in self.slices:
            merge += i
        return merge
slices = []

list1=[ '1.mp3', '2.mp3', '3.mp3']
obj = Music(list1)
obj.displaymMsicSamples()
obj.playMusicSample()

start_min, start_sec=  map(int , input("\n Enter the starting point as (1(mins) 30(secs)) : ").split(' '))
end_min, end_sec = map(int, input("\n Enter the ending point as (1(mins) 30(secs)) : ").split(' ') )
start = start_min*60000 + start_sec*1000
end = end_min*60000 + end_sec*1000

sound= AudioSegment.from_mp3("1.mp3")
slice = musicEdit(start, end, sound, slices)
slice.cut()
slices.append(slice)
slice.export("3.mp3" , format = "mp3")



