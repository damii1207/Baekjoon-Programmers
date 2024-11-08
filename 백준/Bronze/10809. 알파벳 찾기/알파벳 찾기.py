s = input()
str = "abcdefghijklmnopqrstuvwxyz"
sum = []
for i in range(26):
    sum.append(s.find(str[i]))
print(*sum,sep=' ')