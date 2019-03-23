class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0 for x in range(0, num + 1)]
        k = 1;
        while k <= num:
            result[k] = 1
            for i in range(k + 1, k * 2):
                if i > num:
                    break
                result[i] = result[i - k] + 1
            k = k * 2
        return result


solution = Solution()
input = 33
output = solution.countBits(input)
print(output)
