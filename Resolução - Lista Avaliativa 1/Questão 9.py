distanciaASerPercorrida = float(input("Digite a distância a ser percorrida em quilômetros:"))
velocidadeMedia = float(input("\nDigite a velocidade média do veículo em quilômetros/hora:"))

tempoViagemEmHoras = int(distanciaASerPercorrida // velocidadeMedia)

tempoviagemEmMinutos = int(((distanciaASerPercorrida / velocidadeMedia) - tempoViagemEmHoras) * 60)

print("\nO tempo total de viagem é:", tempoViagemEmHoras, "horas e", tempoviagemEmMinutos, "minutos.")