import time

#Nomeando o pet

print('Vocé encontoru um novo pet virtual!! Como deseja chama-lo')
nome = input('Digite o nome do pet: ')
print(f"O nome do seu pet é {nome}. Cuide bem dele")
print("=" * 30)

# Estado inicial do pet
fome = 4    # 0 muita fome 10 ta cheio
sede = 6 
diversao = 3
saudavel = True # Saude inicial do pet

#Status 
print(f"Status {nome}/10")
print(f"Fome: {fome}/10")
print(f"Sede: {sede}/10")
print(f"Diversão: {diversao}/10")
print(f"Saudavel: {'sim' if saudavel else 'não'}")
print("=" * 30)

#funcoes do menu

def fome_pet():
    global fome

    if fome == 10 :
        print('Não cabe mais nada')
    else: 
        print(f"Alimentando {nome}. Está empanturrado") 
        fome = min(fome +2,10)
        

def agua_pet():
    global sede 

    if sede == 10 :
        print('ta cheio dagua')
    else: 
        print(f"dando água {nome}. viro um balão") 
        sede = min(sede +2,10)

def diversao_pet():
    global diversao

    if diversao == 10 :
        print(f"{nome} está muito cansado")

    else: 
        print(f"Voce esta brincando com {nome}. ele está muito feliz") 
        diversao = min(diversao +2,10)
        

def descansar_pet():
    global diversao
    print(f"{nome} está descansando..." )
    diversao = max(diversao -2,0) # inperdir que fique negativo usa MAX

modo_teste = True

if modo_teste:
    nome = "Tikol"
else:
    nome = input("Digite o nome do pet: ")

testes = ["1", "1", "3", "4", "2", "5"]

for opcao in testes:
    print(f"Executando opção {opcao}")

    if opcao == '1':
        fome_pet()
    elif opcao == '2':
        agua_pet()
    elif opcao == '3':
        diversao_pet()
    elif opcao == '4':
        descansar_pet()
    elif opcao == '5':
        print("Encerrar o jogo")
        break

    print(f"Fome: {fome}")
    print(f"Sede: {sede}")
    print(f"Diversão: {diversao}")
    print("-" * 20)


while True:
    #determina se está saudavel ou nao
    saudavel = fome > 3 and sede > 3 and diversao > 3

#validar saudavel
    if saudavel:
        print(f"{nome} está feliz e quer brincar")
    else: 
        print(f"{nome} está triste e cansado")

#Menu de Ações

    print('MENU')
    print("=" * 30)
    print('1 -Alimentar o Pet')
    print('2 -Dar água')
    print('3 -Bricar')
    print(f"4 - Deixar o {nome} descansar")
    print('5 -Encerrar o jogo')

    opcao = input('Escolha entre 1:5: ')
    
    if opcao == '1':
        fome_pet()
    elif opcao == '2':
        agua_pet()
    elif opcao == '3':
        diversao_pet()
    elif opcao == '4':
        descansar_pet()
    elif opcao == '5':
        print("Encerrar o jogo")
        break

#min(..., 10) → cria um teto (não passa de 10).
#max(..., 0) → cria um chão (não fica abaixo de 0).

