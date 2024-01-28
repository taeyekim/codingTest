def solution(l, r):
    answer = []
    for i in range(l, r+1):
        for j in str(i):
            if j not in ('0', '5'):
                break
        else:
            answer.append(i)
    return [-1] if answer == [] else answer