## main.py

from lector.lector_Archivos import leer_matriz_desde_archivo, validar_matriz_cuadrada
from generadorSimetrica.convertidorMatriz import hacer_matriz_simetrica
from recorridoAscendente.recorridoAscendente import recorrido_ascendente
from recorridoTSP.recorridoTsp import recorrido_tsp_minimo,calcular_costo
from graficador.graficador import graficar_recorrido

def imprimir_matriz(m):
    for fila in m:
        print(fila)

def main():
    ruta = input("Ingrese el nombre del archivo (.txt, .xlsx o .pdf): ").strip()

    # Leer la matriz
    matriz = leer_matriz_desde_archivo(ruta)

    if not matriz:
        print("No se pudo leer la matriz.")
        return

    print("\nMatriz original:")
    imprimir_matriz(matriz)

    if not validar_matriz_cuadrada(matriz):
        print("Error: la matriz no es cuadrada.")
        return

    # Hacerla simétrica
    matriz_simetrica = hacer_matriz_simetrica(matriz)
    print("\nMatriz simétrica:")
    imprimir_matriz(matriz_simetrica)

    # Recorrido ascendente
    print("\nRecorrido ascendente (vecino más cercano):")
    recorrido1 = recorrido_ascendente(matriz_simetrica)
    print(recorrido1)
    print("Costo del recorrido ascendente:", calcular_costo(matriz_simetrica, recorrido1))
    graficar_recorrido(matriz_simetrica, recorrido1, "Recorrido Ascendente")

    # Recorrido TSP exacto
    print("\nRecorrido mínimo (TSP exacto):")
    recorrido2 = recorrido_tsp_minimo(matriz_simetrica)
    print(recorrido2)
    print("Costo del recorrido TSP:", calcular_costo(matriz_simetrica, recorrido2))
    graficar_recorrido(matriz_simetrica, recorrido2, "Recorrido TSP Mínimo")

if __name__ == "__main__":
    main()
