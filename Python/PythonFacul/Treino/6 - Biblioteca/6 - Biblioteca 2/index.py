def menu():

    print('1. Cadastrar Livro')
    print('2. Emprestar')
    print('3. Devolver')
    print('4. Sair')

def cadastar_livro(estoque):

    livro = input('Digite o nome do livro: ').strip().lower()

    try: 
        quantidade = int(input('digite a quantidade de livros: '))
       
    except ValueError: #int("abc")   # ValueError
                print('Digite um numero válido.')
                return
    if livro in estoque: 
        print('Livro já cadastrado')

        resposta = input('Deseja adicionar mais quantidade do livro. (sim/não)').strip().lower()

        if resposta == 'sim': 

            try: 
                quantidade = int(input('Digite a quantidade de livros: '))

                if quantidade < 0 :
                    print('A quantidad e não pode ser negativa.')
                    return
            except ValueError: 
                print('Digete um número válido.')
                return

            estoque[livro]["quantidade"] += quantidade
            print('quantidade atualizada com sucesso.')
            
        else: 
            print('Nenhuma alteração realizada.')
    else: 
        estoque[livro] = {
            "quantidade" : quantidade,
            "emprestimos": []
        }
        print('Livro cadastrado com sucesso.')

def emprestar_livro(estoque):

    procurar = input('Digite o livro que deseja emprestar.').strip().lower()

    if procurar not in estoque: 
        print('O livro não exite.')
        return
    
    if estoque[procurar]["quantidade"] <= 0:
        print('No momento não unidade do livro.')
        return

    if procurar in estoque:
        resposta = input(f'Deseja emprestar o livro {procurar}. (sim/não)').strip().lower()

        if resposta == 'sim':
            nome = input('Digite o nome do recebedor: ').strip().lower()
            telefone = input('Digiete o número de telefone.').strip().lower()

            while True: 
                try:
                    dias = int(input('tempo de emprestimo [1 á 10 dias]: '))

                    if 1 <=  dias <= 10:
                        break

                    print('digite entre 1 a 10 dias ')

                except ValueError:
                    print('Digite um número valido.')

            estoque[procurar]["quantidade"] -= 1
            print(f'O livros está sendo emprestava para {nome} por {dias} dia(s).')

            estoque[procurar]["emprestimos"].append({
                "nome": nome,
                "telefone": telefone,
                "dias": dias
            })
                
                 
def devolver_livro(estoque):

    devolver = input('Digite o nome do livro que deseja devolver: ').strip().lower()

    if devolver not in estoque:
        print('Livro não encotrado.')
        return

    if not estoque[devolver]["emprestimos"]:
        print('Não há emprestimos desse livro. ')
        return

    for numero, emprestimos in enumerate(estoque[devolver]["emprestimos"], start=1 ):
        print(f'{numero}. {emprestimos["nome"]}')

    try: 
        escolha = int(input('Qual o número de emprestimo que desejá devolver? '))

        pessoa = estoque[devolver]["emprestimos"].pop(escolha -1)
        estoque[devolver]["quantidade"] += 1

        print(f'Livro devolvido por {pessoa["nome"]}.')

    except (ValueError, IndexError):
        print('Número inválido')
            
def main(): 
    estoque = {}
    while True:
        menu()

        opcao = input('Esolha as opcoes de 1 á 3: ')

        if  opcao == '1':
            cadastar_livro(estoque)
        elif opcao == '2':
            emprestar_livro(estoque)
        elif opcao == '3':
            devolver_livro(estoque)
        elif opcao == '4':
            print('Fechando programa.')
            break
        else:
            print('Opção inváldia.')
main()