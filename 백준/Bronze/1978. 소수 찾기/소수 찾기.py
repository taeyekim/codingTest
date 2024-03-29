def is_prime(num):
    if num == 1:
        return 0
    elif num == 2 or num == 3:
        return 1
    else:
        for i in range(2,num//2 + 1):
            if num % i == 0:
                return 0
        else:
            return 1

N = int(input())
cnt = 0
arr = list(map(int, input().split()))
for num in arr:
    cnt += is_prime(num)
print(cnt)