class solution:
    def rob(self, nums: list[int]) -> int:
        
        @cache
        def recursive_rob(position, money):
            if position >= len(nums):
                return money
            
            return max(
                recursive_rob(position+2, money+nums[position]),
                recursive_rob(position+3, money+nums[position])
            )

        return max(
                recursive_rob(0, 0),
                recursive_rob(1, 0)
            )
