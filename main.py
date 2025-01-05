from random import randrange

"""
Сценарій програми
Ваше завдання — написати просту програму, яка ніби грає з користувачем у хрестики-нулики. Щоб вам було легше, ми вирішили спростити гру. Ось наші припущення:

комп'ютер (тобто ваша програма) має грати в гру за 'X';
користувач (наприклад, ви) має грати в гру, використовуючи 'O';
перший хід належить комп’ютеру − він завжди ставить свій перший 'X' посередині дошки;
усі квадрати пронумеровані послідовно рядок за рядком, починаючи з 1 (для довідки перегляньте приклад нижче)
користувач робить свій хід, вводячи номер вибраного ним квадрата − число має бути дійсним, тобто воно повинно бути цілим та бути більше 0 і менше 10, також не можна вказувати на квадрат, який вже зайнятий;
програма перевіряє, чи закінчилася гра − є чотири можливих вердикти: гра має продовжуватися, гра закінчується нічиєю, ви виграли або виграв комп’ютер;
комп'ютер відповідає своїм ходом і перевірка повторюється;
не впроваджуйте жодної форми штучного інтелекту − для гри достатньо, щоб комп'ютер робив випадковий вибір квадрата.

"""

"""
Вимоги
Реалізуйте наступні функції:

дошка повинна зберігатися у вигляді триелементного списку, тоді як кожен елемент є ще одним список із трьох елементів (внутрішні списки являють собою рядки), 
так щоб усі квадрати могли бути доступні за допомогою наступного синтаксису:

    board[row][column]
    
* кожен з елементів внутрішнього списку може містити 'O', 'X' або цифру, яка відповідає номеру квадрата (такий квадрат вважається вільним)
* зовнішній вигляд дошки повинен бути точно таким, як і у наведеному прикладі.
* реалізувати функції, які наведені у редакторі.
"""

def display_view_board():
    print("+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board[0][0], " " + "  |   ",
          board[0][1], " " + "  |   ", board[0][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board[1][0], " " + "  |   ",
          board[1][1], " " + "  |   ", board[1][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board[2][0], " " + "  |   ",
          board[2][1], " " + "  |   ", board[2][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+"
          )

def display_board(board):
    board[1][1] = "X"
    display_view_board()
    return board
    # Функція приймає один параметр, що містить поточний статус дошки
    # і виводить його на консоль.



def enter_move(board):
    print("Тепер ваша черга ходити. Виберіть число від 1 до 9 (врахуйте зайняті клітинки).")

    while True:
        try:
            number = int(input("Введіть число: "))
        except ValueError:
            print("Це не є числом!")
            continue

        for i in range(len(board)):
            for j in range(len(board[i])):
                if number == board[i][j]:
                    board[i][j] = "0"
                    return board
        else:
            print("Цей квадрат вже зайнятий!")

    # Функція приймає поточний статус дошки, запитує користувача про його хід,
    # перевіряє введення та оновлює дошку відповідно до рішення користувача.



# def make_list_of_free_fields(board):
#     # Функція перевіряє дошку та створює список усіх вільних квадратів;
#     # список складається з кортежів, так що кожен кортеж є парою номерів рядка і стовпчика.
#
#

def winner_for(board):

    count_0 = 0
    count_X = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "0":
                count_0 += 1
                if count_0 == 3:
                    return "Гравець виграв"
            elif board[i][j] == "X":
                count_X += 1
                if count_X == 3:
                    return "Комп'ютер виграв"
        count_0 = 0
        count_X = 0

    for count_column in range(len(board[0])):  # Ітерація по колонках
        for i in range(len(board)):  # Ітерація по рядках
            if board[i][count_column] == "0":
                count_0 += 1
                if count_0 == 3:
                    return "Гравець виграв"
            elif board[i][count_column] == "X":
                count_X += 1
                if count_X == 3:
                    return "Комп'ютер виграв"
        count_0 = 0
        count_X = 0

    for i in range(len(board)):
        if board[i][i] == "0":
            count_0 += 1
            if count_0 == 3:
                 return "Гравець виграв"
        elif board[i][i] == "X":
            count_X += 1
            if count_X == 3:
                return "Комп'ютер виграв"
        count_0 = 0
        count_X = 0

    count_column = 2
    for i in range(len(board)):
        if board[i][count_column] == "0":
            count_0 += 1
            if count_0 == 3:
                return "Гравець виграв"
            count_column -= 1
        elif board[i][count_column] == "X":
            count_X += 1
            if count_X == 3:
                return "Комп'ютер виграв"
            count_column -= 1
        elif board[i][count_column] != "0" or board[i][count_column] != "X":
            count_column -= 1
        count_0 = 0
        count_X = 0

    # Функція аналізує стан дошки, щоб перевірити, чи
    # э в грі переможець



def draw_move(board):

    while True:
        number = randrange(1,10)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if number == board[i][j]:
                    board[i][j] = "X"
                    return board

    # Функція малює хід комп'ютера та оновлює дошку.

while True:

    board = [] # Основний список для масиву 3x3

    for i in range(3):
        start_ = i * 3 + 1
        end_ = start_ + 3
        row = []
        for j in range(start_, end_):
            row.append(j)
        board.append(row)

    choose_status = " "
    while True:
        print("\nДавайте зіграємо в гру. Для початку гри введіть 'Yes'. Для виходу з програми введіть 'No'.")
        choose_status = input("Введіть вашу відповідь: ")

        if choose_status == "Yes":
            break
        elif choose_status == "No":
            break

    print("\nПочатковий вигляд сітки для гри\n")
    display_view_board()
    print("\nПерший хід за комп'ютером\n")

    modify_border = []
    while True:
        modify_border = display_board(board)
        status_game = winner_for(modify_border)
        if status_game == "Гравець виграв":
            print("Гравець виграв")
            break
        elif status_game == "Комп'ютер виграв":
            print("Комп'ютер виграв")
            break
        modify_border = enter_move(modify_border)
        status_game = winner_for(modify_border)
        if status_game == "Гравець виграв":
            print("Гравець виграв")
            break
        elif status_game == "Комп'ютер виграв":
            print("Комп'ютер виграв")
            break
        modify_border = draw_move(modify_border)
        if status_game == "Гравець виграв":
            print("Гравець виграв")
            break
        elif status_game == "Комп'ютер виграв":
            print("Комп'ютер виграв")
            break



