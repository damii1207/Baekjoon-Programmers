str = input()
n = len(str)
for i in range(n//2+1):
    if str[i] == str[len(str)-1-i]:
        sum = 1
    else:
        sum = 0
        break
print(sum)