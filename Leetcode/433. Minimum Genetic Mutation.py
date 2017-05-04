class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        def get_next(set1, set2):
            return set(s2 for s1 in set1 for s2 in set2 if sum(s1[i]!=s2[i] for i in xrange(len(s1)))==1)
        bank = set(bank)
        next = set([start])
        route = [next]
        while 1:
            next = get_next(next, bank)
            bank = bank.difference(next)
            if end in next:
                return len(route)
            if next:
                route.append(next)
            else:
                return False

start = "AACCGGTT"
end = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]

s = Solution()
s.minMutation(start, end, bank)