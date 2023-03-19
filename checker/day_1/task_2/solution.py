"""Решение с двумя указателями.

При больших значениях сыпится по тайм-ауту, хоть и алгоритм верный.
Пройден на компиляторе: Python 3.9 (PyPy 7.3.11)
"""
import sys
import string


k = int(input())
S = sys.stdin.readline()

lns = len(S)
ans = 0

for letter in string.ascii_lowercase:
    right = 0
    t = k
    for left in range(lns - k - 2):
        while right < lns - 1 and t >= 0:
            if S[right] != letter:
                t -= 1
            right += 1

        if S[left] != letter:
            t += 1

        tmp = right - left - 1
        if tmp > ans:
            ans = tmp

print(ans)
