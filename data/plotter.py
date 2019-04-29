"""
Plot particle size distribution for pine feedstock used in NREL 2FBR pyrolyzer.
Data from 150317-cleanpine-particle-size spreadsheet provided by Rick French and
Kristiina Iisa.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

diam, vol, cumul = np.loadtxt('pine-size.csv', delimiter=',', skiprows=1, unpack=True)

fig, ax = plt.subplots(tight_layout=True)
ax.plot(diam, vol, marker='.')
ax.set_xscale('log')
ax.set_xlabel('Diameter [µm]')
ax.set_ylabel('Volume [%]')
ax.grid(True)
ax.grid(True, which='minor', color='0.9')
ax.set_frame_on(False)
ax.tick_params(color='0.7')
ax.tick_params(which='minor', color='0.9')
ax.xaxis.set_major_formatter(FormatStrFormatter("%g"))

fig, ax = plt.subplots(tight_layout=True)
ax.plot(diam, cumul, marker='.')
ax.set_xscale('log')
ax.set_xlabel('Diameter [µm]')
ax.set_ylabel('Cumulative [%]')
ax.grid(True)
ax.grid(True, which='minor', color='0.9')
ax.set_frame_on(False)
ax.tick_params(color='0.7')
ax.tick_params(which='minor', color='0.9')
ax.xaxis.set_major_formatter(FormatStrFormatter("%g"))

plt.show()
