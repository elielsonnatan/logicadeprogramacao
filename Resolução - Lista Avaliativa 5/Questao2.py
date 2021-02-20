import Funcoes

quantidadeitens = input("Digite a quantidade de itens a serem calculados: ")
quantidadeitens = int(quantidadeitens)

valorpago = Funcoes.valorApagar(quantidadeitens)

print("O valor a ser pago é de: R$", valorpago)