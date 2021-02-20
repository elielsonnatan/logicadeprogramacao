listanotasletras = ["a+", "a-", "b+", "b-", "c+", "c-", "d+", "d-"]
listanotasnumeros = [4.0, 3.7, 3.3, 2.7, 2.3, 1.7, 1.3, 0]
listanotasalunos = []
somanotasalunos = 0
indicenotasalunos = 0

print("Digite a nota dos alunos: ")

for quantalunos in range (1,14):
    print("Aluno", quantalunos, ":") 
    notaletra = input()
    notaletra = notaletra.lower()
    indice = listanotasletras.index(notaletra)
    notanumero = listanotasnumeros[indice]
    listanotasalunos.insert(indicenotasalunos, notanumero)
    somanotasalunos += notanumero
    indicenotasalunos += 1

media = somanotasalunos / 13

print("\nNOTAS DOS ALUNOS")

indicenotasalunos = 0
for quantalunos in range (1,14):
    print("Aluno", quantalunos, "-", listanotasalunos[indicenotasalunos])
    indicenotasalunos += 1

print("\nMÉDIA DA TURMA:", media)    