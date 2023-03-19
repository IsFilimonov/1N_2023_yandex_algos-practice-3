def find_best(matrix: list[tuple[int]]) -> int:
    """Заполняем расстояния до кормушки.

    Args:
        adj_list (dict): Список смежночти (ходов конем).
        matrix (list[tuple[int]]): Матрица координат начальных положений блох.

    Returns:
        int: Сумма действий (волн) всех блох до целевой координаты.
    """

    visited = set()
    # queue = {0: deque()}
    queue = {0:[]}

    visited.add((S, T),)
    queue[0].append((S, T))

    wave = 0
    result = 0  # сумма вместе с целевым элементом: кормушкой
    total = Q-1 if (S, T) in matrix else Q  # количество обработанных блох

    mx = max(N, M)  # будем двигаться по самой длинной из осей

    while wave <= mx:
        # оптимизация по памяти
        # добавляем следующую волну (очередь)
        # queue[wave+1] = deque()
        queue[wave+1] = []

        while queue[wave]:
            vertex = queue[wave].pop()

# Оптимизируем по памяти. Имитируем список смежности.
# Всего 8 потенциальных соседей.
# Важно отметить, что мы генерируем все возможные варианты, тк если блохи нет
# в какой-то клетке, то не значит, что другая блоха не может воспользоваться
# этой клеткой. Фильтрацию будем выполнять на конечном этапе.
            r,c = vertex

            w1 = (r-2, c+1) if 1 <= r-2 <= N and 1 <= c+1 <= M else None  # час
            w2 = (r-1, c+2) if 1 <= r-1 <= N and 1 <= c + \
                2 <= M else None  # 2 часа
            w4 = (r+1, c+2) if 1 <= r+1 <= N and 1 <= c + \
                2 <= M else None  # 4 часа
            w5 = (r+2, c+1) if 1 <= r+2 <= N and 1 <= c + \
                1 <= M else None  # 5 часов
            w7 = (r+2, c-1) if 1 <= r+2 <= N and 1 <= c - \
                1 <= M else None  # 7 часов
            w8 = (r+1, c-2) if 1 <= r+1 <= N and 1 <= c - \
                2 <= M else None  # 8 часов
            w10 = (r-1, c-2) if 1 <= r-1 <= N and 1 <= c - \
                2 <= M else None  # 10 часов
            w11 = (r-2, c-1) if 1 <= r-2 <= N and 1 <= c - \
                1 <= M else None  # 11 часов

            row = (w1, w2, w4, w5, w7, w8, w10, w11)

            for neighbour in (el for el in row if el):
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue[wave+1].append(neighbour)

                    # оптимизация по памяти, прощай наглядность
                    # waves[neighbour] = wave+1

                    if neighbour in matrix:
                        total -= 1
                        result += wave+1

        del queue[wave]  # удаляем текущую пустую волну (очередь)

        wave += 1

    if total > 0:
        return -1
    else:
        return result


# N,M: размер доски (с 1)
# S,T: координаты кормушки (row,col)
# Q: количество блох на доске
N, M, S, T, Q = input().strip().split()
N, M, S, T, Q = int(N), int(M), int(S), int(T), int(Q)

matrix = set()  # сет координат блох

for el in ((int(x) for x in input().strip().split()) for _ in range(Q)):
    matrix.add(tuple(el),)

answer = find_best(matrix)

print(answer)
