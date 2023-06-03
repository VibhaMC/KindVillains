import pyttsx3

def text(answer):
    text_speech=pyttsx3.init()

    #answer=input("Write text here!")
    text_speech.say(answer)
    text_speech.runAndWait()