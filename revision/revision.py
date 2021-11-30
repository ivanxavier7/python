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
print(f"Registo na memória: {id(friends)} ------ {id(abroad)}")

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

friends_ages = [
    {"name": "Rolf", "age": 24},
    {"name": "Ivan", "age": 27},
    {"name": "Anne", "age": 12}
]
print(f"Aceder a dicionários dentro de listas: {friends_ages[1]['name']}")

friends_weight = {"Rolf": 96, "Ivan":83, "Anne": 58}

for friend, weight in friends_weight.items():
    print(f"Amigo: {friend} Peso: {weight}")

friends_values = friends_weight.values()    #Extrair os valores do dicionário
print(friends_values)
print("Média: " + str(sum(friends_values) / len(friends_values)))
print(list(friends_weight.items())) #Devolve uma lista com tuples
#Descontruir variaveis - Descontruct
t = 5, 10
x, y = t

friends = [("Ivan", 27, "Programador"), ("Rolf", 24, "Operário"), ("Anne", 12, "Estudante")]

for name, age, profession in friends:
    print(f"Nome: {name} Idade: {age} Profissão: {profession}")
# "_" Comunidade usa para dizer que nao vai usar essa variavel
for name, _, profession in friends:
    print(f"Nome: {name} Profissão: {profession}")

head, *tail = [1, 2, 3, 4, 5]
print(head)     # 1
print(tail)     # 2, 3, 4, 5

*head, tail = [1, 2, 3, 4, 5]
print(*head)    # 1, 2, 3, 4
print(tail)     # 5

def simple_function(x=100, y=10):
    #pass
    result = x + y
    print(f"Hello World, resultado: {result}")

simple_function(5, 10)
simple_function()   # Default Values
#Recolhe os parametros por ordem, mas se podem ser definidos
simple_function(x=2, y=3)   # Podemos misturar posicao com os definidos manualmente

def function_return(x=123, y=321):
    result = x + y
    return f"Hello World, resultado: {result}"

print(f"String devolvida com return:{function_return()}")

# Lambda functions
lambda_function = lambda x, y: x+y 
print(f"Funcao Lambda: {lambda_function(7, 8)}")
# Inline
print((lambda  x, y: x + y)(8,9))


def double(x):
    return x*2

sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = list(map(double, sequence))      #Equivalente com Map
print(doubled)
doubled = list(map(lambda x: x * 2, sequence))  # Equivalente em lambda

def login():
    users = [
    (0, "Bob", "password"),
    (1, "Ivan", "secreta"),
    (2, "Atum", "pescado"),
    (3, "Tomate", "colhido")
        ]
    username_mapping = {user[1]: user for user in users}    # Usa o username para criar um dicionario
    print(username_mapping)
    print(username_mapping['Ivan'])

    # Aplicacao em login do mapeamento
    username_input = input("Enter your username: ")
    password_input = input("Enter your password: ")
    _, username, password = username_mapping[username_input]
    if password_input == password:
        print("Credenciais corretas!")
    else:
        print("Credenciais erradas!")

#login()

# Multiple args
def multiply(*args):
    total = 1
    for arg in args:
        total *= arg
    return total

print(multiply(2, 4, 2))

nums = [3, 5]
print(multiply(*nums))

def add(x, y):
    return x + y
nums = {"x":15, "y":25}
print(add(x=nums["x"], y=nums["y"]))
print(add(**nums))  # Equivalente ao que esta em cima, passa cada chave para a funcao porque o mesmo valor x e y

def apply(*args, operator): # passo o que quiser e no final temos de ter um operador
    if operator == "*":
        return(multiply(*args)) # * para passar o interior do tuple e nao o tuple
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply"

print(apply(1, 3, 6, 7, operator="*"))

def named(**kwargs):
    print(kwargs)

details = {"name":"Bob", "age":25}

named(**details)

def print_named(**kwargs):
    for arg, value in kwargs.items():
        print(f"Argumento: {arg} Valor: {value}")

print_named(**details)
print_named(name="Bob", age=25)

def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)
