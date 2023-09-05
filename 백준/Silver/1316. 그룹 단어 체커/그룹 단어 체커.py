N = int(input())

group = 0
for _ in range(N):
    str = input()
    cnt = 0
    for i in range(len(str)-1):
        if str[i]!= str[i+1]:
            rstr = str[i+1:]
            if rstr.count(str[i]) > 0:
                cnt += 1
    if cnt == 0:
        group += 1
print(group)