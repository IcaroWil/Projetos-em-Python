import random

# # Criando uma variável chamada 'abc' com a string de letras minúsculas do alfabeto
abc = 'abcdefghijklmnopqrstuvwxyz'

# # Criando uma variável chamada 'extras' com a string de caracteres especiais
extras = '0123456789_!*&$%@?>.'

nova_senha = '' # String vazia 

## Definindo o tamanho da senha desejada em 16 caracteres
for i in range(16): 
    x = random.randint(1,2)
    if x == 1:
        nova_senha += random.choice(abc)
    else:
        nova_senha += random.choice(extras)

# Mostra a senha gerada
print(nova_senha)