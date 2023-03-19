# Объяснение решения:
# https://site.ada.edu.az/~medv/acm/Docs%20e-olimp/Volume%2010/987.htm
import sys

def calculator(A: list[int]) -> int:
    A.sort()
    N = len(A)

    a = A[1] - A[0]
    if N == 2:
        return a
    else:
        b = A[2] - A[0]

    if N == 3:
        return b
    else:
        for i in range(3, len(A)):
            c = min(a, b) + A[i] - A[i-1]
            a, b = b, c

        return c

N = int(input().strip())
data = list(map(int, sys.stdin.readline().strip().split()))

print(calculator(data))
