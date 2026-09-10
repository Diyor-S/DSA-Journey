"""
Top K elements
"""

from typing import List

class Solution:
    """

    The task gives us the inputs: list of nums, and k elements.
    
    The idea is that, to use hash table to count the frequencies of 
    each number, because we can not really on the order, 
    this is the pattern where hash_tables again shine.

    We store the number as the key and its freq number as the value.

    And then we are gonna sort those values of the dict so we can get
    the highest freq numbers for the last 'k' elements.
    
    """


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Initialize the hash table
        # O(n) space
        hash_table = {}


        # Iterate over the given input list of nums
        for num in nums:
            # Put the counter to the hash table
            if num not in hash_table:
                hash_table[num] = 1
            else:
                # Increase if already present
                hash_table[num] += 1

        # sort the thing out by turning first it to the list from dictvalues instance
        sorted_priorities = sorted(list(hash_table.values()))

        # create another list
        # O(n) but O(n + n), we drop the constants and get O(n)
        result = []

        # Iterate over the created hash table O(n) + O(n)
        # Results in O(n) again we drop the constants
        for key, value in hash_table.items():
            # Just get the last k elements from the list via subscription syntax
            if value in sorted_priorities[-k:]:
                # and append that key (number) to the final list
                result.append(key)
        # Return the list
        return result

"""

Conclusion:

Memory Complexity:

1. O(n) for hash table
2. O(n) for list of dictvalue instance's values
3. O(k) elements final list

O(n + n + k) => O(n)

Time Complexity:

1. O(n) Iteration over the nums
3. O(n logn) Sorting step for the list
2. O(n) Iteration over the hash table

O(n + n + n log n) => O(nlogn)
"""
            
