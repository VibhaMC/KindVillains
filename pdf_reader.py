import pyttsx3
import PyPDF2

textToSpeech=pyttsx3.init()
result=PyPDF2.PdfReader(r'C:\Vibha\3 rd SEMESTER\DSA\Theory\Data Structures and Applications A Simple and Systematic Approach by Padma Reddy (z-lib.org).pdf')
textToSpeech=pyttsx3.speak(result)
textToSpeech.runAndWait()