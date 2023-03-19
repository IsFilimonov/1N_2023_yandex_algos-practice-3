import sys


def is_good(A: list[int]):
    if len(A) == 1: return 0

    result = 0

    # len()-1 тк для крайней буквы хорошести не получить
    for i in range(0, len(data)-1):

        if data[i] == data[i+1]:
            result += data[i]
        elif data[i] > data[i+1]:
            result += data[i+1]
        elif data[i] < data[i+1]:
            result += data[i]

    return result


N = int(input())
data = list(map(int, sys.stdin.readlines()))

print(is_good(data))
