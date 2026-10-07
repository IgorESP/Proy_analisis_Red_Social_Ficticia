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


# ============================================================
# BLOQUE 1 — Estructuras de datos, Regex y Lambda
# ============================================================

def usuarios_activos(lista_usuarios):
    """
    Recibe una lista de diccionarios con datos de usuarios (cargados desde CSV).
    Devuelve una lista con solo los usuarios cuyo campo 'activo' sea 'True' (string).
    """
    pass  # TODO


def agrupar_por_ciudad(lista_usuarios):
    """
    Recibe una lista de diccionarios con datos de usuarios.
    Devuelve un diccionario {ciudad: [nombres_de_usuarios]}.
    Los usuarios sin ciudad (None o '') deben ignorarse.
    """
    pass  # TODO


def hashtags_unicos(lista_publicaciones):
    """
    Recibe una lista de diccionarios con datos de publicaciones (cargados desde CSV).
    Cada publicación tiene 'hashtags': cadena separada por comas ('#ia,#python,...').
    Devuelve un set con todos los hashtags únicos del dataset.
    """
    pass  # TODO


def top_por_seguidores(lista_usuarios, n=10):
    """
    Recibe una lista de diccionarios con datos de usuarios y un entero n.
    Devuelve una lista con los n usuarios con más seguidores (int), de mayor a menor.
    Debe usar sorted() con una función lambda como key.
    """
    pass  # TODO


def extraer_hashtags_regex(texto):
    """
    Recibe un texto y extrae sus hashtags mediante expresiones regulares.
    Devuelve una lista de hashtags en minúsculas y en el orden encontrado.
    Un hashtag está formado por '#' seguido de letras, números o '_'.
    """
    pass  # TODO


def publicaciones_con_hashtag(lista_publicaciones, hashtag):
    """
    Recibe publicaciones y un hashtag a buscar, por ejemplo '#ia'.
    Devuelve las publicaciones que lo contienen en el campo 'hashtags'.
    La búsqueda no distingue mayúsculas y no debe aceptar coincidencias parciales.
    Por ejemplo, '#ia' no coincide con '#iabd'.
    """
    pass  # TODO
