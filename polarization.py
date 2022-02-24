import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

psi = float(input())
phi = float(input())

psi = (psi*np.pi)/180
phi = (phi*np.pi)/180
E = 1.0

time = np.linspace(0.0, 4*np.pi, 1000)

Amplitude_x = np.sqrt((np.cos(psi)*np.cos(phi))**2 + (np.sin(phi)*np.sin(psi))**2)
Amplitude_y = np.sqrt((np.cos(psi)*np.sin(phi))**2 + (np.sin(psi)*np.cos(phi))**2)

phase_shift_x = np.arcsin((np.sin(phi)*np.sin(psi))/Amplitude_x)
phase_shift_y =	np.arcsin((np.sin(psi)*np.cos(phi))/Amplitude_y)


E_x = np.sin(time + phase_shift_x)*Amplitude_x
E_y = np.cos(time + phase_shift_y)*Amplitude_y

plt.figure(1)
plt.plot(time, E_x, color = 'r')
plt.plot(time, E_y, color = 'b')
plt.grid(color='lightgray',linestyle='--')
ax = plt.gca()
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.figure(figsize=(5,5))
plt.plot(np.cos(psi)*np.sin(time), np.sin(psi)*np.cos(time), color = 'blue')

plt.plot([0, np.cos(psi)], [0, np.sin(psi)], color = 'r')
plt.plot([0, np.cos(phi)], [0, np.sin(phi)], color = 'black')
plt.plot([0, -np.sin(phi)], [0, np.cos(phi)], color = 'black')

plt.plot(E_x, E_y, color = 'darkblue')

plt.ylim(-1.15, 1.15)
plt.xlim(-1.1, 1.1)
plt.grid(color='lightgray',linestyle='--')
ax = plt.gca()
ax.spines['bottom'].set_position('center')
ax.spines['left'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.show()
print("zeliboba")


