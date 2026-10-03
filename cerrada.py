class Cerrada:

    def __init__(self):
        """ Clase que implementa la lista cerrada del algoritmo A*. """
        self.lista_cerrada = {}
        self.expansiones = 0
    
    def insertar_nodo_expandido(self, nodo, coste):
        """ Inserta un nodo ya expandido en la lista cerrada. """
        self.lista_cerrada[nodo] = coste

        # Para contar el número de expansiones realizadas
        self.expansiones += 1
    
    def verificar_existencia(self, nodo):
        """ Verifica si un nodo ya está en la lista cerrada, útil para evitar re-expansiones. """
        return nodo in self.lista_cerrada
