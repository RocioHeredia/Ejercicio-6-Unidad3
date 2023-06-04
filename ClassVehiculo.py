from abc import ABC, abstractmethod


class Vehiculo(ABC):
    __modelo = str
    __cant_puertas = int
    __color = str
    __precio_base = float
    __marca = str

    def __init__(self, modelo, cant_puertas, color, precio_base, marca):
        self.__modelo = str(modelo)
        self.__cant_puertas = int(cant_puertas)
        self.__color = str(color)
        self.__precio_base = float(precio_base)
        self.__marca = str(marca)

    @abstractmethod
    def calcular_importe_venta(self):
        pass

    @abstractmethod
    def mostrar_Datos(self):
        pass

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color

    def get_puertas(self):
        return self.__cant_puertas

    def get_precio_B(self):
        return self.__precio_base

    def get_marca(self):
        return self.__marca

    def set_precio_base(self, precio_nuevo):
        self.__precio_base = precio_nuevo

    def diccionario(self):
        return {
            "modelo": self.__modelo,
            "puertas": self.__cant_puertas,
            "color": self.__color,
            "precio_base": self.__precio_base,
            "marca": self.__marca
        }
