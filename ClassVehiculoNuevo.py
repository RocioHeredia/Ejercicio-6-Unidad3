from ClassVehiculo import Vehiculo

class Vehiculo_Nuevo(Vehiculo):
    __version = str

    def __init__(self, modelo, cant_puertas, color, precio_base, marca, version):
        super().__init__(modelo, cant_puertas, color, precio_base, marca)
        self.__version = str(version)

    def calcular_importe_venta(self):
        precio = (self.get_precio_B() + (self.get_precio_B() * 0.1))  # 10% por gastos de patentamiento
        if self.__version == 'Full':
            precio += (self.get_precio_B() * 0.02)  # 2% si es full
        return precio

    def mostrar_Datos(self):
        return f"Vehículo Nuevo\nModelo: {self.get_modelo()}\nPuertas: {self.get_puertas()}\nColor: {self.get_color()}\nPrecio Base: {self.get_precio_B()}\nMarca: {self.get_marca()}\nVersion: {self.__version}"

    def diccionario(self):
        vehiculo_dic = super().diccionario()
        vehiculo_dic["version"] = self.__version
        return vehiculo_dic