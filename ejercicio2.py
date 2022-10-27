lista=[18,50,210,80,145,333,70,30]
def multiplos(numero):
    for numero in range(0,len(lista)-1):
        if numero % 10 == 0 and numero < 200:
            return numero
def parar(numero):
    for numero in range(0,len(lista)-1):
        if numero > 300:
            break
def organizar(lista):
    return lista.sort

def buscar(numero):
    for numero in lista:
        if numero==145:
            print(145)
        else:
            print(-1)
    return buscar


