import os
import speech_recognition as sr
from datetime import datetime

API_KEY = ''

class SpeechRecognizer:
    def __init__(self):
        os.makedirs("./out", exist_ok=True)
        self.path = f"./out/asr.txt"

        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()
        self.speech = []

        print("Listening surrounding!")
        self.rec.adjust_for_ambient_noise(source)
        return

    def grab_audio(self) -> sr.AudioData:
        print("Say something!")
        with self.mic as source:
            audio = self.rec.listen(source)
        return audio

    def recognize_audio(self, audio: sr.AudioData) -> str:
        print("Understanting!")
        try:
            speech = self.rec.recognize_whisper_api(audio, model='whisper-1', api_key=API_KEY))
        except sr.UnknownValueError:
            speech = "# Failed to recognize speech"
            print(speech)
        except sr.RequestError as e:
            speech = f"# Invalid request:{e}"
            print(speech)
        return speech

    def run(self):
        while True:
            audio = self.grab_audio()
            speech = self.recognize_audio(audio)

            if speech == "Thank you":
                print("Finishing!")
                break
            else:
                self.speech.append(speech)
                print(speech)

        with open(self.path, mode='w', encoding="utf-8") as out:
            out.write(datetime.now().strftime('%Y%m%d_%H:%M:%S') + "\n\n")
            out.write("\n".join(self.speech) + "\n")

if __name__ == "__main__":
    sp = SpeechRecognizer()
    sp.run()
