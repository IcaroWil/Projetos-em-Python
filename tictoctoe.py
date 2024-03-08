from random import randrange

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    ok = False  # Suposição falsa - precisamos dela para entrar no loop
    while not ok:
        move = input("Digite seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'  # A entrada do usuário é válida?
        if not ok:
            print("Má jogada – repita sua entrada!")  # Não, não é - faça a entrada novamente
            continue
        move = int(move) - 1  # Número de célula de 0 a 8
        row = move // 3  # Linha da célula
        col = move % 3  # Coluna da célula
        sign = board[row][col]  # Verifica o quadrado selecionado
        ok = sign not in ['O', 'X']
        if not ok:  # Está ocupado - pare a entrada novamente
            print("Campo já ocupado – repita sua entrada!")
            continue
    board[row][col] = 'O'  # Define 'O' no quadrado selecionado

def make_list_of_free_fields(board):
    free = []
    for row in range(3):  # Iterar pelas linhas
        for col in range(3):  # Iterar pelas colunas
            if board[row][col] not in ['O', 'X']:  # O celular está livre?
                free.append((row, col))  # Sim, é - anexe uma nova tupla à lista
    return free

def victory_for(board, sgn):
    if sgn == "X":  # Estamos procurando por X?
        who = 'me'  # Sim - é do lado do computador
    elif sgn == "O":  # ... ou para O?
        who = 'you'  # Sim - é o nosso lado
    else:
        who = None  # Não devemos cair aqui!
    cross1 = cross2 = True  # Para diagonais
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # Verifica a linha rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # Verifica a coluna rc
            return who
        if board[rc][rc] != sgn:  # Verifica a 1ª diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # Verifica a segunda diagonal
            cross2 = False
    if cross1 or cross2:
        return who
    return None

def draw_move(board):
    free = make_list_of_free_fields(board)  # Faça uma lista de campos livres
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'

# Inicialização do tabuleiro
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
board[1][1] = 'X'  # Coloca primeiro 'X' no meio
free = make_list_of_free_fields(board)
human_turn = True  # Que turno é agora?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("Você ganhou!")
elif victor == 'me':
    print("Eu ganhei")
else:
    print("Empate!")
