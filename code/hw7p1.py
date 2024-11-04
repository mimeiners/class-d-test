#!/usr/bin/env python


""" Dynamisches Mikrofon """

import numpy as np
import matplotlib.pyplot as plt

# %% Spezifikation
R0 = 3  # Innenwiderstand des Mikrofons
L0 = 25  # Hauptinduktivitaet
Ls = 1  # Streuinduktivitaet
Rw = 100  # Wicklungswiderstand
Cw = 800e-12  # Wicklungskapazitaet
Rv = 100e3  # Verstaerker-Eingangswiderstand
Cv = 200e-12  # Verstaerker- und Kabelkapazitaet
u = 1/30  # Uebertragungsfaktor u1/u2

# %% Frequenzvektor
f = np.logspace(0, 5, 1000)
w = 2 * np.pi * f
f0 = 1

# %% Impedanzen/Admittanzen
Y1 = 1j*w*Cw + 1/(1j*w*L0)
Z1 = 1/Y1

Yv = 1j*w*Cv + 1/Rv
Zv = 1/Yv

Z2 = Rw + 1j*w*Ls

Zp = Z1*(Z2 + Zv)/(Z1 + Z2 + Zv)

R0q = R0/u**2

# %% Uebertragungsfunktion
H = 1/u * Zv/(Z2 + Zv) * Zp/(R0q + Zp)


# %% Ortskurve von H(f)
fig1 = plt.figure(1)
plt.title('H-Ebene')
plt.plot(np.real(H), np.imag(H))
plt.xlabel('Re')
plt.ylabel('Im')
plt.legend(('H'))
plt.grid()
plt.show()


# %% Betrag und Phase von H(f)
fig2 = plt.figure(2)
plt.title('Betrag und Phase')
plt.subplot(211)
plt.semilogx(f, np.abs(H))
# plt.xlabel(r'$\log(f/f_0)$')
plt.ylabel(r'|H|')
plt.grid()
plt.subplot(212)
plt.semilogx(f, np.angle(H))
plt.xlabel(r'$\log(f/f_0)$')
plt.ylabel(r'arg(H)')
plt.grid()
plt.show()


# %% Betragsfrequenzgang von H(f)
H_dB = 20*np.log10(np.abs(H))

fig3 = plt.figure(3)
plt.title('Betragsfrequenzgang')
plt.semilogx(f, H_dB)
plt.xlabel(r'$\log(f/f_0)$')
plt.ylabel(r'$|H|$ in dB')
plt.grid()
plt.show()
