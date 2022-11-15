# Задача 1. Создайте программу для игры в "Крестики-нолики".

from random import randint

try:
    def creat_array():
        array = []
        for i in range(3):
            array2 = []
            for j in range(3):
                array2.append('-')
            array.append(array2)
        return array

    def print_array(array):
        for i in range(3):
            print(' '.join(array[i]))

    def chek_win(array):
        win = '-'
        for i in range(3):
            result = ''
            for j in range(3):
                result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result == 'OOO':
                win = 'O'
        result = ''
        for i in range(3):
            for j in range(3):
                if i == j:
                    result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result == 'OOO':
                win = 'O'
        result = ''
        for i in range(3):
            for j in range(3):
                if i + j == 2:
                    result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result == 'OOO':
                win = 'O'
        result = ''
        for i in range(3):
            for j in range(3):
                if j == 0:
                    result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result == 'OOO':
                win = 'O'
        result = ''
        for i in range(3):
            for j in range(3):
                if j == 1:
                    result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result == 'OOO':
                win = 'O'
        result = ''
        for i in range(3):
            for j in range(3):
                if j == 2:
                    result += array[i][j]
            if result == 'XXX':
                win = 'X'
            elif result=='OOO':
                win = 'O'
        return win

    table = creat_array()
    char = 'X'
    prob = '-'
    print('_Введите координаты ячейки_')
    while True:
        print_array(table)
        if char == 'X':
            row = int(input('Введите столбец (от 1 до 3): '))
            line = int(input('Введите строку (от 1 до 3): '))
            while row > 3 or line > 3 or row < 1 or line < 1:
                print('!! Введите корректное значение (от 1 до 3) !!')
                row=int(input('Введите столбец (от 1 до 3): '))
                line=int(input('Введите строку (от 1 до 3): '))
            while table[line-1][row-1] != prob:
                print('!! Выберете пустую ячейку !!')
                row = int(input('Введите столбец: '))
                line = int(input('Введите строку: '))
        if char == 'O':
            row = int(randint(1,3))
            line = int(randint(1,3))
            while table[line-1][row-1] != prob:
                row = int(randint(1,3))
                line = int(randint(1,3))
        table[line-1][row-1] = char
        if char == 'X':
            char = 'O'
        else:
            char='X'
        win = chek_win (table)
        if prob != win:
            print_array (table)
            print(f'Победил - {win}')
            break
except: 
    print('!! Введите целое число !!')