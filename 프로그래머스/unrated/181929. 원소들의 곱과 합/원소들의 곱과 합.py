def solution(num_list):
    product = 1
    total = 0
    for i in num_list:
        product *= i
        total += i
    answer = 1 if product < total**2 else 0
    return answer