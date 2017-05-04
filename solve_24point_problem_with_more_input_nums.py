nums = [3, 5, 7, 13]
target = 24

def search_target(nums, target):
    lst = [[(num, str(num)) for num in nums]]
    return binary_operator(lst, target)

def binary_operator(lst, target):
    # print 'lst: ', lst
    if not lst or not lst[0]:
        return None
    if len(lst[0]) == 1:
        for l in lst:
            if l[0][0] == target:
                # print 'result: ', l[0][1]
                return l[0][1]
        return None
    next_lst = []
    for l in lst:
        # print 'l: ', l
        for i in range(len(l)):
            for j in range(i+1, len(l)):
                binary_result_list = [(l[i][0] + l[j][0], "({0}+{1})".format(l[i][1], l[j][1])),
                                      (l[i][0] - l[j][0], "({0}-{1})".format(l[i][1], l[j][1])),
                                      (l[j][0] - l[i][0], "({1}-{0})".format(l[i][1], l[j][1])),
                                      (l[i][0] * l[j][0], "({0}*{1})".format(l[i][1], l[j][1]))]
                if l[j][0]:
                    binary_result_list.append((1.0 * l[i][0] / l[j][0], "({0}/{1})".format(l[i][1], l[j][1])))
                if l[i][0]:
                    binary_result_list.append((1.0 * l[j][0] / l[i][0], "({1}/{0})".format(l[i][1], l[j][1])))
                for next_element in binary_result_list:
                    next_lst.append(l[0:i] + l[i+1:j] + l[j+1:] + [next_element])
    return binary_operator(next_lst, target)

# binary_operator([[(1, '1'), (2, '2')]], 0.5)
search_target(nums, target)

search_target([3, 5, 7], 24)
search_target([3, 5, 7, 13], 24)
search_target([1, 2, 3, 5, 6], 50)
search_target([1, 2, 3, 5, 6, 31], 94)


def search_target1(nums, target):
    l = [(num, str(num)) for num in nums]
    return binary_operator1(l, target, [])

def binary_operator1(l, target, result=[]):
    if not l:
        return None
    if len(l) == 1:
        if l[0][0] == target:
            result = l[0][1]
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            binary_result_list = [(l[i][0] + l[j][0], "({0}+{1})".format(l[i][1], l[j][1])),
                                  (l[i][0] - l[j][0], "({0}-{1})".format(l[i][1], l[j][1])),
                                  (l[j][0] - l[i][0], "({1}-{0})".format(l[i][1], l[j][1])),
                                  (l[i][0] * l[j][0], "({0}*{1})".format(l[i][1], l[j][1]))]
            if l[j][0]:
                binary_result_list.append((1.0 * l[i][0] / l[j][0], "({0}/{1})".format(l[i][1], l[j][1])))
            if l[i][0]:
                binary_result_list.append((1.0 * l[j][0] / l[i][0], "({1}/{0})".format(l[i][1], l[j][1])))
            for next_element in binary_result_list:
                binary_operator1(l[0:i] + l[i+1:j] + l[j+1:] + [next_element], target, result)
    return result

search_target1([3, 5, 7], 24)
search_target1([3, 5, 7, 13], 24)
search_target1([1, 2, 3, 5, 6], 50)
search_target1([1, 2, 3, 5, 6, 31], 94)
