# Faça um sistema de biblioteca que permita cadastrar livros, emprestar, devolver, pesquisar por título e listar livros disponíveis.

def menu():
    print("--MENU--")
    print('-' * 20)
    print('1. Cadastrar livros')
    print('2. Emprestar')
    print('3. Devolver')
    print('4. Pesquisar por título')
    print('5. Listar livros disponíveis')
    print('6. Sair')
    print('-' * 20)

def cadastrar_livros(estoque):
    print('--CADASTRAR LIVRO--')
    print('=' * 40)

    livro = input('Digite o nome do livro: ')

    try:
        quantidade = int(input('Digite a quantidade de livros: '))

        if quantidade < 0 :
            print('A quantidade não pode ser negativa.')
            return
    except ValueError:
            print('digite uma quantidade válida.')
            return

    if livro in estoque:
        print('Livro já cadastrado.')
        
        resposta = input('Deseja adicionar mais quantidades do livro? (sim/não)').strip().lower()
        if resposta == 'sim' :
            try: 
            
                quantidade = int(input('Quantos livros deseja adicionar: '))
            
                if quantidade < 0: 
                    print('A quantidade não pode ser negativa')
                    return  
            except ValueError :
                print('Digite uma quantidade numérica válida.')
                return
        
            estoque[livro]["quantidade"] += quantidade
            print(f'quantidade atualizada com sucesso.')
        else:
            print('Nenhuma alteração foi feita.')
    else:
        estoque[livro] = {
                    "quantidade": quantidade
                }
        print('Livro cadastrado com sucesso')
      
def emprestar(estoque):
    pass
def devolver(estoque):
    pass
def pesquisar_título(estoque):
    print('-- BUSCCAR LIVRO --')

    procurar = input('Digite o titulo do livro: ').strip().lower()

    if procurar not in estoque:
        print('Não há livro adicionados.')

    for procurar in estoque:

        info = estoque[procurar]
        print(f'\n Nome do livros: {procurar}')
        print(f'Quantidade: {info['quantidade']}')

    else:
        print('Livro não encotrado.')

def listar_disponíveis(estoque):

    print('-- LIVROS DISPOINÍVEIS --')
    print('=' * 30)

    for livros, info in estoque.items():
        print(f"\nNome dos livros: {livros}")
        print(f"Quantidade: {info ["quantidade"]}")
        print('=' * 40)
    
def main():
    estoque = {}
    while True:
        menu()

        opcao = input('Escolha de 1 á 6: ')


        if opcao == '1':
            cadastrar_livros(estoque)
        elif opcao == '2':
            emprestar(estoque)
        elif opcao == '3':
            devolver(estoque)
        elif opcao == '4':
            pesquisar_título(estoque)
        elif opcao == '5':
            listar_disponíveis(estoque)
        elif opcao == '6':
            print('fechando programa...')
            break
        else:
            print('Opção inválida')
main()