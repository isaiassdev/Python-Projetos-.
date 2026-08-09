import time

fome = 4
sede = 3
diversao = 6
interacoes = 0

print('Tikol está acordando')
time.sleep(2)

while True:
    fome +=1 if fome < 10 else 0
    sede +=1 if sede < 10 else 0 
    diversao -=1 if diversao > 0 else 0
    interacoes +=1

    #status tikol
    print(f"\n status tikol")
    print(f"Fome {fome}/10")
    print(f"Sede {sede}/10")
    print(f"Diversao {diversao}/10")

    #Alerta 
    if fome > 8:
        print('Tiko está com fome')
    elif sede > 8:
        print('Tikol está com sede')
    elif diversao < 2: 
        print('Tikol está entediado')
    
    #Interação especial a cada 5 alterações
    if interacoes % 5 == 0: 
        print('Tikol está se aproxiamndo de vocé')

    # Lop para roforça a necessidade de atenção do pet
    for i in range(3):
        print('tikol olha com expectativa')
        time.sleep(1)

    def fome_tikol(): 
        global fome 
        if fome >= 5:
            print('Vocé da comida ao tikol e ele fica de barriga cheia') 
            fome = min(fome -2,10 )

    def agua_tikol():
        global sede 
        if sede >= 5: 
            print('Voce deu agua ao tikol!! Agora ele quer correr mais')
            sede = min(sede -2,10)

    def brincar_tikol():
        global diversao
        if diversao <= 4 :
            print('Voce brinca com tikol!! Ele está se divertindo muito')
            diversao = min(diversao +2,10)

    def deixar_tikol():
        global fome, sede, diversao
        fome = min(fome +2,10 )
        sede = min(sede +2,10)
        diversao = min(diversao -2,0)


        print('como vocé deixou tikol sozinho ele acabou passando necessidade')

    # menu 
    print('1- Alimentar tikol')
    print('2- Dar agua ao tikol')
    print('3- Brincar com tikol')
    print('4- Deixar tikol sozinho ')
    print('5- Encerrar')

    opcao = input('Escolha entre 1:4: ')

    # validar
    if opcao == '1': 
        fome_tikol()
    elif opcao == '2': 
        agua_tikol()
    elif opcao == '3': 
        brincar_tikol()
    elif opcao == '4': 
        deixar_tikol()
    elif opcao == '5': 
        print('Tikol está indo dormir')
        break
    else : 
        print('Opção inválida')
