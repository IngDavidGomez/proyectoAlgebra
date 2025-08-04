import streamlit as st
import pandas as pd
import fitz
import matplotlib.pyplot as plt
import networkx as nx

from lector.lector_Archivos import leer_matriz_desde_archivo, validar_matriz_cuadrada
from generadorSimetrica.convertidorMatriz import hacer_matriz_simetrica
from recorridoAscendente.recorridoAscendente import recorrido_ascendente
from recorridoTSP.recorridoTsp import recorrido_tsp_minimo, calcular_costo

st.title("Recorridos en Matrices 🚀")

def leer_archivo(archivo, extension):
    if extension == ".txt":
        contenido = archivo.read().decode("utf-8")
        matriz = [[int(num) for num in linea.split()] for linea in contenido.strip().splitlines()]
    elif extension == ".xlsx":
        df = pd.read_excel(archivo, header=None)
        matriz = df.fillna(0).astype(int).values.tolist()
    elif extension == ".pdf":
        texto = fitz.open(stream=archivo.read(), filetype="pdf")[0].get_text()
        matriz = []
        for linea in texto.splitlines():
            try:
                fila = [int(num) for num in linea.strip().split()]
                if fila:
                    matriz.append(fila)
            except:
                continue
    else:
        st.error("Formato no soportado.")
        return None
    return matriz

def graficar_pasos(matriz, recorrido, paso_max, titulo="Recorrido"):
    G = nx.Graph()
    n = len(matriz)

    for i in range(n):
        for j in range(i + 1, n):
            peso = matriz[i][j]
            if peso > 0:
                G.add_edge(i, j, weight=peso)

    pos = nx.circular_layout(G)
    fig, ax = plt.subplots(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=600, ax=ax)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, ax=ax)

    if paso_max > 1:
        edges = list(zip(recorrido[:paso_max], recorrido[1:paso_max + 1]))
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2, ax=ax)

    plt.title(f"{titulo} - Paso {paso_max}/{len(recorrido) - 1}")
    st.pyplot(fig)

archivo = st.file_uploader("Subí una matriz (.txt, .xlsx, .pdf)", type=["txt", "xlsx", "pdf"])

if archivo:
    extension = f".{archivo.name.split('.')[-1]}"
    matriz = leer_archivo(archivo, extension)

    if not matriz or not validar_matriz_cuadrada(matriz):
        st.error("Error al leer o validar la matriz.")
    else:
        st.subheader("📊 Matriz Original:")
        st.write(pd.DataFrame(matriz))

        simetrica = hacer_matriz_simetrica(matriz)

        st.subheader("🔁 Matriz Simétrica:")
        st.write(pd.DataFrame(simetrica))

        recorrido1 = recorrido_ascendente(simetrica)
        costo1 = calcular_costo(simetrica, recorrido1)


        st.subheader("🟡 Recorrido Ascendente:")
        st.text(f"Recorrido: {recorrido1}")
        st.text(f"Costo: {costo1}")

        paso1 = st.slider("Paso recorrido ascendente", min_value=1, max_value=len(recorrido1) - 1, value=1, key="asc")
        graficar_pasos(simetrica, recorrido1, paso1, "Recorrido Ascendente")

        recorrido2 = recorrido_tsp_minimo(simetrica)
        costo2 = calcular_costo(simetrica, recorrido2)

        st.subheader("🟢 Recorrido TSP (Heurístico):")
        st.text(f"Recorrido: {recorrido2}")
        st.text(f"Costo: {costo2}")

        paso2 = st.slider("Paso recorrido TSP", min_value=1, max_value=len(recorrido2) - 1, value=1, key="tsp")
        graficar_pasos(simetrica, recorrido2, paso2, "Recorrido TSP")
