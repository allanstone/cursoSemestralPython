import heapq,sys
class Grafo:
    
    def __init__(self):
        """Constructor de la clase Grafo"""
        self.vertices = {}
        
    def agregarVertice(self, nombre, opciones):
        self.vertices[nombre] = opciones
    
    def djkstra(self, inicio, fin):
        distancias = {} # Diccionario de distancias
        anterior = {}  # Diccionario de nodos previos para la ruta optimo
        nodos = [] # Lista de nodos visitados

        for vertice in self.vertices:
            if vertice == inicio: 
                # Distancia tentativa inicial -> cero
                distancias[vertice] = 0
                #Colocamos en una cola de prioridad el nodo y su distancia y 
                heapq.heappush(nodos, [0, vertice])
            else:
                #En caso contrario utilizamos una variable del sistema para asignar
                #un peso infinito
                distancias[vertice] = sys.maxsize
                heapq.heappush(nodos, [sys.maxsize, vertice])
            anterior[vertice] = None
        
        while nodos:
            menor = heapq.heappop(nodos)[1] # vertice en la grafica con la menor distancia
            if menor == fin: #Si es el más pequeño lo añade a la ruta
                ruta = []
                while anterior[menor]: #Hasta que encuentra el mas corto
                    ruta.append(menor)
                    menor = anterior[menor] #Reemplaza el peso
                return ruta
            if distancias[menor] == sys.maxsize: #En este caso el nodo no es alcanzable
                break
            
            for vecino in self.vertices[menor]: 
                suma = distancias[menor] + self.vertices[menor][vecino] 
                if suma < distancias[vecino]: 
                    distancias[vecino] = suma
                    anterior[vecino] = menor
                    for n in nodos:
                        if n[1] == vecino:
                            n[0] = suma
                            break
                    heapq.heapify(nodos)
        return distancias
        
    def __str__(self):
        """
            Método mágico para imprimir el grafico
            :returns: str. self.vertices-- Lista de vertices casteada a cadena.
        """
        return str(self.vertices)

if __name__ == '__main__':
    g = Grafo()
    #g.agregarVertice('A', {'B': 7, 'C': 8})
    #g.agregarVertice('B', {'A': 7, 'F': 2})
    #g.agregarVertice('C', {'A': 8, 'F': 6, 'G': 4})
    #g.agregarVertice('D', {'F': 8})
    #g.agregarVertice('E', {'H': 1})
    #g.agregarVertice('F', {'B': 2, 'C': 6, 'D': 8, 'G': 9, 'H': 3})
    #g.agregarVertice('G', {'C': 4, 'F': 9})
    #g.agregarVertice('H', {'E': 1, 'F': 3})
    g.agregarVertice('A',{'B':1,'C':3})
    g.agregarVertice('B',{'E':1,'D':5})
    g.agregarVertice('C',{'F':3})
    g.agregarVertice('D',{'C':4,"F":3})
    g.agregarVertice('E',{'G':1,'F':2})
    g.agregarVertice('F',{'G':6})
    g.agregarVertice('G',{'A':9,})
    print("Camino de A a G",g.djkstra('A','G'))
    print("Camino de B a G",g.djkstra('B','G'))