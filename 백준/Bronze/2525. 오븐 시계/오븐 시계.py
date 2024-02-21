h,m = map(int,input().split())
c = int(input())

m = m+c
h = h+(m//60)
m = m%60
if h>=24:
    h= h-24
else:
    h = h
print(h,m)