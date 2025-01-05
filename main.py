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

# Функція, що виводить поточний статус дошки.

#date: 05.01.2025
def display_view_board(board_):
    print("+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board_[0][0], " " + "  |   ",
          board_[0][1], " " + "  |   ", board_[0][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board_[1][0], " " + "  |   ",
          board_[1][1], " " + "  |   ", board_[1][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+" + "\n" + "|         " * 3 + "|" + "\n" + "|   ", board_[2][0], " " + "  |   ",
          board_[2][1], " " + "  |   ", board_[2][2], "   |" + "\n" + "|         " * 3 + "|" \
          + "\n" + "+---------" * 3 + "+"
          )

# Функція приймає один параметр, що містить поточний статус дошки
# і виводить його на консоль.

#date: 05.01.2025
def display_board(board_):
    board_[1][1] = "X"
    display_view_board(board_)
    return board_


# Функція приймає поточний статус дошки, запитує користувача про його хід,
# перевіряє введення та оновлює дошку відповідно до рішення користувача.

#date: 05.01.2025
def enter_move(board_):
    print("Тепер ваша черга ходити. Виберіть число від 1 до 9 (врахуйте зайняті клітинки).")

    while True:
        try:
            number = int(input("Введіть число: "))
        except ValueError:
            print("Це не є числом!")
            continue

        for row_ in range(len(board_)):
            for column in range(len(board_[row_])):
                if number == board_[row_][column]:
                    board_[row_][column] = "0"
                    return board_
        else:
            print("Цей квадрат вже зайнятий!")

# Функція аналізує стан дошки, щоб перевірити, чи
# э в грі переможець

#date: 05.01.2025
def winner_for(board_):

    for row_ in range(len(board_)):
        count_0 = 0
        count_x = 0
        for column in range(len(board_[row_])):
            if board_[row_][column] == "0":
                count_0 += 1
                if count_0 == 3:
                    return "Гравець виграв"
            elif board_[row_][column] == "X":
                count_x += 1
                if count_x == 3:
                    return "Комп'ютер виграв"

    for count_column in range(len(board_[0])):
        count_0 = 0
        count_x = 0
        for row_ in range(len(board_)):
            if board_[row_][count_column] == "0":
                count_0 += 1
                if count_0 == 3:
                    return "Гравець виграв"
            elif board_[row_][count_column] == "X":
                count_x += 1
                if count_x == 3:
                    return "Комп'ютер виграв"

    for row_ in range(len(board_)):
        count_0 = 0
        count_x = 0
        if board_[row_][row_] == "0":
            count_0 += 1
            if count_0 == 3:
                 return "Гравець виграв"
        elif board_[row_][row_] == "X":
            count_x += 1
            if count_x == 3:
                return "Комп'ютер виграв"

    count_column = 2
    for row_ in range(len(board_)):
        count_0 = 0
        count_x = 0
        if board_[row_][count_column] == "0":
            count_0 += 1
            if count_0 == 3:
                return "Гравець виграв"
            count_column -= 1
        elif board_[row_][count_column] == "X":
            count_x += 1
            if count_x == 3:
                return "Комп'ютер виграв"
            count_column -= 1
        elif board_[row_][count_column] != "0" or board_[row_][count_column] != "X":
            count_column -= 1

# Функція малює хід комп'ютера та оновлює дошку.

#date: 05.01.2025
def draw_move(board_):

    while True:
        number = randrange(1,10)

        for row_ in range(len(board)):
            for column in range(len(board[row_])):
                if number == board_[row_][column]:
                    board_[row_][column] = "X"
                    return board_

while True:
    # Основний список для масиву 3x3
    board = []

    for i in range(3):
        start_ = i * 3 + 1
        end_ = start_ + 3
        row = []
        for j in range(start_, end_):
            row.append(j)
        board.append(row)

    while True:
        print("\nДавайте зіграємо в гру. Для початку гри введіть 'Yes'. Для виходу з програми введіть 'No'.")
        choose_status = input("Введіть вашу відповідь: ")

        if choose_status == "Yes":
            break
        elif choose_status == "No":
            break

    print("\nПочатковий вигляд сітки для гри\n")
    display_view_board(board)
    print("\nПерший хід за комп'ютером\n")

    modify_border = []
    while True:
        modify_border = display_board(board)
        status_game = winner_for(modify_border)
        if status_game == "Гравець виграв":
            print("Гравець виграв")
            break
        if status_game == "Комп'ютер виграв":
            print("Комп'ютер виграв")
            break
        modify_border = enter_move(modify_border)
        status_game = winner_for(modify_border)
        if status_game == "Гравець виграв":
            print("Гравець виграв")
            break
        modify_border = draw_move(modify_border)
        if status_game == "Комп'ютер виграв":
            print("Комп'ютер виграв")
            break




