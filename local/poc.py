from core import audio
from core import generative


class LocalPoc():

    def run(self):
        script = audio.speech_to_text()
        if not script:
            return

        response = generative.chat(script)
        # audio.text_to_speech(response)
