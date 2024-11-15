arr = [list(map(int, input().split())) for _ in range(9)]
maxs = []
for i in range(9):
    maxs.append(max(arr[i]))
maxx = max(maxs)
print(maxx)

for i in range(9):
    for j in range(9):
        if arr[i][j] == maxx:
            print(i+1,j+1)
            break
        else:
            continue
        break