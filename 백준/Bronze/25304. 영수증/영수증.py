t = int(input())
n = int(input())
s = int()
for i in range(n):
    a, b = map(int, input().split())
    s += (a*b)
if s == t :
    print("Yes")
else :
    print("No")