#Conversor de temperatura

#Celsius → Fahrenheit
# Fahrenheit → Celsius
# Criar um menu.

def conversor_Celsius():

    celsius = float(input("Temperatura em °C: "))

    fahrenheit = (celsius * 9 / 5) + 32

    print(f"{celsius}°C = {fahrenheit:.2f}°F")

def conversor_Fahrenheit():

    fahrenheit = float(input("Temperatura em °F: "))

    celsius = (fahrenheit - 32) * 5 / 9

    print(f"{fahrenheit}°F = {celsius:.2f}°C")


def main():

    while True: 
        print("\n--- Conversor de temperatura ---")
        print('1 - Celsius → Fahrenheit')
        print('2 - Fahrenheit → Celsius')
        print('3 - Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            conversor_Celsius()
        elif escolha == '2': 
            conversor_Fahrenheit()
        elif escolha == '3':
            print('Programa encerrado')
            break
        else: 
            print('Opção inválida.')
        

main()
        
