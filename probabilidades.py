import random
from bokeh.plotting import figure,show

def tirar_dado(numero_de_intentos):
    secuencia_de_tiros = []

    for _ in range(numero_de_tiros):
        dado1 = random.choice([1,2,3,4,5,6])
        dado2 = random.choice([1,2,3,4,5,6])
        secuencia_de_tiros.append((dado1 + dado2))

    return secuencia_de_tiros


def main(numero_de_tiros,numero_de_intentos):
    tiros=[]
    
    for _ in range(numero_de_intentos):
        secuencia_de_tiros= tirar_dado(numero_de_tiros)
        tiros.append(secuencia_de_tiros)
    tiros_con_12 = 0
    for tiro in tiros:
        if 12 in tiro:
            tiros_con_12 +=1
    probabilidad_tiros_con12 = tiros_con_12/ numero_de_intentos
    print(f'probabilidad de obtener por lo menos un 12 en {numero_de_intentos} tiros = {probabilidad_tiros_con12}')
 

if __name__ == "__main__":
    numero_de_tiros= int(input("cuantos tiros?: "))
    numero_de_intentos = int(input(('Cuantas veces quieres simular? ')))

    main(numero_de_intentos, numero_de_intentos)
    
