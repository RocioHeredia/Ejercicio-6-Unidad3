from ClassLista import listaVehiculos

def menu():
    print('1. Insertar un vehículo en la colección en una posición determinada.')
    print('2. Agregar un vehículo a la colección.')
    print('3. Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.')
    print('4. Modificar el precio base, y luego mostrar el precio de venta.')
    print('5. Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.')
    print('6. Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.')
    print('7. Almacenar los objetos de la colección Lista en el archivo')
    print('8. Salir')


if __name__ == '__main__':
    lista = listaVehiculos()
    lista.leerJSONArchivo()
    opcion = None

    while opcion != 0:
        menu()
        opcion = int(input('\n Ingrese una opción: '))

        if opcion == 1:
            posicion = int(input('Ingrese posicion en la que desea insertar el vehiculo: '))
            lista.insertar_vehiculo(posicion)  # Insertar un vehiculo en la coleccion en una posicion determinada
            lista.mostrar()

        elif opcion == 2:
            lista.agregar_un_vehiculo_a_la_coleccion()  # Se agrega un vehiculo a la coleccion
            lista.mostrar()
        elif opcion == 3:
            posicion = int(input('Ingrese posicion para mostrar tipo de objeto: '))
            lista.mostrar_tipo_vehiculo(posicion)
        elif opcion == 4:
            patente = str(input('Ingrese patente del vehiculo usado: '))
            lista.modificacion(patente)
        elif opcion == 5:
            lista.vehiculo_economico()
        elif opcion == 6:
            lista.vehiculo_venta()
        elif opcion == 7:
            lista.AlmacenarEnArchivo()
        elif opcion == 8:
            print('Saliendo...')
            break
        else:
            if opcion >= 9:
                opcion = int(input('\n Ingrese una opción: '))
