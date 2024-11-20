n = int(input())
count = 0
for i in range(n):
    str = input()
    se = set()
    before = ""
    group = True
    for char in str:
        if char != before and char in se:
            group = False 
            break
        se.add(char)
        before = char

    if group:
        count += 1

print(count)