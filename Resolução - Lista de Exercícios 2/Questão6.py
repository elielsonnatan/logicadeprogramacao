codigoproduto = input("Digite o código do produto: ")
quantidadecomprada = int(input("Digite a quantidade comprada: "))

if codigoproduto == "1001":
    valortotal = 5.32 * quantidadecomprada
    print("\nValor total da compra:", valortotal)
else:
    if codigoproduto == "1324":
        valortotal = 6.45 * quantidadecomprada
        print("\nValor total da compra:", valortotal)
    else:
        if codigoproduto == "6548":
            valortotal = 2.37 * quantidadecomprada
            print("\nValor total da compra:", valortotal)
        else:
            valortotal = 5.32 * quantidadecomprada
            print("\nValor total da compra:", valortotal)