arr = [input().strip() for _ in range(5)]
result = ""


for i in range(15):
    for j in arr:
        if i <len(j):
            result += j[i]

print(result)