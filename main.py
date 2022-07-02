class Music:
    def __init__(self,listofmusicsamples):
        self.availablemusic = listofmusicsamples

    def displaymMsicSamples(self):
        print("SAMPLE AUDIOS WE HAVE ARE:")
        print("=========================")
        for mu in self.availablemusic():
            print(mu)
    
    def playMusicSample(self):
        


