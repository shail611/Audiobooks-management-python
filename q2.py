import pyttsx3
import keyboard
import os


# init function to get an engine instance for the speech synthesis
class playing:

    def __init__(self,name):
        engine = pyttsx3.init()
        s = "books/"+name+".text"

        fp = open(s, errors="ignore")
        mytext="You are listening to "+name+"\n\n "
        for line in fp:
            mytext+=line.strip()

        engine.save_to_file(mytext,'audio.mp3')

        # run and wait method, it processes the voice commands.
        engine.runAndWait()
        os.system('audio.mp3')
        os.remove('audio.mp3')

class q:
    def __init__(self,name):
        pl = playing(name)
