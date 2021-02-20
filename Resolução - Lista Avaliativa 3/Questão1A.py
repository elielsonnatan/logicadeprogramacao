# Solução utilizando WHILE
print("Digite 8 valores: ")
contador = 0
somavalor = 0

while contador < 8:
    valor = input()
    valor = float(valor)
    somavalor += valor
    contador += 1

media = somavalor / 8

print("\nMédia:", media)