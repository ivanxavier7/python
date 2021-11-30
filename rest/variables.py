x = 15
price = 9.99
discount = 0.2
result = price * (1 - discount)
print(result)
print("TESTE:{:.2f}:TESTE".format(result))
print(f"TESTE:{result}:TESTE")

l = ["Bob", "Rolf", "Anne"]     # Mantém a ordem dos elementos e pode adicionar e remover
t = ("Bob", "Rolf", "Anne")     # Mantém a ordem e não deixa remover nem adicionar
s = {"Bob", "Rolf", "Anne"}     # Altera a ordem ao adicionar ou remover e não permite repetidos

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(f"This is de fifference: {local_friends}")
union_friends = friends.union(abroad)
print(f"This is the union: {union_friends}")
intersect_friends = friends.intersection(abroad)
print(f"This is the intersection: {intersect_friends}")


friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
print(friends == abroad) # True
print(friends is abroad) # False - Porque usa um registo de memória diferente
print("Registo na memória:" + id(friends) + "----" + id(abroad))

friends = {"Rolf", "Bob"}
if "Rolf" in friends:
    print("Existe")


# Aplicação simples de "in" com tuple

number = 7
print("Adivinhe o Número!")
user_input = input("Introduza 'y' para começar a jogar: ").lower()
while user_input != "n":
    user_number = int(input("Adivinhe o número: "))
    if user_number == number:
        print("Acertou!")
        break
    elif number - user_number in (1, -1): # Aplicação (mais usado para múltiplos elementos)
        print("Falhou por um!")
    elif abs(number - user_number) == 2:  # Equivalente com absoluto
        print("Falhou por dois!")
    else:
        print("Tente novamente!")
    user_input = input("'y' para jogar novamente: ").lower()
    
    
friends = ["Bob", "Rolf", "Anne", "Jon", "Thomas"]

for friend in friends:
    print(f"{friend} is my friend")
    
numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]
somatorio_numeros = sum(numeros)
quantidade_numeros = len(numeros)
print(f"Soma: {somatorio_numeros} Quantidade: {quantidade_numeros}")

dobro_numberos = [nr * 2 for nr in numeros]

# List Comprehension 
comeca_J = [friend for friend in friends if friend.startswith("J")]

