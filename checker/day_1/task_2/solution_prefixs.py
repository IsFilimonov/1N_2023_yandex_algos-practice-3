"""Решение с помощью префиксных сумм и бинарного поиска.
"""

import string
import bisect

# ### >>>>>>
# import debugpy
# debugpy.listen(5678)
# print("Waiting for debugger")
# debugpy.wait_for_client()
# ### <<<<<<

k = int(input())    # количество замен
s = input()         # строка

best = 0

for char in string.ascii_lowercase:
    cnt = 0
    prefixs = []
        
    # Префиксные суммы букв для char
    for el in s:
        if char != el:
            cnt += 1
        prefixs.append(cnt)

    # Если префиксная сумма идет по порядку и итоговое число равно длине, то 
    # совпадений букв нет и рассматривать такую последовательность нет необходимости
    if prefixs[-1] == len(prefixs): continue

    # Бинарный поиск
    for i in range(len(s)):
        # Нет смысла обрабатывать остаток массива, если его длина меньше 
        #   лучшего показателя красивости
        if best >= len(prefixs[i:]): break

        # idx = bisect.bisect_right(prefixs[i:], k+i)
        idx = bisect.bisect(prefixs[i:], k+i)

        best = max(idx-i, best)

print(best)
