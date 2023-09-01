import speech_recognition as sr


def speech_to_text() -> str:
    # device list may be different
    print(sr.Microphone.list_microphone_names())

    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return ""


def text_to_speech(text: str):
    ...
