def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        a = -1
        for i in range(s, e+1):
            if arr[i] >k:
                if a == -1 or arr[i] < a:
                    a = arr[i]
        answer.append(a)
    return answer