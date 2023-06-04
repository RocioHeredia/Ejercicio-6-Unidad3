from ClassVehiculo import Vehiculo

class Vehiculo_usado(Vehiculo):
    __patente = str
    __ani = int
    __kilometraje = float

    def __init__(self, modelo, cant_puertas, color, precio_base, marca, patente, ani, kilometraje):
        super().__init__(modelo, cant_puertas, color, precio_base, marca)
        self.__patente = patente
        self.__ani = int(ani)
        self.__kilometraje = float(kilometraje)

    def calcular_importe_venta(self):
        precio = self.get_precio_B()
        if self.__ani:
            precio -= (self.get_precio_B() * 0.01 * (2023 - self.__ani))
        if self.__kilometraje > 100000:
            precio -= (self.get_precio_B() * 0.02)
        return precio

    def mostrar_Datos(self):
        return f"Vehículo Usado\nModelo: {self.get_modelo()}\nPuertas: {self.get_puertas()}\nColor: {self.get_color()}\nPrecio Base: {self.get_precio_B()}\nMarca: {self.get_marca()}\nPatente: {self.__patente}\nAño: {self.__ani}\nKilometraje: {self.__kilometraje}"

    def get_patente(self):
        return self.__patente

    def diccionario(self):
        vehiculo_dic = super().diccionario()
        vehiculo_dic["patente"] = self.__patente
        vehiculo_dic["anio"] = self.__ani
        vehiculo_dic["kilometraje"] = self.__kilometraje
        return vehiculo_dic