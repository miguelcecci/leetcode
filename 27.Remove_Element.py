class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        remaining = []
        for i in nums:
            if i != val:
                result.append(i)
            else:
                remaining.append(i)

        final = result+remaining
        for i in range(len(nums)):
            nums[i] = final[i]

        return len(result)

