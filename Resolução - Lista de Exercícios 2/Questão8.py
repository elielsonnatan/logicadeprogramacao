precoproduto = float(input("Digite o preço do produto: "))
codigoproduto = input("Digite o código da forma de pagamento: ")

if codigoproduto == "1":
    parcela = precoproduto * 0.7
    print("O valor do produto à vista é R$", parcela)
else:
    if codigoproduto == "2":
        parcela = (precoproduto * 0.8) / 2
        print("O produto será pago em 2 vezes de R$", parcela)
    else:
        if codigoproduto == "3":
            parcela = (precoproduto * 0.9) / 3
            print("O produto será pago em 3 vezes de R$", parcela)
        else:
            parcelas4 = (precoproduto / 4)
            parcelas5 = (precoproduto / 5)
            parcelas6 = (precoproduto / 6)
            print("O produto poderá ser pago em 4 vezes de R$", parcelas4, "ou 5 vezes de R$", parcelas5, "ou 6 vezes de R$", parcelas6)