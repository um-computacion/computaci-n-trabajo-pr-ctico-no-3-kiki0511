
class NumeroDebeSerPositivo(Exception):
    def __init__(self, mensaje="El número debe ser positivo"):
        super().__init__(mensaje)

def ingrese_numero():
    
    entrada = input("Ingrese un número: ")
    try:
        numero = int(entrada)
    except ValueError:
        raise ValueError("La entrada debe ser un número válido")
    
    if numero < 0:
        raise NumeroDebeSerPositivo("El número debe ser positivo")
    
    return numero


"""
    Solicita al usuario que ingrese un número y lo valida.

    Reglas de validación:
      - La entrada debe ser convertible a entero.
      - El número convertido debe ser positivo.
    
    Raises:
      ValueError: Si la entrada no es un número válido.
      NumeroDebeSerPositivo: Si el número es negativo.
    
    Returns:
      int: El número ingresado si es válido.
    """