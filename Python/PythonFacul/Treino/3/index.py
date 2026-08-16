#Verificador de número 
# Usuário digita um número. 
# Informar se é positivo, negativo ou zero. 
# Dizer também se é par ou ímpar.

numero = int(input('Digite um número: '))

if numero > 0 : 
    print('O número é positivo.')
elif numero < 0 : 
    print('O número é negativo')
else : 
    print('O número é zero')

resultado = ('par', 'ímpar')[numero % 2]  
print(resultado)

# numero % 2 resulta em 0 para números pares.
# Resulta em 1 para números ímpares.
# A tupla usa esse resultado como posição: posição 0 é "par" e posição 1 é "ímpar".

# outra forma utilizando dicionario
# resultado = {0: "par", 1: "ímpar"}[numero % 2]
# print(resultado)