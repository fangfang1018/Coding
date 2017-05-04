nums = [2, 2, 3, 5, 4, 5]
from collections import Counter
def median(nums):
    if not nums:
        return None
    count = Counter(nums)
    for i in range(2, 6):
        count[i] += count[i-1]
    print count
    m1 = None
    for i in range(1, 6):
        if i not in count:
            continue
        if len(nums) % 2:
            if count[i] >= len(nums)/2+1:
                return i
        else:
            if count[i] >= len(nums)/2 and not m1:
                m1 = i
            if count[i] >= len(nums)/2+1:
                if not m1:
                    return i
                else:
                    return 1.0*(i+m1)/2

# test cases
cases = [
    [],
    [1],
    [1, 3],
    [1, 4, 5],
    [2, 2, 2, 3, 3],
    [5, 2, 3, 4]
]
for nums in cases:
    print median(nums)
