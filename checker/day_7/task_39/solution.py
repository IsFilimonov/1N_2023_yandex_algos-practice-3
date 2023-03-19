def find_best(matrix, s_idx):
    visited = set()  # посещенные позиции
    queue = {0:[]}  # очередь

    visited.add(s_idx,)  # помечаем стартовую позицию посещенной
    queue[0].append(s_idx)  # начинаем BFS со стартовой позиции

    wave = 0  # волны/шаги до цели
    neighbours = []  # массив соседей (варианты движения ограничены)

    while wave <= N*N*N:  # N*N было недостаточно
        queue[wave+1] = []

        while queue[wave]:
            vertex = queue[wave].pop()

            # [l]evel
            # [b]lock
            # [p]osition
            # matrix[l][b][p]
            l,b,p = vertex

            # tuple(map(lambda x: x in range(10),(a,b,c)))
            # север
            w1 = (l,b-1,p) if 0<=p<N and 0<=b-1<N and 0<=l<N else None
            # восток
            w2 = (l,b,p+1) if 0<=p+1<N and 0<=b<N and 0<=l<N else None
            # юг
            w3 = (l,b+1,p) if 0<=p<N and 0<=b+1<N and 0<=l<N else None
            # запад
            w4 = (l,b,p-1) if 0<=p-1<N and 0<=b<N and 0<=l<N else None
            # вверх
            w5 = (l-1,b,p) if 0<=p<N and 0<=b<N and 0<=l-1<N else None
            # вниз
            w6 = (l+1,b,p) if 0<=p<N and 0<=b<N and 0<=l+1<N else None

            # проверяем доступность соседних вершин
            for z, y, x in (el for el in (w1, w2, w3, w4, w5, w6) if el):
                if matrix[z][y][x] == '#':
                    continue
                if z == 0:  # как только достигаем 0 уровня == победа
                    return wave+1
                neighbours.append((z,y,x),)
                
            # шерстим по соседям
            for neighbour in neighbours:
                if neighbour not in visited:
                    visited.add(neighbour)
                    # соседа на следующий шаг анализа
                    queue[wave+1].append(neighbour)  

            neighbours.clear()
            

        del queue[wave]
        wave += 1


N = int(input().strip())

matrix = tuple()  # матрица координат
stage = tuple()  # уровень l

place = 0  # порядковый номер блока со стартовой позицией от 1 до N*N

start_block = 0
start_pos = 0

# Превращает одномерный массив в многомерный
# N*N + N раз из-за пустых строк
for _ in range(N*N+N):
    row = input().strip()

    # Пропускаем пустые строки
    if len(row) == 0:
        continue

    # 3 уровня данных: matrix -> stage -> row/col
    stage += (row,)
    place += 1

    # если находим стартовую позицию в блоке
    if 'S' in row:
        start_block = place
        start_pos = row.index('S')

    # как только блок заполняется до размера N добавляем в матрицу
    if len(stage) == N:
        matrix += (stage,)
        stage = tuple()

# 1: 0,0
# 2: 0,1
# 3: 0,2
# 4: 1,0
# 5: 1,1
# 6: 1,2
# 7: 2,0
# 8: 2,1
# 9: 2,2
# для крайнего столбца своя логика
if start_block % N == 0:
    n1 = start_block//N-1
    n2 = N-1
else:
    n1 = start_block//N  # строка
    n2 = (start_block-1) % N  # столбец

# Стартовые координаты с 0: (строка, столбец, позиция символа)
start_idx = (n1, n2, start_pos)

if n1 == 0:
    print(0)  # если появляемся сразу на верхнем уровне
else:
    answer = find_best(matrix, start_idx)
    print(answer)
