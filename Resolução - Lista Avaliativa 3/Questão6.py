
print("Aproximação 1 de Pi (π): 3")
numerodaaproximacao = 2

multiplicador1 = 2
multiplicador2 = 3
multiplicador3 = 4

aproximacao = 3 + (4/(multiplicador1 * multiplicador2 * multiplicador3))
print("\nAproximação 2 de Pi (π):", aproximacao)

for quanttermos in range (3,16):
    multiplicador1 += 2
    multiplicador2 += 2
    multiplicador3 += 2
    termo = 4/(multiplicador1 * multiplicador2 * multiplicador3)
    aproximacao -= termo
    print("\nAproximação", quanttermos, "de Pi (π):", aproximacao)