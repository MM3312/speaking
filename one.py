"""from flask import Flask
app = Flask(__name__)

@app.route('/')
def myfun():
    return "hello world"

if __name__ == "__main__":
    app.run()"""
import pyttsx3
from PyDictionary import PyDictionary
class Speak:
    def read(self,audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')

        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait()

class Tell:
    def dic(self):
        speak = Speak()
        dis= PyDictionary()
        print("which word do u want to find the meaning")
        speak.read("which word do u want to find the meaning")

        inp=str(input())
        word =dis.meaning(inp)
        print(len(word))

        for state in word:
            print(word[state])
            speak.read("the meaning is "+str(word[state]))
        
if __name__ =="__main__":
    Tell()
    Tell.dic(self=None)