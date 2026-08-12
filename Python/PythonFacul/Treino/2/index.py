#Calculadora

#Soma, subtração, multiplicação e divisão.
#Usar funções.
#Depois coloque um menu para escolher a operação.

def somar_calcular():
    print('-- SOMAR --')
    print('=' * 40)

    try:
        somar1 = int(input('Digite: '))
        somar2 = int(input('Digite: '))
         
    except ValueError :
            print('Digite uma quantidade numérica válida.')
            return

    print(f"Resultado: {somar1 + somar2}")

def subtrair_calcular():
    print('-- SUBTRAIR --')
    print('=' * 40)

    try:
         subtrair1 = int(input('Digite: '))
         subtrair2 = int(input('Digite: '))
         print(f"Resultado: {subtrair1 - subtrair2}")
         
    except ValueError :
            print('Digite uma quantidade numérica válida.')
            return
    
def multiplicar_calcular():
    print(' -- MULTIPLICAR -- ')
    print('=' * 40)

    try:
         multiplicar1 = int(input('Digite: '))
         multiplicar2 = int(input('Digite: '))
         print(f"Resultado: {multiplicar1 * multiplicar2}")
    except ValueError: 
         print('Digite uma quantidade numérica válida.')
         return

def dividir_calcular():
    print(' -- DIVIDIR -- ')
    print('=' * 40)

    try:
         dividir1 = int(input('Digite: '))
         dividir2 = int(input('Digite: '))
         print(f"Resultado: {dividir1 / dividir2}")
    
    except ValueError :
            print('Digite uma quantidade númerica válida.')
            return
    
    except ZeroDivisionError: 
        print( 'Não é possível dividir por zero.')
        return
    
def main(): 
    while True:
        print(' -- CALCULADORA -- ')
        print('=' * 40)

        print(' + Somar')
        print(' - Subtrair')
        print(' * Multiplicar')
        print(' / Dividir')
        print(' 0 - Sair')

        escolha = input('Escolha a operação: ')  
        

        if escolha == '+':
            somar_calcular()
        elif escolha == '-': 
            subtrair_calcular()
        elif escolha == '*':
            multiplicar_calcular()
        elif escolha == '/': 
            dividir_calcular()
        elif escolha == "0": 
             print("Fechando programa")
             break

main()

