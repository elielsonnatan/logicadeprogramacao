import random
import math

def valorApagar (quantitens):
    if quantitens == 1:
        valor = 59.67
    else:
        valor = 59.67 + ((quantitens - 1) * 16.07)
    return valor

def verificatriangulo (a, b, c):
    if abs(b-c) < a < (b + c) and abs(a-c) < b < (a + c) and abs(a-b) < c < (a + b):
        print ("Esses valores permitem a formação de um triângulo.")
    else:
        print ("Esses valores não permitem a formação de um triângulo.")

def formadepagamento (totalgasto, formadepagamento):
    if formadepagamento == 1:
        valorpago = totalgasto * 0.9
        print(f"Para pagamento à vista: 10% de desconto. \n Valor total a pagar: {valorpago}")
    elif formadepagamento == 2:
        valorparcela = totalgasto/2
        print(f"A compra será paga em 2 parcelas de R$ {valorparcela} sem juros.")
    else:
        montante = totalgasto * (1.03**formadepagamento)
        valorparcela = montante / formadepagamento
        print(f"A compra será paga em {formadepagamento} parcelas de R$ {round(valorparcela + 0.01, 2)} com juros de 3% ao mês")

def calculodistanciapercorrida (velocidadefinal, tempo, aceleracao):
    velocidadeinicial = velocidadefinal - (aceleracao * tempo)
    distanciapercorrida = (velocidadeinicial*tempo) + (aceleracao*(tempo**2))
    return distanciapercorrida

def senhaaleatoria():
    caracteresenha = chr(random.randrange(33,126))
    return caracteresenha

def delta():
    valordelta = (-35)**2 - (4*34)
    return valordelta

def maximoconcentracao():
    coordenadaYvertice = -delta()/4
    indice = coordenadaYvertice * (-0.008)
    return indice

def tempoparaatingirmaximoconcentracao():
    tempomaximoconcentracao = -(-35/2)
    return tempomaximoconcentracao

def sobrionovamente():
    tempoficousobrionovamente = (35 + math.sqrt(delta())) / 2
    return tempoficousobrionovamente

def abrirarquivo (caminho,mode):
    arquivo = open(caminho,mode)
    return arquivo

def escreverarquivo (arquivo,texto):
    arquivo.write(texto)

def fechararquivo (arquivo):
    arquivo.close()

def leituraarquivo (caminho,mode):
    aberturaarquivo = open(caminho,mode)
    leituraarquivo = aberturaarquivo.read()
    print(leituraarquivo)
    aberturaarquivo.close()