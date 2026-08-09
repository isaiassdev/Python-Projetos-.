num1 = int(input("digite um numero :"))
num2 = int(input("Digite outro numero : "))
es = input("+, - , * / : ")

escolha = {
    "-" : num1 - num2,
    "+" : num1 + num2,
    "*" : num1 * num2,
    "/" : num1 / num2
}

print(escolha[es])