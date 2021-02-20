codigousuarioX = 1234
senhausuarioX = 9999
tentativas = 4

codigousuario = input("Digite o código de usuário: ")
codigousuario = int(codigousuario)

while codigousuario != codigousuarioX:
    print("Usuário Inválido!")
    codigousuario = input("Digite o código de usuário: ")
    codigousuario = int(codigousuario)

senhausuario = input("Digite a senha: ")
senhausuario = int(senhausuario)

if senhausuario == senhausuarioX:
    print("Acesso Permitido!")
else:
    while tentativas >=0 and tentativas <=4:
        if senhausuario == senhausuarioX:
            print("Acesso Permitido!")
            break
        else:
            if tentativas > 1:
                print("Senha Incorreta! Você tem mais", tentativas, "tentativas")
                senhausuario = input("Digite a senha: ")
                senhausuario = int(senhausuario)
            else:
                if tentativas == 1:
                    print("Senha Incorreta! Você tem mais", tentativas, "tentativa.")
                    senhausuario = input("Digite a senha: ")
                    senhausuario = int(senhausuario)
                else:
                    print("Usuário Bloqueado")
        tentativas -= 1