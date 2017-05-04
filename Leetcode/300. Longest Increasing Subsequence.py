class Solution(object):

    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        f = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and f[i] < f[j]+1:
                    f[i] = f[j]+1
        return max(f)