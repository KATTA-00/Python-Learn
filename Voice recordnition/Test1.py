import speech_recognition
import pyttsx3

recognition = speech_recognition.Recognizer()

while True:

    try:
        with speech_recognition.Microphone() as mic:
            recognition.adjust_for_ambient_noise(mic,duration = 0.2)
            audio = recognition.listen(mic)

            text = recognition.recognize_google(audio)
            text = text.lower()

            print(text)

    except speech_recognition.UnknownValueError():

        recognition = speech_recognition.Recognizer()
        continue