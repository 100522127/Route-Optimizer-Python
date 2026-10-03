import math

class Grafo:
    def __init__(self, ruta_fichero_adyacencia, ruta_fichero_coordenadas):
        # Inicialización de diccionarios, para guardas nodos y a su vez guardar en un dicionario a sus vecinos y costes
        self.adyacencia = {}
        # Inicialización de diccionarios para guardar las coordenadas de cada nodo
        self.coordenadas = {}

        self.num_vertices = 0
        self.num_aristas = 0
        
        # Proceso de carga del grafo y descripción de cada vértice (nodos y sus coordenadas) y aristas (coste entre dos nodos)
        self._cargar_adyancencia_nodos(ruta_fichero_adyacencia)
        self._cargar_coordenadas_nodos(ruta_fichero_coordenadas)


    # Hemos hecho privado la función para que no pueda ser accesible desde otros ficheros
    def _cargar_adyancencia_nodos(self, ruta_fichero_grafo) -> None:
        print("Cargando las adyacencias de todos los nodos del grafo digirido")
        try:
            with open(ruta_fichero_grafo, "r") as fichero:
                for linea in fichero:
                    if linea.startswith("a"):
                        formato = linea.split()
                        u = int(formato[1])
                        v = int(formato[2])
                        coste = int(formato[3])

                        if u not in self.adyacencia:
                            self.adyacencia[u] = {}

                        self.adyacencia[u][v] = coste
                        self.num_aristas += 1
        
        except FileNotFoundError:
            print("No se ha podido encontrar su archivo.")
    
    def _cargar_coordenadas_nodos(self, ruta_fichero_coordenadas) -> None:
        print("Cargando coordenadas de los nodos")
        try:
            with open(ruta_fichero_coordenadas, "r") as fichero:
                for linea in fichero:
                    if linea.startswith("v"):
                        formato = linea.split()
                        nodo = int(formato[1])
                        longitud = float(formato[2]) / float(10**6)
                        latitud = float(formato[3]) / float(10**6)

                        self.coordenadas[nodo] = (latitud, longitud)
                        self.num_vertices += 1
        except FileNotFoundError:
            print("No se ha podido encontrar el archivo")
    
    # Obtener todos los vecinos del nodo seleccionado
    def obtener_vecinos(self, nodo) -> list:
        vecinos = []
        if nodo in self.adyacencia:
            for vecino in self.adyacencia[nodo]:
                vecinos.append(vecino)
        return vecinos
    
    # Obtener el coste que hay entre dos arcos
    def obtener_coste_arco(self, nodo_origen, nodo_destino) -> int:
        return self.adyacencia[nodo_origen][nodo_destino]

    def heuristica_euclides(self, nodo_actual, nodo_destino) -> float:
        """
        Función para obtener la heurística, utilizando la heurística de Euclides
        que viene dada por la siguiente fórmula:
                        · h = sqrt((Δlat) ^ 2 + (Δlon) ^ 2)
        h -> heuristica
        lat -> latitud
        lon -> lontitud
        """

        # Obtenemos coordenadas del nodo actual
        lat_act = self.coordenadas[nodo_actual][0]
        lon_act = self.coordenadas[nodo_actual][1]

        # Obtenemos coordenadas del nodo destino
        lat_dest = self.coordenadas[nodo_destino][0]
        lon_dest = self.coordenadas[nodo_destino][1]

        # Diferencias de coordenadas en grados
        delta_lat = lat_dest - lat_act
        delta_lon = lon_dest - lon_act

        # Conversión de grados a metros
        metros_lat = delta_lat * 111320
        metros_lon = delta_lon * 111320 * math.cos(math.radians((lat_act + lat_dest) / 2))

        # Aplicamos la fórmula de distancia euclídea en metros
        heuristica = math.sqrt(metros_lat ** 2 + metros_lon ** 2)

        return heuristica
