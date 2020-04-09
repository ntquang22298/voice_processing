import argparse
import tempfile
import queue
import sys


try:
    import sounddevice as sd
    import soundfile as sf
    import numpy
    assert numpy
    import nltk.data
    import codecs
    import os
    import time
    from scipy.io.wavfile import write
    doc = codecs.open('./Thegioi/text', 'r', 'utf-8')
    content = doc.read()
    i = 11
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    for sentence in tokenizer.tokenize(content):
        file_name = 'Thegioi_sent' + str(i)
        i = i+1
        print(sentence)
        print('\n recording.....\n')
        fs = 48000
        duration = 15
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        write(file_name + '.wav', fs, myrecording)
        print('\n end record.....\n')
        time.sleep(3)


except Exception as e:
    print(e)
