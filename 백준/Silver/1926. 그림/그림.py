from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]


def bfs(col, row):
    global painting
    cnt = 1
    q = deque()
    q.append((col, row))
    painting[col][row] = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx <= m - 1 and 0 <= ny <= n - 1 and painting[ny][nx] == 1:
                q.append((ny, nx))
                painting[ny][nx] = 0
                cnt += 1
    return cnt

n, m = map(int, input().split())

painting = [list(map(int, input().split())) for _ in range(n)]

painting_cnt = 0
answer = 0
for y in range(n):
    for x in range(m):
        if painting[y][x] == 1:
            painting_cnt += 1
            total = bfs(y, x)
            answer = max(answer, total)
print(painting_cnt)
print(answer)