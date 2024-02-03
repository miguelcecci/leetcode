
import pandas as pd

def firstMissingPositive(nums):
    if not nums:
        return 1
    for i in range(1, len(nums)+1):
        if i not in nums:
            return i
    return len(nums)+1


if __name__ == '__main__':
    firstMissingPositive([1,2,0]) 