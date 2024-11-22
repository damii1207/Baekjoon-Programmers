N = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    if i >= 2:
        a_count = 0
        for j in range(1,i+1):
            if i %j ==0:
                a_count += 1
        if a_count ==2:
            count += 1
print(count)