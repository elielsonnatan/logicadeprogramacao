# Solução utilizando FOR
print("Digite 8 valores: ")
somavalor = 0

for contador in range (0,8):
    valor = input()
    valor = float(valor)
    somavalor += valor

media = somavalor / 8

print("\nMédia:", media)