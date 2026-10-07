"""
pipeline.py
Script de entrega del proyecto Red Social Ficticia — IABD 2626-27

Instrucciones:
    - Implementa cada función según las especificaciones de su bloque.
    - No cambies los nombres ni las firmas de las funciones.
    - Ejecuta los tests de corrección con:
          python -m pytest tests/test_bloque1.py -v
          python -m pytest tests/test_bloque2.py -v
          python -m pytest tests/test_bloque3.py -v
          python -m pytest tests/test_bloque4.py -v
          python -m pytest tests/test_bloque5.py -v
          python -m pytest tests/ -v              # todos a la vez
"""

import os
import re

import numpy as np
import pandas as pd


# ============================================================
# BLOQUE 1 — Estructuras de datos, Regex y Lambda
# ============================================================

def usuarios_activos(lista_usuarios):
    """
    Recibe una lista de diccionarios con datos de usuarios (cargados desde CSV).
    Devuelve una lista con solo los usuarios cuyo campo 'activo' sea 'True' (string).
    """
    pass # TODO

def agrupar_por_ciudad(lista_usuarios):
    """
    Recibe una lista de diccionarios con datos de usuarios.
    Devuelve un diccionario {ciudad: [nombres_de_usuarios]}.
    Los usuarios sin ciudad (None o '') deben ignorarse.
    """
    pass # TODO


def hashtags_unicos(lista_publicaciones):
    """
    Recibe una lista de diccionarios con datos de publicaciones (cargados desde CSV).
    Cada publicación tiene 'hashtags': cadena separada por comas ('#ia,#python,...').
    Devuelve un set con todos los hashtags únicos del dataset.
    """
    pass # TODO


def top_por_seguidores(lista_usuarios, n=10):
    """
    Recibe una lista de diccionarios con datos de usuarios y un entero n.
    Devuelve una lista con los n usuarios con más seguidores (int), de mayor a menor.
    Debe usar sorted() con una función lambda como key.
    """
    pass # TODO


def extraer_hashtags_regex(texto):
    """
    Recibe un texto y extrae sus hashtags mediante expresiones regulares.
    Devuelve una lista de hashtags en minúsculas y en el orden encontrado.
    Un hashtag está formado por '#' seguido de letras, números o '_'.
    """
    pass # TODO


def publicaciones_con_hashtag(lista_publicaciones, hashtag):
    """
    Recibe publicaciones y un hashtag a buscar, por ejemplo '#ia'.
    Devuelve las publicaciones que lo contienen en el campo 'hashtags'.
    La búsqueda no distingue mayúsculas y no debe aceptar coincidencias parciales.
    Por ejemplo, '#ia' no coincide con '#iabd'.
    """
    pass # TODO

# ============================================================
# BLOQUE 2 — NumPy
# ============================================================

def estadisticas_columna(arr):
    """
    Recibe un array de NumPy con valores numéricos.
    Devuelve un diccionario con las claves:
        'media', 'mediana', 'desv_std', 'minimo', 'maximo'
    Todos los valores deben ser float.
    """
    pass  # TODO


def resumen_publicaciones(matriz):
    """
    Recibe una matriz de NumPy de publicaciones por usuario (filas) y tipo
    de contenido (columnas), como la del ejercicio 5.
    Devuelve un diccionario con las claves:
        'total_por_usuario'         -> array con el total de publicaciones
                                        de cada usuario
        'total_por_tipo'            -> array con el total de publicaciones
                                        de cada tipo de contenido
        'usuario_mas_publicaciones' -> índice (int) del usuario con más
                                        publicaciones en total
    """
    pass  # TODO


def contar_hashtags_array(textos):
    """
    Recibe un array (o lista) de NumPy de textos, como en el ejercicio 7.
    Devuelve un array con el número de hashtags (palabras que empiezan por
    '#') de cada texto, calculado con una función universal (ufunc) de
    NumPy en lugar de un bucle explícito sobre el array.
    """
    pass  # TODO


def normalizar_minmax(arr):
    """
    Recibe un array de NumPy de una dimensión, como en el ejercicio 8.
    Devuelve un array normalizado entre 0 y 1 con la fórmula Min-Max:
        (valor - minimo) / (maximo - minimo)
    """
    pass  # TODO


def estandarizar_zscore(arr):
    """
    Recibe un array de NumPy de una dimensión, como en el ejercicio 8.
    Devuelve su Z-score: (valor - media) / desviación_estándar.
    Si la desviación estándar es 0, debe sustituirse por 1 antes de
    dividir, para evitar una división por cero.
    """
    pass  # TODO

# ============================================================
# BLOQUE 3 — Pandas básico
# ============================================================

def cargar_usuarios(ruta_csv):
    """
    Recibe la ruta del fichero CSV de usuarios.
    Devuelve un DataFrame con su contenido.
    """
    pass  # TODO


def cargar_publicaciones(ruta_excel):
    """
    Recibe la ruta del libro de Excel de publicaciones.
    Devuelve un DataFrame con el contenido de la hoja 'publicaciones'.
    """
    pass  # TODO


def limpiar_dataset(df):
    """
    Recibe un DataFrame y devuelve una COPIA sin nulos: los nulos de las
    columnas numéricas se sustituyen por la mediana de su columna y los de
    las columnas de texto por 'Desconocido'. No debe modificar el original.
    """
    pass  # TODO


# ============================================================
# BLOQUE 4 — Pandas avanzado
# ============================================================

def calcular_engagement(df):
    """
    Recibe un DataFrame con las columnas 'likes', 'comentarios',
    'compartidos' y 'visualizaciones'. Devuelve una COPIA con la columna
    'engagement_rate' = (likes + comentarios + compartidos) / visualizaciones.
    Si 'visualizaciones' es 0, el engagement debe ser 0 (nunca nulo ni
    infinito). No modifica el DataFrame original.
    """
    pass  # TODO


def top_creadores(df_merged, n=10):
    """
    Recibe el DataFrame combinado (con 'engagement_rate') y un entero n.
    Devuelve un DataFrame con UNA fila por usuario y las columnas
    'id_usuario', 'nombre', 'tipo_cuenta' y 'engagement_promedio' (media de
    'engagement_rate' del usuario), ordenado de mayor a menor y limitado a
    n filas. Un usuario se identifica por su 'id_usuario' (hay nombres
    repetidos).
    """
    pass  # TODO


def resumen_por_ciudad(df_merged):
    """
    Recibe el DataFrame combinado (con 'engagement_rate'). Devuelve un
    DataFrame con una fila por ciudad (la ciudad es el índice) y las
    columnas 'media_seguidores' (media de 'seguidores' de las filas de esa
    ciudad), 'n_publicaciones' (número de filas) y 'engagement_promedio',
    ordenado por 'n_publicaciones' de mayor a menor.
    """
    pass  # TODO


def guardar_parquet(df, ruta):
    """
    Guarda el DataFrame 'df' en formato Parquet en 'ruta' con compresión
    'snappy' y sin incluir el índice. Debe crear las carpetas intermedias
    que falten. No devuelve nada (None).
    """
    pass  # TODO


# ============================================================
# BLOQUE 5 — Visualización y Faker
# ============================================================

def exportar_grafico(fig, ruta_html, ruta_png=None):
    """
    Exporta la figura de Plotly 'fig' a un fichero HTML interactivo en
    'ruta_html'. Si se indica 'ruta_png', exporta también una imagen PNG
    (requiere kaleido). Debe crear las carpetas intermedias que falten. No
    devuelve nada (None).
    """
    pass  # TODO


def publicaciones_por_mes(df):
    """
    Recibe un DataFrame de publicaciones con la columna 'fecha' (texto
    'AAAA-MM-DD' o tipo fecha). Devuelve un DataFrame con las columnas 'mes'
    (formato 'AAAA-MM') y 'publicaciones' (número de publicaciones de ese
    mes), ordenado cronológicamente y con índice 0, 1, 2...
    """
    pass  # TODO


def crear_dashboard(df):
    """
    Recibe un DataFrame de publicaciones con sus autores (columnas 'ciudad',
    'tipo_cuenta', 'fecha' y 'likes') y devuelve una figura de Plotly con un
    panel de 2 x 2 gráficos:
        [fila 1, col 1] barras: publicaciones de las 8 ciudades con más
                        publicaciones (de mayor a menor)
        [fila 1, col 2] sectores: publicaciones de cada 'tipo_cuenta'
        [fila 2, col 1] líneas con marcadores: publicaciones por mes
        [fila 2, col 2] histograma de 'likes'
    La figura mide 800 píxeles de alto, se titula 'Dashboard Red Social
    Ficticia', usa la plantilla 'plotly_white' y no muestra leyenda. No debe
    modificar el DataFrame original.
    """
    pass  # TODO


def generar_datos_demo(n=10, seed=2024):
    """
    Genera n usuarios ficticios con Faker en español y devuelve un DataFrame
    con las columnas 'nombre', 'apellidos' (dos apellidos), 'email',
    'ciudad', 'telefono' y 'fecha_registro' (texto 'AAAA-MM-DD' entre
    2018-01-01 y 2024-06-01). Es REPRODUCIBLE: con la misma 'seed' devuelve
    siempre los mismos datos. Con n <= 0 devuelve una tabla vacía con esas
    columnas.
    """
    pass  # TODO


def ampliar_dataset(df_usuarios, n_nuevos):
    """
    Recibe la tabla de usuarios y un entero n_nuevos. Devuelve un DataFrame
    con los usuarios originales (sin cambios y al principio) seguidos de
    n_nuevos usuarios ficticios generados con Faker en español:
      - 'id_usuario' continúa desde el máximo existente + 1 (sin repetirse)
      - mismas columnas, orden y tipos de dato que la tabla original
      - 'tipo_cuenta': 60% free, 30% premium y 10% creator
      - 'seguidores': entre 1000 y 50000 si es creator, entre 10 y 5000 si no
      - 'edad' entre 18 y 55; 'ciudad', 'pais' y 'genero' se eligen entre los
        valores que ya existen en la tabla original
    Con n_nuevos <= 0 devuelve una copia de la tabla original.
    """
    pass  # TODO
