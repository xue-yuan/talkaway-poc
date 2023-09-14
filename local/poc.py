from core import audio
from core import generative


class LocalPoc():

    def run(self):
        script = audio.speech_to_text()
        response = generative.chat(script)
        audio.text_to_speech(response)
