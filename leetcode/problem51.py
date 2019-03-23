class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []

        def nqueen(y_index, chessboard):
            if y_index == n:
                # debug
                chessboard_str = ["" for x in range(0, n)]
                for ii in range(0, n):
                    chessboard_str[ii] = chessboard_str[ii].join(chessboard[ii])
                result.append(chessboard_str)
                return 1
            avail_point = [1 for x in range(0, n)]
            for j in range(0, y_index):
                for i in range(0, n):
                    if chessboard[i][j] == "Q":
                        avail_point[i] = 0
                        if i - (y_index - j) >= 0:
                            avail_point[i - (y_index - j)] = 0
                        if i + (y_index - j) < n:
                            avail_point[i + (y_index - j)] = 0
                        # debug
            # print(y_index, avail_point)
            for i in range(0, n):
                if avail_point[i] == 1:
                    chessboard[i][y_index] = "Q"
                    nqueen(y_index + 1, chessboard)
                    chessboard[i][y_index] = "."
                    # backtracking
            return 0

        chessboard = [["." for x in range(0, n)] for x in range(0, n)]
        nqueen(0, chessboard)
        return result


solution = Solution()
input = 8
output = solution.solveNQueens(input)
print(output)
print(len(output))
