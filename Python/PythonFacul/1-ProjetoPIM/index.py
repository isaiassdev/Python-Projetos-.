    # Lista dos alunos
listaAlunos = []

# Cadastro dos alunos
def cadastrar_alunos():
    nome = input("Nome do aluno: ") 
    dataPagamento = input("Data de pagamento: ")
    plano = input("Plano: ")

    addAlunos = {
        "nome" : nome,
        "dataPagamento" : dataPagamento,
        "plano" : plano
    }
    listaAlunos.append(addAlunos) 

    print("Aluno cadastrado!")
        
# Lista de alunos
def lista_alunos():
    print("LISTA DE ALUNOS")

    for addAlunos in listaAlunos:
        print("=" * 30)
        print(f"Nome: {addAlunos['nome']}")
        print(f"Data de Pagamento: {addAlunos['dataPagamento']}")
        print(f"Plano: {addAlunos['plano']}")
        
#Alterar dados 
def alterar_dados():
    nomeBusca = input("Digite o nome do aluno: ")
    encontrado = False
    
    for addAlunos in listaAlunos:
        if addAlunos["nome"] == nomeBusca:
            encontrado = True

            escolha = input(
            "O que deseja alterar? \n" 
            "1- Nome \n" 
            "2- Data de pagamento \n" 
            "3- Plano \n " 
            "Escolha: ").strip()
            
            if escolha == "1":
                addAlunos["nome"] = input("Novo nome: ")
                print("Aluno atualizado!")

            elif escolha == "2":
                addAlunos["dataPagamento"] = input("Nova data: ")
                print("Aluno atualizado!")

            elif escolha == "3":
                addAlunos["plano"] = input("Novo plano: ")
                print("Aluno Atualizado!")
            else:
                    print("Opção inválida!")

    if encontrado == False:
      print("Aluno não encontrado!")


# Remover aluno
def remover_aluno():
    nome = input("Nome do aluno: ")
    encontrado = False

    for addAlunos in listaAlunos:
        if addAlunos["nome"] == nome:
            listaAlunos.remove(addAlunos)
            encontrado = True  
            print("Aluno removido!") 

    if encontrado == False:
        print("Aluno não encontrado")


# Opcões de Escolha 
while True:
    print("=" * 30)
    print("1- Cadastrar a aluno ")
    print("2- Lista dos alunos ")
    print("3- Alterar dados")
    print("4- Remover alunos")
    print("5- Encerrar")

    opcao = input("Escolha: ")

    if opcao == "1":
        cadastrar_alunos()
    elif opcao == "2":
        lista_alunos() 
    elif opcao == "3":
        alterar_dados()
    elif opcao == "4":
        remover_aluno()
    # Fim
    elif opcao == "5":
        print("ENCERRADO")
        break

    else: 
        print("Opcao invalida")
    
