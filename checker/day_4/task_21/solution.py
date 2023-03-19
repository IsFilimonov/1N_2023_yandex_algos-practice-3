n = int(input())
f = [0] * 36
f[1], f[2], f[3] = 2,4,7

i = 4
while i <= n:
  f[i] = (f[i-1] + f[i-2] + f[i-3])
  i += 1

print(f[n])
