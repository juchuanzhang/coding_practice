class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        result = [[0 for x in range(0, n)] for x in range(0, m)]
        for i in range(0, m):
            result[i][0] = 1
        for i in range(0, n):
            result[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = result[i - 1][j] + result[i][j - 1]
        return(result[m - 1][n - 1])


solution = Solution()
input_m = 7
input_n = 3
output = solution.uniquePaths(input_m, input_n)
print(output)
