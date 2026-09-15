from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Found a good problem, we need to study it thoroughly.        
        """


        left = 0

        while seats[left] == 0:
            left += 1

        right = 0
        right_idx = len(seats) - 1

        while seats[right_idx] == 0:
            right += 1
            right_idx -= 1


        mid = 0
        mid_max = 0

        for i in range(left, right_idx + 1):
            if seats[i] == 0:
                mid += 1
                mid_max = max(mid_max, mid)
            else:
                mid = 0

        mid_max = (mid_max + 1) // 2

        return max(left, right, mid_max)
