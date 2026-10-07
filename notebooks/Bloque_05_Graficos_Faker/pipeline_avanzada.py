"""Plantilla de ejercicios avanzados del proyecto Red Social Ficticia.

Implementa cada funcion sin cambiar su nombre, firma ni tipo de retorno.
Ejecuta la correccion con ``python -m pytest tests/*_avanzado.py -v``.
"""

import os
from typing import Any
import numpy as np
import pandas as pd

# ============================================================
# BLOQUE 1 — Estructuras de datos, Regex y Lambda
# ============================================================

def informe_actividad_ciudades(lista_usuarios: list[dict[str, Any]]) -> dict[str, dict[str, float]]:
    """Resume usuarios, activos y seguidores por ciudad."""
    pass


def recomendaciones_por_conexiones(lista_usuarios: list[dict[str, Any]], conexiones: list[dict[str, Any]], id_usuario: int, limite: int = 5) -> list[dict[str, Any]]:
    """Devuelve personas seguidas por contactos pero no por el usuario."""
    pass


def hashtags_normalizados(lista_publicaciones: list[dict[str, Any]]) -> set[str]:
    """Normaliza hashtags, elimina espacios y devuelve los valores unicos."""
    pass


def validar_publicaciones(lista_publicaciones: list[dict[str, Any]], lista_usuarios: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Separa publicaciones validas y publicaciones con usuario inexistente."""
    pass

# ============================================================
# BLOQUE 2 — NumPy
# ============================================================

def puntuacion_usuarios(seguidores: np.ndarray, seguidos: np.ndarray, publicaciones: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Calcula y normaliza una puntuacion vectorizada de usuarios."""
    pass


def resumen_matriz(matriz: np.ndarray) -> dict[str, np.ndarray]:
    """Calcula totales por filas y columnas y sus posiciones maximas."""
    pass


def conexiones_indirectas(matriz_conexiones: np.ndarray) -> np.ndarray:
    """Calcula conexiones de longitud dos mediante producto matricial."""
    pass


def simular_engagement(n: int = 30, seed: int = 42) -> np.ndarray:
    """Genera un vector reproducible de engagement sintetico."""
    pass

# ============================================================
# BLOQUE 3 — Pandas básico
# ============================================================

def auditar_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe un DataFrame y devuelve una NUEVA tabla con una fila por cada
    columna de 'df' y las columnas:
        'columna'          -> nombre de la columna auditada
        'tipo_dato'        -> tipo de dato de la columna, como texto
        'n_nulos'          -> número de valores nulos
        'porcentaje_nulos' -> porcentaje de nulos sobre el total de filas,
                              redondeado a 2 decimales
        'n_distintos'      -> número de valores distintos (sin contar nulos)
    """
    pass


def limpiar_usuarios_avanzado(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe la tabla de usuarios y devuelve una COPIA limpia, sin modificar
    el original:
      - texto: elimina espacios sobrantes de los extremos y pone en formato
        título 'nombre', 'apellidos' y 'ciudad' (' ana ' -> 'Ana'); el resto
        de nulos de texto pasan a 'Desconocido'
      - numéricas: los nulos se sustituyen por la mediana de la columna
      - 'fecha_registro' (si existe) se convierte a tipo fecha
    La operación debe ser idempotente: limpiar dos veces da el mismo
    resultado que limpiar una.
    """
    pass


def comparar_imputaciones(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Recibe un DataFrame y el nombre de una columna numérica. Devuelve una
    NUEVA tabla con una fila por estrategia, en este orden ('eliminar filas',
    'rellenar con media', 'rellenar con mediana'), y las columnas:
        'estrategia', 'n_filas', 'media_resultante', 'mediana_resultante'
    donde 'n_filas' son las filas que conserva la tabla con esa estrategia y
    las dos últimas son la media y la mediana de la columna tras aplicarla.
    No debe modificar el DataFrame original.
    """
    pass


def validar_calidad_usuarios(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe la tabla de usuarios y devuelve un DataFrame booleano con las
    mismas filas (y el mismo índice) que 'df' y una columna por regla. Un
    valor True significa que esa fila INCUMPLE la regla:
        'edad_nula'                   -> la edad es nula
        'edad_fuera_de_rango'         -> la edad es menor de 18 o mayor de 55
        'mas_seguidos_que_seguidores' -> 'seguidos' > 'seguidores'
        'fila_duplicada'              -> repite por completo una fila anterior
        'id_repetido'                 -> su 'id_usuario' ya apareció antes
    """
    pass


# ============================================================
# BLOQUE 4 — Pandas avanzado
# ============================================================

def analizar_categorias(df: pd.DataFrame, columnas: list[str]) -> pd.DataFrame:
    """
    Recibe un DataFrame y una lista de nombres de columnas de texto.
    Devuelve una NUEVA tabla con una fila por columna (el índice es el
    nombre de la columna) y las columnas:
        'tipo'                  -> tipo de dato tras convertirla a categórica
        'categorias'            -> número de categorías
        'memoria_antes_bytes'   -> memoria de la columna original (contando
                                   el contenido de los textos)
        'memoria_despues_bytes' -> memoria de la columna ya categórica
        'ahorro_bytes'          -> memoria antes menos memoria después
    No debe modificar el DataFrame original.
    """
    pass


def tabla_engagement_ciudad_contenido(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recibe un DataFrame con las columnas 'tipo_contenido', 'ciudad' y
    'engagement_rate'. Devuelve una tabla dinámica con 'tipo_contenido' en
    las filas, 'ciudad' en las columnas y el engagement medio como valor;
    las combinaciones sin publicaciones valen 0.
    """
    pass


def comparar_formatos(df: pd.DataFrame, ruta_base) -> dict[str, float]:
    """
    Guarda 'df' en '<ruta_base>.csv' (sin índice) y en '<ruta_base>.parquet'
    (compresión snappy, sin índice) y devuelve un diccionario con:
        'csv_bytes'     -> tamaño en bytes del CSV
        'parquet_bytes' -> tamaño en bytes del Parquet
        'ratio'         -> parquet_bytes / csv_bytes, con 3 decimales
    Si no hay motor de Parquet instalado, se propaga el ImportError.
    """
    pass


# ============================================================
# BLOQUE 5 — Visualización y Faker
# ============================================================

def exportar_figuras_avanzadas(figuras: dict[str, Any], carpeta) -> list[str]:
    """
    Recibe un diccionario {nombre: figura de Plotly} y una carpeta. Guarda
    cada figura en '<carpeta>/<nombre>.html' (creando la carpeta si no
    existe) y devuelve la lista con las rutas de los ficheros creados, en el
    mismo orden que el diccionario.
    """
    pass


def ampliar_dataset_avanzado(df_usuarios: pd.DataFrame, n: int, seed: int = 42) -> pd.DataFrame:
    """
    Igual que la ampliación básica, pero REPRODUCIBLE: con la misma 'seed'
    debe devolver siempre exactamente los mismos usuarios. Devuelve los
    usuarios originales (sin cambios, al principio) seguidos de 'n' usuarios
    ficticios con Faker en español que cumplen:
      - 'id_usuario' único, continuando desde el máximo existente + 1
      - mismas columnas, orden y tipos de dato que la tabla original
      - 'tipo_cuenta': 60% free, 30% premium y 10% creator
      - 'seguidores' coherentes con el tipo de cuenta (creator: 1000-50000;
        resto: 10-5000), 'edad' entre 18 y 55
      - 'fecha_registro' entre 2018-01-01 y 2024-06-01 (formato AAAA-MM-DD)
      - 'ciudad', 'pais' y 'genero' elegidos entre los valores existentes
    Con n <= 0 devuelve una copia de la tabla original.
    """
    pass
