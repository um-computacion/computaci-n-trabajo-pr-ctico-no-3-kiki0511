from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
   
    while True:
        try:
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
        except NumeroDebeSerPositivo as error_negativo:
            print(f"Error: {error_negativo}")
        except ValueError as error_valor:
            print(f"Error: {error_valor}")
       
if __name__ == '__main__':
    main()
