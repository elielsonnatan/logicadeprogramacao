tipousuario = input("Digite o tipo de usuário (cliente, fornecedor ou vendedor):")

if (tipousuario == "cliente"):
    print("Abrindo módulo de compras...")
else: 
    if (tipousuario == "fornecedor"):
        print("Abrindo Visualização de Estoque...")
    else: 
        if (tipousuario == "vendedor"):
            print("Abrindo Módulo de Vendas...")
        else:
            print("Usuário Inválido.")