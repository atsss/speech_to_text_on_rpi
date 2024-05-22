import os
import speech_recognition as sr
from datetime import datetime
from concurrent import futures

API_KEY = ''

class SpeechRecognizer:
    def __init__(self):
        os.makedirs("./out", exist_ok=True)
        self.path = f"./out/asr.txt"

        self.rec = sr.Recognizer()
        self.mic = sr.Microphone()

        self.pool = futures.ThreadPoolExecutor(thread_name_prefix="Rec Thread")
        self.speech = []

    def recognize_audio_thread_pool(self, audio, event=None):
        future = self.pool.submit(self.recognize_audio, audio)
        self.speech.append(future)

    def grab_audio(self) -> sr.AudioData:
        print("Say something!")
        with self.mic as source:
            audio = self.rec.listen(source)
        return audio

    def recognize_audio(self, audio: sr.AudioData) -> str:
        print("Understanting!")
        try:
            speech = self.rec.recognize_whisper_api(audio, model='whisper-1', api_key=API_KEY)
        except sr.UnknownValueError:
            speech = "# Failed to recognize speech"
            print(speech)
        except sr.RequestError as e:
            speech = f"# Invalid request:{e}"
            print(speech)
        return speech

    def run(self):
        print("Listening surrounding!")
        with self.mic as source:
            self.rec.adjust_for_ambient_noise(source, duration=5)

        try:
            while True:
                audio = self.grab_audio()
                self.recognize_audio_thread_pool(audio)
        except KeyboardInterrupt:
          print("Finished")
        finally:
            with open(self.path, mode='w', encoding="utf-8") as out:
                futures.wait(self.speech)

                for future in self.speech:
                    print(future.result())
                    out.write(f"{future.result()}\n")

if __name__ == "__main__":
    sp = SpeechRecognizer()
    sp.run()
