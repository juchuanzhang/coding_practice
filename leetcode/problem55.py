class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        reachable = [False for x in range(nums_len)]
        reachable[0] = True
        for i in range(1, nums_len):
            j = i - 1
            flag = False
            while j >= 0:
                if nums[j] >= i - j and reachable[j] == 1:
                    flag = True
                    break
                j = j - 1
            if flag:
                reachable[i] = True
        return reachable[nums_len - 1]


solution = Solution()
input = [2, 3, 1, 1, 4]
# input = [3, 2, 1, 0, 4]
output = solution.canJump(input)
print(output)
