# Solution - PYTHON

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0] if nums[0] % 3 == 0 else 0
        
        total = sum(nums)
        if total % 3 == 0:
            return total
        
        nums.sort()
        nums_0 = [i for i in nums if i % 3 == 0]
        nums_1 = [i for i in nums if i % 3 == 1]
        nums_2 = [i for i in nums if i % 3 == 2]
        
        INF = float('inf')
        
        if total % 3 == 1:
            # Option A: remove smallest single number with remainder 1
            optA = nums_1[0] if len(nums_1) >= 1 else INF
            # Option B: remove two smallest numbers with remainder 2
            optB = (nums_2[0] + nums_2[1]) if len(nums_2) >= 2 else INF
            remove = min(optA, optB)
        else:  # total % 3 == 2
            # Option A: remove smallest single number with remainder 2
            optA = nums_2[0] if len(nums_2) >= 1 else INF
            # Option B: remove two smallest numbers with remainder 1
            optB = (nums_1[0] + nums_1[1]) if len(nums_1) >= 2 else INF
            remove = min(optA, optB)
        
        if remove == INF:
            # no valid removal to make sum divisible by 3 -> return 0 (empty selection)
            return 0
        
        return total - remove
