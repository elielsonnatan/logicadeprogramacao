idade = input("Digite a idade dos membros da família, quando terminar tecle ENTER: ")

valordevido = 0
while idade != "":
    idade = input("Digite a idade: ")
    if idade != "":
        idade = int(idade)
        if idade <= 2:
            valor = 0.0
        elif idade >= 3 and idade <= 12:
            valor = 10.0
        elif idade >= 65:
            valor = 15.0
        else:
            valor = 20.0
        valordevido += valor
    else:
        break

print("\nValor total: R$", valordevido)