import sys


def fill_table(dp):
    # Сначала заполняем первую строку
    for col in range(1, M):
        dp[0][col] = dp[0][col-1] + data[0][col]
    
    # Потом заполняе первый столбец
    for row in range(1, N):
        dp[row][0] = dp[row-1][0] + data[row][0]

    # Двигаемся к нижней крайней точке заполняя построчно
    for row in range(1, N):
        for col in range(1, M):
            dp[row][col] = max(dp[row][col-1], dp[row-1][col])+data[row][col]


def make_route():
    # i строка, j столбец
    row, col = N-1, M-1
    answer = []
    while row >= 0 and col >= 0:
        down = dp[row-1][col]
        right = dp[row][col-1]

        # Если уперлись в стену/потолок
        if row == 0:
            answer += ["R"] * col
            return answer
        if col == 0:
            answer += ["D"] * row
            return answer

        # Оставляем >= так как может быть развилка, а доп условий нет.
        if down >= right:
            answer.append("D")
            row -= 1
        else:
            answer.append("R")
            col -= 1

    return answer


# Строки, Столбцы
N, M = tuple(map(int, sys.stdin.readline().strip().split()))
# Матрица значений
data = tuple(tuple(map(int, row.split())) for row in sys.stdin.readlines())

dp = [[0]*M for _ in range(N)]  # Инициализируем поле нулевых значений

dp[0][0] = data[0][0]  # Цена начальной клетки

fill_table(dp)
        
print(dp[-1][-1])

if answer:= " ".join(make_route()[::-1]):
    print(answer)
