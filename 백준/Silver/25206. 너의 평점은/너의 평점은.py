score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
count = 0
exam_sum=0
for i in range(20):
    n, t, s = input().split()
    if s != 'P':
        s_sum = float(t)*score[s]
        exam_sum += s_sum
        count += float(t)
final = exam_sum/count
print(f"{final:.6f}")