def solution(numbers):
    
    # 정수 배열 numbers의 원소 중 2개를 곱해 만들 수 있는 최댓값 return
    numbers.sort()
    answer = max(
        numbers[0] * numbers[1],
        numbers[-1] * numbers[-2]
    )
    return answer