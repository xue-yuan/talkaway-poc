# Installation

**Prerequisite:**

- Python Interpreter: `python 3.10^`
- Package Manager: `poetry 1.6.1`

```shell
# create new environment
python -m venv venv

# activate
source venv/bin/activate

# deactivate
deactivate

# install all packages
poetry install
```

# Workflow

## Remote(Web, Mobile)

Client ->(send audio) STT -> G-AI ->(send text) Client(TTS, play audio)

## Local

Record Audio -> STT -> G-AI -> TTS

# Tech Stack

- STT (Speech to Text)

  - [SpeechRecognition](https://github.com/Uberi/speech_recognition)

- Generative AI

- TTS (Text to Speech)

# Note

1. [web recorder](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/mediaDevices)
