
nomes = { 'Miguel','Ravi','Théo','Gael','Noah','Arthur'}

def nome_pessoas(nomes,escolha):
     
    if escolha not in nomes: 
        print(f"Nome {escolha} não encontrado! ")
        return False

    if escolha in nomes:
        print(f"  nome encotrando {escolha}")
        return True
    
while True:
        escolha = input('Digite o nome que quer buscar')
        encontro = nome_pessoas(nomes, escolha)
        if encontro:
            break
