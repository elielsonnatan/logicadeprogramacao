quantdeprodutos = input("Informe o número de produtos a serem digitados: ")
print("")
quantdeprodutos = int(quantdeprodutos)

listavaloressemdesconto = []
listavalorescomdesconto = []

indice = 0
produto = 1
print("Digite o valor dos produtos:")
while produto <= quantdeprodutos:
    print("Produto", produto)
    valorproduto = input()
    valorproduto = float(valorproduto)
    listavaloressemdesconto.insert(indice, valorproduto)
    valorcomdesconto = valorproduto * 0.4
    listavalorescomdesconto.insert(indice, valorcomdesconto)
    indice += 1
    produto += 1

print("\nProduto", " | ", "Valor sem desconto", " | ", "Valor com desconto")

indice = 0
produto = 1
while produto <= quantdeprodutos:
    print("\n", produto, "\t\tR$", listavaloressemdesconto[indice], "\t\tR$ {:.1f}".format(listavalorescomdesconto[indice]))
    indice += 1
    produto += 1