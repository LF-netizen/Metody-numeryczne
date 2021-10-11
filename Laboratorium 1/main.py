from math import pi
import numpy as np


def cylinder_area(r: float, h: float) -> float:
    """Obliczenie pola powierzchni walca.
    Szczegółowy opis w zadaniu 1.

    Parameters:
    r (float): promień podstawy walca
    h (float): wysokosć walca

    Returns:
    float: pole powierzchni walca
    """
    if isinstance(r, (int, float)) and (h, (int, float)):
        if r > 0 and h > 0:
            return 2 * pi * r * (r + h)
    return float('NaN')


def fib(n: int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego.
    Szczegółowy opis w zadaniu 3.

    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia

    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """
    if n < 1 or type(n) is not int:
        return None

    if n == 1:
        return [1]

    output = np.ones(n)
    for it in range(2, n):
        output[it] = output[it - 1] + output[it - 2]
    return [output]


def matrix_calculations(a: float):
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej
    na podstawie parametru a.
    Szczegółowy opis w zadaniu 4.

    Parameters:
    a (float): wartość liczbowa

    Returns:
    touple: krotka zawierająca wyniki obliczeń
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    M = np.array([[a, 1, -a], [0, 1, 1], [-a, a, 1]])
    Mdet = np.linalg.det(M)
    Mt = np.transpose(M)
    if Mdet != 0:
        return np.linalg.inv(M), Mt, Mdet
    return float('Nan'), Mt, Mdet


def custom_matrix(m: int, n: int):
    """Funkcja zwraca macierz o wymiarze mxn zgodnie
    z opisem zadania 7.

    Parameters:
    m (int): ilość wierszy macierzy
    n (int): ilość kolumn macierzy

    Returns:
    np.ndarray: macierz zgodna z opisem z zadania 7.
    """
    if type(m) != int or type(n) != int or m < 1 or n < 1:
        return None

    output = np.zeros((m, n), dtype=int)
    for r in range(m):
        for c in range(n):
            output[r][c] = r if r > c else c

    return output
