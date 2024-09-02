#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrementar n para evitar bucle infinito
    return result

# Asegúrate de que se pase un argumento y que sea un número entero
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    f = factorial(int(sys.argv[1]))
    print(f)
else:
    print("Por favor, proporciona un número entero como argumento.")
