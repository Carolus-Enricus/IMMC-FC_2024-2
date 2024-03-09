#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 13:34:00 2024

@author: Carolus_Enricus
"""

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from vpython import *

#------------------------------------------------#
#---Parámetros físicos y condiciones iniciales---#
#------------------------------------------------#
G = 6.674 * 10**(-11) # Constante de Gravitación Universal
M = 1.989 * 10**30 # La masota del cuerpo grandote.
m = 5.972 * 10**24 # La masita del cuerpo que orbita
p0 = 1.496*10**(11) # Posición inicial física. Que coincide con x_0. Una unidad astronómica.

# Velocidades iniciales en SI. En general ambas son distintas de cero.
# Para la tierra considera directamente que la v0_x = 0
v0_x = 21213
v0_y = 21213

#---------------------------------------------------------------#
#---Velocidades para Órbitas cerradas (range=1.5*p0), tf = 20---#
#---------------------------------------------------------------#
# Se observa una colisión:
#    v0_x = 28300
#    v0_y = 10000

# Se visualiza bien la segunda ley de Kepler
#    v0_x = 21213
#    v0_y = 21213

# La órbita de la Tierra:
#    v0_x = 0.0
#    v0_y = 30000

#-------------------------------------------------#
#---Velocidades para Órbitas abiertas (tf = 10)---#
#-------------------------------------------------#
# Parábola, energía = 0, range = 4*p0 
#    v0_x = 0.0
#    v0_y = sqrt(2*G*M/p0)

# Hiérbola, energía positiva, range = 6*p0
#    v0_x = 0.0
#    v0_y = 45000

# Aquí sugiero invertir el tiempo con: for i in range(len(X_real)-1,-1,-1)
  
v0 = sqrt(v0_x**2 + v0_y**2)
#sqrt(2*G*M/p0) #(Parábola) #30000 (Velocidad de la Tierra)
print("Velocidad inicial en el sistema SI: ", v0)

# Tiempo final considerando 365 días
print("Tiempo Adiomensional sugerido: ", sqrt((G*M)/p0**3)*(3.154*10**(7)))
E0 = 0.5*m*v0**2 - (G*M*m)/p0

print("Energía Inicial en Joules: ", E0)


#--------------------------------------------#
#---Las Ecuaciones y sus Valores Iniciales---#
#--------------------------------------------#

def S(x, vx, y, vy):
    r = np.sqrt(x**2 + y**2)
    return np.array([vx, -x/(r**3), vy, -y/(r**3)])

# Posiciones iniciales al tiempo inicial
t0 = 0.0
x0 = 1.0
y0 = 0.0

# Velocidades iniciales
vx0 = sqrt(p0/(G*M))*v0_x
vy0 = sqrt(p0/(G*M))*v0_y

#-------------#
#---Dominio---#
#-------------#

tf = 20 # Duración de la solución
h = 0.001
N = int(tf/h) # Número de pasos temporales

Tiempo = [t0]
X = [x0]
Vx = [vx0]
Y = [y0]
Vy = [vy0]

#-----------------------------------------#
#---Solución Numérica por Runge-Kutta 4---#
#-----------------------------------------#
for n in range(N):
    t = t0 + n * h
    k1 = h * S(X[-1], Vx[-1], Y[-1], Vy[-1])
    k2 = h * S(X[-1] + 0.5 * k1[0], Vx[-1] + 0.5 * k1[1], Y[-1] + 0.5 * k1[2], Vy[-1] + 0.5 * k1[3])
    k3 = h * S(X[-1] + 0.5 * k2[0], Vx[-1] + 0.5 * k2[1], Y[-1] + 0.5 * k2[2], Vy[-1] + 0.5 * k2[3])
    k4 = h * S(X[-1] + k3[0], Vx[-1] + k3[1], Y[-1] + k3[2], Vy[-1] + k3[3])
    
    X.append(X[-1] + (k1[0] + 2*k2[0] + 2*k3[0] + k4[0])/6)
    Vx.append(Vx[-1] + (k1[1] + 2*k2[1] + 2*k3[1] + k4[1])/6)
    Y.append(Y[-1] + (k1[2] + 2*k2[2] + 2*k3[2] + k4[2])/6)
    Vy.append(Vy[-1] + (k1[3] + 2*k2[3] + 2*k3[3] + k4[3])/6)
    Tiempo.append(t + h)

#----------------------------------------------------------------------------#
#---Recuperamos las cantidades en unidades SI y hacemos un Recorte Bolillo---#
#----------------------------------------------------------------------------#
# El recorte bolillo se hace para no satural al graficador
X_recortada = X[0::100]
Y_recortada = Y[0::100]

X_real = [p0*i for i in X_recortada]
Y_real = [p0*i for i in Y_recortada]


#             _____
#          .-'.  ':'-.
#        .''::: .:    '.
#       /   :::::'      \
#      ;.    ':' `       ;  --------------------------------------
#      |       '..       |  ---Gráfica y Animación de la Órbita---
#      ; '      ::::.    ;  --------------------------------------
#       \       '::::   /
#        '.      :::  .'
#          '-.___'_.-'

# Graficar x vs y
plt.plot(X_real, Y_real)
plt.plot(0,0, marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectoria orbital')
plt.grid(True)
plt.show()


ventana = canvas(title="Trayectoria Orbital", width=600, height=600, center=vec(0,0,0), range=1.5*p0, align = "center")
Tierra = sphere(radius=0.05*p0, color=color.blue, pos=vec(p0,0,0))
Sol = sphere(radius=0.1*p0, color=color.orange, pos=vec(0,0,0))

label(pos=vec(1.4*p0, 0, 0), text="X", color=color.white, height=15, box=False)
label(pos=vec(0, 1.4*p0, 0), text="Y", color=color.white, height=15, box=False)

for i in range(len(X_real)):
    rate(20) # Cuántas veces por segundo quieres que la pantalla se actualice
    Tierra.pos=vec(X_real[i],Y_real[i],0)









