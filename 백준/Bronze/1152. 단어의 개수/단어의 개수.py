str = input().strip()

if str =='':
    count = 0
else:
    count = 1
    for i in range(len(str)):
        if str[i] == ' ':
            count += 1
print(count)