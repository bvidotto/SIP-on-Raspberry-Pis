# -*- coding: utf-8 -*-
"""
File: AudioLatency.py
Author: Benoît Vidotto
Date: Q2/Q3 2021
"""


""" 
This python file provides all the codes needed to measure the latency 
and its fft (Fast Fourier Transform). To do this, this script has 
3 parts to be launched individually.
The 1st part plays the selected audio, receives the audio via the PC's microphone, 
    saves the result in .wav format and displays it graphically using 
    matplotlib.
The 2nd part allows you to close open streams in the event of SIP 
    communication should fail, so that the 1st part can be restarted cleanly.
The 3rd part serves the same purpose as the 1st part, except that several audio files
    files will be launched one after the other.

Translated with DeepL.com (free version)
"""

#%% latencyfreqtest

"""PyAudio Example: Play a wave file (callback version)."""
"""Sources : http://people.csail.mit.edu/hubert/pyaudio/
            https://github.com/google/audio-sync-kit
"""
""" 
To run this script on Windows, the default device for the SIP application on the PC must be Stereo Mix. 
the PC must be Stereo Mix, so that the sound played on the PC is transmitted to the SIP communication.
The Sip phone under test must be connected to the PC via a jack cable and a Y splitter.
The default Windows recording device should be the jack socket on which the
the audio result will be recorded
"""

import pyaudio
import wave
import numpy as np
import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5

path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests"
# file = r"\audio_fs_48khz_b_128__freq_1000hz.wav"
file = r"\audio_az_8KHz.wav"
# file = r"\raspberry_fs_48khz_b_128__freq_300to3400hz.wav"
wf = wave.open(path+file, 'rb')
length = wf.getnframes()/wf.getframerate()
p = pyaudio.PyAudio()

# define callback (2)
def callback(in_data, frame_count, time_info, status):
    data = wf.readframes(frame_count)
    return (data, pyaudio.paContinue)

# open stream using callback (3)
""" Cette ligne ouvre le stream pour jouer l'audio dans le background (callback)"""
streamRX = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)
""" Cette ligne ouvre le stream pour lancer l'enregistrement du microphone"""
streamTX = p.open(format=pyaudio.paInt16,
                channels=CHANNELS,
                rate=RATE, #wf.getframerate(),
                input=True,
                output=False)                

signal = []
# start the stream (4)
print("Starting stream")
streamRX.start_stream()
a = datetime.datetime.now()

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = streamTX.read(CHUNK)
    if max(np.frombuffer(data,dtype=np.int16)) > 5000:
        b = datetime.datetime.now()
        print('The stream has been received and latency will be mesured.')
        break

while (datetime.datetime.now() - a).total_seconds() < length:
    data = streamTX.read(CHUNK)
    """La condition ci-dessous est utile pour les fichiers audio pour lesquels 
    le volume reste élevé durant toute la durée du fichier. Cette condition est à éliminer 
    (placer en commentaire) s'il s'agit plutôt d'un enregistrement de voix humaine."""
    # if max(np.frombuffer(data,dtype=np.int16)) < 1000:
    #     break
    signal.append(data)
    
c = b - a
print('Latency: ' + str(c.total_seconds()) + ' s')

# stop stream (6)
streamRX.stop_stream()
streamRX.close()
streamTX.stop_stream()
streamTX.close()

# close PyAudio (7)
p.terminate()

# WAVE_OUTPUT_FILENAME_TX = "zycoo"+file[6:]
"""The recording of the microphone will be saved under this name below."""
"""L'enregistrement du microphone sera sauvegarder sous le nom défini ci-dessous."""
"""Zycoo est le nom de l'appareil mesuré par le script."""
WAVE_OUTPUT_FILENAME_TX = "terra11_"+file[1:]

wf = wave.open(WAVE_OUTPUT_FILENAME_TX, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(signal))
wf.close()

"""If you wish to visualise the audio sent on the graph of the audio received, uncomment these lines"""
"""Si vous voulez voir l'audio envoyé sur le graphique de l'audio reçu, décommentez les lines ci-dessous"""
# sampFreq, signal = wavfile.read(path+file)
# fft_spectrum = np.fft.rfft(signal)
# freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
# fft_spectrum_abs = np.abs(fft_spectrum)
# plt.plot(freq[:], fft_spectrum_abs[:], label = "Reference")

fileName = WAVE_OUTPUT_FILENAME_TX
sampFreq, signal = wavfile.read(fileName)
signal = signal[:,0]
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)
plt.plot(freq[:], fft_spectrum_abs[:], 'r', label = 'SIPphone')


plt.figtext(0.5, 0.7, 'Latency: ' + str(c.total_seconds()))
"""Si vous affichez la référence, décommentez cette ligne pour afficher la légende et 
    les différencier sur le graphique"""
# plt.legend() 
plt.xlim(left = -500) #, right = 5000)
plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")
plt.title(fileName)
plt.show()

#%% Close streams

# stop stream (6)
streamRX.stop_stream()
streamRX.close()
streamTX.stop_stream()
streamTX.close()

# close PyAudio (7)
p.terminate()

#%% test multiple files


"""PyAudio Example: Play a wave file (callback version)."""
"""Sources : http://people.csail.mit.edu/hubert/pyaudio/
            https://github.com/google/audio-sync-kit
"""

import pyaudio
import wave
import numpy as np
import datetime
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RECORD_SECONDS = 5

path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\audio"
"""Voici la liste des fichiers qui vont être testés sur un appareil"""
# files = [r"\audio_fs_48khz_b_128__freq_300to3400hz",r"\audio_fs_48khz_b_128__freq_1000hz"]#,r"\audio_MsgTestFR"]
files = [r"\audio_fs_8khz_b_128__freq_300to3400hz", r"\audio_fs_8khz__freq_1khz"]
for x in files:

    file = x+".wav"
    wf = wave.open(path+file, 'rb')
    RATE = 44100
    length = wf.getnframes()/wf.getframerate()
    

    p = pyaudio.PyAudio()
    
    # define callback (2)
    def callback(in_data, frame_count, time_info, status):
        data = wf.readframes(frame_count)
        return (data, pyaudio.paContinue)
    
    # open stream using callback (3)
    streamRX = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True,
                    stream_callback=callback)
    
    streamTX = p.open(format=pyaudio.paInt16,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    output=False)                
    
    signal = []
    # start the stream (4)
    print("Starting stream")
    streamRX.start_stream()
    a = datetime.datetime.now()
    
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = streamTX.read(CHUNK)
        # frames.append(data)
        #print(max(np.frombuffer(data,dtype=np.int16)))
        if max(np.frombuffer(data,dtype=np.int16)) > 5000:
            print('ok')
            b = datetime.datetime.now()
            break
    
    while (datetime.datetime.now() - a).total_seconds() < length:
        data = streamTX.read(CHUNK)
        if max(np.frombuffer(data,dtype=np.int16)) < 1000 and (x != r"\audio_az_8KHz" or x!= r"\audio_MsgTestFR") :
            break
        signal.append(data)
        
    c = b - a
    print('Latency: ' + str(c.total_seconds()) + ' s')
    
    
    
    # stop stream (6)
    streamRX.stop_stream()
    streamRX.close()
    streamTX.stop_stream()
    streamTX.close()
    
    # close PyAudio (7)
    p.terminate()
    
    # WAVE_OUTPUT_FILENAME_TX = "zycoo"+file[6:]
    WAVE_OUTPUT_FILENAME_TX = "zycoo7_"+file[1:].replace('audio_', '')
    
    wf = wave.open(WAVE_OUTPUT_FILENAME_TX, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(signal))
    wf.close()
    
    input("continue?")
    """si la communication est arrétée en l'absence de son, il vaut mieux utiliser 
    la ligne ci-dessus que celle ci-dessus"""
    # time.sleep(2)
