def solution(my_string):
    answer = []
    # my_string이 매개변수로 주어질 때 my_string 안에 있는 숫자만 골라 오름차순 정렬
    for s in my_string:
        if s.isdigit():
            answer.append(int(s))
    return sorted(answer)