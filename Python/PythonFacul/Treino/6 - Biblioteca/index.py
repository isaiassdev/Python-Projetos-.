# Faça um sistema de biblioteca que permita cadastrar livros, emprestar, devolver, pesquisar por título e listar livros disponíveis.

def menu():
    print("-- MENU --")
    print('-' * 20)
    print('1. Cadastrar livros')
    print('2. Emprestar')
    print('3. Devolver')
    print('4. Pesquisar por título')
    print('5. Listar livros disponíveis')
    print('6. Sair')
    print('-' * 20)

def cadastrar_livros(estoque):
    print('-- CADASTRAR LIVRO --')
    print('=' * 40)

    livro = input('Digite o nome do livro: ').strip().lower()

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
        # Armazena as informações
            estoque[livro] = {
            "quantidade": quantidade,
            "emprestimos": []  
            }
            print('Livro cadastrado com sucesso.')
      
def emprestar(estoque):
    print(' -- EMPRESTAR --')

    procurar = input('Digite o nome do livro: ').strip().lower()

    if procurar not in estoque:
        print('Livro não encontrado.')
        return

    if estoque[procurar]["quantidade"] <= 0:
        print('Esse livro está sem unidades disponíveis.')
        return

    if procurar in estoque: 
        resposta = input(f'Deseja emprestar o livro {procurar} (sim/não)?').strip().lower()

        if resposta == 'sim':

            nome = input('Nome: ').strip()
            telefone = input('Telefone: ').strip()
            dias = input('tempo de emptréstimo [1 á 10 dias]: ').strip()

            estoque[procurar]["quantidade"] -= 1
            print(f'Livro emprestado para {nome} por  {dias} dias(s).')

            estoque[procurar]["emprestimos"].append({
             "nome": nome,
             "telefone": telefone,
             "dias": dias
            })

        elif resposta == 'não':
            print('nenhuma alteração realizada.')

        else:
            print('Resposta inválida.')

def devolver(estoque):
    print('-- DEVOLVER --')

    livros = input("Digite o nome do livro que desejá devolver: ").strip().lower()

    if livros not in estoque: 
        print('Livro não encontrado.')
        return
    
    if not estoque[livros]["emprestimos"]:
        print('Não há empréstimos desse livro.')
        return

    for numero, emprestimos in enumerate(estoque[livros]["emprestimos"], start=1 ):
        print(f'{numero}. {emprestimos["nome"]}')

    try:
        escolha = int(input('Qual número de emprétimo deseja devolver ?  '))

        pessoa = estoque[livros]["emprestimos"].pop(escolha - 1 )
        estoque[livros]["quantidade"] += 1

        print(f'Livro devolvido por {pessoa["nome"]}.')

    except (ValueError, IndexError):
        print('Número inválido')

def pesquisar_título(estoque):
    print('-- BUSCCAR LIVRO --')

    procurar = input('Digite o titulo do livro: ').strip().lower()

    if procurar not in estoque:
        print('Não há livro adicionados.')
        return
    
    info = estoque[procurar]

    print(f'\n Nome do livros: {procurar}')
    print(f'Quantidade: {info['quantidade']}')

    if info["emprestimos"]:
        print('Empréstimos:')

        for emprestimo in info["emprestimos"]:
            print(f'- Nome: {emprestimo["nome"]}')
            print(f'  Telefone: {emprestimo["telefone"]}')
            print(f'  Dias: {emprestimo["dias"]}')
    else:
        print('Não há empréstimos para este livro.')

def listar_disponíveis(estoque):

    print('-- LIVROS DISPOINÍVEIS --')
    print('=' * 30)

    encontrou_livro = False

    for livro, info in estoque.items():
        quantidade = info["quantidade"]

        if quantidade > 0:
            encontrou_livro = True
            print(f'Livro: {livro.title()}')
            print(f'Unidades disponíveis: {quantidade}')

            if info["emprestimos"]:
                print('Emprestado para:')

                for emprestimo in info["emprestimos"]:
                    print(f'  - {emprestimo["nome"]} '
                          f'({emprestimo["dias"]} dia(s))')

            print('-' * 40)

    if not encontrou_livro:
        print('Não há livros disponíveis no momento.')
    
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