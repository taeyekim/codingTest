from collections import deque

def bfs(col, row):
    q = deque()
    q.append((col, row))
    cnt = 1
    lst[col][row] = 0
    while q:
        y, x = q.popleft()

        for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= N-1 and 0 <= nx <= N-1 and lst[ny][nx] == 1:
                lst[ny][nx] = 0
                q.append((ny, nx))
                cnt += 1
    return cnt

N = int(input())
lst = [list(map(int, input())) for _ in range(N)]
answer = []
cnt = 0
for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            answer.append(bfs(i, j))
            cnt += 1
answer.sort()
print(cnt)
for i in range(cnt):
    print(answer[i])
    