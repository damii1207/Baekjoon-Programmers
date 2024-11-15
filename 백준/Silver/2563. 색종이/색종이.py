arr = [[0 for _ in range(100)] for _ in range(100)]
n = int(input())
total = 0

for i in range(n):
    a,b = map(int,input().split())
    for j in range(b,b+10):
        for k in range(a,a+10):
            arr[j][k] = 1

for i in range(100):
    for j in range(100):
        total += arr[i][j]
print(total)