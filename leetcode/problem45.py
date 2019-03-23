class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        min_jump = [-1 for x in range(0, nums_len)]
        min_jump[0] = 0
        max_jump = nums[0]
        for i in range(1, nums_len):
            if nums[i] > max_jump:
                max_jump = nums[i]
            # print(max_jump)
            for j in range(i - 1, -1, -1):
                if i - j > max_jump:
                    break
                if i - j <= nums[j] and min_jump[j] != -1:
                    if min_jump[i] == -1:
                        min_jump[i] = min_jump[j] + 1
                    else:
                        if min_jump[i] > min_jump[j] + 1:
                            min_jump[i] = min_jump[j] + 1
        # print(min_jump)
        return min_jump[nums_len - 1]


solution = Solution()
# input = [2, 3, 1, 1, 4]
input = [2, 1, 1, 1, 1]
output = solution.jump(input)
print(output)
