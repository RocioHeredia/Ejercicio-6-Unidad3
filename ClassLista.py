from ClassVehiculoNuevo import Vehiculo_Nuevo
from ClassVehiculoUsado import Vehiculo_usado
from ClassNodo import Nodo
import json
from pathlib import Path


class listaVehiculos:
    __comienzo = Nodo

    def __init__(self):
        self.__comienzo = None

    def agregar_vehiculo(self, vehiculo):
        nodo = Nodo(vehiculo)
        nodo.set_siguiente(self.__comienzo)
        self.__comienzo = nodo

    def leerJSONArchivo(self):
        with Path('vehiculos.json').open(encoding="utf-8-sig") as fuente:
            diccionario = json.load(fuente)
        for vehiculo_data in diccionario:
            if vehiculo_data["tipo"] == "nuevo":
                vehiculo = Vehiculo_Nuevo(
                    vehiculo_data["modelo"],
                    vehiculo_data["puertas"],
                    vehiculo_data["color"],
                    vehiculo_data["precio_base"],
                    vehiculo_data["marca"],
                    vehiculo_data["version"]
                )
            else:
                vehiculo = Vehiculo_usado(
                    vehiculo_data["modelo"],
                    vehiculo_data["puertas"],
                    vehiculo_data["color"],
                    vehiculo_data["precio_base"],
                    vehiculo_data["marca"],
                    vehiculo_data["patente"],
                    vehiculo_data["anio"],
                    vehiculo_data["kilometraje"]
                )

            self.agregar_vehiculo(vehiculo)

    def mostrar(self):
        actual = self.__comienzo
        while actual is not None:
            vehiculo = actual.get_dato()
            print('\n')
            print(vehiculo.mostrar_Datos())  # Imprime el vehículo
            actual = actual.get_sig()

    def agregar_por_posicion(self, vehiculo, posicion):
        nuevo_nodo = Nodo(vehiculo)
        if posicion == 0:
            nuevo_nodo.set_siguiente(self.__comienzo)
            self.__comienzo = nuevo_nodo
        else:
            aux = self.__comienzo
            cont = 0
            while aux is not None and cont < posicion - 1:
                aux = aux.get_sig()
                cont += 1
            nuevo_nodo.set_siguiente(aux.get_sig())
            aux.set_siguiente(nuevo_nodo)
            print('Vehiculo insertado en la posicion deseada')

    def insertar_vehiculo(self, posicion):
        modelo = input("Ingrese el modelo del vehículo: ")
        cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
        color = input("Ingrese el color del vehículo: ")
        precio_base = float(input("Ingrese el precio base del vehículo: "))
        opcion = input("¿Es un vehículo nuevo o usado? (nuevo/usado): ")
        if opcion == 'nuevo':
            marca = input('Ingrese marca: ')
            version = input('¿Es un vehiculo full/base?: ')
            vehiculo = Vehiculo_Nuevo(modelo, cantidad_puertas, color, precio_base, marca, version)
        else:
            marca = input('Ingrese marca: ')
            patente = input('Ingrese patente: ')
            ani = input('ingrese año: ')
            kilometraje = input('Ingrese Kilometraje: ')
            vehiculo = Vehiculo_usado(modelo, cantidad_puertas, color, precio_base, marca, patente, ani, kilometraje)
        self.agregar_por_posicion(vehiculo, posicion)

    def agregar_un_vehiculo_a_la_coleccion(self):
        modelo = input("Ingrese el modelo del vehículo: ")
        cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
        color = input("Ingrese el color del vehículo: ")
        precio_base = float(input("Ingrese el precio base del vehículo: "))
        opcion = input("¿Es un vehículo nuevo o usado? (nuevo/usado): ")
        if opcion == 'nuevo':
            marca = input('Ingrese marca: ')
            version = input('¿Es un vehiculo full/base?: ')
            vehiculo = Vehiculo_Nuevo(modelo, cantidad_puertas, color, precio_base, marca, version)
        else:
            marca = input('Ingrese marca: ')
            patente = input('Ingrese patente: ')
            ani = input('ingrese año: ')
            kilometraje = input('Ingrese Kilometraje: ')
            vehiculo = Vehiculo_usado(modelo, cantidad_puertas, color, precio_base, marca, patente, ani, kilometraje)
        self.agregar_vehiculo(vehiculo)

    def mostrar_tipo_vehiculo(self, posicion):
        actual = self.__comienzo
        indice = 0

        while actual is not None and indice < posicion:
            actual = actual.get_sig()
            indice += 1

        if actual is None:
            print(f'La posicion {posicion} esta fuera de rango.')

        else:
            vehiculo = actual.get_dato()

            if isinstance(vehiculo, Vehiculo_Nuevo):
                print(f'El objeto de la posicion {posicion} es un Vehiculo Nuevo.')

            elif isinstance(vehiculo, Vehiculo_usado):
                print(f'El objeto de la posicion {posicion} es un Vehiculo Usado.')

    def modificacion(self, patente):
        actual = self.__comienzo
        while actual is not None:
            vehiculo = actual.get_dato()
            if isinstance(vehiculo, Vehiculo_usado) and str(vehiculo.get_patente()) == patente:
                nuevo_precio = float(input('Ingrese nuevo precio base: '))
                vehiculo.set_precio_base(nuevo_precio)
                print(f'El precio de venta es ${vehiculo.calcular_importe_venta()}')
            actual = actual.get_sig()

    def vehiculo_economico(self):
        actual = self.__comienzo
        minimo = float('inf')
        vehiculo_economico = None
        while actual is not None:
            vehiculo = actual.get_dato()
            importe_venta = vehiculo.calcular_importe_venta()
            if importe_venta < minimo:
                minimo = importe_venta
                vehiculo_economico = vehiculo
            actual = actual.get_sig()

        if vehiculo_economico is not None:
            importe_total = vehiculo_economico.calcular_importe_venta()
            print(f'{vehiculo_economico.mostrar_Datos()}\n Tiene un precio de venta de ${importe_total}')

    def vehiculo_venta(self):
        actual = self.__comienzo
        print('\n VEHICULOS EN LA CONSECIONARIA\n')
        while actual is not None:
            vehiculo = actual.get_dato()
            print(
                f'Modelo: {vehiculo.get_modelo()}    Cantidad de Puertas: {vehiculo.get_puertas()}\n Importe venta: ${vehiculo.calcular_importe_venta()}')
            actual = actual.get_sig()

    def AlmacenarEnArchivo(self):
        vehiculos_lista = []
        actual = self.__comienzo
        while actual is not None:
            vehiculo = actual.get_dato()
            if isinstance(vehiculo, Vehiculo_Nuevo):
                vehiculo_dic = vehiculo.diccionario()
                vehiculo_dic["tipo"] = "nuevo"
                vehiculos_lista.append(vehiculo_dic)
            else:
                if isinstance(vehiculo, Vehiculo_usado):
                    vehiculo_dic = vehiculo.diccionario()
                    vehiculo_dic["tipo"] = "usado"
                    vehiculos_lista.append(vehiculo_dic)

            actual = actual.get_sig()
        with Path('vehiculos.json').open('w', encoding="utf-8-sig") as archivo:
            json.dump(vehiculos_lista, archivo, indent=4)
            archivo.close()
