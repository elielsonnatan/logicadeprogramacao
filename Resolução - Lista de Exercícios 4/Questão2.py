listajogo = [["Brasil","Itália",[10,9]],["Brasil","Espanha",[5,7]],["Itália","Espanha",[7,8]]]
totalfaltascampeonato = 0

for elemento in range(0,3):
    totalfaltascampeonato += sum(listajogo[elemento][2])

faltasBrasil = listajogo[0][2][0] + listajogo[1][2][0]
faltasItalia = listajogo[0][2][1] + listajogo[2][2][0]
faltasEspanha = listajogo[1][2][1] + listajogo[2][2][1]

totalfaltasportime = [["Brasil", faltasBrasil],["Itália", faltasItalia],["Espanha",faltasEspanha]]

indicemenor = totalfaltasportime.index(min(totalfaltasportime))
indicemaior = totalfaltasportime.index(max(totalfaltasportime))

print("O total de faltas cometidas no campeonato foi:", totalfaltascampeonato,"\nTime que fez mais faltas:", totalfaltasportime[indicemaior][0], "\nTime que fez menos faltas:", totalfaltasportime[indicemenor][0])