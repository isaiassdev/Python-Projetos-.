import time

print('Como deseja chamar o seu pet ?')
nome = input('Digite o nome do seu PET: ')
print(f"Ok, seu pet se chama {nome}")
time.sleep(1)

fome = 4 #0 ta cheio 10 muita fome
sede = 5 
diversao = 5


def status_tikol():
    "Status atual do Pet"
    print(f"Fome: {fome}/10")
    print(f"Sede: {sede}/10")
    print(f"Diversão: {diversao}/10")
    if fome >= 8 and sede >= 8 and diversao <=2: 
        print(f"{nome} precisa de antenção")
    else :
        print(f"{nome} está feliz")

def alimentar_tikol(quantidade):
    global fome
    "Reduz a fome com base na quantidade de comida fornecida"
    fome = max(0, fome - quantidade) 
    return f"Vocé alimetou {nome} com {quantidade} unidade de comida"

def agua_tikol(quantidade):
    global sede 
    "Redeuz a sede com base na quantidade de agua fornecida"
    sede = max(0, sede - quantidade)
    return f"{nome} bebeu {quantidade} unidade de agua!"

def bricar_tikol(tempo):
    global diversao 
    diversao = min(10, diversao + tempo)
    return f"Voce brincou com {nome} por {tempo} minutos"

def descansar_tikol():
    while True:
            global fome,sede,diversao

            fome = min(10, fome + 4 )    
            sede = min(10, sede + 4)     
            diversao = max(0, diversao - 4) 
            print(f"{nome} agora vai descansar...")
            break

while True: 
    # Menu de opções
    print('1 - Alimentar tikol')
    print('2 - Dar água')
    print('3 - brincar')
    print('4 - ver status')
    print('5 - Deixar descansar')
    print('6 - Encerrar oo progama')

    opcoes = input('Escolha entre 1:4: ')

    if opcoes == '1':
        quantidade = int(input('Quantas unidades deseja dar? '))
        print(alimentar_tikol(quantidade))
    elif opcoes == '2':
        quantidade = int(input('Quantas unidades deseja dar? '))
        print(agua_tikol(quantidade))
    elif opcoes == '3':
        tempo = int(input("Por quanto tempo deseja brincar? "))
        print(bricar_tikol(tempo))
    elif opcoes == '4': 
        status_tikol()
    elif opcoes == '5': 
        descansar_tikol()
        print("=" * 30)
        print(f"Depois de 2horas {nome} acorda...")
    elif opcoes == '6':
        print('Jogo encerrado')
        break
    else : 
        print("Escolha uma opção válida")
        
