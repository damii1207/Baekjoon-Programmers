# 덩치
N = int(input())
li = []
rank = []

for i in range(N):
    x,y = map(int,input().split())
    li.append([x,y])
for j in range(N):
    cnt = 0
    for k in range(N):
        if li[k][0] > li[j][0] and li[k][1] > li[j][1]:
            cnt += 1
    print(cnt+1, end=' ')