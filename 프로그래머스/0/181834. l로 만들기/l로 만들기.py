def solution(myString):
    i_string = "abcdefghijk"
    answer = ''
    for i in myString:
        if i in i_string:
            answer += 'l'
        else:
            answer += i
    return answer