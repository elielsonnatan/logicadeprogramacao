baseterreno = input("Digite o comprimento da base do terreno:")
alturaterreno = input("\nDigite a altura do terreno:")

areaterrenometros = (int(baseterreno) * int(alturaterreno))/2
areaterrenohectares = areaterrenometros/10000

print("\nA área do terreno é", areaterrenometros, "metros quadrados ou", areaterrenohectares, "hectares.")