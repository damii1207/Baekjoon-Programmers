n = int(input())
sum = 0
for i in range(n-2):
    sum += (n-(i+1))*(n-(i+2))//2
print(sum)
print(3)