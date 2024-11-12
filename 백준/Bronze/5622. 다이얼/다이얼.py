call = input()
SEC = 0
for i in range(len(call)):
    alph = call[i] 
    if alph =='A' or alph =='B' or alph == 'C':
        SEC = SEC + 3
    elif alph =='D' or alph =='E' or alph == 'F':
        SEC = SEC + 4
    elif alph =='G' or alph =='H' or alph == 'I':
        SEC = SEC + 5
    elif alph =='J' or alph =='K' or alph == 'L':
        SEC = SEC + 6
    elif alph =='M' or alph =='N' or alph == 'O':
        SEC = SEC + 7
    elif alph =='P' or alph =='Q' or alph == 'R' or alph =='S':
        SEC = SEC + 8
    elif alph =='T' or alph =='U' or alph == 'V':
        SEC = SEC + 9
    elif alph =='W' or alph =='X' or alph == 'Y' or alph =='Z':
        SEC = SEC + 10
    elif alph =='D' or alph =='E' or alph == 'F':
        SEC = SEC + 11
print(SEC)