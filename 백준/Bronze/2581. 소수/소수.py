m = int(input())
n = int(input())
li = []

for i in range(m,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        li.append(i)

if li:
    print(sum(li))
    print(min(li))
else:
    print(-1)