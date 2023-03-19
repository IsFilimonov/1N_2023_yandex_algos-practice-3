"""
Компилятор: Python 3.9 (PyPy 7.3.11)

отсортируем задачи по возрастанию старта

будем поддерживать параллельно всех нанятых работников

для каждой новой задачи мы будем выбирать работника, у которого последняя задача закончилась раньше всех 

если мы можем выдать работнику текущую задачу - выдаем

иначе нанимаем нового работника

поддерживать последние задачи работников можно в Priority Queue

чтобы вывести ответ, будем для каждого работника в процессе поддерживать список выданных ему задач (список списков получится)

"""
from collections import deque
import heapq

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


def read_line(): return lines.popleft()


def read_int(): return int(read_line())


def read_ints(): return map(int, read_line().split())


n, w = read_ints()
segments = [tuple([*read_ints(), i + 1]) for i in range(n)]

segments.sort()

inf = w + 1
ends = [(inf, -1)]

levels = []
for start, width, index in segments:
    end = start + width

    smallest_end, smallest_level = ends[0]
    if smallest_end > start:
        smallest_level = len(levels)
        levels.append([])
    else:
        heapq.heappop(ends)

    levels[smallest_level].append(index)
    heapq.heappush(ends, (end, smallest_level))

print(len(levels))

order = []
for level in levels:
    order.extend(level)

print(*order)
