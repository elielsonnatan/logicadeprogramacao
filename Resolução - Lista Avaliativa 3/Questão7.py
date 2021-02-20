print("Digite dois números inteiros positivos:")
numero1 = input("Número 1: ")
numero1 = int(numero1)
numero2 = input("Número 2: ")
numero2 = int(numero2)

divisor = 2

if numero1 % numero2 == 1 or numero2 % numero1 == 1:
    print("\nO MDC de", numero1, "e", numero2, "é 1")
elif numero1 / numero2 == 0:
    print("\nO MDC de", numero1, "e", numero2, "é:", numero2)
elif numero2 / numero1 == 0:
    print("\nO MDC de", numero1, "e", numero2, "é:", numero1)
else:
    MDC = 1
    while divisor <= numero1 or divisor <= numero2:
        if numero1 % divisor == 0 and numero2 % divisor == 0:
            MDC *= divisor
            numero1 = numero1 / divisor
            numero2 = numero2 / divisor
        else:
            divisor += 1
    print("\nO MDC é:", MDC)