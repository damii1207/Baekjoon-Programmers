N, B = map(int,input().split())

digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result=""

if N == 0:
    result = "0"
else:
    while N:
        result = digits[N%B] + result
        N //= B

print(result)