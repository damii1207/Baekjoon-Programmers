def solution(num_list):
    s = 1
    sum = 0
    for i in num_list:
        s = i*s
        sum += i
    if s < sum**2:
        answer = 1
    else:
        answer = 0
    return answer