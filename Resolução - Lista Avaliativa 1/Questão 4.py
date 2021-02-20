quantidadeRecipientes1litro = input("Digite a quantidade de recipientes de 1 litro:")
quantidadeRecipientes2litros = input("\nDigite a quantidade de recipientes de 2 litros:")

valorRecebidoPeloUsuario = float(int(quantidadeRecipientes1litro) * 0.1) + float(int(quantidadeRecipientes2litros) * 0.25)

print("\nO valor recebido pelo usuário é de: R$", valorRecebidoPeloUsuario)