valor = int(input("Digite o valor em reais (sem centavos): "))

if valor < 2:
    print ("\nDigite um valor maior que 2, com exceção do 3, pois não existem mais notas de R$ 1,00")
elif valor % 2 != 0:
    valor = valor - 5
    quantidadenotas200 = valor // 200
    quantidadenotas100 = (valor % 200) // 100
    quantidadenotas50 = ((valor % 200) % 100) // 50
    quantidadenotas20 = (((valor % 200) % 100) % 50) // 20
    quantidadenotas10 = ((((valor % 200) % 100) % 50) % 20) // 10
    quantidadenotas2 = (((((valor % 200) % 100) % 50) % 20) % 10) // 2

    if quantidadenotas200 != 0:
        print("Lobo-Guará:", quantidadenotas200)

    if quantidadenotas100 != 0:
        print("\nGaroupa:", quantidadenotas100)

    if quantidadenotas50 != 0:
        print("\nOnça-Pintada:", quantidadenotas50)

    if quantidadenotas20 != 0:
        print("\nMico-Leão-Dourado:", quantidadenotas20)

    if quantidadenotas10 != 0:
        print("\nArara:", quantidadenotas10)

    print("\nGarça: 1")

    if quantidadenotas2 != 0:
        print("\nTartaruga de Pente:", quantidadenotas2)
else:
    quantidadenotas200 = valor // 200
    quantidadenotas100 = (valor % 200) // 100
    quantidadenotas50 = ((valor % 200) % 100) // 50
    quantidadenotas20 = (((valor % 200) % 100) % 50) // 20
    quantidadenotas10 = ((((valor % 200) % 100) % 50) % 20) // 10
    quantidadenotas2 = (((((valor % 200) % 100) % 50) % 20) % 10) // 2

    if quantidadenotas200 != 0:
        print("Lobo-Guará:", quantidadenotas200)

    if quantidadenotas100 != 0:
        print("\nGaroupa:", quantidadenotas100)

    if quantidadenotas50 != 0:
        print("\nOnça-Pintada:", quantidadenotas50)

    if quantidadenotas20 != 0:
        print("\nMico-Leão-Dourado:", quantidadenotas20)

    if quantidadenotas10 != 0:
        print("\nArara:", quantidadenotas10)

    if quantidadenotas2 != 0:
        print("\nTartaruga de Pente:", quantidadenotas2)