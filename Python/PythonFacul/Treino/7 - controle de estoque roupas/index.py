def menu(): 

    print('1 - Cadastro de roupa ')
    print('2 - lista de produtos')
    print('3 - Remover do estoque')
    print('4 - Fechar programa')

def cadastro_roupas(estoque):
    print('----CADASTRO-----')

    while True: 


        print("1 - Camisa" )
        print("2 - Calça" )
        print("3 - Bermuda" )
        print("4 - Vestido" )
        
        escolha = input('Qual produto deseja cadastrar? (1 á 4): ') 

        if escolha == '1':
            categoria = 'Camisa'
        elif escolha == '2': 
            categoria = 'Calça'
        elif escolha == '3': 
            categoria = 'Bermuda'
        elif escolha == '4': 
            categoria = 'Vestido'
        else: 
            print('Opção inválida')
            continue

        break

    try: 
         quantidade = int(input(f'Digete a quantidade do produto da {categoria}:  '))

         if quantidade < 0 : 
            print('a quantidae não pode ser negativa.')
            return

    except ValueError: 
        print('Digite um número válido')
        return

        
    resposta = input('Deseja adicionar mais quantidades do produto? Sim/Não: ').strip().lower()
    if resposta == 'sim':

            try: 
                quantidade = int(input('Digete a quantidade do produto: '))
            
                if quantidade < 0 : 
                    print('a quantidae não pode ser negativa.')
                    return
            
            except ValueError: 
                print('Digite um número válido')
                return
            estoque[categoria]["quantidade"] += quantidade
            print('Quantidade atualizada com sucesso.')
    else:
            print('Nenhua alteração realizada.')
    
    #armazena informações
            estoque[categoria] = {
                "quantidade": quantidade,
            }
            print('Categoria cadastrada com sucesso.')
       
def lista(estoque):
    print(' -- ESTOQUE -- ')

    for categoria, info in estoque.items():
        print(f'{categoria}: {info["quantidade"]} unidades')

    pass 

def remover_estoque(estoque):
    pass

def main():
    estoque = {}
    while True: 
        menu()

        opcao = input('Escaolha umas das opções de 1 á 4: ')

        if opcao == '1':
            cadastro_roupas(estoque)
        elif opcao == '2':
            lista(estoque)
        elif opcao == '3': 
            remover_estoque(estoque)
        elif opcao == '4':
            print('Fechando programa...')
            break
        else :
            print('Opção inválida')
main()






















    
