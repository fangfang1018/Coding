class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        if x==0:
            return True
        for i in range(12, -1, -1):
            if x / 10**i:
                break
        while i > 0:
            left = x / 10**i
            x %= 10**i
            right = x % 10
            x /= 10
            if right != left:
                return False
            i -= 2
        return True

s = Solution()
s.isPalindrome(11)