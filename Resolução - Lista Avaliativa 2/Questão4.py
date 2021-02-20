letra = input("Digite a letra: ")
representacaoletradecimal = ord(letra)

if representacaoletradecimal >= 65 and representacaoletradecimal <= 90:
    print("Esta letra é maiúscula.")
else:
    print("Esta letra é minúscula.")