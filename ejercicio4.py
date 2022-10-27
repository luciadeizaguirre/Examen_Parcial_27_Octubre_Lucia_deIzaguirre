class Alumno():
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        print(f"El alumno {self.nombre} ha obtenido un {self.nota}")
        
    def __str__(self):
        return f"El alumno se llama {self.nombre} y ha obtenido un {self.nota}"

    def calificacion(self):
        if self.nota >= 5:
            print(f"El alumno {self.nombre} ha aprobado con un {self.nota}")
        else:
            print(f"El alumno {self.nombre} ha suspendido con un {self.nota}")
