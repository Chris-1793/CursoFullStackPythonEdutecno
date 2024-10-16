# Clase base que representa una Persona en la familia
class Persona:
    def __init__(self, nombre, apellido=None):
        self.nombre = nombre
        self.apellido = apellido
    
    def presentarse(self):
        return f"Mi nombre es {self.nombre} {self.apellido}"

# Subclase Abuelo que hereda de Persona
class Abuelo(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        
    
    def presentarse(self):
        return f"Soy el abuelo {self.nombre} {self.apellido}."

# Subclase Padre que hereda de Abuelo
class Padre(Abuelo):
    def __init__(self, nombre, apellido):
        # El apellido se hereda automáticamente del abuelo
        super().__init__(nombre, apellido)
        
        
    
    def presentarse(self):
        return f"Soy el padre {self.nombre} {self.apellido}."

# Subclase Hijo que hereda de Padre
class Hijo(Padre):
    def __init__(self, nombre, apellido):
        # El apellido se hereda automáticamente del padre (y del abuelo)
        super().__init__(nombre, apellido)
        
    
    def presentarse(self):
        return f"Soy el hijo {self.nombre} {self.apellido}."

# Polimorfismo en acción: presentación de cada miembro de la familia
def presentacion_familiar(miembro):
    print(miembro.presentarse())

# Crear instancias de cada miembro de la familia
# Solo el abuelo especifica el apellido
abuelo = Abuelo("Juan", "Gómez")
#Padre.apellido = abuelo.apellido  # El apellido se hereda automáticamente
padre = Padre("Carlos", abuelo.apellido)
hijo = Hijo("Luis", padre.apellido)
presentacion_familiar(abuelo)
presentacion_familiar(padre)
presentacion_familiar(hijo)
print(abuelo.apellido)
# Presentación polimórfica de cada miembro
#familia = [abuelo, padre, hijo]
#for miembro in familia:
#    presentacion_familiar(miembro)
