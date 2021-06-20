import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline

name = 'datos_presion_U2.xlsx'
DF = pd.read_excel(name, engine='openpyxl')

t_difusora = DF['tiempo_difusora(min)']
t_rotatoria = DF['tiempo_rotatoria(min)']
presion_difusora = DF['presion_difusora(Pa)']
presion_rotatoria = DF['presion_rotatoria(mbar)']*100

spline2 = CubicSpline(t_rotatoria, presion_rotatoria, bc_type='clamped')
tiempo_plot = np.linspace(t_rotatoria[0], np.max(t_rotatoria), 1000)

plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.rcParams.update({"font.size": 9, "font.family": "serif"})

fig1, ax1 = plt.subplots(figsize=(3.25, 3.25))
ax1.scatter(t_difusora, presion_difusora, zorder=2)
ax1.set_xlabel('Tiempo [min]')
ax1.set_ylabel('Presión [Pa]')
ax1.set_yscale('log')
fig1.tight_layout()    
fig1.savefig("img/presion-difusora.png")

fig2, ax2 = plt.subplots(figsize=(3.25, 3.25))
ax2.scatter(t_rotatoria, presion_rotatoria, zorder=2)
ax2.plot(tiempo_plot, spline2(tiempo_plot))
ax2.set_xlabel('Tiempo [min]')
ax2.set_ylabel('Presión [Pa]')
ax2.set_yscale('log')
fig2.tight_layout()    
fig2.savefig("img/presion-rotatoria.png")
