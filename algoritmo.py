from grafo import Grafo
from abierta import Abierta
from cerrada import Cerrada

class Algoritmo:
    def __init__(self, grafo: Grafo, fuerza_bruta):
        """ 
        Implementación del algoritmo A*, con posibilidad de 
        fuerza bruta donde la heurística es 0, lo que lo convierte en Dijkstra.
        """
        self.grafo = grafo
        self.fuerza_bruta = fuerza_bruta
        self.obj_abierta = Abierta()
        self.obj_cerrada = Cerrada()

    def calcular_heuristica(self, nodo_actual, nodo_destino):
        """ Determina si se va a usar la heurística o no."""

        if self.fuerza_bruta:
            return 0
        else:
            return self.grafo.heuristica_euclides(nodo_actual, nodo_destino)
    
    def solver(self, nodo_origen, nodo_destino) -> tuple[int, int, int, list]:
        """ Implementación del algoritmo A*. """

        # Inicializamos un diccionario g(n) para almacenar los costes desde el nodo origen hasta cada nodo
        g_n = {nodo_origen: 0}

        # Diccionario para posteriormente poder reconstruir el camino
        memoria = {}

        # Insertamos el nodo origen en la lista abierta con su f(n), donde g(n) = 0
        f_n_inicial = self.grafo.heuristica_euclides(nodo_origen, nodo_destino)

        # Insertar nodo origen en lista abierta
        self.obj_abierta.insertar_nodo(nodo_origen, f_n_inicial)
        
        # Mientras la lista no esté vacía
        while self.obj_abierta.lista_abierta is not None:

            # Se extrae el mejor nodo de la lista abierta e intenta expandirlo
            mejor_nodo = self.obj_abierta.expandir_mejor_nodo()

            # Si no hay mejor nodo, la lista está vacía y se termina el algoritmo
            if mejor_nodo is None:
                return 0, 0, 0, None

            # Separa la tupla en f(n) y el nodo actual
            f_n_actual, nodo_actual = mejor_nodo[0], mejor_nodo[1]

            # Terminación: detenerse cuando se expande el nodo_destino
            if nodo_actual == nodo_destino:
                
                coste_total = g_n[nodo_actual]
                num_expansiones = self.obj_cerrada.expansiones
                num_nodos_generados = self.obj_abierta.nodos_generados
                camino = self._recorrido(memoria, nodo_origen, nodo_destino)

                return coste_total, num_expansiones, num_nodos_generados, camino

            # Si el nodo está en la lista cerrada, no se inserta
            if self.obj_cerrada.verificar_existencia(nodo_actual):
                continue
            
            # Insertar el nodo actual en la lista cerrada
            self.obj_cerrada.insertar_nodo_expandido(nodo_actual, f_n_actual)
            
            # Obtener los vecinos del nodo actual
            lista_vecinos = self.grafo.obtener_vecinos(nodo_actual)

            # Para cada vecino, calcular g(n), h(n) y f(n)
            for vecino in lista_vecinos:

                # Obtiene los costes del vecino y del nodo actual expandido
                coste_arco = self.grafo.obtener_coste_arco(nodo_actual, vecino)

                # Calcula el coste g(n) del vecino a partir del coste del nodo actual
                g_siguiente = g_n[nodo_actual] + coste_arco

                # Si el vecino no está en g(n) o se ha encontrado un camino mejor
                if vecino not in g_n or g_siguiente < g_n[vecino]:
                    
                    # Actualiza la memoria y los costes
                    memoria[vecino] = nodo_actual
                    g_n[vecino] = g_siguiente

                    # Calcula la heurística y f(n)
                    h = self.calcular_heuristica(vecino, nodo_destino)
                    f_n = g_siguiente + h

                    # Inserta el vecino en la lista abierta
                    self.obj_abierta.insertar_nodo(vecino, f_n)

    def _recorrido(self, memoria, nodo_origen, nodo_destino):
        """Reconstruye el camino desde el nodo origen al nodo destino"""

        # Lista para almacenar el camino realizado desde el origen al destino
        camino = []

        # Recontruimos hacía detrás hasta llegar al nodo origen
        nodo_actual = nodo_destino

        # Mientras no lleguemos al nodo origen, se va añadiendo el nodo la lista
        while nodo_actual != nodo_origen:
            camino.append(nodo_actual)
            nodo_actual = memoria[nodo_actual]

        # Añadimos el nodo origen y revertimos la lista para tener el camino ordenado
        camino.append(nodo_origen)
        camino.reverse()
        
        return camino