t = int(input())
c = int(input())
sum = 0

for i in range(c):
    a,b  = map(int,input().split())
    sum = sum + a*b
if sum == t:
    print("Yes")
else:
    print("No")