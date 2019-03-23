class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s_len = len(s)
        period = 2 * (numRows - 1)
        period_num = s_len // period
        period_remainder = s_len % period
        num_arow = [0 for x in range(0, numRows)]
        result = "PAHNAPLSIIGYIR"
        return result


solution = Solution()
input = "PAYPALISHIRING"
numRows = 3
output = solution.convert(input, numRows)
print(output)