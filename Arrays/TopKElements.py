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
        # Initializing the hash_table
        hash_table = {}

        # Iterating over the given input
        for num in nums:
            # Initializing the counter - freq to 1
            if num not in hash_table:
                hash_table[num] = 1
            else:
                # Increasing the counter
                hash_table[num] += 1
        
        # Getting list of lists for freq and values.
        bucket_list = [[] for _ in range(len(nums) + 1)]

        # Index of the inner list is freq index
        # that is why we did + 1 to len(nums) because we needed the include the max freq of n as well.
        
        # Iterate over the key, value pair of the hash_table
        for num, freq in hash_table.items():
            # get the inner list which is at freq index
            # and add the number to that list
            # that way we implemented grouping of numbers with same freqs
            bucket_list[freq].append(num)
            # Now we can have different nums like 2, 3 appearing the 5 times
            # go into the same inner list because they would go at index 5 list

        # prepare the result list, to get individual k element list
        result = []

        # Start iterating backwards from the end of the bucket_list
        for i in range(len(nums), 0, -1):
            # Get each item from the end lists to the result list
            for num in bucket_list[i]:
                result.append(num)

                # We keep appending the numbers until we hit the length of k 
                # Because that would mean if k = 2, return last 2 "frequencies"
                # and that can actually meant that there might be far more numbers like: if the 2 largest freqs are 7 and 5, and within 7 freq range there are actually numbers: 2, 4, 5, 8, 9, then we would need to return them and also
                # for 5 freq range ther emight be 1, 3
                # and we would need to return the final list of:
                # 2, 4, 5, 8, 9, 1, 3!!! 
                if len(result) == k:
                    return result


            
"""

Conclusion:

Solution 2 (latest)

Memory Complexity:

1. Hash_table O(n).
2. Bucket list O(n) * 1 => O(n).
3. Result list O(n) (potentially).

Overall we add them all up and get: O(n).

Time Complexity:

1. Iterating over input array O(n).
2. Iterating over the hash_table O(n) (potentially).
3. Iterating over the bucket_list O(n) (potentially).

Overall again we get: O(n).

Solution 1:

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


Memory Complexity:

1. O(n) for hash table
2. O(n) for list of dictvalue in numbers from the buckets, stance's values
3. O(k) elements final list

O(n + n + k) => O(n)

Time Complexity:

1. O(n) Iteration over the nums
3. O(n logn) Sorting step for the list
2. O(n) Iteration over the hash table

O(n + n + n log n) => O(nlogn)
"""
            
