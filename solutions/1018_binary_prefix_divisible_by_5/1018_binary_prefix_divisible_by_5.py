# Solution - PYTHON

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        
        result = []
        number = ""
        
        for bit in nums:
            number += str(bit)          # append as string
            int_num = int(number, 2)    # convert binary string to int
            
            result.append(int_num % 5 == 0)
        
        return result

