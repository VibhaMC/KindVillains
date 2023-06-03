import pyttsx3

def text(object,distance):
#def text():
    text_speech=pyttsx3.init()

    #answer=input("Write text here!")

    output = "Object " + object + " detected at distance " + distance + " meters"

    text_speech.say(output)
    text_speech.runAndWait()
