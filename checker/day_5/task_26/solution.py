import sys

# Строки, Столбцы
N, M = tuple(map(int, sys.stdin.readline().strip().split()))
# Матрица значений
data = tuple(tuple(map(int, row.split())) for row in sys.stdin.readlines())

# Инициализируем поле нулевых значений
dp = [[0]*M for _ in range(N)]
# Цена начальной клетки
dp[0][0] = data[0][0]

for i in range(1, N):
  # Рассчет 0 строки/столбца можно было вынести в отдельные циклы
  # Рассчитываем граничные значения (первый столбец)
  dp[i][0] = dp[i-1][0]+data[i][0]
  for j in range(1, M):
    # Рассчитываем граничные значения (первую строку)
    dp[0][j] = dp[0][j-1]+data[0][j]

    # Рассчитываем ценность внутренник клеток
    dp[i][j] = min(dp[i][j-1], dp[i-1][j])+data[i][j]


print(dp[-1][-1])
