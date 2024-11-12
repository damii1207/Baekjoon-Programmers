while True:
    try:
        str = input()
        if len(str) == 0:
            break
        print(str)
    except EOFError:
        break