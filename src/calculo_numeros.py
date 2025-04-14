from src.exceptions import ingrese_numero, NumeroDebeSerPositivo

def main():
   
    while True:
        
            numero = ingrese_numero()
            print(f"Número válido: {numero}")
       
            
       
if __name__ == '__main__':
    main()
