def solution(my_string, index_list):
    st = str()
    for i in index_list:
        st += my_string[i]
    return st