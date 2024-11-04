#!/usr/bin/env python

""" Lautsprecher """

import numpy as np
import matplotlib.pyplot as plt

# %% Spezifikation
L1 = 200e-6
R1 = 3
C2 = 1000e-6
L2 = 4e-3
R2 = 30

# %% Frequenzvektor
f = np.logspace(0, 4, 2000)
w = 2 * np.pi * f

# %% Impedanzen/Admittanzen
YM = 1j*w*C2 + 1/(1j*w*L2) + 1/R2
ZM = 1/YM

ZE = R1 + 1j*w*L1 + ZM

ZE0 = R1 + ZM


# %% Ortskurve von ZE0(w)
fig1 = plt.figure(1)
plt.title('Ortskurve')
plt.plot(np.real(ZE0), np.imag(ZE0), label=r'$Z_{E0}$')
plt.xlabel('Re')
plt.ylabel('Im')
plt.legend()
plt.grid()
plt.show()

# %% Uebertragungsfunktion
Q = R2/(np.sqrt(L2/C2))  # Guete
print(Q)

w0 = 1/np.sqrt(L2*C2)
print(w0)

v = (w/w0 - w0/w)  # Verstimmung

HI = 1/(1 + 1j*Q*v)
HI_dB = 20*np.log10(np.abs(HI))
w_w0 = w/w0

# %% Betrag und Phase von HI(w/w0)
fig2 = plt.figure(2)
plt.title('Betrag und Phase')
plt.subplot(211)
plt.semilogx(w_w0, HI_dB)
plt.ylabel(r'$|I_R/I|$ in dB' )
plt.grid()
plt.subplot(212)
plt.semilogx(w_w0, np.angle(HI))
plt.xlabel(r'$\log(\omega/\omega_0)$')
plt.ylabel(r'$\arg(I_R/I)$')
plt.grid()
plt.show()


# %% Schallleistung Ps
U0s = 10
Ri = 0.5

Ps = R2 * (U0s**2/2)/(np.abs(ZE + Ri)**2) * 1/(1 + Q**2 * v**2)

fig3 = plt.figure(3)
plt.title(r'Schallleistung')
plt.plot(v, Ps)
plt.xlabel(r'$\nu$')
plt.ylabel(r'$P_S$ in W')
plt.axis([-4, 4, 0, 1.5])
plt.grid()
plt.show()
