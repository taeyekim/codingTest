from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(col, row):
    q = deque()
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    q.append((col, row, 1))

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny <= N-1 and 0 <= nx <= M-1 and lst[ny][nx] == 1 and not visited[ny][nx]:
                if ny == N-1 and nx == M-1:
                    return cnt + 1
                visited[ny][nx] = True
                q.append((ny, nx, cnt + 1))

N, M = map(int, input().split())

lst = [list(map(int, input())) for _ in range(N)]
answer = bfs(0, 0)
print(answer)