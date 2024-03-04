import random 

#  Lista com as letras do alfabeto em minúsculas e um espaço vazio
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
#  String de entrada de texto
text = input('enter text:\n')

# Variáveis para percorrer o texto
x = 0
y = 1

# Variável para armazenar a nova palavra criptografada
new_word = ''

# Lista para armazenar o deslocamento aleatório de cada caractere
secret = []

# Número de caracteres no texto
text_length = len(text)

# Loop para percorrer o texto
for i in range(text_length):
    shift = random.randint(1,27) # Gera um deslocamento aleatório entre 1 e 27
    secret.append(shift) # Adiciona o deslocamento aleatório à lista
    character = text[x:y] # Obtém o caractere atual no texto
    if character not in abc:
        new_word += character # Adiciona o caractere não-alfabético à nova palavra
    place = abc.index(character) 
    x += 1 
    y += 1
    for move in range(shift): # Realiza o deslocamento no alfabeto
        letter_hold = abc[0]
        abc.pop(0)
        abc.append(letter_hold)
    new_char = abc[place]
    new_word += new_char

print(new_word) # Imprime a nova palavra criptografada
print(secret) # Imprime a lista com os deslocamentos aleatórios