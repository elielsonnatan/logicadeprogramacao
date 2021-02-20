idades = input("Digite as idades: ")
idades = int(idades)
pessoas = 0
quantpessoasmaiorigual18 = 0
quantpessoasmenor18 = 0

while pessoas < 10:
    if idades >= 18:
        quantpessoasmaiorigual18 += 1
    else:
        quantpessoasmenor18 += 1
    idades = input()
    idades = int(idades)
    pessoas += 1

print("Quantidade de pessoas com idade maior ou igual a 18:", quantpessoasmaiorigual18, "\nQuantidade de pessoas com idade menor que 18:", quantpessoasmenor18)