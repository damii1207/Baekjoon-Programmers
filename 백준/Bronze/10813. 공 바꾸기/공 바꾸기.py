N,M = map(int,input().split())
basket = [i for i in range(1,(N+1))]
hat = 0
for _ in range(M):
    i,j = map(int,input().split())
    hat = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = hat

for n in range(N):
    print(basket[n], end=' ')