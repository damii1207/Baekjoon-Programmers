N = int(input())

can = [[0 for _ in range(1001)] for _ in range(1001)]
papers = []
for i in range(1,N+1):
    start_x,start_y,w,h = map(int,input().split())
    for y in range(start_y,start_y+h):
        can[y][start_x:start_x+w] = [i]*w

for i in range(1,N+1):
    result = 0
    for j in range(1001):
        result += can[j].count(i)
    print(result)
