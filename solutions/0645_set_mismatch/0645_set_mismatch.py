# Solution - PYTHON

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        
        duplicate = -1
        missing = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicate = nums[i]     # found duplicate
                break
        
        set_nums = set(nums)

        for num in range(1, len(nums) + 1):
            if num not in set_nums:
                missing = num
        
        return [duplicate, missing]

