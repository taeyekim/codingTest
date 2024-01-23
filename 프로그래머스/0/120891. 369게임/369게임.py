def solution(order):
    cnt = 0
    for i in list(str(order)):
        if i in ['3', '6', '9']:
            cnt += 1
    return cnt