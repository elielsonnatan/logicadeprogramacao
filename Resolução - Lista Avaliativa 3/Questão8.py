valorbinario = input("Digite o valor binário: ")
quantidadedigitos = len(valorbinario)

contador = 0
indice = -1
potencia = 0
valordecimal = 0

while contador < quantidadedigitos:
    termo = int(valorbinario[indice]) * (2 ** potencia)
    valordecimal += termo
    indice -= 1
    potencia += 1
    contador += 1

print("O valor em decimal é:", valordecimal)