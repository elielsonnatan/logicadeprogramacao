carrosconsumo = [["Vectra", 9], ["Gol", 10], ["Corsa", 11], ["Fit", 12.5]]
consumo = []
custoMilQuilometros = []

for contador in range (0,4):
    consumo.append(carrosconsumo[contador][1])
    valorConsumo = (1000 / carrosconsumo[contador][1]) * 4.69
    custoMilQuilometros.append(valorConsumo)
    contador += 1

indiceMaisEconomico = consumo.index(max(consumo))

print("O carro mais econômico é:", carrosconsumo[indiceMaisEconomico][0])
print("\n-------------------------------------")
print("Modelo | Custo para percorrer 1000 KM")
print("-------------------------------------")

for contador in range (0,4):
    print(f"\n{carrosconsumo[contador][0]}", "\t\tR$ {:.2f}".format(custoMilQuilometros[contador]))