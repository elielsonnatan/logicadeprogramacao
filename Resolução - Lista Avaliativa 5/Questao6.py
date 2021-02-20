import random
import Funcoes

contador = 0
senha = []
quantcaracteres = random.randrange(7,11)

while contador < quantcaracteres:
    numero = Funcoes.senhaaleatoria()
    if numero not in senha:
        senha.append(numero)
    else:
        continue
    contador += 1

print(senha)
