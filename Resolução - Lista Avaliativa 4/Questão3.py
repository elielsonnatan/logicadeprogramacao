import random
numerosmegasena = []
while len(numerosmegasena) < 6:
    numero = random.randrange(1,61)
    if numero not in numerosmegasena:
        numerosmegasena.append(numero)
    else:
        continue

print(numerosmegasena)
