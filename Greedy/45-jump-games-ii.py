class Solution:
    def jump(self, nums: List[int]) -> int:
        # 正向遍历
        # 处理出从每个点开始能够跳到的最远的地方
        to = []
        n = len(nums)
        for i in range(n):
            to.append(i + nums[i])

        # O(n^2)
        # end = 1
        # start = 0
        # step = 0
        # while end < n:
        #     maxpos = 0
        #     for i in range(start, end):
        #         maxpos = max(maxpos, to[i])
        #     start = end
        #     end = maxpos + 1
        #     step += 1
        # return step

        # 2, 3, 1, 1, 4
        # 2, 4, 3, 4, 8
        # start = 0, end = 1, maxpos = to[0] = 2, step = 1
        # start = 1, end = 3, maxpos = to[1] = 4, step = 2
        # start = 3, end = 5, break
        # return 2

        # O(n)
        end = 0
        step = 0
        maxpos = 0
        for i in range(n - 1):
            maxpos = max(maxpos, to[i])
            if i == end:
                end = maxpos
                step += 1
        return step

        # maxpos = to[0], i == end, end = 2, step = 1
        # maxpos = to[1], i < end
        # maxpos = to[1], i == end, end = 4, step = 2
        # maxpos = to[1], i < end
