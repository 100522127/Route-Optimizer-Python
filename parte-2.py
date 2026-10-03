#!/usr/bin/env python3
import sys
import time
from algoritmo import Algoritmo
from grafo import Grafo



def leer_argumentos():
    """ Función para extraer los argumentos pasados como parámetros"""
    if len(sys.argv) != 5:
        raise Exception ("Error: Debe seguir este formato: ./parte-2.py 1 309 USA-road-d.BAY solucion")

    return int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], sys.argv[4]

def cargar_grafo(ruta_del_mapa):
    """ Función para cargar el grafo desde los ficheros de adyacencia y coordenadas"""
    ruta_fichero_adyacencia, ruta_fichero_coordenadas = f"{ruta_del_mapa}.gr", f"{ruta_del_mapa}.co"
    grafo_cargado = Grafo(ruta_fichero_adyacencia, ruta_fichero_coordenadas)

    return grafo_cargado

def main():
    """ Función principal del programa """

    # Extracción de argumentos
    nodo_origen, nodo_destino, ruta_del_mapa, ruta_salida = leer_argumentos()

    # Carga del grafo
    grafo = cargar_grafo(ruta_del_mapa)

    # Extracción de información del grafo
    num_vertices = grafo.num_vertices
    num_aristas = grafo.num_aristas

    # Selector del algoritmo que se quiera probar
    while True:
        fuerza_bruta = input("¿Desea utilizar el algoritmo de fuerza bruta? (s/n): ")
        if fuerza_bruta.lower() == "s":
            fuerza_bruta = True
            break
        elif fuerza_bruta.lower() == "n":
            fuerza_bruta = False
            break
        else:
            print("Entrada no válida")
            continue
    
    # Ejecución del algoritmo
    algoritmo = Algoritmo(grafo, fuerza_bruta)

    # Inicio de la medición del tiempo
    timepo_inicial = time.time()

    # Resolución del problema de busqueda del camino óptimo
    coste_total, num_expasiones, num_nodos_generados, camino = algoritmo.solver(nodo_origen, nodo_destino)

    # Fin de la medición del tiempo
    tiempo_final = time.time()

    # Cálculo del tiempo total que tardó en encontrar el camino óptimo
    tiempo_ejecucion = tiempo_final - timepo_inicial

    # Cálculo de nodos generados por segundo
    nodos_por_segundo = round(num_nodos_generados / tiempo_ejecucion, 2)

    # Impresión de resultados por pantalla según el formato solicitado
    print(f"# vertices: {num_vertices}")
    print(f"# arcos: {num_aristas}")
    print(f"Solución optima con coste: {coste_total}")
    print("\n")
    print(f"Tiempo de ejecución: {tiempo_ejecucion} segundos")
    print(f"# expansiones: {num_expasiones} ({nodos_por_segundo} nodos/segundo)")

    if camino is None:
        print("No se ha encontrado solución")
        return
    
    # Generación del fichero de saldida con el camino óptimo siguiendo el formato solicitado: <nodo> - (<coste_arista>) - <nodo> ...
    with open(ruta_salida, "w") as fichero:

        for i in range(len(camino) - 1):
            u = camino[i]
            v = camino[i+1]
            arista = grafo.obtener_coste_arco(u, v)
            fichero.write(f"{u} - ({arista}) - ")

        fichero.write(f"{camino[-1]}\n")
    
if __name__ == "__main__":
    main()