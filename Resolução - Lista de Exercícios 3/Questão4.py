mediaidades = 0 
pessoa = 0 
somaidades = 0 
idade = 0
quantidademasculino = 0
quantidadefeminino = 0
quantidadenaodeclarar = 0

while pessoa < 8:
    idade = input("Digite a idade da pessoa: ")
    idade = int(idade)
    sexo = input("Digite o sexo da pessoa (masculino, feminino ou não quero declarar): ")
    sexo = sexo.lower()
    somaidades += idade
    if sexo == "masculino":
        quantidademasculino += 1
    else:
        if sexo == "feminino":
            quantidadefeminino += 1
        else:
            quantidadenaodeclarar += 1
    pessoa += 1

mediaidades = somaidades / 8
print("\nMédia das idades: ", mediaidades, "\nQuantidade de pessoas do sexo masculino:", quantidademasculino, "\nQuantidade de pessoas do sexo feminino:", quantidadefeminino, "\nQuantidade de pessoas que não quiseram declarar o sexo:", quantidadenaodeclarar)