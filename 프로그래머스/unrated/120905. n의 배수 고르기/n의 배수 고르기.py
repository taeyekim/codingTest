def solution(n, numlist):
    answer = numlist
    for i in numlist[:]:
        if i % n != 0:
            answer.remove(i)
    return answer