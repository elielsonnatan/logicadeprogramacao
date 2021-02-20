import math

def calculahipotenusa (cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    print("O valor da hipotenusa é:", hipotenusa)

cateto1 = input("Digite o valor do cateto 1: ")
cateto1 = float(cateto1)
cateto2 = input("Digite o valor do cateto 2: ")
cateto2 = float(cateto2)

calculahipotenusa(cateto1, cateto2)