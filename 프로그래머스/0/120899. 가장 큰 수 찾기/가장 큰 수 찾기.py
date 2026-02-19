def solution(array):
    # answer = []
    # index = 0
    # num = array[0]
    # for i in range(1, len(array)):
    #     if num < array[i]:
    #         num = array[i]
    #         index = i
    # answer = [num, index]
    # return answer
    
    val = max(array)
    answer = [val, array.index(val)]
    return answer