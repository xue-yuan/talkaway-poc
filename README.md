# Installation

**Prerequisite:**

- MacOS(Unsure if it works on other OS)
- Python Interpreter: `python 3.10^`
- Package Manager: `poetry 1.6.1`
- Apply OpenAI's [secret key](https://platform.openai.com/account/api-keys)

```shell
# create new environment
python -m venv venv

# activate
source venv/bin/activate

# deactivate
deactivate

# install all packages
poetry install

# copy example config file as config.py and fill your secret key
cp config.py.example config.py
```

# Usage

```shell
python main.py [local|remote]
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

  - [OpenAI](https://github.com/openai/openai-python)

- TTS (Text to Speech)

# Note

1. [web recorder](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/mediaDevices)
