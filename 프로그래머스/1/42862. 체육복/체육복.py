from collections import deque

def solution(n, lost, reserve):
    
    # 학생 수 n, 도난 학생 번호 배열 lost, 여벌 체육복 가져온 학생 번호 배열 reverse
    
    lost = set(lost)
    reserve = set(reserve)
    
    both = lost & reserve
    lost -= both
    reserve -= both
    
    for x in lost:
        if x-1 in reserve:
            reserve.remove(x-1)
        elif x+1 in reserve:
            reserve.remove(x+1)
        else:
            n -= 1
    return n