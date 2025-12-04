def solution(num_list):
    two = ""
    one = ""
    for i in num_list:
        if i%2==0:
            two += str(i)
        else:
            one += str(i)
    return int(one)+int(two)