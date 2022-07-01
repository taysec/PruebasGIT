import math
import time as pausa
import random
print(math.sin(math.pi/2))
pausa.sleep(0.5)
pi=3.14
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None
print(sin(pi/2))


lista = [numero for numero in range (0,101)]
print(lista)
print(random.choice(lista))
print(random.sample(lista,25))
print(random.sample(lista,5))

lista = [random.randint(0,25) for numero in range(0,25)]
print (lista)



import platform

print(platform.processor())
print(platform.system())
print(platform.freedesktop_os_release())
