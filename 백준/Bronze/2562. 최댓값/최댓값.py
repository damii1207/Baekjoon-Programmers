list = list(int(input()) for i in range(9))
print(max(list))
for i in range(9):
    if list[i] == max(list):
        print(i+1)