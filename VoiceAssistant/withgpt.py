import os, time, playsound, openai
import speech_recognition as sr
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

is_looping = True

# while is_looping == True:

def speak(text):
    tts = gTTS(text=text, lang="en", tld='com.au')
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)

        except Exception as e:
            print("Exception" + str(e))

    return said

def get_response():
    completion = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [
            {"role": "system", "content": "Your are a nice person who enjoys having conversation."},
            {"role": "user", "content": text}],
            temperature = 0.1, max_tokens = 1000)

    response = completion.choices[0].message.content
    return response

text = get_audio()

reply = get_response()

    # if "i'm done" in text:
    #     break
    # else:
speak(reply)







