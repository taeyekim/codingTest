def solution(s):
    x_cnt = 0
    not_x_cnt = 0
    str1 = ''
    first_char = ''
    arr = []
    for element in s:
        if str1 == '':
            x_cnt += 1
            first_char += element
            str1 += first_char
        else:
            if first_char == element:
                x_cnt += 1
            else:
                not_x_cnt += 1
            str1 += element
        if x_cnt == not_x_cnt:
            first_char = ''
            str1 = ''
            arr.append(str1)
    if str1 != '':
        arr.append(str1)
    return len(arr)