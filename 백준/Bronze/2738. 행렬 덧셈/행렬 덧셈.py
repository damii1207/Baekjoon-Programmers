n, m = map(int, input().split(' '))
mat1 = [[0 for j in range(m)] for i in range(n)]
mat2 = [[0 for j in range(m)] for i in range(n)]
mat3 = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    col = list(map(int, input().split()))
    for j in range(m):
      mat1[i][j] = col[j] 

for i in range(n):
    col = list(map(int, input().split()))
    for j in range(m):
      mat2[i][j] = col[j]
   
    
for row in range(n):
    for col in range(m):
        mat3[row][col] = mat1[row][col] + mat2[row][col]

for row in range(n):
    for col in range(m):
        print(mat3[row][col], end=' ')
    print()