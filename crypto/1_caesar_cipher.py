# Cifra de cesar
# Padrao:
# Alice Contem a mensagem       Possuí a chave 3
# Bob: Quer receber a mensagem  Possuí a chave 3
# Eve: Quer interceptar a mensagem
# Se chave = 3
# Altera três posições num alfabeto:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Para
# D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

# B R X     D U H       D Z H V R P H
# Y O U     A R E       A W E S O M E

def encryption_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    cnt = 0
    for char in letters:
        key[char] = letters[(cnt + n) % len(letters)]   # Gerar dicionario
        # print((cnt + n) % len(letters)) # Index
        cnt += 1
    return key


def decryption_key(key):
    dkey={}
    for char in key:
        dkey[key[char]] = char      # Traduz no dicionario
    return dkey


def encrypt(key, message):
    cipher = ""
    for char in message:
        if char in key:
            cipher += key[char]
        else:
            cipher += char  # Caso seja um espaço em branco adiciona na mesma
    return cipher


key = encryption_key(3)
print(key)

message = "YOU ARE AWESOME"
cipher = encrypt(key, message)
print(cipher)

dkey = decryption_key(key)
message = encrypt(dkey, cipher)
print(message)

# So existem 26 chaves por isso é fácil de partir,
# a segurança desta cifra baseava-se na segurança do algoritmo e não da chave.
# Principal erro ao criar uma cifra segura, o adversário não deve ganhar vantagem ao descobrir o algoritmo
print(cipher)
for i in range(26):
    dkey = encryption_key(i)
    message = encrypt(dkey, cipher)
    print(message)
