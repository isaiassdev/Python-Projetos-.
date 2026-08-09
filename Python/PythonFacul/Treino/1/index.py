#sistema de estoque

#tela 1'
def menu_produtos(estoque):
        
        print('1.Adicionar produto')
        print('2.Buscar produto')
        print('3.Saida de Produtos')
        print('4.Fechar')

def Adicionar_produto(estoque):
   print("--- ADICIONAR PRODUTO ---")
   print('=' * 40)
   produto = input('Nome do produto: ')
   quantidade = input('Quantidade do Produto: ')

   if produto in estoque:
        print('Produto já cadastrado.')
        return
   else:
        print('Produto não encontrado.')
     # Armazenando informacoes
     
   estoque[produto] = {
      "quantidade": quantidade
    }
   print(f"O {produto} foi adicionado com sucesso.")

def Buscar_produto(estoque):
    print('--- BUSCAR PRODUTO ---')
    print('=' * 40)
    if not estoque: 
        print("Nenhum produto encontrado.")
        return

    produto = input('Digite o nome do produto: ')
    if produto in estoque:
        info = estoque[produto]
        print(f"\nProduto: {produto}")
        print(f"Quantidade: {info['quantidade']}")
        print('=' * 40)
    else:
        print('Produto não encotrado.')

def Saida_Produtos(estoque):
    print("--- SAÍDA DE PRODUTOS ---")
    print('=' * 40)
    if not estoque:
        print('Nenhum produto econtrado')
        return
    
    produto = input('Digite o nome do produto: ')

    if produto in estoque:
        escolha = input('Produto encontrado. Deseja remove-lo? (SIM/NÃO:) ').strip().upper()
        

        if escolha == "SIM":
            del estoque[produto]
            print('Produto removido com sucesso.')
        elif escolha == "NÃO":
            print('Voltando ao menu')
            
    
def main():
    estoque = {}

    while True:
        menu_produtos(estoque)
        opcao = input("Esolha a opção")

        if opcao == '1':
            Adicionar_produto(estoque)
        elif opcao == '2':
            Buscar_produto(estoque)
        elif opcao == '3':
            Saida_Produtos(estoque)
        elif opcao == '4':
            print('Fechando...')
            break
        else:
            print('Opção inválida.')
main()
