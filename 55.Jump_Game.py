class Solution:
    def canJump(self, nums: List[int]) -> bool:

        def get_index_of_zeros(nums):

            """"""
            
            zeros = []
            for i in range(len(nums)):
                if nums[i] == 0 and i != len(nums)-1:
                    zeros.append(i)
            return zeros

        def zero_can_be_skipped(nums, z_index):
            for i in range(z_index):
                possible_jumps = nums[i]
                if i+possible_jumps > z_index:
                    return True
            return False
        
        zeros = get_index_of_zeros(nums)

        for z_index in zeros:
            if not zero_can_be_skipped(nums, z_index):
                return False
        return True
                

                

        

        
