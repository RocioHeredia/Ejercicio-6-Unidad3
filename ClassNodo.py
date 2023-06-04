from ClassVehiculo import Vehiculo
class Nodo:
    __vehiculo = Vehiculo
    __sig = object

    def __init__(self, vehiculo):
        self.__vehiculo = vehiculo
        self.__sig = None

    def set_siguiente(self, siguiente):
        self.__sig = siguiente

    def get_sig(self):
        return self.__sig

    def get_dato(self):
        return self.__vehiculo