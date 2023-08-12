A,B,C = map(int,input().split())

li = []
for i in range(3):
    s,f = list(map(int,input().split()))
    li.append([s,f])

time = 100*[0]

for i in range(li[0][0],li[0][1]):
    time[i] += 1
for i in range(li[1][0],li[1][1]):
    time[i] += 1
for i in range(li[2][0], li[2][1]):
    time[i] += 1

for i in range(100):
    if time[i] == 1:
        time[i] = 1*A
    elif time[i] == 2:
        time[i] = 2*B
    elif time[i] == 3:
        time[i] = 3*C

print(sum(time))