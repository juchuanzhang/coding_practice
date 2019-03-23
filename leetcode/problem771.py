class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for i in range(0, len(J)):
            for j in range(0, len(S)):
                if J[i] == S[j]:
                    result = result + 1
        return result


solution = Solution()
# input_J = "aA"
# input_S = "aAAbbbb"
input_J = "z"
input_S = "ZZZ"
output = solution.numJewelsInStones(input_J, input_S)
print(output)