def solution(s):
    numbers = list(map(int, s.split()))
    answer = str(min(numbers)) + ' ' + str(max(numbers))
    return answer