while 1:
    n = int(input())
    if n == -1:
        break
    li = []
    for i in range (1,n):
        if n%i == 0:
            li.append(i)
    if n == sum(li):
        print(f"{n} = {' + '.join(map(str, li))}")
    else:
        print(f"{n} is NOT perfect.")