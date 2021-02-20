
quantidadepessoas = 0
resposta = input("Tem alguém presente? ")
resposta = resposta.lower()

if resposta == "não":
    print("Não há ninguém presente.")
else:
    while resposta == "sim":
        quantidadepessoas += 1
        resposta = input("Tem mais alguém presente? ")
    print("Quantidade de pessoas presentes:", quantidadepessoas)