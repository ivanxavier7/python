# Permutações

# Elementos     1 - 2 - 3 - 4
# Permutações   1 - 2 - 6 - 24

# 1

# 1 - 2
# 2 - 1

# 1 - 2 - 3
# 1 - 3 - 2
# 2 - 1 - 3
# 2 - 3 - 1
# 3 - 2 - 1
# 3 - 1 - 1

# 1 - 2 - 3 - 4
# 1 - 2 - 4 - 3
# 1 - 3 - 2 - 4
# 1 - 3 - 4 - 2
# 1 - 4 - 3 - 2
# 1 - 4 - 2 - 3
# 2 - 1 - 3 - 4
# 2 - 1 - 4 - 3
# 2 - 3 - 1 - 4
# 2 - 3 - 4 - 1
# 2 - 4 - 3 - 1
# 2 - 4 - 1 - 3
# 3 - 2 - 1 - 4
# 3 - 2 - 4 - 1
# 3 - 1 - 2 - 4
# 3 - 1 - 4 - 2
# 3 - 4 - 1 - 2
# 3 - 4 - 2 - 1
# 4 - 2 - 3 - 1
# 4 - 2 - 1 - 3
# 4 - 3 - 2 - 1
# 4 - 3 - 1 - 2
# 4 - 1 - 3 - 2
# 4 - 1 - 2 - 3
# Recolhemos o primeiro bloco com a coluna igual a "1"
# Quando alteramos a coluna para outro numero, por exemplo dois
# Temos de alterar todos os bits do bloco "1" com os valores = 2 para 1

# 1 = 1
# 2*1 = 2
# 3*2*1 = 6
# 4*3*2*1 = 24
# n! = n*(n-)*...*2*1

import cProfile     # Usado para estrair estatisticas das partes do codigo a serem usadas
from itertools import permutations

my_list = [1, 2, 3, 4, 5, 6, 7]
list_of_permutations = permutations(my_list)
cnt = 0
for permutation in list_of_permutations:
    #print(permutation)
    cnt += 1

print(len(my_list), cnt)


def faculty(n):
    if n <= 1:
        return n
    else:
        return faculty(n-1)*n


def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt


for i in range(10):
    print(faculty(i))
# A inteção de extrair estatistica da recursividade é encontrar números mais prováveis de serem usados na chave
cProfile.run("counter(faculty(11))")

