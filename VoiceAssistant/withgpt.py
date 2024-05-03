import os, time, playsound, openai
import speech_recognition as sr
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')


while True:

    convo_memory = []
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
                {"role": "system", "content": "Your are a nice person who enjoys having conversation. "},
                {"role": "user", "content": text}],
                temperature = 0.1, max_tokens = 1000)

        response = completion.choices[0].message.content
        convo_memory.append({"role": "user", "content": text})
        convo_memory.append({"role": "user", "content": response})
        return response

    text = get_audio()
    reply = get_response()

    if text.lower() == "i'm done":
        break
    else:
        speak(reply)







