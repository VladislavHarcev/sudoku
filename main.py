from itertools import product
print("Правила ввода значений:\n", "1. Необходимо вводить данные судоку 9х9\n" " 2. Каждый новый элемент вводится через пробел (за исключением первого)\n", "3. После ввода всей строки длиной равной 9 нажмите ENTER\n","4. Пустые ячейки обозначаются нулем")
one = list(map(int, input("Введите 1-ю строку: ").split()))
two = list(map(int, input("Введите 2-ю строку: ").split()))
three = list(map(int, input("Введите 3-ю строку: ").split()))
four = list(map(int, input("Введите 4-ю строку: ").split()))
five = list(map(int, input("Введите 5-ю строку: ").split()))
six = list(map(int, input("Введите 6-ю строку: ").split()))
seven = list(map(int, input("Введите 7-ю строку: ").split()))
eight = list(map(int, input("Введите 8-ю строку: ").split()))
nine = list(map(int, input("Введите 9-ю строку: ").split()))
puzzle = [one, two, three, four, five, six, seven, eight, nine]
print("Ваше судоку:")
print('\n'.join(str(value) for value in puzzle))
def sudoku_solution(puzzle):
    for(row,col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0:
            for number in range(1,10):
                funct = True
                for i in range(0,9):
                    if (puzzle[i][col] == number) or (puzzle[row][i] == number):
                        funct = False
                        break
                for (i,j) in product(range(0,3), repeat = 2):
                    if puzzle[row-row%3 + i][col-col%3+j] == number:
                        funct = False
                        break
                if funct:
                    puzzle[row][col] = number
                    if trial := sudoku_solution(puzzle):
                        return trial
                    else:
                        puzzle[row][col] = 0
            return False
    return puzzle
sudoku_solution(puzzle)
print("Решение вашего судоку:")
print('\n'.join(str(value) for value in puzzle))