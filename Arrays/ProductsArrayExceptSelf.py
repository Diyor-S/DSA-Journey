class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [] # O(n) MC

        for i in range(len(nums)): # O(n) TC
            product = 1 # O(1)

            for j in range(len(nums)): # O(n) Tc
                if i == j: # O(1) check
                    continue

                product *= nums[j] # O(1) multiplication operation  

            result.append(product) # O(1) operation



        return result 

"""

Memory Complexity:
1. O(n) for array initialization

Overall: O(n)

Time Complexity:
1. O(n) iteration first
2. for each iteration another iteration over all the elemtnts O(n)

Overall: O(n^2)

"""   
