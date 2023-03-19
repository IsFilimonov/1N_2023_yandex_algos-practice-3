import heapq
import sys

H = []
N = int(sys.stdin.readline().strip())

for el in sys.stdin.readlines():
    operation = tuple(map(int, el.strip().split()))

    if operation[0] == 0:
        heapq.heappush(H, operation[1]*-1)

    elif operation[0] == 1:
        print(heapq.heappop(H)*-1)
