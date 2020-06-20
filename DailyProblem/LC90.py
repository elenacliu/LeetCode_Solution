from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        n = len(nums)
        nums.sort()
        visited = [False for _ in range(n)]

        # 闭包
        def solve(path, start):
            if len(path) >= n:
                return
            # print("start, ", start)
            for i in range(start, n):
                if visited[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and visited[i - 1] == False:
                    continue
                visited[i] = True
                ans.append(path + [nums[i]])
                # print(path+[nums[i]])
                solve(path + [nums[i]], i + 1)  # 因为是组合，因此前面选择过的后面不再选择，即从i+1开始选择
                visited[i] = False

        solve([], 0)
        return ans