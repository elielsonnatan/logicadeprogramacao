valorRefeicaoPedida = input("Digite o valor da refeição:")

gorjeta = float(valorRefeicaoPedida) * 0.1
valorTotal = float(valorRefeicaoPedida) + gorjeta

print("\nValor da refeição: R$", valorRefeicaoPedida, "\nValor da gorjeta: R$", gorjeta, "\nValor total (Refeição + Gorjeta): R$", valorTotal)