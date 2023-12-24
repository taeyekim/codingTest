def solution(s):
    answer = True
    flag = 0
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in s:
        if i == '(':
            flag += 1
        else:
            flag -= 1
        if flag < 0:
            return False
    if flag == 0:
        return True
    return False