import time

#Apresnetação do tikol
print('Bem-Vindo ao mundo digital! Um pequeno ovo começa a se quebrar')
time.sleep(2)
print('O ovo se quebra e de dentro aparece tikol')
time.sleep(2)

#Status do tikol

fome = 4 # 0 (muita fome) a (10) Muito cheio
sede = 3 # (0) Muita sede à 10 ( Vai explodir)
diversao = 6 # (0) Muito  triste 10 (To feliz)

#Exibição dos status
print('tikol está olhando para vocé!... Como ele está  se sentindo?\n')
time.sleep(2)
print(f"Fome: {fome}/10"  )
print(f"sede: {sede}/10")
print(f"Diversão: {diversao}/10")

# Menu das Ações 
print('O que voce quer fazer com tikol')

def fome_tikol():  
    global fome 
    
    if fome < 10:
        print('Escolha a comida do tikol')
    
        while True:
            print('1-Semente dos Deuses')
            print('2-Maça criada do cosmos')

            opcao = input("Escolha a opcao 1:2: ")
            
            if opcao in ["1","2"]:
                fome = min(fome +2,10)
                print(f"Vocé escolheu a opcao a {opcao}! Vocé saciou a fome de tikol {fome} ")
                break
            else:
                print('Opção inválida')
    else:
        print('Tikol está cheio')   

def agua_tikol():
    global sede
    if sede < 10:
    
        while True:
                print('1- Bebida preferida do tikol')
                print('2- Agua da garrafinha preferida')
                opcao = input("Escolha a opcao 1:2: ")

                if opcao in ["1","2"]:
                    sede = min(sede +2,10)
                    print(f"Voce escolheu a opcao {opcao}!! Voce saciou a sede de tikol em {sede}")
                    time.sleep(1)
                    print('Tikol agora vai correr mais')
                    break
                else:
                    print('Opção inválida')
    else:
        print('Tikol está igual um balão')

def brincar_tikol():
    global diversao
    if diversao < 10:
        
        while True:
            print('1- Correr com tikol pelo mundo')
            print('2- Tacar bolinha para tikol')

            opcao = input("Escolha entre à 1:2: ")
            
            if opcao in ["1","2"]:
                diversao =min(diversao +2,10)
                print(f"Voce escolheu a opcao {opcao}!! Tikol gosta muito de brincar e abana a cauda...")
                break
            else:
                print('Opção inválida')

    else:       
        print("Tikol está cansado")

def status_tikol():

    print(f"fome: {fome}/10")
    print(f"sede: {sede}/10")
    print(f"Divesão: {diversao}/10")

while True: 
    print('1-Alimentar tikol')
    print('2-Dar água a tikol')
    print('3-Brincar com tikol')
    print('4-Ver status')
    escolha = input("Escolha uma ação entre 1:4: ")

    if escolha == "1":
        fome_tikol()
    elif escolha == "2":
        agua_tikol()
    elif escolha == "3":
        brincar_tikol()
    elif escolha == "4":
        status_tikol()
    else :
        print('Opcao inválida')