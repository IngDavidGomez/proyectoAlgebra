def recorrido_ascendente(matriz):
    n = len(matriz)
    recorrido = list(range(n))  # [0, 1, 2, ..., n-1]
    recorrido.append(0)         # Regresa al inicio
    return recorrido
