from ..core import audio
from ..core import generative


class LocalPoc():

    def run(self):
        record = audio.record_audio()
        script = audio.speech_to_text(record)
        response = generative.chat(script)
        audio.text_to_speech(response)
