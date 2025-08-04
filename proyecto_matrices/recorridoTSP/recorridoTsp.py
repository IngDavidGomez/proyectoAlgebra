# recorrido_tsp.py

def vecino_mas_cercano(matriz):
    n = len(matriz)
    visitado = [False] * n
    recorrido = [0]
    visitado[0] = True

    for _ in range(n - 1):
        actual = recorrido[-1]
        siguiente = min(
            ((matriz[actual][j], j) for j in range(n) if not visitado[j]),
            key=lambda x: x[0]
        )[1]
        recorrido.append(siguiente)
        visitado[siguiente] = True

    recorrido.append(0)  # Vuelve al inicio
    return recorrido


def calcular_costo(matriz, recorrido):
    return sum(matriz[recorrido[i]][recorrido[i + 1]] for i in range(len(recorrido) - 1))


def two_opt(matriz, recorrido):
    mejorado = True
    mejor_ruta = recorrido[:]
    mejor_costo = calcular_costo(matriz, mejor_ruta)

    while mejorado:
        mejorado = False
        for i in range(1, len(mejor_ruta) - 2):
            for j in range(i + 1, len(mejor_ruta) - 1):
                if j - i == 1:
                    continue
                nueva_ruta = mejor_ruta[:]
                nueva_ruta[i:j] = mejor_ruta[j - 1:i - 1:-1]  # invertir segmento
                nuevo_costo = calcular_costo(matriz, nueva_ruta)
                if nuevo_costo < mejor_costo:
                    mejor_ruta = nueva_ruta
                    mejor_costo = nuevo_costo
                    mejorado = True
    return mejor_ruta


def recorrido_tsp_minimo(matriz):
    ruta_inicial = vecino_mas_cercano(matriz)
    ruta_mejorada = two_opt(matriz, ruta_inicial)
    return ruta_mejorada
