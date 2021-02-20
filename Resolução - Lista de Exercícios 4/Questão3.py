import random
numeroslancamentos = []
vezesnumeros = []

for contador in range (0,10):
    numeroslancamentos.append(random.randrange(1,6))

for contador2 in range(1,7):
    vezesnumeros.append(numeroslancamentos.count(contador2))

print(numeroslancamentos)

print(vezesnumeros)