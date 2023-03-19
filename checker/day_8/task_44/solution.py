"""
Компилятор: Python 3.9 (PyPy 7.3.11)

допустим, что мы знаем радиус стола

построим граф, где вершинами будут
- левая и правая стенки коридора
- колонны

ребро между вершинами будет только в том случае, если между вершинами НЕЛЬЗЯ пронести круглую кровать

в таком случае кровать НЕЛЬЗЯ пронести по коридору, если существует путь от левой стенки до правой стенки по ребрам, которые я выше описал (подумайте почему)

заметим, что если мы можем пронести кровать с радиусом R, то и с радиусом < R можем

аналогично, если не можем с R, то и с > R не можем

получаем бинпоиск по радиусу, внутри которого проверяем связность между левой и правой стенками (dfs / bfs)
"""
from collections import deque
from math import sqrt


# Локально не отрабатывает блок чтения из файла, а в контесте работает
# with open('input.txt', 'r') as f_in:
#     lines = deque(
#         line.rstrip()
#         for line in f_in.readlines()
#     )

# Локальная альтернатива
import sys
lines = deque(line.rstrip() for line in sys.stdin.readlines())
#######################################################################



def read_line():
    return lines.popleft()


def read_int():
    return int(read_line())


def read_ints():
    return map(int, read_line().split())


xl, xr = read_ints()
radius = read_int()

n = read_int()
centers = [tuple(read_ints()) for _ in range(n)]

distances = [[0] * (n + 2) for _ in range(n + 2)]

left, right = n, n + 1

distances[left][right] = distances[right][left] = xr - xl
for i in range(n):
    xi, yi = centers[i]

    distances[i][left] = distances[left][i] = max(0.0, xi - radius - xl)
    distances[i][right] = distances[right][i] = max(0.0, xr - xi - radius)

    for j in range(n):
        xj, yj = centers[j]

        dx = xi - xj
        dy = yi - yj

        distances[i][j] = max(0.0, sqrt(dx * dx + dy * dy) - 2 * radius)


def can(diameter):
    used = [False] * len(distances)

    def dfs(v):
        used[v] = True
        for to, distance in enumerate(distances[v]):
            if used[to]:
                continue

            if distance >= diameter:
                continue

            dfs(to)

    dfs(left)
    return not used[right]


d_left, d_right = 0, distances[left][right]
for it in range(100):
    d_mid = (d_left + d_right) / 2

    if can(d_mid):
        d_left = d_mid
    else:
        d_right = d_mid

ans = int(d_left * 10 ** 4)
if ans % 10 >= 5:
    ans += 10

ans -= ans % 10
ans /= 10**4

print('{:.3f}'.format(ans))
