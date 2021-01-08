import random
import math

def media (X):
    return sum(X)/len(X)

def varianza(X):
    mu= media(X)
    acumulador = 0
    for x in X:
        acumulador += (x-mu)**2
    return acumulador/len(X)

def desviacion_estandar(X):
    return math.sqrt(varianza(X))

if __name__ == "__main__":
    X=[random.randint(9,12) for i in range(20)]
    mu= media(X)
    Var = varianza(X)
    sigma = desviacion_estandar(X)

    print(f' el arreglo es {X}')
    print(f' el promedio es: {mu}')
    print(f' la varianza es {Var} ')
    print(f' la desviancion estandar es {sigma}')

