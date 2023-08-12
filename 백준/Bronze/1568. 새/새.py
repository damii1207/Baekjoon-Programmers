N = int(input())
K=1
cnt = 0
while True:
    if K <= N:
        N = N - K
        K = K + 1
        cnt = cnt+1
    elif N == 0:
        break
    elif K > N:
        K=1
        N = N-K
        K = K + 1
        cnt = cnt + 1
print(cnt)