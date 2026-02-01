def solution(A,B):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # 자연수로 이루어진 서로 같은 길이의 배열 A, B
    # A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱함. 이 과정을 배열의 길이만큼
    # 반복하여 두 수를 곱한 값을 누적하여 더함. 누적된 값이 최소가 되는 경우.
    # 숫자 재사용 X
    A.sort()
    B.sort(reverse=True)
    answer = sum(i*j for (i, j) in zip(A, B))
    
    return answer