L = int(input())
s = input()

MOD = 1234567891

answer = 0
base = 1

for c in s:
    coefficient = ord(c) - ord('a') + 1
    answer = (answer + coefficient * base) % MOD
    base = (base * 31) % MOD

print(answer)
