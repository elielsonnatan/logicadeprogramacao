angulo1 = float(input("Digite o ângulo 1: "))
angulo2 = float(input("Digite o ângulo 2: "))
angulo3 = float(input("Digite o ângulo 3: "))

if angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
    print("Triângulo retângulo.")
else:
    if angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        print("Triângulo obtusângulo.")
    else:
        print("Triângulo acutângulo.")