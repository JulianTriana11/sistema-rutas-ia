import heapq

# (Estaciones y conexiones)

grafo = {
    "Portal Norte" : {"Calle 100": 5, "Calle 85": 7},
    "Calle 100" : {"Portal Norte" : 5, "Calle 85": 3, "Calle 72": 4},
    "Calle 85" : {"Potal Norte" : 7, "Calle 100" : 3, "Calle 72": 2},
    "Calle 72" : {"Calle 100" : 4, "Calle 85" : 2, "Calle 45": 6},
    "Calle 45" : {"Calle 72": 6}

}

#Funcion para encontrar la mejor ruta
def mejor_ruta( grafo, inicio, destino):
    cola = [(0, inicio, [])]
    visitados = set()

    while cola:
        (costo, nodo, ruta) = heapq.heappop(cola)

        if nodo in visitados:
            continue

        ruta = ruta + [nodo]
        visitados.add(nodo)
        
        if nodo == destino:
            return costo, ruta
        
        for vecino, distancia in grafo[nodo].items():
            if vecino not in visitados:
                heapq.heappush(cola, (costo + distancia, vecino,ruta))

    return float("inf"), []


#Programa principal

inicio = input("ingrese estacion de inicio: ")
destino = input("ingrese estacion de destino: ")

costo, ruta = mejor_ruta(grafo, inicio, destino)

print("\n Mejor ruta encontrada: ")
for estacion in ruta:
    print(estacion)

print("Costo total: ", costo)
        