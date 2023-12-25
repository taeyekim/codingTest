def solution(arr):
    answer = []
    flag = -1
    for i in arr:
        if i != flag:
            flag = i
            answer.append(i)
        else:
            continue
    return answer