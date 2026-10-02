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

        Now the task is to understand that brute force was failing because we were recalculating the products that we already calculated. To avoid this, we need to somehow preserve the already calculated products and differentiate when to use those products seemlessly.
        
        I found the pattern, so in this problem, we can take everything from the left, and everything from the right
        """
        left = [0] * len(nums) # O(n) memory
        right = [0] * len(nums) # O(n) memory
        # 2*O(n) => O(n) - we drop the constants

        left_total = 1 # Left product accumulation O(1) memory

        for i in range(len(nums)): # O(n)
            # First add the product
            left[i] = left_total
            # Only then update the left product by current index value
            left_total *= nums[i] # O(1)
            
        # The same for the right product accumulation
        right_total = 1 # O(1) memory
        
        # The only difference, iterate backwards
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right_total
            right_total *= nums[i]

        # Allocate the new array for the final result
        result = [] # O(n) memory

        # Iteration O(n)
        for i in range(len(nums)): 
            product = left[i] * right[i]
            result.append(product)
        
        return result        


"""

Solution 3:

        left = [0] * len(nums) # O(n) memory
        right = [0] * len(nums) # O(n) memory
        # 2*O(n) => O(n) - we drop the constants

        left_total = 1 # Left product accumulation O(1) memory

        for i in range(len(nums)): # O(n)
            # First add the product
            left[i] = left_total
            # Only then update the left product by current index value
            left_total *= nums[i] # O(1)
            
        # The same for the right product accumulation
        right_total = 1 # O(1) memory
        
        # The only difference, iterate backwards
        for i in range(len(nums) - 1, -1, -1):
            right[i] = right_total
            right_total *= nums[i]

        # Allocate the new array for the final result
        result = [] # O(n) memory

        # Iteration O(n)
        for i in range(len(nums)): 
            product = left[i] * right[i]
            result.append(product)
        
        return result     


MC:

1. left - O(n) 
2. right - O(n)
3. result - O(n)
4. left_total - O(1)
5. right_total - O(1)

3*O(n) + 2*O(1) => O(n), we drop the constants

TC:
1. Iteration for left fill - O(n)
2. Iteration for right fill - O(n)
3. Iteration for result fill - O(n)

3*O(n) => O(n), we drop the constants

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
