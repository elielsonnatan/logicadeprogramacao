import Funcoes
velocidadefinal = input("Digite a velocidade final do veículo: ")
velocidadefinal = float(velocidadefinal)
opcaovelocidadefinal = input("Digite a unidade de velocidade - m/s ou km/h: ")
opcaovelocidadefinal = opcaovelocidadefinal.lower()
if opcaovelocidadefinal == "km/h":
    velocidadefinal = velocidadefinal / 3.6

aceleracao = input("\nDigite a aceleração do veículo: ")
aceleracao = float(aceleracao)
opcaoaceleracao = input("Digite a unidade de aceleração - m/s ou km/h: ")
opcaoaceleracao = opcaoaceleracao.lower()
if opcaoaceleracao == "km/h":
    aceleracao = aceleracao / 3.6

tempo = input("\nDigite o tempo que o veículo levou para percorrer essa distância: ")
tempo = int(tempo)
opcaotempo = input("Digite a unidade de tempo - segundos, minutos ou horas: ")
opcaotempo = opcaotempo.lower()
if opcaotempo == "minutos":
    tempo = tempo * 60
elif opcaotempo == "horas":
    tempo = tempo * 3600

unidaderesultado = input("\nA distância percorrida deve ser retornada em metros ou quilômetros? ")
unidaderesultado = unidaderesultado.lower()

distanciapercorrida = Funcoes.calculodistanciapercorrida(velocidadefinal, tempo, aceleracao)

if unidaderesultado == "metros":
    if distanciapercorrida == 1:
        print("A distância percorrida foi 1 metro.")
    else:
        print("A distância percorrida foi", distanciapercorrida, "metros.")
else:
    distanciapercorrida = distanciapercorrida / 1000
    if distanciapercorrida == 1:
        print("A distância percorrida foi 1 quilômetro.")
    else:
        print("A distância percorrida foi", distanciapercorrida, "quilômetros.")