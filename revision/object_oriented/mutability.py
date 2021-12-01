a = []
b = a

print(id(a))
print(id(b))

a.append(35)    # aponta para o mesmo registo de memoria

print(a)
print(b)


a = []
b = []

print(id(a))
print(id(b))

a.append(35)    # aponta para um registo de memoria diferente

print(a)
print(b)

# Python recicla ints se forem iguais, quando diferirem cria um registo novo automaticamente

a = 1234
b = 1234
print(id(a))
print(id(b))
b = 0000
print(id(a))
print(id(b))
