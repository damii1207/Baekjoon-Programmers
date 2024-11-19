n = int(input())

if n == 1:
    print(1)
else:
    layer = 1
    end = 1
    while end < n:
        end = end+6*layer
        layer += 1
    print(layer)