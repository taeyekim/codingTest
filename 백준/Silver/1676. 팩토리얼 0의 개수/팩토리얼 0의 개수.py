def count_zero(N):
    total = 1
    cnt = 0
    for i in range(1, N+1):
        total *= i
    total = str(total)
    for i in range(len(str(total))):
        if total[-i-1] == '0':
            cnt += 1
        else:
            return cnt

N = int(input())

print(count_zero(N))