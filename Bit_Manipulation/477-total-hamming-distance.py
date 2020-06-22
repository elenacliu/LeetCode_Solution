from typing import List


class Solution0:
    def totalHammingDistance(self, nums: List[int]) -> int:
        bin_nums = [str(bin(num))[2:][::-1] for num in nums]
        k = 0
        ans = 0
        n = len(bin_nums)
        while k < 31:
            cnt = 0
            for bin_num in bin_nums:
                if k < len(bin_num):
                    if bin_num[k] == '1':
                        cnt += 1

            ans += cnt * (n - cnt)
            k += 1
        return ans


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for k in range(31):
            cnt = 0
            temp = 0
            # 注意，这样num并不会被修改
            # for num in nums:
            #     if num & 1:
            #         cnt += 1
            #     num >>= 1
            # Python官方建议不要在for loop中修改元素，而要在while中手动修改
            i = 0
            while i < n:
                if nums[i] & 1:
                    cnt += 1
                nums[i] >>= 1
                if nums[i] == 0:
                    temp += 1
                i += 1
            ans += cnt * (n - cnt)
            if temp == n:
                break
        return ans
