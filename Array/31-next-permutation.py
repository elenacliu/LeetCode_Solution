class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                ind = i
                break
        else:
            nums[:] = nums[::-1]
            return
        
        lt = nums[ind]
        # print(ind)
        for i in range(n - 1, ind, -1):
            if nums[i] > lt:
                nums[i], nums[ind] = nums[ind], nums[i]
                # print(nums)
                break

        # print(nums[n-1:ind:-1])
        nums[ind+1:n] = nums[n-1:ind:-1]
        return
