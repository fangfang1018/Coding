nums = [3, 5, 7, 13]
target = 24

def search_target(nums, target):
    l = [(num, str(num)) for num in nums]
    return binary_search(l, target, result=[])

def binary_search(l, target, result=[]):
    # print 'lst: ', lst
    if result:
        return
    if not l:
        return None
    if len(l) == 1:
        if l[0][0] == target:
            # print 'result: ', l[0][1]
            result.append(l[0][1])
            return l[0][1]
        return None
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
                binary_search(l[0:i] + l[i+1:j] + l[j+1:] + [next_element], target, result)
    return result

# binary_operator([[(1, '1'), (2, '2')]], 0.5)
search_target(nums, target)

search_target([3, 5, 7], 24)
search_target([3, 5, 7, 13], 24)
search_target([1, 2, 3, 5, 6], 50)
search_target([1, 2, 3, 5, 6, 31], 94)