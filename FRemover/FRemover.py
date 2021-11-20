from google.cloud import speech_v1 as speech
from pygame import mixer
import time 
import threading
import winsound
import json

mixer.init()

class FRemover:
    def __init__(self, audiogcspath, audiopcpath):
        self.lowerwal = False
        self.sound = 0
        
        self.start = time.time()
        with open("AbusiveWords.txt") as abusive:
            lines = abusive.read()
            badwords = json.loads(lines)["words"]
            
        
        config = dict(language_code="en-US", audio_channel_count=2,  enable_word_time_offsets=True,
        )
        audio = dict(uri=audiogcspath)

        self.offsets = self.print_word_offsets(self.speech_to_text(config, audio)[1])
            
        lasttime = self.offsets[-1]
        lasttime = lasttime[1]
        lastfdetectedtime = 0
        fs = []
        for j in self.offsets:
            if j[2] in badwords:
                fs.append(j)
        fs = fs
        t1 = threading.Thread(target=self.playaudio, args=(audiopcpath,))
        t2 = threading.Thread(target=self.censor, args=(badwords,self.offsets))

        t1.start()
        t2.start()
        t1.join()
        t2.join()
  
            # Setting the volume
    

    def speech_to_text(self,config, audio):
        client = speech.SpeechClient()
        response = client.recognize(config=config, audio=audio)
        return self.print_sentences(response)


    def print_sentences(self, response):
        for result in response.results:
            best_alternative = result.alternatives[0]
            transcript = best_alternative.transcript
            confidence = best_alternative.confidence
            print("-" * 80)
            return [transcript, best_alternative]
        #print(f"Confidence: {confidence:.0%}")
        #print_word_offsets(best_alternative)

    def print_word_offsets(self, alternative):
        allofsets = []
        for word in alternative.words:
            start_s = word.start_time.total_seconds()
            end_s = word.end_time.total_seconds()
            word = word.word
            allofsets.append([start_s,end_s,word])
        return allofsets           



    def playaudio(self, audiopath):
        mixer.init()
        global sound
    
    # Loading the song
        sound = mixer.Sound(audiopath)
   
                # Setting the volume
        sound.set_volume(0.7)
    

                # Start playing the song
        sound.play()
        
    def censor(self, badwords, offsets):
        import time 
        starttime = time.time()
        nextindex = 0
                # Setting the volume
    

        print(offsets)        
        global sound 
            
        lasttime = offsets[-1]
        lasttime = lasttime[1]
        lastfdetectedtime = 0
        fs = []
        for j in offsets:
            if j[2] in badwords:
                fs.append(j)
    
        #for i in offsets:
        #   if i[2] in badwords:
            
                #lastfdetectedtime = i[1]-lastfdetectedtime
                #time.sleep(lastfdetectedtime)
                # Start playing the song
                #bsound.play()
                #sound.set_volume(0)
                #time.sleep(int(round(i[1]-i[0])))
                #print(i[1]-i[0])
                #sound.set_volume(1)
                #bsound.set_volume(0)
                #time.sleep(lasttime-i[1])

        for i in fs:
        
        
            time.sleep(i[0] - lastfdetectedtime)
            lastfdetectedtime = i[1]
            print(time.time()-starttime)
            sound.set_volume(0)
            print(lastfdetectedtime+i[0])
        
            winsound.Beep(2500, int((i[1]-i[0])*1000))
        
        
            sound.set_volume(1)
        
            nextindex+=1
            lasttimes = offsets[-1]
            lasttimes = lasttimes[1]
            if i == fs[-1]:
                time.sleep(lasttimes-i[1])


##FRemover("gs://audiosforgdetectorandbeeper1231/Recording-16.flac",r'C:\Users\Dell\Downloads\Recording-16.flac')