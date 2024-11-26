list_x = []
list_y = []
for _ in range (3):
    x,y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
x4 = [x for x in list_x if list_x.count(x) == 1][0]
y4 = [y for y in list_y if list_y.count(y) == 1][0]
print(x4,y4)