# lector_matriz.py

import os
import pandas as pd
import fitz  # PyMuPDF

def leer_matriz_desde_archivo(ruta_archivo):
    """
    Detecta la extensión del archivo y llama a la función correspondiente.
    """
    ext = os.path.splitext(ruta_archivo)[1].lower()

    if ext == ".txt":
        return leer_txt(ruta_archivo)
    elif ext == ".xlsx":
        return leer_excel(ruta_archivo)
    elif ext == ".pdf":
        return leer_pdf(ruta_archivo)
    else:
        raise ValueError("Formato no soportado. Usa .txt, .xlsx o .pdf")


def leer_txt(ruta):
    matriz = []
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            if linea.strip():
                fila = [int(num) for num in linea.strip().split()]
                matriz.append(fila)
    return matriz


def leer_excel(ruta):
    df = pd.read_excel(ruta, header=None)
    return df.fillna(0).astype(int).values.tolist()


def leer_pdf(ruta):
    """
    Lee una matriz numérica desde un PDF.
    Se asume que cada línea contiene números separados por espacio.
    """
    matriz = []
    with fitz.open(ruta) as doc:
        for pagina in doc:
            texto = pagina.get_text()
            for linea in texto.splitlines():
                try:
                    fila = [int(num) for num in linea.strip().split()]
                    if fila:
                        matriz.append(fila)
                except:
                    continue  # Ignora líneas no numéricas
    return matriz


def validar_matriz_cuadrada(matriz):
    """
    Verifica que la matriz sea cuadrada.
    """
    n = len(matriz)
    return all(len(fila) == n for fila in matriz)
