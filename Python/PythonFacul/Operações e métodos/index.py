# Operação Cipher: Coleta e Organização de Evidéncias
# Durante a investigação, a equipe coleta logs, alertas e registos de acesso dos servidores e edes internas
# Cada evidéncia é armazenada em um lista para posterior ánalise

def mostrar_menu():

    print('1. Adicionar Evidéncias')
    print('2. Remover Evidéncias')
    print('3. Exibir Evidencias')
    print('4. Ordenar Evidencias')
    print('5. Filtar Evidencias')
    print('6. Sair')

def Adicionar_Evidencias(evidencias):
    """Soliita e adiciona um nova evidencia a lista"""
    evidencia = input("Digite a nova evidencia (ex: 'IP: 192.168.1.1', 'Log: falha de autentição): ")
    evidencias.append(evidencia)
    print("Evidenia adicionada com sucesso.")

def Remover_Evidéncias(evidencias):
    if not evidencias: 
        print("Nenhuma evidencia para remove.")
        return
    print("Evidencias disponivez para remoção: ")
    for i, ev in enumerate(evidencias):
        print(f"{i+1}. {ev}")

    escolha = input("digite o número para remoção: ")

    if escolha.isdigit():
        escolha = int(escolha)

        if 1 <= escolha <= len(evidencias):
            removida = evidencias.pop(escolha - 1)
            print(f"Evidência removida: {removida}")
        else:
            print('Número inválido.')
    else: 
        print("Entrada inválida. Por favor, digite um número.")
        
def Exibir_Evidencias(evidencias):
    if not evidencias:
        print('Nenhuma evidencia registrada.')
    else:
        print("\n Lista de Evidencias")
        for i, ev in enumerate(evidencias):
            print(f"{i+1}. {ev}")

def Ordenar_Evidencias(evidencias):
    """Odernar a lista de evidencias em ordem alfabetica """
    evidencias.sort()
    print('evidencias ordenadas em odem alfabetica.')


def Filtar_Evidencias(evidencias):
    """Filtra e exibe evidencias que contenham uma palava-chave informada pelo usuáio"""

    palavra = input("Digite a palava-chave para filtra a evidencia: ")
    Filtradas = [ev for ev in evidencias if palavra.lower() in ev.lower()] #list comprehension: é uma forma compacta de criar uma nova lista filtrando elementos.
    if Filtradas:
        print("\n Evindecias filtradas: ")
        for ev in Filtradas: 
            print(f"- {ev}")
    else:
        print("Nenhuma evidencia encotrada com essa palava-chave ")

def main():

    evidencias = []
    print("Operação Cipher: Coleta e Organização de Evidéncias")
    print("Iniciando a coleta de evidencias dos servidoes e redes internas...")
    
    while True:
        mostrar_menu()
        
        opcao = input('Esolha a opção: ')

        if opcao == '1':
            Adicionar_Evidencias(evidencias)
        elif opcao == '2':
            Remover_Evidéncias(evidencias)
        elif opcao == '3':
            Exibir_Evidencias(evidencias)
        elif opcao == '4':
            Ordenar_Evidencias(evidencias)
        elif opcao == '5':
            Filtar_Evidencias(evidencias)
        elif opcao == '6':
            break
        else:
            print('Opção inválida')
main()