#sistema de estoque

#tela 1'
def menu_produtos(estoque):
        
        print('1.Adicionar produto')
        print('2.Buscar produto')
        print('3.Saida de Produtos')
        print('4.Fechar')

def adicionar_produto(estoque):
    print("--- ADICIONAR PRODUTO ---")
    print('=' * 40)

    produto = input('Nome do produto: ').strip().lower()

    try:
         quantidade = int(input('Quantidade do Produto: '))

         if quantidade < 0: 
            print('A quantidade não pode ser negativa')
            return  
    except ValueError :
            print('Digite uma quantidade numérica válida.')
            return
     
    if produto in estoque:
        print('Produto já cadastrado.')
        return
    
     # Armazenando informacoes
     
    estoque[produto] = {
      "quantidade": quantidade
    }
    print(f"O {produto} foi adicionado com sucesso.")

def buscar_produto(estoque):
    print('--- BUSCAR PRODUTO ---')
    print('=' * 40)
    if not estoque: 
        print("Nenhum produto encontrado.")
        return

    produto = input('Digite o nome do produto: ').strip().lower()
    if produto in estoque:
        info = estoque[produto]
        print(f"\nProduto: {produto}")
        print(f"Quantidade: {info['quantidade']}")
        print('=' * 40)
    else:
        print('Produto não encontrado.')

def saida_Produtos(estoque):
    print("--- SAÍDA DE PRODUTOS ---")
    print('=' * 40)
    if not estoque:
        print('Nenhum produto encontrado')
        return
    produto = input('Digite o nome do produto: ').strip().lower()

    if produto in estoque:
        escolha = input('Produto econtrado. Deseja remove-lo? (SIM/NÃO: ) ').strip().upper()
        

        if escolha == "SIM":
            del estoque[produto]
            print('Produto removido com sucesso.')
        elif escolha == "NÃO":
            print('Voltando ao menu')
        else: 
            print('Opção inválida')    
    
def main():
    estoque = {}

    while True:
        menu_produtos(estoque)
        opcao = input("Escolha a opção: ")

        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            buscar_produto(estoque)
        elif opcao == '3':
            saida_Produtos(estoque)
        elif opcao == '4':
            print('Fechando...')
            break
        else:
            print('Opção inválida.')
if __name__ == "__main__":
    main()
