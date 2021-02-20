nomecandidato = input("Digite o nome do candidato: ")
notaportugues = float(input("Digite a nota da prova de Português: "))
notamatematica = float(input("Digite a nota da prova de Matemática: "))
notaconhecimentosgerais = float(input("Digite a nota da prova de Conhecimentos Gerais: "))

media = (notaportugues + notamatematica + notaconhecimentosgerais) / 3

print("\nNome do candidato:", nomecandidato, "\nNota de Português:", notaportugues, "\nNota de Matemática:", notamatematica, "\nNota de Conhecimentos Gerais:", notaconhecimentosgerais, "\nMédia:", media)
if notaportugues >= 5 and notamatematica >= 5 and notaconhecimentosgerais >= 5 and media > 7:
    print("\nO candidato foi aprovado!")
else:
    print("\nO candidato não foi aprovado!")