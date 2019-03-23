class Solution:
    def totalNQueens(self, n):
        result = [0]

        def nqueen(y_index, chessboard, result):
            if y_index == n:
                # debug
                result[0] = result[0] + 1
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
                    nqueen(y_index + 1, chessboard, result)
                    chessboard[i][y_index] = "."
                    # backtracking
            return 0

        chessboard = [["." for x in range(0, n)] for x in range(0, n)]
        nqueen(0, chessboard, result)
        return result[0]


solution = Solution()
input = 8
output = solution.totalNQueens(input)
print(output)

