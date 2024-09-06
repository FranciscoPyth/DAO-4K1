class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    
    def __str__(self):
        return f"{self.nombre} - {self.edad} - {self.dni}"
    

    def esMayorDeEdad(self):
        return self.edad >= 18