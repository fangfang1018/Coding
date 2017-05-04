__author__ = 'ffpku_000'
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pair = {'(':')', '{':'}', '[':']'}
        if len(s)%2:
            return False
        temp = []
        for i in s:
            if i in pair:
                temp.append(i)
            elif not temp:
                return False
            else:
                last = temp.pop()
                if pair[last] != i:
                    return False
        if not temp:
            return True
        else:
            return False


string = "[()]"
s = Solution()
s.isValid(string)