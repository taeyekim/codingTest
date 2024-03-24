K, N = map(int, input().split())
lengths = []
for i in range(K):
    lengths.append(int(input()))

# 이진 검색을 이용한 랜선 자르기
def find_max_length(K, N, lengths):
    start, end = 1, max(lengths) # 시작 길이와 끝 길이 설정

    while start <= end:
        mid = (start + end) // 2 # 중간 길이
        num_cables = sum(length // mid for length in lengths) # 중간 길이로 잘랐을 때 만들 수 있는 랜선 개수

        # 만들어진 랜선의 개수가 목표 개수보다 많거나 같다면, 더 긴 길이 탐색
        if num_cables >= N:
            start = mid + 1
        else: # 만들어진 랜선의 개수가 목표 개수보다 적다면, 더 짧은 길이 탐색
            end = mid - 1

    return end # 최대 길이 반환

answer = find_max_length(K, N, lengths)
print(answer)