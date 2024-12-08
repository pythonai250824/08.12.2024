
# [4, 3, 2, 2] + 1 == [4, 3, 2, 3]
# [6, 8] == [6, 9]
# [4] == [5]
# int(''.join([4, 3, 2, 2]])) + 1
# 4323
# "4322"

# easy -- last digit is not 9
# list_digits[-1] = list_digits[-1] + 1
# [4, 3, 2, 1] ==> [4, 3, 2, 2]

# hard -- last digit is 9
# [ 9 ]      ->       [1, 0]
# [9, 9, 9]  -> [1, 0, 0, 0]
# [4, 9]     ->       [5, 0]
# [4, 9, 9] ->     [5, 0, 0]
# 1 -- all are '9' then insert 1 and all other 0
# 2 -- not all are '9' then turn last '9' to 0 and add 1

def add_1(list_digits: list[int]) -> list[int]:
    # empty
    if not list_digits:
        return []

    # there is no 9 at the end
    # [4, 3, 2, 1] ==> [4, 3, 2, 2]
    result: list[int] = list_digits.copy()
    if result[-1] != 9:
        result[-1] += 1
        return result

    # there is 9 at the end
    # case 1 all 9, i.e. [9, 9] [9] [9, 9, 9, 9]
    #                     [9, 9, 9]
    #                     [0, 0, 0]
    #                   [1, 0, 0, 0]
    all_9: bool = True
    for num in result:
        if num != 9:
            all_9 = False
            break
    if all_9:
        # all 9
        for i in range(len(result)):
            result[i] = 0
        result.insert(0, 1)
        return result

    # not all 9
    # |
    # 5 0 0
    index = len(result) - 1
    while result[index] == 9:
        result[index] = 0
        index -= 1
    result[index] += 1
    return result

print(add_1([4, 3, 2, 2]))
print(add_1([9]))
print(add_1([9, 9, 9]))
print(add_1([8, 9, 9]))

# 1. logic
# 2. ugly impl
# 3. refactor


def add_1pretty(list_digits: list[int]) -> list[int]:
    # empty
    if not list_digits:
        return []

    # start from most right digit , jump left
    # if it is not a 9 => plus 1. done
    # if it is a 9 => turn to 0. move left
    # if finish digits insert 1

    #     |
    # 0 3 3
    # 0 1 2 (3)
    # |
    # 5 0 0
    # |
    # 1 0 0 0
    result = list_digits.copy()
    # for index in range(len(list_digits) - 1, 0 - 1, -1):
    index = len(list_digits) - 1
    while index >= 0:
        # digit is not
        if result[index] != 9:
            result[index] += 1
            return result
        # digit is 9
        result[index] = 0
        index -= 1
    return [1] + result

print(add_1pretty([4, 3, 2, 2]))
print(add_1pretty([9]))
print(add_1pretty([9, 9, 9]))
print(add_1pretty([8, 9, 9]))
