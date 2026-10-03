class Abierta:

    def __init__(self):
        """ Clase para la gestión de una lista abierta que guarda los posibles nodos aún sin expandir. """

        # Inicizalización de una lista abierta vacía
        self.lista_abierta = []
        self.nodos_generados = 0

    def insertar_nodo(self, nodo, funcion_n) -> None:
        """ Método para insertar nodos candidatos a expandir. """

        # Agrega el elemento al final
        self.lista_abierta.append([funcion_n, nodo])

        self.nodos_generados += 1

        # Reordena hacia arriba
        self._subir(len(self.lista_abierta) - 1)

    def expandir_mejor_nodo(self) -> list:
        """ 
        Método para la seleccionar el mejor nodo a expandir, es decir, el que tenga menor f(n), donde
        f(n) = h(n) + g(n).
        h(n) -> heurística
        g(n) -> coste del origen al nodo
        
        """

        # Si la lista está vacia se ha terminado el algoritmo
        if not self.lista_abierta:
            return None

        # Toma el primer valor porque estará en el índice cero
        mejor_nodo = self.lista_abierta[0]

        # Toma el último elemento para ponerlo en la raíz (para lógica de cola de prioridad)
        ultimo = self.lista_abierta.pop()

        # Si aún quedan elementos, pone el último al principio y reordena
        if self.lista_abierta:
            self.lista_abierta[0] = ultimo

            # Reordena hacia abajo
            self._bajar(0)
        
        # Retorna la tupla con el nodo y el coste correspondiente
        return mejor_nodo 

    # Funciones adicionales que se ha incluido para la implementación de una cola de prioridad
        
    def _subir(self, indice) -> None:
        """ 
        Método para reordenar hacia arriba un nodo insertado
        Pasos:
        1. Se toma el nodo insertado como el hijo.
        2. Se compara con su padre.
        3. Si es menor que su padre, se intercambian.
        4. Si ya no es menor que su padre, termina.
        5. En otro caso, volver al paso 1.
        """

        # Buscamos el índice del padre del nodo que se acaba de insertar
        padre = (indice - 1) // 2
        # Mientras no sea la raíz y sea menor que su padre
        while indice > 0 and self.lista_abierta[indice][0] < self.lista_abierta[padre][0]:
            # Intercambio
            self.lista_abierta[indice], self.lista_abierta[padre] = self.lista_abierta[padre], self.lista_abierta[indice]
            # Actualizo índices
            indice = padre
            padre = (indice - 1) // 2

    def _bajar(self, indice) -> None:
        """ 
        Método para reordenar hacia abajo, tras expandir el mejor nodo.
        Pasos:
        1. Se el último nodo como el padre.
        2. Compara con sus hijos.
        3, Si alguno de los hijos es menor, intercambia con el menor de los dos.
        4. Si ya no es mayor que ninguno de sus hijos, termina.
        5. En otro caso, volver al paso 1. 
        """


        longitud = len(self.lista_abierta)
        # Inicializamos suponiendo que el menor es el padre.
        menor = indice
        
        # Índices de los hijos
        izq = 2 * indice + 1
        der = 2 * indice + 2

        # Comparar con la f(n) con el hijo izquierdo
        if izq < longitud and self.lista_abierta[izq][0] < self.lista_abierta[menor][0]:
            menor = izq

        # Comparar con con la f(n) con el hijo derecho, y si es mejor candidato que el izquierdo
        if der < longitud and self.lista_abierta[der][0] < self.lista_abierta[menor][0]:
            menor = der

        # Si el menor no es el actual, intercambiamos y seguimos bajando
        if menor != indice:
            # Intercambiamos el padre con el hijo menor
            self.lista_abierta[indice], self.lista_abierta[menor] = self.lista_abierta[menor], self.lista_abierta[indice]

            # Repetimos el proceso
            self._bajar(menor)
    