nivelsomdecibeis = int(input("Digite o nível do som em decibéis (dB): "))

if nivelsomdecibeis > 130 or nivelsomdecibeis < 40:
    print("Barulho desconhecido.")
else:
    if nivelsomdecibeis == 130:
        print("\nO que está causando o barulho é uma britadeira.")
    else:
        if nivelsomdecibeis < 130 and nivelsomdecibeis > 106:
            print("\n", nivelsomdecibeis, "dB está entre o barulho de uma britadeira e de um cortador de grama a gás.")
        else:
            if nivelsomdecibeis == 106:
                print("\nO que está causando o barulho é um cortador de grama a gás.")
            else:
                if nivelsomdecibeis < 106 and nivelsomdecibeis > 70:
                    print("\n", nivelsomdecibeis, "dB está entre o barulho de um cortador de grama a gás e de um despertador.")
                else:
                    if nivelsomdecibeis == 70:
                        print("\nO que está causando o barulho é um despertador.")
                    else:
                        if nivelsomdecibeis < 70 and nivelsomdecibeis > 40:
                            print("\n", nivelsomdecibeis, "dB está entre o barulho de um despertador e de uma sala tranquila.")
                        else:
                            print("\nO que está causando o barulho é uma sala tranquila.")