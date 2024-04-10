from collections import deque

def bfs(col, row):
    q = deque()
    q.append((col, row))
    lst[col][row] = 1
    cnt = 1
    while q:
        y, x = q.popleft()
        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= M - 1 and 0 <= nx <= N - 1 and lst[ny][nx] == 0:
                q.append((ny, nx))
                lst[ny][nx] = 1
                cnt += 1
    return cnt

M, N, K = map(int, input().split()) # 세로 M, 가로 N, 직사각형 수 K 5 7 3
lst = [[0] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split()) # 0 2 4 4
    for i in range(y1, y2):
        for j in range(x1, x2):
            if lst[i][j] == 0:
                lst[i][j] = 1

cnt = 0
answer = []
for j in range(N):
    for i in range(M-1, -1, -1):
        if lst[i][j] == 0:
            cnt += 1
            answer.append(bfs(i, j))
            # for i in range(M - 1, -1, -1):
            #     print(lst[i])
            # print()
answer.sort()
print(cnt)
print(*answer)

