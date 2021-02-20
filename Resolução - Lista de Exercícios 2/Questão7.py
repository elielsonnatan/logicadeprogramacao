nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3

if media > 6:
    print("Aluno aprovado por média!")
else:
    if media < 6 and media >= 4:
        print("Exame final.")
    else:
        print("Aluno reprovado.")