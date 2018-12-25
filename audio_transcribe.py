#!/usr/bin/env python3

# https://github.com/Uberi/speech_recognition/blob/master/examples/audio_transcribe.py

import sys
from os import path
import speech_recognition as sr
from io import BytesIO, StringIO

AUDIO_FILE = sys.argv[1]

# transcode non-wave files
if not AUDIO_FILE.lower().endswith(".wav"):
    from pydub import AudioSegment
    sound = AudioSegment.from_file(AUDIO_FILE)
    AUDIO_FILE = "temp.wav"
    sound.export(AUDIO_FILE, format="wav")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
try:
    print("Sphinx thinks you said: " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
