listanumeros = []

print("Digite os números inteiros:")
numero = input()
numero = int(numero)

while numero != 0:
    if numero != 0:
        listanumeros.append(numero)
    else:
        break
    numero = input()
    numero = int(numero)

listanumeros.sort()
print(listanumeros)