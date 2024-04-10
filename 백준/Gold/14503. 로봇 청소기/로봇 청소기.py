from collections import deque

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))

def solve(col, row, d):
    q = deque()
    q.append((col, row, d))
    cnt = 0
    while q:
        y, x, d = q.popleft()
        if room[y][x] == 0:
            room[y][x] = 2
            cnt += 1

        check = False
        for dy, dx in direction:
            if 0 <= y + dy <= N - 1 and 0 <= x + dx <= M - 1 and room[y + dy][x + dx] == 0:
                check = True
                break
        if not check:
            dy, dx = direction[(d + 2) % 4]
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1 and room[ny][nx] != 1:
                q.append((ny, nx, d))
            else:
                return cnt
        else:
            nd = (d + 3) % 4
            dc, dr = direction[nd]
            ny = y + dc
            nx = x + dr
            if 0 <= ny <= N - 1 and 0 <= nx <= M - 1 and room[ny][nx] == 0:
                q.append((ny, nx, nd))
            else:
                q.append((y, x, nd))

N, M = map(int, input().split()) # y, x 좌표

r, c, d = map(int, input().split()) # 로봇청소기 좌표 r, c, 방향 d 0 : 북, 1 : 동, 2 : 남, 3 : 서

room = [list(map(int, input().split())) for _ in range(N)]

answer = solve(r, c, d)
print(answer)