import sys

# 입력 함수를 빠른 sys.stdin.readline으로 변경
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def bfs(row, col):
    lst = []
    lst.append((row, col))

    visited[row][col] = True
    while lst:
        x, y = lst.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= h - 1 and 0 <= ny <= w - 1:
                if jido[nx][ny] == 1 and visited[nx][ny] == False:
                    lst.append((nx, ny))
                    visited[nx][ny] = True

while True:

    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    visited = [[False] * w for _ in range(h)]
    jido = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if visited[i][j] == False and jido[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)