from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        visited = [False for _ in range(n)]

        def solve(path):
            if len(path) == n:
                res.append(path)
                return

            for i in range(n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                    continue
                visited[i] = True
                solve(path + [nums[i]])
                visited[i] = False

        solve([])
        return res
