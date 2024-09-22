# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 22:42:47 2024

@author: D€GA
"""

import pyaudio
import wave

# %% Audio-Aufnahmeparameter
sample_rate = 44100  # Abtastrate in Hz
kanäle = 1  # Mono für's Mikrofon
format = pyaudio.paInt16  # 16 Bit pro Sample
chunk = 1024  # Datenblockgröße
dauer = 20  # Aufnahmedauer in Sekunden

# %% PyAudio initialisieren
p = pyaudio.PyAudio()

# %% Aufnahme-Stream öffnen
stream = p.open(format=format, channels=kanäle, rate=sample_rate, input=True, frames_per_buffer=chunk)

print("Aufnahme läuft...")

# Audiodaten vom Mikrofon lesen
frames = []

for _ in range(0, int(sample_rate / chunk * dauer)):
    data = stream.read(chunk)
    frames.append(data)

print("Aufnahme beendet.")

# %% Stream stoppen und schließen
stream.stop_stream()
stream.close()
p.terminate()

# %% Die Audiodaten in einer WAV-Datei speichern
wf = wave.open("aufnahme_pyaudio.wav", 'wb')
wf.setnchannels(kanäle)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()

print("Die Audiodatei 'aufnahme_pyaudio.wav' wurde gespeichert.")
