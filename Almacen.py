import csv
import random

ArticulosELectronica = {}
ArticulosElectrodomesticos = {}
ArticulosMobiliarios = {}
ArticulosHerramientas = {}

# Abre el archivo CSV
with open("BaseDatos.csv", "r") as f:

    # Crea un lector de CSV
    reader = csv.reader(f, delimiter=",")

    # Ignora el encabezado
    next(reader, None)
    
    # Lee las filas del archivo CSV
    for row in reader:
       
        if row [1] == "ElectrÃ³nica":
            ArticulosELectronica[row[0]] = random.randint(1, 100)
            
        elif row[1] == "ElectrodomÃ©sticos":
            ArticulosElectrodomesticos[row[0]] = random.randint(1, 100)
            
        elif row[1] == "Mobiliario":
            ArticulosMobiliarios[row[0]] = random.randint(1, 100)
            
        elif row[1] == "Herramientas":
            ArticulosHerramientas[row[0]] = random.randint(1, 100)
            
         
ArticulosELectronica =sorted(ArticulosELectronica.items())
AE= random.sample(ArticulosELectronica, 3)

ArticulosElectrodomesticos=sorted(ArticulosElectrodomesticos.items())
AD= random.sample(ArticulosElectrodomesticos, 3)

ArticulosMobiliarios =sorted(ArticulosMobiliarios.items())
AM= random.sample(ArticulosMobiliarios, 3)

ArticulosHerramientas =sorted(ArticulosHerramientas.items())
AH= random.sample(ArticulosHerramientas, 3)

Carrito = [AE,AD,AM,AH]

ar = []
productos =[]

for sublista in Carrito:
    for elemento in sublista:
        productos.append(elemento[0])
        ar.append(elemento[1])
       
NumArticulosElectronica = sum(ar[:3]) 
NumArticulosElectrodomesticos = sum(ar[3:6])
NumArticulosMobiliario = sum(ar[6:9]) 
NumArticulosHerramientas = sum(ar[9:12]) 

productosElectronica = productos[:3]
productosElectrodomesticos = productos[3:6]   
productosMobiliarios = productos[6:9]   
productosHerramientas = productos[9:12]  

ArticulosA = {productos[i]: ar[i] for i in range(3)}
ArticulosB = {productos[i]: ar[i] for i in range(3, 6)}
ArticulosC = {productos[i]: ar[i] for i in range(6, 9)}
ArticulosD = {productos[i]: ar[i] for i in range(9, 12)}



        
        