import speech_recognition as sr

API_KEY = ''

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(device_index=0) as source:
    print("Listening surrounding!")
    r.adjust_for_ambient_noise(source,duration=5)
    print("Say something!")
    audio = r.listen(source)
    print("Understanting!")

# recognize speech using whisper
try:
    print("Whisper thinks you said " + r.recognize_whisper_api(audio, model='whisper-1', api_key=API_KEY))
except sr.UnknownValueError:
    print("Whisper could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Whisper; {e}")
