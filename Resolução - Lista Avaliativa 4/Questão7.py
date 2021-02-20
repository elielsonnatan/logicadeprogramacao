listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
listanumerospares = []
listanumerosimpares = []

for numero in listanumeros:
    if numero % 2 == 0:
        listanumerospares.append(numero)
    else:
        listanumerosimpares.append(numero)

print("Lista de números pares:", listanumerospares, "\nLista de números ímpares:", listanumerosimpares)