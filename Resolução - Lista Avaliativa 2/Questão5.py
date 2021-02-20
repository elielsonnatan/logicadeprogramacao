quantidadelados = int(input("Digite a quantidade de lados (no mínimo 3 e no máximo 10): "))

if quantidadelados < 3 or quantidadelados > 10:
    print("Digite um número maior ou igual a 3 e menor ou igual a 10.")
else:
    if quantidadelados == 3:
        print("Triângulo")
    else:
        if quantidadelados == 4:
            print("Quadrado")
        else:
            if quantidadelados == 5:
                print("Pentágono")
            else:
                if quantidadelados == 6:
                    print("Hexágono")
                else:
                    if quantidadelados == 7:
                        print("Heptágono")
                    else:
                        if quantidadelados == 8:
                            print("Octógono")
                        else:
                            if quantidadelados == 9:
                                print("Eneágono")
                            else:
                                print("Decágono")