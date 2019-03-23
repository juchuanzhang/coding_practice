class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        corrent_location = nums_len - 1
        for i in range(nums_len - 1, -1, -1):
            if i + nums[i] >= corrent_location:
                corrent_location = i
        if corrent_location <= 0:
            return True
        else:
            return False


solution = Solution()
input = [2, 3, 1, 1, 4]
# input = [3, 2, 1, 0, 4]
output = solution.canJump(input)
print(output)
