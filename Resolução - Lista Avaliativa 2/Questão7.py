dia = int(input("Digite o dia: "))
nomeMes = input("Digite o nome do mês: ")
nomeMes = nomeMes.lower()

if nomeMes == "janeiro" or nomeMes == "fevereiro":
    print("\nA estação é Verão")
else:
    if nomeMes == "março" and dia < 20:
        print("\nA estação é Verão")
    else:
        if nomeMes == "março" and dia >=20:
            print("\nA estação é Outono")
        else:
            if nomeMes == "abril" or nomeMes == "maio":
                print("\nA estação é Outono")
            else:
                if nomeMes == "junho" and dia < 21:
                    print("\nA estação é Outono")
                else:
                    if nomeMes == "junho" and dia >= 21:
                        print("\nA estação é Inverno")
                    else:
                        if nomeMes == "julho" or nomeMes == "agosto":
                            print("\nA estação é Inverno")
                        else:
                            if nomeMes == "setembro" and dia < 22:
                                print ("\nA estação é Inverno")
                            else:
                                if nomeMes == "setembro" and dia >= 22:
                                    print("\nA estação é Primavera")
                                else:
                                    if nomeMes == "outubro" or nomeMes == "novembro":
                                        print("\nA estação é Primavera")
                                    else:
                                        if nomeMes == "dezembro" and dia < 21:
                                            print("\nA estação é Primavera")
                                        else:
                                            print("\nA estação é Verão")