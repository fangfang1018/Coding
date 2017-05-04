ls = [213, 21, 2, 2, 13, 12]

class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(k) for k in nums]
        if len(nums) <= 1:
            return str(nums[0])
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j] < nums[j]+nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
            if nums[0] == '0':
                return '0'
            return ''.join(nums)

s = Solution()
s.largestNumber(ls)
