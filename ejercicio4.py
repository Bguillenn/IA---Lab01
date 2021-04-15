import math

def media(numbers):
    return sum(numbers) / len(numbers)


def desvEstandar(numbers):
    varianza = 0
    mediaN = media(numbers)
    for num in numbers:
        varianza += (num - mediaN) ** 2

    return math.sqrt( varianza / len(numbers) )

def mediana(numbers):
    pos = int(len(numbers) / 2)
    ordenado = sorted(numbers)
    return ordenado[pos]



if __name__ == '__main__':
    numbers = [87, 94, 51, 2, 7, 93, 59, 27, 84, 45, 13, 28, 43, 56, 30, 53, 22, 15, 26]
    print("Media: ", media(numbers))
    print("Desviacion estandar: ", desvEstandar(numbers))
    print("Mediana: ", mediana(numbers))
