# Operação Cipher: Perfis dos Suspeitos
# Nesta etapa da investigação, são registrados os perfis dos colaboradores e acessos extenos suspeitos.
# Cada suspeito possui informaoes como nome, cago, ultimo acesso e alertas, que serão armazenados em dicionario.

def menu_suspeitos(suspeitos):
    # Exibir lista de opções

    print('1. Adicionar Suspeitos')
    print('2. Atualizar informações de um usuário')
    print('3. Exibir todos os suspeitos')
    print('4. Buscar um suspeito')
    print('5. Remover um suspeito')
    print('6. Sair')

def adicionar_suspeitos(suspeitos):
    # adicionar um novo suspeito a lista
    print('\n--- Adicionar Suspeitos ---')
    nome = input('Digete o nome do suspeito: ').strip()

    if nome in suspeitos:
     print('Suspeito já cadastrado! Utilize a operação para modificar os dados')
     return
    
    cargo = input("Adicione o cargo ou posição: ").strip()
    ultimo_acesso = input("Digite a ultima data de acesso (ex: dd/mm/aaa): ").strip()
    alertas = input("Digite alertas ou observações iniciais: ").strip()

     # Armazenando informacoes
    suspeitos[nome] = { # pyright: ignore[reportUndefinedVariable]
     "cargo": cargo,
     "ultimo_acesso": ultimo_acesso,
     "alertas": alertas
    }  
    print(f"Suspeito'{nome}' adicionado com sucesso") # type: ignore

def atualizar_suspeitos(suspeitos):
    # atualizar suspeito
     print('\n--- Atualizar suspeito ---')
     nome = input('Digete o nome do suspeito a ser atualizado: ').strip()

     if nome not in suspeitos:
        print('Suspeito já cadastrado! Utilize a operação para modificar os dados')
        return
     print(f"\n informações atuais de '{nome}': ")
     print(f"1. Cargo: {suspeitos [nome]['cargo']}")
     print(f"2. Ultimo acesso: {suspeitos[nome]['ultimo_acesso']}")
     print(f"3. Alertas: {suspeitos[nome]['alertas']}")
     opcao = input("Escolha a a opção para atualizar: ")

     if opcao == '1':
         novo_cargo = input('Digite o novo cargo: ')
         suspeitos[nome]['cargo'] = novo_cargo
         print('Cargo atualizado com sucesso.')
     elif opcao == '2': 
         novo_acesso = input('Digite o ultimo acesso: ')
         suspeitos[nome]['ultimo_acesso'] = novo_acesso
         print('Ultimo acesso atualizado.')
     elif opcao == '3':
         novo_alerta = input('Digite os novos alertas: ')
         suspeitos[nome]['alertas'] = novo_alerta
         print('Alertas atualizado.')
     else: 
         print('Opção inválida.')



def exibir_suspeitos(suspeitos):
    # Exibir todos os perfis suspetios 
    print("\n--- Lista de Suspeitos ---")

    if not suspeitos:
        print("Nenhum suspeito cadatrado.")
        return

    for nome, info in suspeitos.items():  # type: ignore
        print(f"\nNome: {nome}")
        print(f" Cargo: {info['cargo']}")
        print(f"Ultimo acesso: {info ['ultimo_acesso']}")
        print('=' * 40)

def buscar_suspeitos(suspeitos):
    # buscar suspetios 
    print('\n--- Buscar suspeito ---')
    if not suspeitos: 
        print("Nenhum susepeito encontrado")
        return
    
    nome = input('Digete o nome do suspetio: ').strip()
    for nome in suspeitos: # pyright: ignore[reportUndefinedVariable]
        
        info = suspeitos[nome]
        print(f"\nNome: {nome}")
        print(f"Cargo: {info['cargo']}")
        print(f"Ultimo acesso: {info ['ultimo_acesso']}")
        print('=' * 40)
    else:
        print("Suspeito não encontrado")

def remover_suspeitos(suspeitos):
    # remover suspetios 
    print('\n--- Remover suspeito ---')
    if not suspeitos: 
        print("Nenhum susepeito encontrado")
        return
    
    nome = input('Digete o nome do suspetio: ').strip()
    if not suspeitos:
        print("Nenhum susepeito encontrado")
        return
    
    if nome in suspeitos:
        del  suspeitos[nome]
        print(f"Suspeito '{nome}' foi removido com sucesso. ")
    else:
        print("Suspeito não encotrado.")
   
def main():
    
    suspeitos = {}
    print('Operação Cipher: Perfis dos Suspeitos')

    while True:
        menu_suspeitos(suspeitos)
        opcao = input('Escolha uma opção: ')

        if opcao == '1': 
            adicionar_suspeitos(suspeitos)
        elif opcao == '2':
            atualizar_suspeitos(suspeitos)
        elif opcao == '3':
            exibir_suspeitos(suspeitos)
        elif opcao == '4':
            buscar_suspeitos(suspeitos)
        elif opcao == '5':
            remover_suspeitos(suspeitos)
        elif opcao == '6':
            print('ENCERRANDO PROGRAMA')
            break
main()