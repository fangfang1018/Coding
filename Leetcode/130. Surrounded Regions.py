class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not any(board):
            return

        m, n = len(board), len(board[0])
        border = [(i, j) for i in range(m) for j in (0, n-1)] + [(i, j) for j in range(n) for i in (0, m-1)]

        while border:
            i, j = border.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                border += (i, j+1), (i, j-1), (i+1, j), (i-1, j)
        board[:] = [["XO"[val == "S"] for val in row] for row in board]

board = ["XXXX","XOOX","XXOX","XOXX"]
s = Solution()
s.solve(board)