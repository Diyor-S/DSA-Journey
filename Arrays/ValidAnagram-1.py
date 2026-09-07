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
        So today, using a different approach to find identify valid anagram!

        The idea is to use hash tables to track the each characters occurence!
        """
        # First check the length!
        if len(s) != len(t):
            return False

        char_count = {}

        # The idea is to fill up the counter!
        for ch in s:
            if ch not in char_count:
                char_count[ch] = 1
            else:
                char_count[ch] += 1
        
        # Then we subtract the counter each time we see familiar character in the second string

        for ch in t:
            # If ch is not present as the key, then False!
            if ch not in char_count:
                return False
            else:
                char_count[ch] -= 1 # So now we subtract ch count
                # Crucial to check whether the value did not drop below 0!!!
                if char_count[ch] < 0:
                    return False

        # If all the checks did not result in False, then they are the anagrams!

        return True
"""
Approaches 1.

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

Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        '''
        The very first idea that comes into mind, to extract each character of the string into 
        an array, and then sorting that array, and forming the full word again.
        '''

        # Yes, so I am using list comprehensions here, to just get raw list of characters
        seq_s = [ch for ch in s]
        seq_t = [ch for ch in t]

        # Just sorting them out
        seq_s.sort()
        seq_t.sort()

        # And then forming the characters for both strings again and comparing them.
        return "".join(seq_s) == "".join(seq_t)


Conclusion 1:

For now, let's stick with this implementation, but this can't be the fastest, so we'll need to explore.


# --------------------------------------------------------------------------------------------------------------------------

Approach 2.


1. Memory Complexity:
Allocated hashtable of potentially size length of the string!

O(n)

2. Time Complexity:

Iterated over string of size two times
We drop the constant 2, so we get O(n)


Conclusion: O(n), O(n).

"""