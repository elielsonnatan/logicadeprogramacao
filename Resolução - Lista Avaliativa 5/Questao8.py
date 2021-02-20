import Funcoes

print("1 - Desejo apenas ler o arquivo. \n2 - Desejo escrever no arquivo.")
opcaoarquivo = input("Digite o número correspondente ao que você deseja fazer no arquivo: ")
caminhoarquivo = input("Digite o nome ou caminho do arquivo: ")

if opcaoarquivo == "1":
    Funcoes.leituraarquivo(caminhoarquivo,"r")
else:
    arquivo = Funcoes.abrirarquivo(caminhoarquivo,"a")
    print("Agora digite o que você deseja escrever no arquivo: ")
    linha = input()
    Funcoes.escreverarquivo(arquivo,linha)
    while linha != "":
        Funcoes.escreverarquivo(arquivo," ")
        linha = input()
        Funcoes.escreverarquivo(arquivo,linha)
    Funcoes.fechararquivo(arquivo)
    Funcoes.leituraarquivo(caminhoarquivo,"r")
    Funcoes.fechararquivo(arquivo)