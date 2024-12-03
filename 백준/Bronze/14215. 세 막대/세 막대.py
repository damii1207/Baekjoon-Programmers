a,b,c = map(int,input().split())
li = sorted([a,b,c],reverse=True)
while li[0] >= li[1] +li[2]:
    li[0] -= 1
    
print(sum(li))