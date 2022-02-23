# O que é uma lista?
# Uma lista é uma estrutura de dados composta por elementos, ou seja,
# é uma sequência ou coleção ordenada de valores sendo que cada valor
# na lista é identificado por um índice.

# - Defina uma list

# lista vazia
empty_list = []            

# lista contendo 3 strings
beatles = ["john", "ringo", "seb"]

# lista contendo dados diferentes
my_list = [1, True, "string", 3.4]

# Acessar um elemento utilizando indexes
beatles = ["john", "ringo", "seb"]
beatles[0]  #=> "john"
beatles[2]  #=> "seb"
# beatles[8]  #=> breaks!!

# indexes começam no 0
beatles = ["john", "ringo", "seb"]
# index =>    0       1       2

# print(beatles[8])


# - Modifique um elemento
beatles = ["john", "ringo", "seb"]
beatles[2] = "george"
print(beatles)    # => ["john", "ringo", "george"]

# Adicione um elemento
beatles = ["john", "ringo", "george"]
beatles.append("paul")
print(beatles)    # => ["john", "ringo", "george", "paul"]

# - Delete um elemento
# Você pode remover todos os itens da lista com clear()
beatles.clear()
print(beatles)

# Você pode remover o item na posição especificada e obter seu valor com pop()
print(beatles.pop(1))
print(beatles)

# Você pode remover qualquer elemento da lista com remove()
print(beatles)
beatles.remove("george")
print(beatles)

# Você também pode remover elementos de uma lista com o comando del passando o index.
print(beatles)
del beatles[1]
print(beatles)

# - Iterando sobre uma lista
# A iteração tem o objetivo de percorrer os elementos contidos numa lista.

for beatle in beatles:
  print(f"- {beatle}")

for number in [1, 2, 3, 4, 5]:
  print(number * 10)

# Então com tudo isso em mente, vamos a um cenário simples:

students = ['Mary', 'Peter', 'Lilly', 'Andy']
favorite_foods = ["Pizza", "Pasta", "Sandwiches", "Salad"]

# Gostaríamos de imprimir o nome do aluno e sua comida favorita, assim:

# Mary gosta de comer Pizza
# Peter gosta de comer Pasta
# etc...

# Se tivéssemos apenas listas, o código seria algo assim:

for index, student in enumerate(students):
  print(f"{student} likes to eat {favorite_foods[index]}")

# E se alguém inserir outro aluno, mas não tiver
# informações sobre sua comida favorita:

students = ['Laura', 'Mary', 'Peter', 'Lilly', 'Andy']
favorite_foods = ["Pizza", "Pasta", "Sandwiches", "Salad"]

# print(favorite_foods['Mary']) # ==> "Pizza"