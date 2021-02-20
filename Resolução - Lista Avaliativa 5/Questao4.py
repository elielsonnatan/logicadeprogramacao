import Funcoes

valorgasto = input("Digite o valor gasto pelo cliente: ")
valorgasto = float(valorgasto)
print("\nInstruções: \n - Para pagamento à vista digite 1. \n - Para pagamento a prazo digite o número de parcelas.")
formadepagamento = input("\nDigite a forma de pagamento: ")
formadepagamento = int(formadepagamento)

while valorgasto <= 100.0 and formadepagamento >= 3:
        print("\nPara valor igual ou inferior a R$ 100,00 só é permitido pagamento à vista ou dividido em duas vezes.")
        valorgasto = input("Digite o valor gasto pelo cliente: ")
        formadepagamento = input("Digite a forma de pagamento: ")

Funcoes.formadepagamento(valorgasto, formadepagamento)