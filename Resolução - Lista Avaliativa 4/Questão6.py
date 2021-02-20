horoscopoChines = ((0, "Macaco"), (1, "Galo"), (2, "Cão"), (3, "Porco"), (4, "Rato"), (5, "Boi"), (6, "Tigre"), (7, "Coelho"), (8, "Dragão"), (9, "Serpente"), (10, "Cavalo"), (11, "Carneiro"))

anoNascimento = input("Digite seu ano de nascimento: ")
anoNascimento = int(anoNascimento)

indice = anoNascimento % 12

print("\nSeu signo no horóscopo chinês é:", horoscopoChines[indice][1])