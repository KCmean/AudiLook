from playsound import playsound

class Music:
    def __init__(self,listofmusicsamples):
        self.availablemusic = listofmusicsamples

    def displaymMsicSamples(self):
        print("SAMPLE AUDIOS WE HAVE ARE:")
        print("=========================")
        for mu in self.availablemusic():
            print(mu)
    
    def playMusicSample(self):
        print("Enter which music sample you want to play from -->")
        self.sample = input()
        if self.sample in self.availablemusic:
            print("playing your sample:")
            playsound(self.sample)
        else:
            print("!!!PLEASE ENTER A CORRECT SAMPLE NAME!!!")



