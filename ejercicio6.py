#De forma iterativa
import numpy as np
from typing import Any
def construccion(matriz):
    matriz=np.array([[4,2,4,5,6],[3,6,2,1,0],[2,6,4,1,0],[2,1,4,5,3],[2,5,7,3,1]])
    determinante=np.linalg.det(matriz)
    return determinante

#De forma recursiva
class Matriz():
    def __init__(self,filas:list[list[int]]):
        self.filas=filas
        self.filas=[]
    def columns (self, columnas:list[list[int]]):
        self.columnas=columnas
        return [[fila[i] for fila in self.filas] for i in range(len(self.filas[0]))]
    def numero_filas(self):
        return len(self.filas)
    def numero_columnas(self):
        return len(self.filas[0])
    def determinante(self): 
        return sum(self.filas[0][self.filas[0]] * self.filas[0][columna] for columna in range(self.numero_columnas))
        






