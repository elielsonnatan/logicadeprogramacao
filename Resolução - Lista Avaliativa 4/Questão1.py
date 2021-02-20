listanumeros = []
condicao = True
contador = 0

print("Digite números inteiros. Para parar digite 0: ")

while condicao == True:
    numero = input()
    numero = int(numero)
    if numero != 0:
        listanumeros.append(numero)
    else:
        condicao = False

listanumerosinversa = listanumeros[::-1]
quantelementoslistanumeros = len(listanumeros)
print("\nLista de números invertidos:")
while contador < quantelementoslistanumeros:
    print(listanumerosinversa[contador])
    contador += 1