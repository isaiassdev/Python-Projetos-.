
senha = ""


while senha != "1234":
    senha = input("Digite a senha: ")

    if senha == "1234":
        print("senha correta")
        break
    else:   
        print("erro")