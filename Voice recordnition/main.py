import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source :
    print("Speak Anything : ")
    audio = r.listen(source)

    try :
        text = r.recognize_google(audio)
        print(text)
    except:
        print(111111111111)