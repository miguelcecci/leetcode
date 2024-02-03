class Solution:
    def jump(self, nums: List[int]) -> int:
        def asdf(my_list):
            i_biggest_jump = -1
            for i in range(len(my_list)):
                rev_index = len(my_list) - i - 1

                possible_jumps = my_list[rev_index]

                if my_list[rev_index] >= i:  # check current jump reachs the end
                    if my_list[rev_index] > i_biggest_jump:
                        i_biggest_jump = i

            return len(my_list) - i_biggest_jump - 1

        step_count = 0
        while len(nums) != 1:
            nums = nums[: asdf(nums) + 1]
            step_count = step_count + 1

        return step_count

