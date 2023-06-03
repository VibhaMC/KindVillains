import test2
import sys
sys.path.insert(0, r'C:\Users\mcvan\PycharmProjects\emotionDetection')
import emotion_detect
import main2
import text_speech
import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="SpecialTreatment",page_icon=":innocent",layout="wide")

def load_lottieurl0(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def load_lottieurl2(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def load_lottieurl3(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

def load_lottieurl4(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#lottie url
lottie_coding0= load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_f8nlBX3HyP.json")


#header
with st.container():
    st.subheader("Find ways to make your life easier!")
    st.title("SpecialTreatment ⬆")
    st.write("#Inclusivity")
    st_lottie(lottie_coding0,height=400,key="hands")

# Create a menu using Streamlit option menu
option = st.sidebar.selectbox(
    'Select an option',
    ('choose an option','Blind Assist', 'ASL', 'Text to Speech')
)

# Based on the selected option, call the respective function
if option == 'Blind Assist':
    main2.object_detect()
elif option == 'ASL':
    test2.webcam1()
elif option == 'Text to Speech':
    input = st.text_input("Enter the text here")
    result3 = text_speech.text(input)
