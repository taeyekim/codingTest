import sys
def input():
    return sys.stdin.readline().rstrip()

L = int(input())
s = input()
coefficient = 0 # 계수
answer = 0
for c in s:
    answer += (ord(c) - ord('a') + 1) * 31 ** coefficient
    coefficient += 1
print(answer)