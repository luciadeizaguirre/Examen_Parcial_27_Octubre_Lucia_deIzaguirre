class Alumno():
    def __init__(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota
        print(f"El alumno {self.nombre} ha obtenido un {self.nota} de 10 puntos")

    def calificacion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con un {self.nota}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con un {self.nota}")

if __name__=="__main__":
    import doctest
    doctest.testmod()
