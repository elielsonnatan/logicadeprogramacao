print("Digite a temperatura média de cada mês do ano:")
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
mediaTemperaturaMeses = []
for contador in range (0,12):
    temperatura = input(f"{meses[contador]} ")
    temperatura = float(temperatura)
    mediaTemperaturaMeses.append(temperatura)

mediaAnual = sum(mediaTemperaturaMeses) / 12
print("A média anual de temperaturas é:", mediaAnual, "graus.")

print("\nMeses com temperatura acima da média anual:")
for temperaturaMes in mediaTemperaturaMeses:
    if temperaturaMes > mediaAnual:
        indice = mediaTemperaturaMeses.index(temperaturaMes)
        print(meses[indice],"\t",temperaturaMes,"graus")