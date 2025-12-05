def solution(code):
    mode = 0
    ret = ""

    for idx in range(len(code)):
        if code[idx] == "1":
            # mode 전환
            mode = 1 - mode
        else:
            # mode가 0일 때 → 짝수 idx만 추가
            if mode == 0 and idx % 2 == 0:
                ret += code[idx]
            # mode가 1일 때 → 홀수 idx만 추가
            elif mode == 1 and idx % 2 == 1:
                ret += code[idx]

    return ret if ret else "EMPTY"