"""
~~~~~ Сценарій програми ~~~~

    Ваше завдання — написати просту програму, яка ніби грає з користувачем у хрестики-нулики.
    Щоб вам було легше, ми вирішили спростити гру. Ось наші припущення:

    *комп'ютер (тобто ваша програма) має грати в гру за 'X';
    *користувач (наприклад, ви) має грати в гру, використовуючи 'O';
    * перший хід належить комп’ютеру − він завжди ставить свій перший 'X' посередині дошки;
    * усі квадрати пронумеровані послідовно рядок за рядком, починаючи з 1 (для довідки
    перегляньте приклад нижче);
    * користувач робить свій хід, вводячи номер вибраного ним квадрата − число має бути дійсним,
    тобто воно повинно бути цілим та бути більше 0 і менше 10, також не можна вказувати на
    квадрат, який вже зайнятий;
    * програма перевіряє, чи закінчилася гра − є чотири можливих вердикти: гра має продовжуватися,
    гра закінчується нічиєю, ви виграли або виграв комп’ютер;
    * комп'ютер відповідає своїм ходом і перевірка повторюється;
    * не впроваджуйте жодної форми штучного інтелекту − для гри достатньо, щоб комп'ютер робив
    випадковий вибір квадрата.


~~~~ Вимоги до реалізації ~~~~~

    Реалізуйте наступні функції: дошка повинна зберігатися у вигляді триелементного списку, тоді як
    кожен елемент є ще одним список із трьох елементів (внутрішні списки являють собою рядки), так щоб
    усі квадрати могли бути доступні за допомогою наступного синтаксису:

        board[row][column]
    
    * кожен з елементів внутрішнього списку може містити 'O', 'X' або цифру, яка відповідає номеру
    квадрата (такий квадрат вважається вільним);
    * зовнішній вигляд дошки повинен бути точно таким, як і у наведеному прикладі;
    * реалізувати функції, які наведені у редакторі.
"""

from random import randrange

def display_board(board):
        print("+-------" * 3,"+", sep="")
        for row in range(3):
                print("|       " * 3,"|", sep="")
                for col in range(3):
                        print("|   " + str(board[row][col]) + "   ", end="")
                print("|")
                print("|       " * 3,"|",sep="")
                print("+-------" * 3,"+",sep="")


def enter_move(board):
    ok = False
    while not ok:
        move = input("Введіть свій хід: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'
        if not ok:
            print("Невдалий хід - повторіть введення даних!")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row ][col]
        ok = sign not in ['O','X']
        if not ok:
            print("Поле вже зайнято - повторіть введення!")
            continue
    board[row][col] = 'O'


def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['O','X']:
                free.append((row,col))
    return free


def victory_for(board,sgn):
    if sgn == "X":
        who = 'me'
    elif sgn == "O":
        who = 'you'
    else:
        who = None
    cross1 = cross2 = True
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:
            return who
        if board[rc ][rc] != sgn:
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)
    cnt = len(free)
    if cnt > 0:
        this = randrange(cnt )
        row, col = free[this]
        board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = 'X'
free = make_list_of_free_fields(board)
human_turn = True
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board,'O')
    else:
        draw_move(board)
        victor = victory_for(board,'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("Ви виграли!")
elif victor == 'me':
    print("Я виграв!")
else:
    print("Нічия!")