class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = len(nums)
        max_reachable = 0
        jumps = 0
        next_max_reachable = 0

        for i in range(n):
            if i > next_max_reachable:
                return 0
            elif i > max_reachable:
                jumps += 1
                max_reachable = next_max_reachable
            next_max_reachable = max(next_max_reachable, nums[i] + i)

        return jumps


solution = Solution()
# input = [2, 3, 1, 1, 4]
input = [2, 1, 1, 1, 1]
output = solution.jump(input)
print(output)
