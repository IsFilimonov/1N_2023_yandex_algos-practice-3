import sys


def grasshopper(n: int, k: int) -> int:
    # Чтобы понять сколько констант есть для первых k случаев, обратимся не к
    # разбиению натурального числа, а к композиции натурального числа, тк
    # композиция не учитывает порядок. 
    # Подробнее:
    # https://ru.wikipedia.org/wiki/Разбиение_числа
    # https://ru.wikipedia.org/wiki/Композиция_числа
    dp = [0, 1] + [2**(k-1) for k in range(2, k+1)] + [0]*(N-k-1)

    # 1 клетка (хотя мы, вроде, на ней и стоим, но можем не прыгать)
    if n == 1:
        return 1

    # Случаи, когда можно перепрыгнуть за 1 ход
    if n <= k:
        return dp[n-1]

    # Все остальные случаи
    for i in range(k+1, n):
        step = k

        while step > 0:
            # Суммируем k предыдущих вариантов, чтобы получить i-ый
            dp[i] += dp[i-step]
            step -= 1

    return dp[-1]

N, k = tuple(map(int, input().strip().split()))

print(grasshopper(N,k))
