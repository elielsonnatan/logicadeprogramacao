codigoproduto = input("Digite o código do produto: ")
quantidadecomprada = int(input("Digite a quantidade comprada: "))

if codigoproduto == "ABCD":
    valortotal = 5.30 * quantidadecomprada
    print("\nValor total da compra:", valortotal)
else:
    if codigoproduto == "XYPK":
        valortotal = 6.00 * quantidadecomprada
        print("\nValor total da compra:", valortotal)
    else:
        if codigoproduto == "KLMP":
            valortotal = 3.20 * quantidadecomprada
            print("\nValor total da compra:", valortotal)
        else:
            valortotal = 2.50 * quantidadecomprada
            print("\nValor total da compra:", valortotal)