# Не проходит 8 тест по памяти: 65 mb

from collections import deque

# ### >>>>>>
# import debugpy
# debugpy.listen(5678)
# print("Waiting for debugger")
# debugpy.wait_for_client()
# ### <<<<<<

def fill_adjacency_list(N:int,M:int) -> dict[tuple[int]: tuple[int]]:
    """Заполняем список смежности по размерам поля.

    Соседями будут возможные ходы конем. Всего 8 потенциальных соседей.
    Важно отметить, что мы генерируем все возможные варианты, тк если блохи нет
    в какой-то клетке, то не значит, что другая блоха не может воспользоваться
    этой клеткой. Фильтрацию будем выполнять на конечном этапе.

    Returns:
        dict[tuple[int]: tuple[int|None]]: Список смежности.
    """
    # Список смежности для каждой прилегающей соседней клетки
    # adj_list = {}
    # for r in range(1, N+1):
    #     for c in range(1, M+1):
    #         # по часовой

    #         w15 = ((r-1),(c+1)) if 1<=r-1<=N and 1<=c+1<=M else None  # U+R
    #         w3 = ((r),(c+1)) if 1<=c+1<=M else None  # R
    #         w45 = ((r+1),(c+1)) if 1<=r+1<=N and 1<=c+1<=M else None  # D+R
    #         w6 = ((r+1),(c)) if 1<=r+1<=N else None  # D
    #         w75 = ((r+1),(c-1)) if 1<=r+1<=N and 1<=c-1<=M else None  # D+L
    #         w9 = ((r),(c-1)) if 1<=c-1<=M else None  # L
    #         w105 = ((r-1),(c-1)) if 1<=r-1<=N and 1<=c-1<=M else None  # L+U
    #         w12 = ((r-1),(c)) if 1<=r-1<=N else None  # U

    #         row = (w15, w3, w45, w6, w75, w9, w105, w12)
    #         adj_list[(r, c)] = row

    adj_list = {}

    for r in range(1,N+1):
        for c in range(1,M+1):
            # по часовой
            w1 = (r-2, c+1) if 1<=r-2<=N and 1<=c+1<=M else None  # час
            w2 = (r-1,c+2) if 1<=r-1<=N and 1<=c+2<=M else None # 2 часа
            w4 = (r+1,c+2) if 1<=r+1<=N and 1<=c+2<=M else None # 4 часа
            w5 = (r+2,c+1) if 1<=r+2<=N and 1<=c+1<=M else None # 5 часов
            w7 = (r+2,c-1) if 1<=r+2<=N and 1<=c-1<=M else None # 7 часов
            w8 = (r+1,c-2) if 1<=r+1<=N and 1<=c-2<=M else None # 8 часов
            w10 = (r-1,c-2) if 1<=r-1<=N and 1<=c-2<=M else None # 10 часов
            w11 = (r-2,c-1) if 1<=r-2<=N and 1<=c-1<=M else None # 11 часов

            row = (w1,w2,w4,w5,w7,w8,w10,w11)

            # Генератор без None позиций, чтобы не нагружать обход
            # Для наглядности тестирования можно обернуть в list, а так генератор быстрее
            adj_list[(r, c)] = (el for el in row if el)


    return adj_list


def find_best(adj_list: dict, matrix: list[tuple[int]]) -> int:
    """Заполняем расстояния до кормушки.

    Args:
        adj_list (dict): Список смежночти (ходов конем).
        matrix (list[tuple[int]]): Матрица координат начальных положений блох.

    Returns:
        int: Сумма действий (волн) всех блох до целевой координаты.
    """

    visited = set()
    # queue = {el: deque() for el in range(len(adj_list))},
    queue = {0: deque()}
    # waves = {k:-1 for k in adj_list.keys()}

    visited.add((S,T),)
    queue[0].append((S,T))

    wave = 0
    # waves[(S, T)] = wave

    mx = max(N, M)  # будем двигаться по самой длинной из осей
    
    result = 0  # сумма с 1 элементом
    total = Q-1 if (S,T) in matrix else Q  # количество обработанных блох

    while wave <= mx:
        # оптимизация по памяти
        # добавляем следующую волну (очередь)
        queue[wave+1] = deque()

        while queue[wave]:
            vertex = queue[wave].popleft()
            

            for neighbour in adj_list[vertex]:
                if neighbour not in visited and neighbour:
                    visited.add(neighbour)
                    queue[wave+1].append(neighbour)
                    
                    # оптимизация по памяти, прощай наглядность
                    # waves[neighbour] = wave+1

                    if neighbour in matrix:
                        total -= 1
                        result += wave+1

        del queue[wave]  # удаляем текущую пустую волну (очередь)
        wave += 1


    # Оставляем только тех блох, которые изначально заданы условием
    # Мы можем так поступить (тут, в конце), тк по пустым ячейкам блохи
    # передвигаться могут, иначе, надо было фильтровать ячейки на уровне
    # формирования списка смежности.
    # result = {k:v for k,v in waves.items() if k in matrix}
    # return -1 if -1 in result.values() else sum(result.values())

    # Экономим память. Проверяем, есть ли -1 среди элементов
    # result = 0
    # for k,v in waves.items():
    #     if k in matrix:
    #         if v == -1:
    #             return -1
    #         else:
    #             result+=v

    # return result

    if total>0:
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
    matrix.add(tuple(el))

# Сортировка по порядку: строки,столбцы
# Сортировка матрицы нужна для наглядного дебага
# matrix.sort(key=lambda x: (x[0], x[1]))

adj_list = fill_adjacency_list(N,M)

answer = find_best(adj_list, matrix)

print(answer)
