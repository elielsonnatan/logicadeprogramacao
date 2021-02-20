numero = input("Digite o número: ")
numero = int(numero)
guardarnumero = numero
fatorial = 1

if numero < 0:
    print("ERRO!")
else:
    if numero == 0:
        print("0! = 1")
    else:
        for numero in range(numero, 0, -1):
            fatorial *= numero
        print(guardarnumero, "! =", fatorial)