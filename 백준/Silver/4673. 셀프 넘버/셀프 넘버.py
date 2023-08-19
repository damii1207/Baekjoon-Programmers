def self_num(N):
    self_num = N
    while N > 0:
        self_num = self_num + N % 10  # 1의 자리수
        N = N//10 # 몫
    return self_num

self = []
for i in list(range(1, 10001)):
    self.append(self_num(i))
    if i not in self:
        print(i)