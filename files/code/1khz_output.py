# -*- coding: utf-8 -*-
"""
Created on Mon Sep 01 12:55:56 2024

@author: D€GA
"""

import numpy as np
import matplotlib.pyplot as plt
import wave
import struct

# Audioparameter
sample_rate = 44100  # Abtastrate
dauer = 5  # Signaldauer in Sekunden
frequenz = 1000.0  # Frequenz des Signals in Hz

# Erzeuge das Sinussignal
t = np.linspace(0, dauer, int(sample_rate * dauer), False)
Dc_offset = 0.3 
signal = Dc_offset + (0.5 * np.sin(2 * np.pi * frequenz * t))

# Signal darstellen
plt.figure(1)
plt.figure(figsize=(12, 6))
plt.title("Sinussignal")
plt.plot(t, signal, "blue")
plt.xlabel("Zeit in s")
plt.ylabel("Amplitude in V")
plt.grid()
plt.show()

# Konvertiere in 16-Bit-Audiodaten
signal_int = np.int16(signal * 32767)

# Speichere das Audiosignal als .wav-Datei
with wave.open("1khz_output.wav", "w") as file:
    file.setnchannels(1)  # Mono
    file.setsampwidth(2)  # 16 Bit
    file.setframerate(sample_rate)
    for s in signal_int:
        file.writeframes(struct.pack('h', s))

print("1 kHz-Signal erfolgreich generiert und gespeichert!")
