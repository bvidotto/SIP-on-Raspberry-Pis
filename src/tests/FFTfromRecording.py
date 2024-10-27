# -*- coding: utf-8 -*-
"""
File: FFTfromRecording.py
Author: Benoît Vidotto
Date: Q2/Q3 2021
"""


"""
Ce fichier python permet de visualiser la fft d'un fichier audio.
La 1ère partie crée un graphique statique avec matplotlib d'un fichier audio
La 2ième partie crée un graphique interactif à l'aide de plotly
La 3ième partie crée un graphique interactif de multiples appareils sur un 
    fichier audio afin de pouvoir comparer les appareils.
La 4ième partie crée plusieurs graphiques interactifs de multiples appareils 
    sur base de multiple fichiers audio et les enregistre au format html.
Il est possible de sauvegarder les graphiques interactifs plotly au format html 
    pour les visualiser plus tard.
"""
#%% get FFT of .wav signal

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def computeFFT(path, filename):
    sampFreq, signal = wavfile.read(path+fileName)
    if signal.shape[1] == 2:
        signal = signal[:,0]
    fft_spectrum = np.fft.rfft(signal)
    freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
    fft_spectrum_abs = np.abs(fft_spectrum)
    return freq, fft_spectrum_abs

"""Ici, on choisit les fichiers à visualiser: les fichiers commencent par le 
nom de l'appareil ou "audio" et sont suivi par différents paramètres qui sont 
les mêmes pour "audio" ou pour les appareils"""
# fileName = 'outputRX.wav'
# fileName = r"C:\Users\bevid\Documents\Enregistrements audio\Enregistrement (3).m4a"
# path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\TestsS5"
path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests"

device = ['raspberry', 'zycoo', 'terra'][2] + '_'
audio = 'audio_'
file = r"\fs_48khz__freq_20to20khz.wav"
# file = "az_8KHz.wav"

fileName = r"\\" + device + file
sampFreq, signal = wavfile.read(path+r"\\S7"+fileName)
signal = signal[:,0]
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)
plt.plot(freq[:], fft_spectrum_abs[:], 'r', label = 'SIPphone')
plt.title(fileName[1:-4])

"""Pour afficher le fichier audio initial, décommenter les lignes ci-dessous"""
# fileName = r"\\" + audio + file
# sampFreq, signal = wavfile.read(path+fileName)
# fft_spectrum = np.fft.rfft(signal)
# freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
# fft_spectrum_abs = np.abs(fft_spectrum)
# plt.plot(freq[:], fft_spectrum_abs[:], label = 'Reference')
# plt.legend()

"""Différentes options qui peuvent être pour améliorer le graphique"""
# plt.ylim(bottom = 0.01, top=100*10**8)
# plt.xticks(np.arange(min(freq[:]), max(freq[:])+1, 500.0))
# plt.xlim(left = -500, right=4000)
# plt.grid(axis = 'x')
# plt.xscale( 'log' )

plt.xlabel("frequency, Hz")
plt.ylabel("Amplitude, units")

plt.show()

#%%Interactive chart

import numpy as np
from scipy.io import wavfile
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default='browser'


# fileName = 'outputRX.wav'
# fileName = r"C:\Users\bevid\Documents\Enregistrements audio\Enregistrement (3).m4a"
# path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\TestsS5"
path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\S7"
# fileName = r"\audio_fs_48khz__freq_20to20khz.wav"
device = ['raspberry', 'zycoo', 'terra'][0] + '_'
audio = 'audio_'
file = "fs_48khz_b_128__freq_500hz.wav"

fig = go.Figure()

fileName = r"\\" + device + file
sampFreq, signal = wavfile.read(path+fileName)
signal = signal[:,0]
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)

fig.add_trace(
    go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
    name=device[:-1]))

fig.update_layout(
    title_text=fileName[1:-4]
)

"""Les lignes ci-dessous affichent le fichier audio original (référence)"""
fileName = r"\\" + audio + file
sampFreq, signal = wavfile.read(path+fileName)
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)

fig.add_trace(
    go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
    name="Reference"))

"""Pour enregistrer le graphique dans un fichier html, décommenter la ligne ci-dessous"""
# fig.write_html(path + "\\All_" + file[:-4] + ".html")

fig.show()



#%% Interactive compare devices

"""
    https://stackoverflow.com/questions/68894919/how-to-set-the-values-of-args-and-args2-in-plotlys-buttons-in-updatemenus
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default='browser'

def scatterDevice(device, file):
    fileName = r"\\" + device + file
    sampFreq, signal = wavfile.read(path+fileName)
    signal = signal[:,0]
    fft_spectrum = np.fft.rfft(signal)
    freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
    fft_spectrum_abs = np.abs(fft_spectrum)
    fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name=device[:-1]))
    return freq, fft_spectrum_abs

# fileName = 'outputRX.wav'
# fileName = r"C:\Users\bevid\Documents\Enregistrements audio\Enregistrement (3).m4a"
# path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\TestsS5"
path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\S7"
# fileName = r"\audio_fs_48khz__freq_20to20khz.wav"
devices = ['raspberry', 'zycoo', 'terra']
audio = 'audio_'
file = "fs_8khz__freq_1khz.wav"
# file = 'az_8KHz.wav'
# file = "MsgTestFR.wav"

fig = go.Figure()

fileName = r"\\" + audio + file
sampFreq, signal = wavfile.read(path+fileName)
fft_spectrum = np.fft.rfft(signal)
freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)

fig.add_trace(
    go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
    name="Reference"))

"""Les appareils à afficher sont définis dans 'devices'"""
for i in range(3):
    scatterDevice(devices[i]+'_',file)
    
"""Les lignes ci-dessous affichent le fichier audio original (référence)"""
# fileName = r"\\" + device + file
# sampFreq, signal = wavfile.read(path+fileName)
# signal = signal[:,0]
# fft_spectrum = np.fft.rfft(signal)
# freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
# fft_spectrum_abs = np.abs(fft_spectrum)
# # plt.plot(freq[:], fft_spectrum_abs[:], 'r', label = 'SIPphone')
# # plt.title(fileName[1:-4])
# fig.add_trace(
#     go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
#     name=device[:-1]))

fig.update_layout(
    title_text=file[:-4]
)


# fig.write_html(path + "\\All_" + file[:-4] + ".html")
fig.show()
#%%   SNR marche pas
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import plotly.graph_objects as go

import plotly.io as pio
pio.renderers.default='browser'

def scatterDevice(device, file):
    fileName = r"\\" + device + file
    sampFreq, signal = wavfile.read(path+fileName)
    signal = signal[:,0]
    fft_spectrum = np.fft.rfft(signal)
    freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
    fft_spectrum_abs = np.abs(fft_spectrum)
    fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name=device[:-1]))
    return freq, fft_spectrum_abs

# fileName = 'outputRX.wav'
# fileName = r"C:\Users\bevid\Documents\Enregistrements audio\Enregistrement (3).m4a"
# path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\TestsS5"
path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\S8"
# fileName = r"\audio_fs_48khz__freq_20to20khz.wav"
devices = ['raspberry', 'zycoo', 'terra']
audio = ''
# file = "fs_8khz_b_128__freq_300to3400hz.wav"
# file = 'az_8KHz.wav'
"""Les fichiers à analyser sont définis ci-dessous"""
files = [r"\audio_fs_8khz_b_128__freq_300to3400hz",r"\audio_fs_48khz_b_128__freq_300to3400hz",r"\audio_fs_8khz__freq_1khz",r"\audio_fs_48khz_b_128__freq_1000hz", r"\audio_az_8KHz",r"\audio_MsgTestFR"]
for x in files:
    file = x + ".wav"
    
    fig = go.Figure()
    
    fileName = file
    sampFreq, signal = wavfile.read(path+fileName)
    fft_spectrum = np.fft.rfft(signal)
    freq = np.fft.rfftfreq(signal.size, d=1./sampFreq)
    fft_spectrum_abs = np.abs(fft_spectrum)
    
    fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name="Reference"))
    
    for i in range(3):
        scatterDevice(devices[i]+'_', file[1:].replace('audio_', ''))
    
    fig.update_layout(title_text=file[:-4])
    fig.write_html(path + "\\All_" + file[1:-4] + ".html")

#%%

import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
import plotly.graph_objects as go
import plotly.io as pio
pio.renderers.default='browser'

path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\SNR"
referenceFile = r"\audio_fs_8khz__freq_1khz.wav"
deviceFile = r"\terra11_fs_8khz__freq_1khz_mono.wav"

sampFreq, device = wavfile.read(path+deviceFile)
sampFreq, reference = wavfile.read(path+referenceFile)

if len(device)>len(reference):
    device = device[1:len(reference)+1]
else:
    reference = reference[4:len(device)+4]

maxDevice = max(device)
maxReference = max(reference)
# noise = np.int16([])
noise = np.int16(np.zeros(len(device)))

for i in range(len(device)):
    device[i] = np.int16(np.float64(device[i])* maxReference/maxDevice)
    noise[i] = device[i]-reference[i]
    

fft_spectrum = np.fft.rfft(noise)
freq = np.fft.rfftfreq(noise.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum)  

fig = go.Figure()
fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name="noise"))

fft_spectrum = np.fft.rfft(device)
freq = np.fft.rfftfreq(device.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum) 

fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name="device"))

fft_spectrum = np.fft.rfft(reference)
freq = np.fft.rfftfreq(reference.size, d=1./sampFreq)
fft_spectrum_abs = np.abs(fft_spectrum) 

fig.add_trace(
        go.Scatter(x=freq[:], y=fft_spectrum_abs[:],
        name="reference"))

# fig.show()
 
    
# plt.plot(freq[:], fft_spectrum_abs[:], label = 'noise')
 
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")

# plt.show()
   
# plt.xlabel("frequency, Hz")
# plt.ylabel("Amplitude, units")

# plt.show()

#%% SNR marche pas

import scipy.io.wavfile as wavfile
import numpy
import os.path


path = r"C:\Users\bevid\Documents\ProjetStage\VoIP\Tests\SNR"
referenceFile = r"\audio_fs_8khz__freq_1khz.wav"
# deviceFile = r"\terra11_fs_8khz__freq_1khz_mono.wav"
deviceFile = r"\raspberry_fs_8khz__freq_1khz.wav"
# deviceFile = r"\zycoo7_fs_8khz__freq_1khz.wav"

def signaltonoise(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)

def snr(file):
  if (os.path.isfile(file)):
    data = wavfile.read(file)[1]
    singleChannel = data
    try:
      singleChannel = numpy.sum(data, axis=1)
    except:
      # was mono after all
      pass
      
    norm = singleChannel / (max(numpy.amax(singleChannel), -1 * numpy.amin(singleChannel)))
    return signaltonoise(data[1])

print(snr(path + deviceFile))
# print(snr(path + referenceFile))