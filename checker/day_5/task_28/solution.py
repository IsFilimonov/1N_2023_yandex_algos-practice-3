import sys


def count_routes(N, M):
    # 0 индексы для разметки
    dp = [[0] * (M+1) for _ in range(N+1)]
    # начальная точка марщрута
    dp[1][1] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if i == 1 and j == 1:
                continue
            # Проверка, чтобы не выходить за границы области, 
            # чтобы не исп отрицательные индексы
            if i-2>=0 and i-1>=0 and j-2>=0 and j-1>=0:
                dp[i][j] = dp[i-2][j-1] + dp[i-1][j-2]
    return dp[N][M]
    # return dp


N, M = tuple(map(int, sys.stdin.readline().strip().split()))
print(count_routes(N, M))

# for row in count_routes(N, M):
#     print(row)