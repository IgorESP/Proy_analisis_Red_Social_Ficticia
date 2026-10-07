"""Plantilla de ejercicios avanzados del proyecto Red Social Ficticia.

Implementa cada funcion sin cambiar su nombre, firma ni tipo de retorno.
Ejecuta la correccion con ``python -m pytest tests/*_avanzado.py -v``.
"""

from typing import Any


# Bloque 1: estructuras de datos y lambda

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