# generador_simetrica.py

def hacer_matriz_simetrica(matriz):
    """
    Convierte una matriz triangular superior o inferior en simétrica,
    copiando el valor correspondiente de la otra mitad.
    Si ya es simétrica, no la modifica.
    """
    n = len(matriz)
    simetrica = [fila[:] for fila in matriz]  # Copia profunda

    for i in range(n):
        for j in range(n):
            if i != j:
                # Si una de las dos entradas es 0, copiar la otra
                if simetrica[i][j] == 0 and simetrica[j][i] != 0:
                    simetrica[i][j] = simetrica[j][i]
                elif simetrica[j][i] == 0 and simetrica[i][j] != 0:
                    simetrica[j][i] = simetrica[i][j]
                # Si ambas existen y son diferentes, escoger la mayor (o menor si se prefiere)
                elif simetrica[i][j] != simetrica[j][i]:
                    simetrica[i][j] = simetrica[j][i] = max(simetrica[i][j], simetrica[j][i])
    return simetrica
