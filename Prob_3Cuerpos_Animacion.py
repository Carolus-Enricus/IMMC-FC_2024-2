"""
Created on Mon Mar 11 21:35:51 2024
@author: carolusenricus
"""
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from vpython import *

#--------------------------------------------#
#---Las Ecuaciones y sus Valores Iniciales---#
#--------------------------------------------#

def S(t, z, mu):
    x, vx, y, vy = z
    z_z1 = sqrt((x+mu)**2 + y**2) # z-z1
    z_z2 = sqrt((x+mu-1)**2 + y**2) # z-z2
    #-------------------------------------
    dx = vx
    dvx = 2*vy + x -(1-mu)*(x+mu)/(z_z1**3) - mu*(x+mu-1)/(z_z2**3)
    dy = vy
    dvy = -2*vx + y -(1-mu)*(y)/(z_z1**3) - mu*(y)/(z_z2**3)
    #--------------------------------------------------------------
    return [dx, dvx, dy, dvy]

# Posiciones y velocidades iniciales
x0 = 1.0
vx0 = 0.0
y0 = 0.0
vy0 = -1.0
#--------------------------------
mu = 0.3 # Aquí define la masa mu

#-------------#
#---Dominio---#
#-------------#
t0 = 0.0
tf = 10.0
N = 500

# Esto es una solución pero quién sabe con cuántos puntos
sol = solve_ivp(S, [t0, tf], [x0, vx0, y0,vy0], args=(mu,), dense_output=True)

# Definiéndo ésto ya especifícas cuántos puntos quieres
t = np.linspace(t0, tf, N)
z = sol.sol(t)

x = z[0]
vx = z[1]
y = z[2]
vy = z[3]

# Graficamos
plt.figure(figsize=(5,5))
# Ajuste de límites para hacer que los ejes tengan el mismo intervalo
max_range = max(max(x), max(y)) * 1.1
plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.plot(x, y, label='Trayectoria')  # Agregamos la etiqueta 'trayectoria'

#---Cuerpos Primarios---
plt.plot(-mu,0, marker="o", label='z1')
plt.plot(1-mu,0, marker="o", label='z2')

#---Ejes---
plt.axhline(0, color='black', linewidth=0.5)  # Marca el eje y
plt.axvline(0, color='black', linewidth=0.5)  # Marca el eje x
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.title('Problema Restringido de 3 Cuerpos')
plt.show()

#        ~+
#
#                 *       +
#           '                  |
#       ()    .-.,="``"=.    - o -     --------------
#             '=/_       \     |       ---ANIMACIÓN--
#          *   |  '=._    |            --------------
#               \     `=./`,        '
#            .   '=.__.=' `='      *
#   +                         +
#        O      *        '       .

grafica = graph(title="Trayectoria", xtitle="x", ytitle="y", xmin=-max_range, xmax=max_range, ymin=-max_range, ymax=max_range)
Trayectoria = gcurve(color=color.orange)

z1 = [-mu,0]
z2 = [1-mu,0]
titulo = "Problema Planar Circular Restringido de 3 Cuerpos"
ventana = canvas(title=titulo, width=600, height=600, center=vec(0,0,0), range=max_range, align = "right")

# Los objetos
CM = sphere(radius=0.01, color=color.white, pos=vec(0,0,0))

M1 = sphere(radius=0.04, color=color.green, pos=vec(z1[0],z1[1],0))
rastro1 = attach_trail(M1, radius=0.003, color=color.green, retain=200)

M2 = sphere(radius=0.03, color=color.blue, pos=vec(z2[0],z2[1],0))
rastro2 = attach_trail(M2, radius=0.003, color=color.blue, retain=200)

M3 = sphere(radius=0.04*mu, color=color.orange, pos=vec(1,0,0))
rastro3 = attach_trail(M3, radius=0.003, color=color.orange, retain=50)

# Los echamos a Girar
xcos = [cos(i) for i in t]
ysin = [sin(i) for i in t]

for i in range(N):
    rate(20)
    M1.pos = vec(-mu * xcos[i], -mu * ysin[i], 0)
    M2.pos = vec((1-mu) * xcos[i], (1-mu) * ysin[i], 0)   
    M3.pos = vec(xcos[i]*x[i] - ysin[i]*y[i], ysin[i]*x[i] + xcos[i]*y[i], 0)
    Trayectoria.plot(pos=(x[i],y[i]))
















