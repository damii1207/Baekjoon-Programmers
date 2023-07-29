n = int(input())
result = list()
sol = list()
for i in range(n):
    str_ = input()
    if "push" in str_:
        result.append(int(str_[5:]))
    elif str_ == "pop":
        if len(result) > 0:
            sol.append(result.pop())
        else:
            sol.append(-1)
    elif str_ == "size":
        sol.append(len(result))
    elif str_ == "empty":
        if len(result) == 0:
            sol.append(1)
        else:
            sol.append(0)
    elif str_ == "top":
        if len(result) > 0:
            sol.append(result[-1])
        else:
            sol.append(-1)
for i in sol:
    print(i)
