class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = list(set(nums))
        for i in range(len(x)):
            nums[i] = x[i]
        return len(x)
