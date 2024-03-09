# Este programa es una animación básica en 2D que aprendí a hacer. Será la base para visualizar el movimiento de los planetas.

import matplotlib.pyplot as plt
from vpython import *
from math import *

t0 = 0.0
tf = 3.0
h = 0.1
N = int(tf / h)

# Dominio y Curva
# range(N) va de 0 a 29. Si quieres que el último punto sea 30 utiliza range(N+1) pero tus arreglos tendrán 31 elementos (N+1)
t = [t0 + n * h for n in range(N)]
x = [cos(i) for i in t]
y = [sin(j) for j in t]

# Graficar x vs y
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectoria')
plt.grid(True)
plt.show()


# Código para la animación

# La ventana aparece de tal modo que el eje z es normal a la pantalla. 
# Con range determinamos el tamaño del dominio, no de la aventana
ventana = canvas(title="Ping-Pong", width=600, height=600, center=vec(0,0,0), range=2.0, align = "center")
esfera_roja = sphere(radius=0.05, color=color.red, pos=vec(1,0,0))
esfera_central = sphere(radius=0.1, color=color.yellow, pos=vec(0,0,0))

# Vamos a colocar esferas al inicio y al final de la taryectoria

inicio = sphere(radius=0.03, color=color.green, pos=vec(x[0],y[0],0))
final = sphere(radius=0.03, color=color.green, pos=vec(x[-1],y[-1],0))

# Etiqueta para los ejes
label(pos=vec(1.8, 0, 0), text="X", color=color.white, height=15, box=False)
label(pos=vec(0, 1.8, 0), text="Y", color=color.white, height=15, box=False)


# Ahora vamos a darle movilidad a tu animación utilizando los arreglos con los que empezaste el código

for k in range(10):
    if k % 2 == 0:  # Si el residuo de la división de k por 2 es 0, entonces k es par
        for i in range(N):
            rate(20) # Cuántas veces por segundo quieres que la pantalla se actualice
                     # O qué tan rápida quieres que sea tu animación
            esfera_roja.pos=vec(x[i],y[i],0) # Aquí asignamos la posición a la esfera
    else:
        # Haz lo otro para números impares
        for i in range(N-1,-1,-1): # Recorro los índices al revés sólo para comprobar que la trayectoria es la correcta.
            rate(20) # Cuántas veces por segundo quieres que la pantalla se actualice
            esfera_roja.pos=vec(x[i],y[i],0) # Aquí asignamos la posición a la esfera

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    