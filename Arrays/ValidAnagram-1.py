"""
Valid Anagram - can we form the same word from given inputs?
"""

class Solution:
    """
    The task gives two string as input, and want to identify whether the second input is anagram or not.

    This task involves the usage of separating the string and brick by brick forming the first given string by using the letters from the second one. 
    """

    def isAnagram(self, s: str, t: str) -> bool:
        """
        The very first idea that comes into mind, to extract each character of the string into 
        an array, and then sorting that array, and forming the full word again.
        """

        # Yes, so I am using list comprehensions here, to just get raw list of characters
        seq_s = [ch for ch in s]
        seq_t = [ch for ch in t]

        # Just sorting them out
        seq_s.sort()
        seq_t.sort()

        # And then forming the characters for both strings again and comparing them.
        return "".join(seq_s) == "".join(seq_t)
        
"""
Approaches:

1. Breaking strings into arrays, sorting arrays, and comparing the newly formed sorted characters.

Strings are of the same length.

Time Complexity:
1. The use of "List Comprehensions" to extract the characters into list - O(n + m) -> O(n).
n + m, it should be valid to do 2n -> but constant should give us back n, so it is overall O(n).
2. Sorting both arrays, O(n + m ) -> O(2n) -> O(n) again.
3. Joining the characters back into newly formed strings, O(n + m) -> O(2n) -> O(n) again.

So, overall time complexity should be: O(n) + O(n) + O(n)?

I actually misjudged. Only on the part of sorting, tho. The sorting step takes O(n log n) time.
And overall Time Complexity is gonna be O(n log n) for my current algorithm.

And what about the Memory Complexity?

Memory Complexity:
1. Creating two arrays of the same length, we drop it to O(n).
2. Creating two new strings of the same length, we again drop it to O(n).

O(2n + 2n) => O(4n) => we drop the 4 constant and get O(n).

Does that mean O(n) is the overall Memory Complexity? Yes.


Conclusion:

For now, let's stick with this implementation, but this can't be the fastest, so we'll need to explore.
"""