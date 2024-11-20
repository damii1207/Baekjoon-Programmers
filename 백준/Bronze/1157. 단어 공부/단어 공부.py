from collections import Counter
str = input().upper()
count = Counter(str)
max = max(count.values())
same_count = []
for char, count in count.items():
    if count == max:
        same_count.append(char)
if len(same_count) > 1:
    print("?")
else:
    print(same_count[0])