def solution(box, n):
    answer = 1
    # 박스 가로, 세로, 높이가 저장된 배열 box[0, 1, 2]
    # n은 정육면체 모서리 길이(정수) n
    # 박스에 들어갈 수 있는 정육면체의 개수 answer
    for x in box:
        if x < n:
            return 0
        answer *= x // n
    return answer