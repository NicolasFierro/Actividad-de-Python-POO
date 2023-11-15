# Definición de la clase Avion
class Avion:
    def __init__(self, modelo, capacidad_pasajeros, velocidad_maxima):
        # Inicializa los atributos del avión durante la creación de una instancia
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.en_vuelo = False  # Inicializa el estado de vuelo como falso al principio

    def despegar(self):
        # Método para indicar que el avión está despegando
        if not self.en_vuelo:
            print(f"{self.modelo} despegando.")
            self.en_vuelo = True
        else:
            print(f"{self.modelo} ya está en vuelo.")

    def aterrizar(self):
        # Método para indicar que el avión está aterrizando
        if self.en_vuelo:
            print(f"{self.modelo} aterrizando.")
            self.en_vuelo = False
        else:
            print(f"{self.modelo} ya está en tierra.")

    def obtener_informacion(self):
        # Método para obtener información detallada sobre el avión
        estado_vuelo = "en vuelo" if self.en_vuelo else "en tierra"
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidad_pasajeros} pasajeros, Velocidad Máxima: {self.velocidad_maxima} km/h, Estado: {estado_vuelo}"

# Crear un objeto de la clase Avion
avion_comercial = Avion(modelo="Boeing 747", capacidad_pasajeros=416, velocidad_maxima=920)

# Acceder a los atributos y métodos del objeto
print(avion_comercial.modelo)  # Imprime el modelo del avión
print(avion_comercial.capacidad_pasajeros)  # Imprime la capacidad de pasajeros del avión
print(avion_comercial.obtener_informacion())  # Imprime información detallada del avión
avion_comercial.despegar()  # Llama al método para indicar que el avión está despegando
avion_comercial.aterrizar()  # Llama al método para indicar que el avión está aterrizando
