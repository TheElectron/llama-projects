import speech_recognition as sr
import pyttsx3

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def record_text(self):
            try:
                with sr.Microphone() as input:
                    self.recognizer.adjust_for_ambient_noise(input, duration=0.2)
                    print("Say something!")
                    audio = self.recognizer.listen(input)
                    return self.recognizer.recognize_sphinx(audio)
            except sr.RequestError as e:
                print(e)
            except sr.UnknownValueError as e:
                print(e)

    def output_text(self, text_input):
        f = open("output.txt", "a")
        f.write(text_input)
        f.write("\n")
        f.close()


aux = SpeechToText()
while True:
    text = aux.record_text()
    aux.output_text(text)
    