# graficador.py

import networkx as nx
import matplotlib.pyplot as plt

def graficar_recorrido(matriz, recorrido, titulo='Recorrido'):
    """
    Dibuja un grafo con el recorrido resaltado.
    """
    G = nx.Graph()
    n = len(matriz)

    # Agregar todos los nodos y aristas con peso
    for i in range(n):
        for j in range(i + 1, n):
            peso = matriz[i][j]
            if peso > 0:
                G.add_edge(i, j, weight=peso)

    pos = nx.circular_layout(G)

    # Dibujar el grafo base
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Dibujar el recorrido en rojo
    path_edges = list(zip(recorrido, recorrido[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)

    plt.title(titulo)
    plt.tight_layout()
    plt.show()
