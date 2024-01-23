def solution(left, right):
    total = 0
    for i in range(left, right+1):
        cnt = 0
        if i == 2:
            total += cnt
            continue
        for j in range(2, i//2 + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            total += i
        else:
            total -= i
    return total