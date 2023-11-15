import math

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

# Definición de la clase AvionPasajeros que hereda de Avion
class AvionPasajeros(Avion):
    def __init__(self, modelo, capacidad_pasajeros, velocidad_maxima, entretenimiento_a_bordo):
        # Inicializa los atributos específicos para aviones de pasajeros
        super().__init__(modelo, capacidad_pasajeros, velocidad_maxima)
        self.entretenimiento_a_bordo = entretenimiento_a_bordo

    def obtener_informacion(self):
        # Sobrescribe el método de la clase base para incluir el entretenimiento a bordo
        info_base = super().obtener_informacion()
        return f"{info_base}, Entretenimiento a Bordo: {self.entretenimiento_a_bordo}"

# Función que imprime la información de cualquier objeto de las clases Avion, AvionCarga o AvionPasajeros
def imprimir_informacion(avion):
    print(avion.obtener_informacion())

# Crear instancias de las clases
avion_generico = Avion(modelo="Generico", capacidad_pasajeros=100, velocidad_maxima=800)
avion_carga = AvionCarga(modelo="Boeing 747 Cargo", capacidad_carga=134, velocidad_maxima=900)
avion_pasajeros = AvionPasajeros(modelo="Airbus A320", capacidad_pasajeros=150, velocidad_maxima=850, entretenimiento_a_bordo=True)

# Llamada a la función de Polimorfismo
imprimir_informacion(avion_generico)
imprimir_informacion(avion_carga)
imprimir_informacion(avion_pasajeros)
