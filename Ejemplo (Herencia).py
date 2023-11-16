# Definición de la clase Avion
class Avion:
    def __init__(self, modelo, capacidadPasajeros, velocidadMaxima):
        # Inicializa los atributos del avión
        self.modelo = modelo
        self.capacidadPasajeros = capacidadPasajeros
        self.velocidadMaxima = velocidadMaxima
        self.enVuelo = False

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
        # Método para obtener información del avión
        estadoVuelo = "en vuelo" if self.enVuelo else "en tierra"
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidadPasajeros} pasajeros, Velocidad Máxima: {self.velocidadMaxima} km/h, Estado: {estadoVuelo}"

# Definición de la clase AvionCarga que hereda de Avion
class AvionCarga(Avion):
    def __init__(self, modelo, capacidadCarga, velocidadMaxima):
        # Inicializa los atributos específicos para aviones de carga
        super().__init__(modelo, capacidadPasajeros=0, velocidadMaxima=velocidadMaxima)
        self.capacidadCarga = capacidadCarga

    def obtenerInformacion(self):
        # Sobrescribe el método de la clase base para incluir la capacidad de carga
        infoBase = super().obtenerInformacion()
        return f"{infoBase}, Capacidad de Carga: {self.capacidadCarga} toneladas"

# Crear un objeto de la clase AvionCarga
avionCarga = AvionCarga(modelo="Boeing 747 Cargo", capacidadCarga=134, velocidadMaxima=900)

# Acceder a los atributos y métodos del objeto
print(avionCarga.modelo)  # Imprime el modelo del avión de carga
print(avionCarga.capacidadCarga)  # Imprime la capacidad de carga del avión de carga
print(avionCarga.obtenerInformacion())  # Imprime información detallada del avión de carga
avionCarga.despegar()  # Llama al método para indicar que el avión de carga está despegando
avionCarga.aterrizar()  # Llama al método para indicar que el avión de carga está aterrizando
