from collections import deque


def fill_adjacency_list() -> dict[int: list[int]]:
    """Заполняем список смежности из матрицы смежности.

    Returns:
        dict[int: list[int]]: Список смежности
    """
    adj_matrix = tuple()  # матрица смежности
    adj_list = {k: [] for k in range(1, N+1)}  # список смежности

    # Создаем генератор пар - так быстрее
    for el in ((int(x) for x in input().strip().split()) for _ in range(N)):
        adj_matrix += (list(el),)

    # Дан неориентированный граф, значит матрица симметрична
    for i in range(len(adj_matrix)):
        neighbors = tuple()
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] == 1:
                neighbors += (j+1,)
        adj_list[i+1] = neighbors

    return adj_list


def find_shortcut(adj_list, start, end) -> tuple[int, dict[int:int]]:
    """Поиск кратчайшего пути.

    Returns:
        tuple[int, dict[int:int]]: Длина кратчайшего пути и сам путь
    """
    def path_decode(d: dict[int:int], start: int, end: int) -> list[int]:
        """_summary_

        Args:
            d (dict[int:int]): Словарь предыдущих вершин.
            start (int): Начальная вершина.
            end (int): Конечная вершина.

        Returns:
            list[int]: Расшифрованный путь.
        """
        answer = []  # последовательност пути
        position = end  # разворачиваем клубок с конца

        while position != start:
            answer.append(position)
            position = d[position]

        answer.append(start)  # не забываем и про начальную вершину

        return answer[::-1]  # реверс
    
    # В списке смежности пусто, значит пути нет
    if len(adj_list[start]) == 0 or len(adj_list[end]) == 0:
        return None, [-1]
    elif start == end:  # вершина сама в себя
        return 0, None

    visited = set()  # множество посещенных вершин
    # волновая очередь для каждой волны соседей
    queue = {el: deque() for el in range(len(adj_list))}
    # словарь предыдущих вершин
    pathway = {el: -1 for el in range(1, len(adj_list))}

    # Инициализация первого обхода
    visited.add(start)
    queue[0].append(start)
    pathway[start] = 0  # у начального элемента нет предыдущего
    wave = 0  # Волна обхода соседей

    while wave <= N:

        while queue[wave]:
            vertex = queue[wave].popleft()

            for neighbour in adj_list[vertex]:
                if neighbour not in visited:
                    pathway[neighbour] = vertex  # фиксируем предыдущую вершину
                    if neighbour == end:
                        return wave+1, path_decode(pathway, start, end)
                    visited.add(neighbour)
                    queue[wave+1].append(neighbour)


        wave += 1


N = int(input().strip())  # число вершин в графе

adj_list = fill_adjacency_list()  # матрица смежности -> список смежности

# Начальная, конечная вершины
start, end = input().split()
start, end = int(start), int(end)

answer_len, answer_path = find_shortcut(adj_list, start, end)

if answer_len or answer_len == 0:
    print(answer_len)

if answer_path:
    print(" ".join(map(str,answer_path)))
