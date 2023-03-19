import sys

N = int(input().strip())
data = tuple(tuple(map(int,row.split())) for row in  sys.stdin.readlines())

# Расширяем массив на виртуальных людей
X = ((0, 0, 0), (0, 0, 0), (0, 0, 0)) + data
dp = [0]*(3+N)  # -2,-1,0 индекс вирт людей

for i in range(3, N+3):
    row = (dp[i-1]+X[i][0], dp[i-2]+X[i-1][1], dp[i-3]+X[i-2][2])
    dp[i] = min(el for el in row if el > 0)

print(dp[-1])
