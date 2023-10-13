from Almacen import *

class Nodo():
    def __init__(self, estado, padre, accion):
        self.estado = estado
        self.padre = padre
        self.accion = accion

class Frontera():
    def __init__(self):
        self.frontera = []

    def empty(self):
        return len(self.frontera) == 0

    def add(self, nodo):
        self.frontera.append(nodo)

    def eliminar(self):
        if self.empty():
            raise Exception("Frontera vacía")
        else:
            nodo = self.frontera[0]
            self.frontera = self.frontera[1:]
            return nodo

    def contiene_estado(self, estado):
        return any(nodo.estado == estado for nodo in self.frontera)

class Laberinto():
    def __init__(self, filename):
        with open(filename) as file:
            contenido = file.read()

        contenido = contenido.splitlines()
        self.altura = len(contenido)
        self.ancho = max(len(line) for line in contenido)
        self.muros = []

        for i in range(self.altura):
            filas = []
            for j in range(self.ancho):
                try:
                    if contenido[i][j] == "$":
                        self.inicio = (i, j)
                        filas.append(False)
                    elif contenido[i][j] == "A":
                        self.AlmacenA = (i, j)
                        filas.append(False)
                    elif contenido[i][j] == "B":
                        self.AlmacenB = (i, j)
                        filas.append(False)
                    elif contenido[i][j] == "C":
                        self.AlmacenC = (i, j)
                        filas.append(False)
                    elif contenido[i][j] == "D":
                        self.AlmacenD = (i, j)
                        filas.append(False)
                    elif contenido[i][j] == " ":
                        filas.append(False)
                    else:
                        filas.append(True)
                except IndexError:
                    filas.append(False)
            self.muros.append(filas)
        self.solucion = None

    def print(self):
        sol = self.solucion[1] if self.solucion is not None else None
        print()
        for i, fila in enumerate(self.muros):
            for j, col in enumerate(fila):
                if col:
                    print("█", end="")
                elif (i, j) == self.inicio:
                    print("❖", end="")
                elif (i,j) == self.objetivo:
                    print("✩" , end="")    
                elif (i, j) == self.AlmacenA:
                    print("🜟", end="")
                elif (i, j) == self.AlmacenB:
                    print("✂", end="")
                elif (i, j) == self.AlmacenC:
                    print("☎", end="")
                elif (i, j) == self.AlmacenD:
                    print("☭", end="")
                elif sol is not None and (i, j) in sol:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def vecinos(self, estado):
        fila, col = estado
        candidatos = [
            ("up", (fila - 1, col)),
            ("down", (fila + 1, col)),
            ("left", (fila, col - 1)),
            ("right", (fila, col + 1))
        ]
        
        resultados = []
        for accion, (f, c) in candidatos:
            if 0 <= f < self.altura and 0 <= c < self.ancho and not self.muros[f][c]:
                resultados.append((accion, (f, c)))
        return resultados

    def solve(self):
        self.num_explorados = 0
    
        start = Nodo(estado=self.inicio, padre=None, accion=None)
        frontera = Frontera()
        frontera.add(start)
        
        self.explorado = set()

        while not frontera.empty():
            nodo = frontera.eliminar()
            self.num_explorados += 1
            self.productos_descargados =[]
            
            if nodo.estado == self.objetivo:
                if self.objetivo == self.AlmacenA:
                    self.productos_descargados.extend(productosElectronica)
                    self.numerodeproductos = NumArticulosElectronica
                    Carrito[0].clear()
                    
                elif self.objetivo == self.AlmacenB:
                    self.productos_descargados.extend(productosElectrodomesticos)
                    self.numerodeproductos = NumArticulosElectrodomesticos
                    Carrito[1].clear()
                    
                elif self.objetivo == self.AlmacenC:
                    self.productos_descargados.extend(productosMobiliarios)
                    self.numerodeproductos = NumArticulosMobiliario
                    Carrito[2].clear()
                    
                elif self.objetivo == self.AlmacenD:
                    self.productos_descargados.extend(productosHerramientas)
                    self.numerodeproductos = NumArticulosHerramientas
                    Carrito[3].clear()
                    
            if nodo.estado == self.objetivo:
                acciones = [] ; cel = []
                
                while nodo.padre is not None:
                    acciones.append(nodo.accion)
                    cel.append(nodo.estado)
                    nodo = nodo.padre
                acciones.reverse()
                cel.reverse()
                self.solucion = (acciones, cel)
                return

            self.explorado.add(nodo.estado)

            for accion, estado in self.vecinos(nodo.estado):
                if not frontera.contiene_estado(estado) and estado not in self.explorado:
                    hijo = Nodo(estado=estado, padre=nodo, accion=accion)
                    frontera.add(hijo)

    def imprimir_productos_descargados(self):
        asa =[]
        for producto in self.productos_descargados:
            asa.append(producto)
        print("Los productos descargados son:" , asa)    
        print("EL numero total de articulos descargados son: ",(self.numerodeproductos))

l = Laberinto('almacen.txt')

def distancia(punto1, punto2):
    return abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])

objetivosO = []

AA = (NumArticulosElectronica, l.AlmacenA)
objetivosO.append(AA)

BB = (NumArticulosElectrodomesticos, l.AlmacenB)
objetivosO.append(BB)

CC = (NumArticulosMobiliario, l.AlmacenC)
objetivosO.append(CC)

DD = (NumArticulosHerramientas, l.AlmacenD)
objetivosO.append(DD)

objetivosCompletados = []
objetivossorted = sorted(objetivosO,reverse=True)

while objetivosO:
    # Calcula la distancia a todos los almacenes
    objetivo_actualNum = objetivossorted.pop(0)
    distancias = [distancia(l.inicio, objetivo[1]) for objetivo in objetivosO]

    # Encuentra los almacenes con artículos pendientes
    almacenes_con_pendientes = [objetivo for objetivo in objetivosO if objetivo[0] > 0]
    
    # Si hay almacenes con artículos pendientes, selecciona el más cercano
    
    if almacenes_con_pendientes:
        objetivo_actualD = min(almacenes_con_pendientes, key=lambda x: distancias[objetivosO.index(x)]) 
      
    print(objetivo_actualD,objetivo_actualNum)
        
    if objetivo_actualNum == objetivo_actualD:
        objetivo_actual = objetivo_actualNum
    else:
        objetivo_actual = objetivo_actualD    
            
    # Agrega el almacén actual a los objetivos completados y elimínalo de objetivosO
    objetivosCompletados.append(objetivo_actual[1])
    objetivosO.remove(objetivo_actual)

    l.objetivo = objetivo_actual[1]
    
    if l.objetivo == l.AlmacenA:
                 print("\n---------------------Almacen Electronica")
    elif l.objetivo== l.AlmacenB:
                print("\n---------------------Almacen Electrodomesticos")
    elif l.objetivo == l.AlmacenC:
                 print("\n---------------------Almacen Mobiliarios")
    elif l.objetivo == l.AlmacenD:
                print("\n---------------------Almacen Herramientas")
    # Aquí puedes realizar cualquier otra operación necesaria antes de visitar el almacén, si es necesario.
    
    # Luego, ejecuta la búsqueda y visita el almacén
    l.solve()
    l.print()
    l.imprimir_productos_descargados()
    
    l.inicio = l.objetivo  # Actualiza el punto de inicio para la próxima visita
