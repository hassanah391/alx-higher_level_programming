#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return 0
    uniq_numbers = [my_list[0]]
    is_uniq = True
    sum = my_list[0]
    for i in range(1, len(my_list)):
        for j in range(0, len(uniq_numbers)):
            if my_list[i] == uniq_numbers[j]:
                is_uniq = False
        if is_uniq:
            uniq_numbers.append(my_list[i])
            sum += my_list[i]
        else:
            is_uniq = True
    return sum