def solution(n):
    list = [n]
    while n != 1:
        if n%2==0:
            n=n/2
            list.append(n)
        else:
            n = 3*n+1
            list.append(n)
    return list