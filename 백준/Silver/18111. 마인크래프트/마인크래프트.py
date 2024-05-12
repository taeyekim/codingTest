import sys

def input():
    return sys.stdin.readline().rstrip()

N, M, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 최대 최소값 찾기
answer_time = int(1e9)
answer_height = 0
# 최소값 ~ 최대값 높이 탐색
for target_height in range(257):
    get_blocks = 0
    build_blocks = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > target_height:
                get_blocks += arr[i][j] - target_height
            else:
                build_blocks += target_height - arr[i][j]

    if build_blocks > get_blocks + B:
        continue

    time = get_blocks * 2 + build_blocks
    if answer_time >= time:
        answer_height = target_height
        answer_time = time

print(answer_time, answer_height)

