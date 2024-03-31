from collections import deque

def melt_cheese():
    q = deque([(0, 0)])  # 판의 가장자리에서 시작
    visited = [[False] * row for _ in range(col)]
    melt_list = []  # 이번 단계에서 녹을 치즈의 위치를 저장

    while q:
        y, x = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not visited[ny][nx]:
                if lst[ny][nx] == 1:
                    melt_list.append((ny, nx))  # 외부 공기에 접촉한 치즈 저장
                elif lst[ny][nx] == 0:
                    q.append((ny, nx))
                visited[ny][nx] = True

    # 외부 공기에 접촉한 치즈 녹이기
    for y, x in melt_list:
        lst[y][x] = 0

    return len(melt_list)  # 이번 단계에서 녹은 치즈의 수 반환

col, row = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(col)]
time = 0
last_melt = 0

while True:
    melted = melt_cheese()
    if melted == 0:
        break
    last_melt = melted
    time += 1

print(time)
print(last_melt)