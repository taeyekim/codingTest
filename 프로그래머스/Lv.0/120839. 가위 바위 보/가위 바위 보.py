def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            element = '0'
        elif i == '0':
            element = '5'
        else:
            element = '2'
        answer += element
    return answer