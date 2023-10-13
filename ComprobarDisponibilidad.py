from RedBayesianaAlmacen import modelo
from Laberinto import *

def disponibilidad(articulos):
    for producto, cantidad in articulos.items():
        R1 = {'Demanda': producto, 'Unidades': 'Pocas unidades' if cantidad < 40 else 'Unidades promedio' if 40 <= cantidad <= 70 else 'Muchas unidades'}
        predit_R1 = modelo.predict_proba(R1)
        disponibilidad = (predit_R1[-1].parameters[0]['Disponible']) * 100
        print(f"El artículo es: {producto} y tiene una disponibilidad del {disponibilidad:.2f}% de estar disponible en los próximos días")

def mostrar_menu():
    print("\nConsulta de productos: \n")
    print("1. Articulos Electronicos")
    print("2. Articulos Electrodomesticos")
    print("3. Articulos Mobiliario")
    print("4. Articulos Herramientas\n")

def main():
    while True:
        mostrar_menu()
        opcion_elegida = input("Elige una de las anteriores opciones (o ingresa '5' para salir): ")

        if opcion_elegida == "1":
            print("\nHas elegido Articulos Electrónicos.\n")
            disponibilidad(ArticulosA)
        elif opcion_elegida == "2":
            print("\nHas elegido Articulos Electrodomesticos.\n")
            disponibilidad(ArticulosB)
        elif opcion_elegida == "3":
            print("\nHas elegido Articulos Mobiliario.\n")
            disponibilidad(ArticulosC)
        elif opcion_elegida == "4":
            print("\nHas elegido Articulos Herramientas.\n")
            disponibilidad(ArticulosD)
        elif opcion_elegida == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")
        
        # Preguntar si se desea ver el menú nuevamente
        print("\n¿Deseas ver el menú nuevamente?\n ")
        print("1.Si")
        print("2.No")
        repetir = input("\nPor favor, ingresa una de las opciones: ").strip().lower()
        
        if repetir != "1":
            print("\nSaliendo del programa.")
            break

if __name__ == "__main__":
    main()
