#--------------------------------#
#---PARTE 1: Solucionar lambda---#
#--------------------------------#

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from vpython import *

# Aquí lambda será x y mu será y

def S(z,t): # z = (x,y)
    x, y = z
    dzdt = [y,-1/(x**2)]
    return dzdt

# Casos según Ortega-Ureña

# 1.- Big-Bang inicial, colapso final.
x0, y0 = 1.0, 1.0
z0 = [x0, y0] # Vector de condiciones iniciales
t0 = 0.0
tf = 5.7
# range a 2.2
# etiquetas a 2.1

# 2.- Contracción desde tiempos remotos. Colapso final.
#x0, y0 = 1.0, 0.0
#z0 = [x0, y0] # Vector de condiciones iniciales
#t0 = 0.0
#tf = 1.1
# range a 1.2
# etiquetas a 1.1

# 3.- Big-Bang inicial. Expansión indefinida después
#x0, y0 = 1.0, 2.0
#z0 = [x0, y0] # Vector de condiciones iniciales
#t0 = 0.0
#tf = 5
# range a 4.2
# Etiquetas a 4.1

N = 200
t = np.linspace(t0, tf, N) # El dominio. Es un array.

# Solucionador en acción
sol = odeint(S, z0, t)
# Extraemos la solución, dijera el Chat GPT
Lambda = sol[:,0]

# Grafica la solución
plt.figure(figsize=(6, 3))
plt.plot(t, Lambda, 'b', label='λ(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()

#-------------------------------------------#
#---PARTE 2: Generar el triángulo inicial---#
#-------------------------------------------#


# Coordenadas del primer punto
p1 = np.array([1,0])

# Martriz de rotación que general el triángulo
R = np.array([[-1/2, -np.sqrt(3)/2],
              [np.sqrt(3)/2, -1/2]])
# Segundo punto
p2 = np.dot(R, p1)

# Tercer punto
p3 = np.dot(R, p2)

# Graficar todos los puntos y el origen
plt.figure(figsize = (5,5))
plt.scatter(p1[0], p1[1], color='green')
plt.scatter(p2[0], p2[1], color='red')
plt.scatter(p3[0], p3[1], color='blue')
plt.plot(0,0, marker="o", color='black')

# Opcional: ajustar los límites de los ejes para centrar el punto en la gráfica
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)

# Etiquetas de los ejes y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Triángulo inicial')

# Mostrar la gráfica
plt.grid(True)
plt.show()

#     /\
#   .'  `.
# .'      `.------------|
#<  PARTE 3:> Animación-|
# `.      .'------------|
#   `.  .'
#     \/

# Ventana y sol central
Ventana = canvas(title="Triángulo de Lagrange", width=600, height=600, center=vec(0,0,0), range=2.2, align = "center")
Origen = sphere(radius=0.02, color=color.orange, pos=vec(0,0,0))

# Etiqueta para los ejes
label(pos=vec(2.1, 0, 0), text="X", color=color.white, height=15, box=False)
label(pos=vec(0, 2.1, 0), text="Y", color=color.white, height=15, box=False)

# El triángulo de Lagrange al inicio

P1 = sphere(radius=0.04, color=color.green, pos=vec(p1[0],p1[1],0))
P2 = sphere(radius=0.04, color=color.red, pos=vec(p2[0],p2[1],0))
P3 = sphere(radius=0.04, color=color.blue, pos=vec(p3[0],p3[1],0))

# Ahora vamos a darle movimiento
for i in range(N):
    rate(30)
    P1.pos=vec(Lambda[i]*p1[0],Lambda[i]*p1[1],0)
    P2.pos=vec(Lambda[i]*p2[0],Lambda[i]*p2[1],0)
    P3.pos=vec(Lambda[i]*p3[0],Lambda[i]*p3[1],0)

























