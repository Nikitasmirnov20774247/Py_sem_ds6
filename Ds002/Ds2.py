# Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

# *Пример:* 

# 2+2 => 4; 

# 1+2*3 => 7; 

# 1-2*3 => -5;

try:
    def solution(num, coef):
        for i in range(len(num)):
            for j in range(len(coef)):
                if coef[j] == '*':
                    num[j] *= num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    break

            for j in range(len(coef)):
                if coef[j] == '/':
                    num[j] /= num[j + 1]
                    del num[j + 1]
                    del coef[j]
                    break

            for j in range(len(coef)):
                if coef[j] == '+' or coef[j] == '-':
                    if coef[j] == '+':
                        num[j] += num[j + 1]
                        del num[j + 1]
                        del coef[j]
                        break
                    elif coef[j] == '-':
                        num[j] -= num[j + 1]
                        del num[j + 1]
                        del coef[j]
                        break
        return num

    def print_result():
        str = input('Введите вырожение: ')
        lst = list(str)
        coef = []
        num = []
        for n in lst:
            if n.isdigit():
                num.append(int(n))
            else:
                coef.append(n)
        print(solution(num, coef))

    print_result()
except:
    ('!! Введите корректное вырожение !!')