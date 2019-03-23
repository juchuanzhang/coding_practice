class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # get rows m and columns n        
        if len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        search_status = [[0 for x in range(0, n)] for x in range(0, m)]
        def dfs_search(x_index, y_index):
            if x_index < 0 or x_index >= m:
                return 0
            if y_index < 0 or y_index >= n:
                return 0
            if grid[x_index][y_index] == "1" and search_status[x_index][y_index] == 0:
                search_status[x_index][y_index] = 1
                dfs_search(x_index - 1, y_index)
                dfs_search(x_index + 1, y_index)
                dfs_search(x_index, y_index - 1)
                dfs_search(x_index, y_index + 1)
                return 1
            return 0
        result = 0
        for i in range(0, m):
            for j in range(0, n):
                if dfs_search(i, j) == 1:
                    result = result + 1
        return result


solution = Solution()
# input = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
#          ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
input = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
output = solution.numIslands(input)
print(output)

# test
# print(len(input[0]))
