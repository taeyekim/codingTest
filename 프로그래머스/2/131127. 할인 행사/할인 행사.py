def solution(want, number, discount):
    
    answer = 0
    for i in range(len(discount) - sum(number) + 1):
        arr = [0 for i in range(len(number))]
        for j in range(i, sum(number) + i):
            if discount[j] in want:
                arr[want.index(discount[j])] += 1
            else:
                break
        if arr == number:
            answer += 1
    return answer