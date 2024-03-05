N, M = map(int, input().split())
S = []
total = 0
for _ in range(N):
    S.append(input())
for _ in range(M):
    s = input()
    if s in S:
        total += 1
print(total)