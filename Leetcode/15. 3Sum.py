class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = []
        for i, target in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            nums_i = nums[i+1:]
            a = 0
            b = len(nums_i) - 1
            while a<b:
                sum = nums_i[a] + nums_i[b] + target
                if sum == 0:
                    print nums, nums_i
                    print i, target, a, nums_i[a], b, nums_i[b]
                    result.append([target, nums_i[a], nums_i[b]])
                    while (a<b and nums_i[a] == nums_i[a+1]):
                        a += 1
                    a += 1
                    while (a<b and nums_i[b-1] == nums_i[b]):
                        b -= 1
                    b -= 1
                elif sum < 0:
                    while (a<b and nums_i[a] == nums_i[a+1]):
                        a += 1
                    a += 1
                else:
                    while (a<b and nums_i[b-1] == nums_i[b]):
                        b -= 1
                    b -= 1
        return result

s = Solution()
s.threeSum([-1,0,1,2,-1,-4])