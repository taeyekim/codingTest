def solution(A, B):
    cnt = 0
    for _ in range(len(A)):
        if A == B:
            return cnt
        else:
            A = A[-1] + A[:-1]
            cnt += 1
    else:
        return -1