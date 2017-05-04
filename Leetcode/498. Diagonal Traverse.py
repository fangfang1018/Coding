class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix or not matrix[0]:
            return result
        
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        right_upper = 1
        while i<m and j<n:
            result.append(matrix[i][j])
            if (i+j) % 2 == 0:
                if j == n-1:
                    i += 1
                elif i == 0:
                    j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i == m-1:
                    j += 1
                elif j == 0:
                    i += 1
                else:
                    i += 1
                    j -= 1
        return result
                
matrix = [[1,2,3],[4,5,6],[7,8,9]]