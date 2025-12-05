def solution(numLog):
    s=""
    for i in range(len(numLog)-1):
        if numLog[i+1]-numLog[i] == 1:
            s += "w"
        elif numLog[i+1]-numLog[i] == -1:
            s += "s"
        elif numLog[i+1]-numLog[i] == 10:
            s += "d"
        else:
            s += "a"
    return s