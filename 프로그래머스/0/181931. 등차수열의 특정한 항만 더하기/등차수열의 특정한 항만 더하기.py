def solution(a, d, included):
    s= 0
    answer = 0
    for i in range(len(included)):
        if included[i] == 1:
            s = a + d*i
            answer = answer + s
    return answer