# Definición de la clase Avion
class Avion:
    def __init__(self, modelo, capacidadPasajeros, velocidadMaxima):
        # Inicializa los atributos del avión durante la creación de una instancia
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros
        self.velocidadMaxima = velocidadMaxima
        self.enVuelo = False  # Inicializa el estado de vuelo como falso al principio

    def despegar(self):
        # Método para indicar que el avión está despegando
        if not self.enVuelo:
            print(f"{self.modelo} despegando.")
            self.enVuelo = True
        else:
            print(f"{self.modelo} ya está en vuelo.")

    def aterrizar(self):
        # Método para indicar que el avión está aterrizando
        if self.enVuelo:
            print(f"{self.modelo} aterrizando.")
            self.enVuelo = False
        else:
            print(f"{self.modelo} ya está en tierra.")

    def obtenerInformacion(self):
        # Método para obtener información detallada sobre el avión
        estadoVuelo = "en vuelo" if self.enVuelo else "en tierra"
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidadPasajeros} pasajeros, Velocidad Máxima: {self.velocidadMaxima} km/h, Estado: {estadoVuelo}"

# Crear un objeto de la clase Avion
avionComercial = Avion(modelo="Boeing 747", capacidadPasajeros=416, velocidadMaxima=920)

# Acceder a los atributos y métodos del objeto
print(avionComercial.modelo)  # Imprime el modelo del avión
print(avionComercial.capacidadPasajeros)  # Imprime la capacidad de pasajeros del avión
print(avionComercial.obtenerInformacion())  # Imprime información detallada del avión
avionComercial.despegar()  # Llama al método para indicar que el avión está despegando
avionComercial.aterrizar()  # Llama al método para indicar que el avión está aterrizando
