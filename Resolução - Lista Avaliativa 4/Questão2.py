condicao = True
listanumeros = []
listanumerosordenada = []
contador = 0
print("Digite números inteiros. Para parar tecle ENTER sem digitar nada: ")

while condicao == True:
    numero = input()
    if numero != "":
        numero = int(numero)
        listanumeros.append(numero)
    else:
        condicao = False

quantelementoslistanumeros = len(listanumeros)

for elementolista in listanumeros:
    if elementolista < 0:
        listanumerosordenada.append(elementolista)

for elementolista in listanumeros:
    if elementolista == 0:
        listanumerosordenada.append(elementolista)

for elementolista in listanumeros:
    if elementolista > 0:
        listanumerosordenada.append(elementolista)

print(listanumerosordenada)