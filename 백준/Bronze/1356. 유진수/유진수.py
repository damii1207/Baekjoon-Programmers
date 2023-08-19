# 유진수
N = input()

sol = False
# 입력받은 숫자의 길이 FOR문 이용하여 분리
for i in range(1,len(N)):
    L, R = N[:i], N[i:]
    mulL = 1
    mulR = 1
    # 곱셈
    for j in L:
        mulL = mulL * int(j)
    for k in R:
        mulR = mulR * int(k)
    if mulL == mulR:
        sol = True
        break

if sol == True:
    print('YES')
else:
    print('NO')
