def solution(a, b):
    a_b = int(str(a) + str(b))
    if a_b >= 2 * a * b:
        answer = a_b
    else:
        answer = 2 * a * b
    return answer