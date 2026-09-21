"""
Products of the entire array, excluding Self.
"""

from typing import List

class Solution:
    """
    The task gives us the input of array nums, we need to return
    each value of the array to be the product of the entire array,
    excluding that value itself.
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        We have tried that brute force of O(n^2)
        We have tried that division-approach which failed for zeros as input.
        """
        pass


"""

Solution 2:

        
        total_product = 1

        for num in nums:
            total_product *= num

        result = []

        for num in nums:
            value = total_product // num

            result.append(value)

        return result

MC:

O(n) for the result

TC: 

O(n) - for non-zero cases 
Failed for cases where zeros present in the input array.


Solution 1:

result = [] # O(n) MC

        for i in range(len(nums)): # O(n) TC
            product = 1 # O(1)

            for j in range(len(nums)): # O(n) Tc
                if i == j: # O(1) check
                    continue

                product *= nums[j] # O(1) multiplication operation  

            result.append(product) # O(1) operation



        return result 

Memory Complexity:
1. O(n) for array initialization

Overall: O(n)

Time Complexity:
1. O(n) iteration first
2. for each iteration another iteration over all the elemtnts O(n)

Overall: O(n^2)

"""   
