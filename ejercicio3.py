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
alumno1=Alumno("Juan Perez",5)
alumno2=Alumno("Lucia de Izaguirre",5)
alumno3=Alumno("Lola Gallego",10)
print(alumno1.calificacion)
print(alumno2.calificacion)
if __name__=="__main__":
    import doctest
    doctest.testmod()
