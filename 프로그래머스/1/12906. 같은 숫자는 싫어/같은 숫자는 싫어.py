def solution(arr):
    answer = []
    answer.append(arr[0])
    flag = arr[0]
    for x in arr[1:]:
        if flag != x:
            answer.append(x)
            flag = x
    return answer