import random 
acertos  = 0

for i in range(10): # mostra quantas questões 
    num1, num2 = random.randint(1,100), random.randint(1,100)
    result = num1 + num2
    pergunta = int(input(f'Quanto é:\n\n{num1} + {num2}?\n'))
    if pergunta == result:
        print('Correto!')
        acertos  += 1
    else:
        print('Incorreto!')

print(f'Você acertou {acertos} questões!') # quantas foram corretas 
