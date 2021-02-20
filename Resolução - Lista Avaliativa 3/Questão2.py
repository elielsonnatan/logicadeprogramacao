contador = 0
somanumero = 0
quantidadeiteracoes = 0

numero = input("Digite um número: ")
numero = float(numero)

while numero != 0:
    somanumero += numero
    numero = input()
    numero = float(numero)
    quantidadeiteracoes += 1

media = somanumero / quantidadeiteracoes
print("\nMédia: ", media)