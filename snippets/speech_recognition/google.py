import speech_recognition as sr

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
    print("Google thinks you said " + r.recognize_google(audio, language="en-US"))
except sr.UnknownValueError:
    print("Google could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google; {e}")
