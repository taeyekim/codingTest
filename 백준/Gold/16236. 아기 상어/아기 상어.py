from collections import deque

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def bfs(col, row, size):
    q = deque([(col, row, 0)])  # 아기 상어의 위치와 이동 시간을 큐에 저장
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 저장하는 배열
    visited[col][row] = True  # 아기 상어의 위치 방문 처리
    eatable_fishes = []  # 먹을 수 있는 물고기의 위치와 이동 시간을 저장하는 배열

    while q:
        y, x, move = q.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            # 다음 위치가 범위 내에 있고 방문하지 않았으며 아기 상어가 지나갈 수 있는 칸인 경우
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and lst[ny][nx] <= size:
                visited[ny][nx] = True  # 다음 위치 방문 처리
                q.append((ny, nx, move + 1))  # 큐에 다음 위치 추가
                # 다음 위치에 먹을 수 있는 물고기가 있는 경우
                if 0 < lst[ny][nx] < size:
                    eatable_fishes.append((ny, nx, move + 1))  # 먹을 수 있는 물고기의 위치와 이동 시간 저장

    # 먹을 수 있는 물고기가 있는 경우, 가장 가까운 물고기의 위치와 이동 시간 반환
    if eatable_fishes:
        eatable_fishes.sort(key=lambda x: (x[2], x[0], x[1]))  # 이동 시간, 위쪽 위치, 왼쪽 위치 순으로 정렬
        return eatable_fishes[0][0], eatable_fishes[0][1], eatable_fishes[0][2]
    else:  # 먹을 수 있는 물고기가 없는 경우
        return None, None, None


N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if lst[i][j] == 9:  # 아기 상어의 초기 위치
            col, row = i, j
            lst[i][j] = 0  # 아기 상어가 있는 위치는 빈 칸으로 변경

time = 0  # 아기 상어가 물고기를 먹으며 이동한 총 시간
ate_fishes = 0  # 아기 상어가 먹은 물고기의 수
baby_shark_size = 2  # 아기 상어의 초기 크기

while True:
    # 아기 상어가 먹을 수 있는 물고기의 위치와 이동 시간을 구함
    next_col, next_row, eat_time = bfs(col, row, baby_shark_size)

    # 먹을 수 있는 물고기가 없는 경우 종료
    if next_col is None:
        break

    # 아기 상어가 먹은 물고기의 수를 증가시키고, 아기 상어의 위치를 업데이트
    ate_fishes += 1
    time += eat_time
    lst[next_col][next_row] = 0
    col, row = next_col, next_row

    # 아기 상어의 크기를 증가시키고, 먹은 물고기의 수가 아기 상어의 크기와 같아지면 크기 증가
    if ate_fishes == baby_shark_size:
        baby_shark_size += 1
        ate_fishes = 0

print(time)