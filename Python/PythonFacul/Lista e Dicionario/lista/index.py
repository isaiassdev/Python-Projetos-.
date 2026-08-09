listaDeNumeros = []

numeros = (input("Digite 6 numeros : "))

if len(numeros) == 6 :
    
    for i in numeros:
        listaDeNumeros.append(int(i))
        soma = sum(listaDeNumeros)

    print(f"soma dos nuemros e {soma}")
    
else:
    print("nao tem 6 digitos")

