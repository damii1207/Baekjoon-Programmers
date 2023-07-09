H = []
a,b=0,0

for i in range(9):
  H.append(int(input()))

su = sum(H)
for i in range(8):
  for j in range(i+1,9):
    if su - H[i] - H[j] ==100:
      a=H[i]
      b=H[j]
H.remove(a)
H.remove(b)
H.sort()

for i in H:
  print(i)