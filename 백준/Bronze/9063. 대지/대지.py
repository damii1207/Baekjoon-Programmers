n = int(input())
list_x = []
list_y = []
for _ in range(n):
    x,y = map(int,input().split())
    list_x.append(x)
    list_y.append(y)
mi_x, ma_x = min(list_x),max(list_x)
mi_y, ma_y = min(list_y),max(list_y)
wi = (ma_x-mi_x)*(ma_y-mi_y)
print(wi)