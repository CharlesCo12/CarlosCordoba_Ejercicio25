import numpy as np
import matplotlib.pylab as plt
#Función resultado
def f(x):
    return np.exp(-x)

#Llamado de los datos
filename = 'euler_001.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
x1=np.linspace(0,4,100)
#Gráfica
plt.figure(figsize=(12,10))
plt.subplot(2,3,1)
plt.title('Euler 0.01')
plt.plot(x,y,label='Euler 0.01')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

#Llamado de los datos
filename = 'euler_01.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
#Gráfica
plt.subplot(2,3,2)
plt.title('Euler 0.1')
plt.plot(x,y,label='Euler 0.1')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

#Llamado de los datos
filename = 'euler_1.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
#Gráfica
plt.subplot(2,3,3)
plt.title('Euler 1')
plt.plot(x,y,label='Euler 1')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

#Llamado de los datos
filename = 'implicit_001.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
#Gráfica
plt.subplot(2,3,4)
plt.title('Implicit 0.01')
plt.plot(x,y,label='Implicit 0.01')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

#Llamado de los datos
filename = 'implicit_01.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
#Gráfica
plt.subplot(2,3,5)
plt.title('Implicit 0.1')
plt.plot(x,y,label='Implicit 0.1')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

#Llamado de los datos
filename = 'implicit_1.dat'
x=np.loadtxt(filename, usecols=0)
y=np.loadtxt(filename, usecols=1)
#Gráfica
plt.subplot(2,3,6)
plt.title('Implicit 1')
plt.plot(x,y,label='Implicit 1')
plt.plot(x1,f(x1),label='Model')
plt.legend()
plt.grid()

plt.savefig('Graficas.png')