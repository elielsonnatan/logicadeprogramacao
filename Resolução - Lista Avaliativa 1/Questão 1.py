# a) Errado, 0.02 é um valor do tipo float.
print("0.02: ", type(0.02))

# b) Errado, -65.89 é sim um número real.

# c) Correto, "Maria" é uma string.
print("'Maria':", type("Maria"))

# d) Errado, 15 é um valor numérico do tipo inteiro.
print("15:", type(15))

# e) Errado, no python o valor lógico True é escrito com inicial maiúscula. Na forma apresentada no exercício 
# o compilador a entende como uma variável indefinida. E mesmo assim não teria como ser um conjunto de
# caracteres porque não está entre aspas. 
print("true:", type(true)) # Retorna um erro

# f) Errado, '2558' é uma string.
print("'2558':", type('2558'))

# g) Certo, "True" é uma string.
print("'True':", type("True"))

# h) Certo, "35.6003" é uma string.
print("'35.6003':", type("35.6003"))

# i) Errado, no python o valor lógico False é escrito com inicial maiúscula. Na forma apresentada no exercício
# o compilador a entende como uma variável indefinida. Entretanto, se fosse escrita com inicial maiúscula seria
# sim um valor lógico.
print("false:", type(false)) # retorna um erro