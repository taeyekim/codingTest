def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fibo = []
    for i in range(0, n + 1):
        if i == 0:
            fibo.append(0)
        elif i == 1:
            fibo.append(1)
        else:
            fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n] % 1234567