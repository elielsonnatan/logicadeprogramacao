casas = 1
quantgraos = 1

while casas <= 64:
    quantgraos *= 2
    casas += 1

quanttotalgraos = quantgraos - 1
print("Quantidade de grãos de arroz que o monge recebeu:", quanttotalgraos)