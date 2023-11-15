# Definición de la clase Avion
class Avion:
    def __init__(self, modelo, capacidad_pasajeros, velocidad_maxima):
        # Inicializa los atributos del avión
        self.modelo = modelo
        self.capacidad_pasajeros = capacidad_pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.en_vuelo = False

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
        # Método para obtener información del avión
        estado_vuelo = "en vuelo" if self.en_vuelo else "en tierra"
        return f"Modelo: {self.modelo}, Capacidad: {self.capacidad_pasajeros} pasajeros, Velocidad Máxima: {self.velocidad_maxima} km/h, Estado: {estado_vuelo}"

# Definición de la clase AvionCarga que hereda de Avion
class AvionCarga(Avion):
    def __init__(self, modelo, capacidad_carga, velocidad_maxima):
        # Inicializa los atributos específicos para aviones de carga
        super().__init__(modelo, capacidad_pasajeros=0, velocidad_maxima=velocidad_maxima)
        self.capacidad_carga = capacidad_carga

    def obtener_informacion(self):
        # Sobrescribe el método de la clase base para incluir la capacidad de carga
        info_base = super().obtener_informacion()
        return f"{info_base}, Capacidad de Carga: {self.capacidad_carga} toneladas"

# Crear un objeto de la clase AvionCarga
avion_carga = AvionCarga(modelo="Boeing 747 Cargo", capacidad_carga=134, velocidad_maxima=900)

# Acceder a los atributos y métodos del objeto
print(avion_carga.modelo)  # Imprime el modelo del avión de carga
print(avion_carga.capacidad_carga)  # Imprime la capacidad de carga del avión de carga
print(avion_carga.obtener_informacion())  # Imprime información detallada del avión de carga
avion_carga.despegar()  # Llama al método para indicar que el avión de carga está despegando
avion_carga.aterrizar()  # Llama al método para indicar que el avión de carga está aterrizando
