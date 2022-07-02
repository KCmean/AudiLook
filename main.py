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
    def trimMuisc(self,start , end):
        print("Enter the required values i.e the end and start time in minutes and seconds >>")
        self.start= start
        self.end  = end
            
list1= ['1.mp3', '2.mp3']
music = Music(list1)
music.displaymMsicSamples()
music.playMusicSample()



