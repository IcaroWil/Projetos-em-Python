menu = int(input('O que você gostaria de fazer?\n1. Criar um arquivo\n2. Adicionar dados a um arquivo\n3. Sobrescrever um arquivo\n4. Limpar um arquivo'))
name = input('Digite o nome do arquivo:\n')

if menu != 4:
    data = input('Digite os dados que deseja inserir no arquivo:\n')
if menu == 1:
    with open(f'{name}.txt','w') as f:
        f.write(data)
elif menu == 2:
    with open(name,'a') as f:
        f.write(data)
elif menu == 3:
    with open(name,'w') as f:
        f.write('')

print('Obrigado por utilizar nosso programa!')
        