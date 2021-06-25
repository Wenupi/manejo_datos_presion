import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import CubicSpline
from scipy.optimize import curve_fit

name = 'datos_presion_U2.xlsx'
DF = pd.read_excel(name, engine='openpyxl')

t_difusora = DF['tiempo_difusora(min)'][:4]
t_rotatoria = DF['tiempo_rotatoria(min)'][:14]
presion_difusora = DF['presion_difusora(Pa)'][:4]
presion_rotatoria = DF['presion_rotatoria(mbar)'][:14]*100
t_d_r = DF['tiempo_d-r']
presion_d_r = DF['presion_d-r(mTorr)']*0.1333223

def inversa(x, a, exponente, b):
    return 1/((x+a)**exponente) + b

popt_difusora, pcov_difusora = curve_fit(inversa, t_difusora-t_difusora[0], presion_difusora,
                                         p0=(4, 2, 0))
#popt_rotatoria, pcov_rotatoria = curve_fit(inversa, t_rotatoria-t_rotatoria[0], presion_rotatoria,
#                                           p0=(4, 2, 0))

#spline2 = CubicSpline(t_rotatoria, presion_rotatoria)
tiempo_dif_plot = np.linspace(t_difusora[0], np.max(t_difusora), 1000)
tiempo_rot_plot = np.linspace(t_rotatoria[0], np.max(t_rotatoria), 1000)

plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 1
plt.rcParams['grid.color'] = "#cccccc"
plt.rcParams.update({"font.size": 9, "font.family": "serif"})

fig1, ax1 = plt.subplots(figsize=(3.25, 3.25))
ax1.scatter(t_difusora-t_difusora[0], presion_difusora, zorder=2)
ax1.plot(tiempo_dif_plot-tiempo_dif_plot[0],
         inversa(tiempo_dif_plot-tiempo_dif_plot[0], *popt_difusora),
         label='Interpolación')
ax1.set_xlabel('Tiempo [min]')
ax1.set_ylabel('Presión [Pa]')
ax1.set_yscale('log')
ax1.legend()
fig1.tight_layout()    
fig1.savefig("img/presion-difusora.pdf")

fig2, ax2 = plt.subplots(figsize=(3.25, 3.25))
ax2.scatter(t_rotatoria-t_rotatoria[0], presion_rotatoria, zorder=3)
#ax2.plot(tiempo_rot_plot, inversa(tiempo_rot_plot, *popt_rotatoria),
#         label='Interpolación')
#ax2.plot(tiempo_rot_plot, spline2(tiempo_rot_plot))
ax2.plot(t_rotatoria-t_rotatoria[0], presion_rotatoria, zorder=2)
ax2.set_xlabel('Tiempo [min]')
ax2.set_ylabel('Presión [Pa]')
ax2.set_yscale('log')
fig2.tight_layout()    
fig2.savefig("img/presion-rotatoria.pdf")

fig3, ax3 = plt.subplots(figsize=(3.25, 3.25))
ax3.scatter(t_d_r-t_d_r[0], presion_d_r, zorder=3)
#ax3.plot(tiempo_dif_plot-tiempo_dif_plot[0],
#         inversa(tiempo_dif_plot-tiempo_dif_plot[0], *popt_difusora),
#         label='Interpolación')
ax3.plot(t_d_r-t_d_r[0], presion_d_r, zorder=2)
ax3.set_xlabel('Tiempo [min]')
ax3.set_ylabel('Presión [Pa]')
#ax3.set_yscale('log')
#ax3.legend()
fig3.tight_layout()    
fig3.savefig("img/presion-d-r.pdf")
